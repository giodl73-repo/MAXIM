---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-INFECTIOUS-DISEASE.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:veterinary-medicine:infectious-disease
kind: guide
module: veterinary-medicine
section: veterinary-medicine
title: Infectious Disease - Agents and Major Animal Diseases
status: source-custody
source_custody: partial
current_path: veterinary-medicine/03-INFECTIOUS-DISEASE.md
canonical_path: veterinary-medicine/03-INFECTIOUS-DISEASE.md
backsource_ids: [proof-backfill:veterinary-medicine:03-infectious-disease, git-history:veterinary-medicine:03-infectious-disease]
concepts: [infectious disease]
root_concepts: [infectious disease]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Infectious Disease — Agents and Major Animal Diseases

```
+------------------------------------------------------------------------------+
|                     THE PATHOGEN TAXONOMY (by agent)                         |
|                                                                              |
|   PRION      VIRUS        BACTERIUM     PARASITE          FUNGUS             |
|   -----      -----        ---------     --------          ------             |
|   protein    nucleic      cell, no      protozoa /        yeast /            |
|   only, no   acid +       nucleus,      helminths /       mold               |
|   genome     capsid       own metab.    arthropods                           |
|                                                                              |
|   smallest -------------------- size / complexity --------------> largest    |
|                                                                              |
|   no drug    antivirals   antibiotics   antiparasitics    antifungals        |
|   target     (few)        (many)        (dewormers, etc)  (limited)          |
|                                                                              |
|   EXAMPLES across the row:                                                   |
|   BSE/scrapie | rabies,    | anthrax,    | heartworm,      | ringworm,       |
|               | FMD, parvo | brucellosis | coccidia, ticks | aspergillosis   |
+------------------------------------------------------------------------------+
```

**Read left to right by agent size and complexity.** The agent class determines the drug
class, the diagnostic, and the control strategy. Veterinary infectious disease is the same
five-agent taxonomy as human medicine (`disease/`, `microbiology/`, `virology/`) — but with a
different roster of star pathogens, many of which are economically catastrophic, reportable to
governments, or zoonotic.

**Systems Bridge:** A pathogen is malware with a host tropism (which species/cell it can
"run" on) and a transmission protocol (aerosol, fecal-oral, vector, direct contact). Control
is defense-in-depth: perimeter (biosecurity), patching (vaccination), runtime detection
(surveillance), and quarantine/isolation of compromised nodes. The reportable diseases are the
"call the authorities immediately" CVEs — a single positive can trigger a national response.

Zoonotic spillover (agent jumping to humans) is covered in `04-ZOONOSES-AND-ONE-HEALTH.md`;
this file is the animal-disease roster and the agent classes.

---

## Prions — Disease With No Genome

Prions are the strangest agent: a misfolded version of a normal host protein (PrP) that
induces neighboring normal proteins to misfold, accumulating until the brain becomes spongy.
No nucleic acid, no immune response, no fever, no inflammation. Always fatal, long incubation.

```
   NORMAL PrP (alpha-helical)  +  PRION PrP (beta-sheet)
            |                              |
            +--------- contact ------------+
                       |
                       v
            NORMAL PrP refolds into PRION shape  (autocatalytic cascade)
                       |
                       v
            Aggregates -> neuron death -> SPONGIFORM brain -> death
```

| Disease | Species | Note |
|---------|---------|------|
| **Scrapie** | Sheep, goats | The original recognized prion disease; gives the field its template |
| **BSE** ("mad cow") | Cattle | Spread by feeding rendered ruminant protein back to cattle; caused a major UK epidemic and led to feed bans |
| **Variant CJD** | Humans | Acquired from BSE-contaminated beef — the zoonotic bridge that made prions a public crisis (see file 04) |
| **Chronic Wasting Disease (CWD)** | Deer, elk, moose | Spreading in North American cervids; environmentally persistent; no treatment |

Prions resist normal sterilization (standard autoclaving, formalin, alcohol) — a surgical and
food-safety nightmare. They contaminate the environment for years. The control lever is
breaking transmission: feed bans for BSE, culling and genetic-resistance breeding for scrapie.

---

## Viruses — The High-Impact Roster

Viruses dominate the list of feared animal diseases because several are highly contagious,
have no cure, and are economically or ecologically devastating. A representative roster:

```
+------------------------------------------------------------------------------+
|                    MAJOR ANIMAL VIRAL DISEASES                               |
|                                                                              |
|  AGENT                  HOST(S)        WHY IT MATTERS                        |
|  -----                  -------        -------------                         |
|  Rabies (Lyssavirus)    all mammals    ~100% fatal once clinical; zoonotic;  |
|                                        vaccine-preventable. (file 04)        |
|  Foot-and-Mouth (FMD)   cloven-hoofed  NOT usually fatal, but so contagious  |
|                         (cattle, pig,  that an outbreak halts all trade and  |
|                         sheep)         triggers mass culls. Reportable.      |
|  Canine parvovirus      dogs (esp.     Attacks dividing gut + marrow cells;  |
|  (CPV-2)                puppies)       bloody diarrhea, often fatal if       |
|                                        untreated; vaccine-preventable.       |
|  Canine distemper       dogs, ferrets, multisystem (resp + GI + neuro);      |
|                         wild canids/   vaccine-preventable; devastates       |
|                         big cats       unvaccinated and wildlife.            |
|  Feline leukemia (FeLV) cats           retrovirus; immunosuppression,        |
|                                        lymphoma; testable + vaccine.         |
|  Feline immunodef.(FIV) cats           "cat AIDS"; retrovirus, bite-spread.  |
|  Avian influenza H5N1   poultry, wild  high-path strains kill flocks fast;   |
| (HPAI)                 birds, spillover zoonotic/pandemic concern. (file 04) |
|  Newcastle disease      poultry        reportable; devastates flocks.        |
|  African swine fever     pigs           ~100% fatal in pigs; no vaccine for  |
|  (ASFV)                                 years; wiped out herds across Asia/  |
|                                        Europe. NOT zoonotic but economically |
|                                         catastrophic.                        |
|  Bluetongue / BVD        ruminants      vector-borne / production losses.    |
+------------------------------------------------------------------------------+
```

A few of these deserve a closer look because they teach a general principle.

### Canine parvovirus — why puppies, why the gut

Parvovirus targets **rapidly dividing cells**. In a puppy, those are the intestinal crypt
cells and bone-marrow precursors. Destroying crypt cells strips the gut lining (bloody
diarrhea, vomiting, fluid loss, bacterial translocation -> sepsis); hitting the marrow drops
white cells just when the animal needs them. Maternal antibody protects neonates, then wanes —
leaving a vulnerable window that the vaccine schedule is designed to cover. This is a clean
illustration of *tropism* (the virus's cell preference) explaining the entire clinical picture.

### Foot-and-mouth disease — contagion over lethality

FMD rarely kills adult animals, yet it is one of the most feared diseases on Earth. Why?
Extreme contagiousness across all cloven-hoofed species, spread by aerosol, fomites, and even
wind over distance. A single case can shut a country's livestock exports and trigger mass
culling. It teaches that in production medicine, *transmissibility and trade impact* can matter
more than case fatality. (Note: FMD is an animal disease; the unrelated human "hand, foot and
mouth disease" is a different virus entirely.)

### Retroviruses in cats — FeLV vs FIV

Both are retroviruses (RNA genome reverse-transcribed into host DNA), echoing HIV mechanism
(`virology/`), but they differ:

| | FeLV | FIV |
|---|------|-----|
| Spread | Saliva, social contact (sharing bowls, grooming) | Bite wounds (fighting) |
| Population at risk | Friendly multi-cat households | Outdoor, fighting (often male) cats |
| Vaccine | Yes (non-core, risk-based) | Limited/region-dependent |
| Outcome | Immunosuppression, anemia, lymphoma | Slow immune decline, "cat AIDS" |

---

## Bacteria — Classic and Reportable

Bacterial diseases in animals run the same drug logic as human medicine (antibiotics by
class; `medicine/01-ANTIBIOTICS.md`) but include several headline zoonotic and reportable
agents.

```
+-------------------------------------------------------------------------------+
|                    NOTABLE ANIMAL BACTERIAL DISEASES                          |
|                                                                               |
|  AGENT                   HOST / DISEASE          NOTE                         |
|  -----                   ---------------          ----                        |
|  Bacillus anthracis      grazers; ANTHRAX         spore-forming, persists     |
|                                                   in soil for decades;        |
|                                                   zoonotic, bioterror agent.  |
|  Brucella spp.           cattle/pig/goat;         abortion storms; major      |
|                         BRUCELLOSIS              zoonosis ("undulant fever"). |
|  Mycobacterium bovis     cattle; BOVINE TB        zoonotic via raw milk;      |
|                                                   why milk is pasteurized.    |
|  Clostridium spp.        many; tetanus, botulism, spore-formers; toxin-       |
|                          blackleg, enterotoxemia  mediated; vaccine-          |
|                                                   preventable (e.g. tetanus   |
|                                                   in horses).                 |
|  Leptospira spp.         dogs, livestock,         zoonotic via urine-         |
|                          LEPTOSPIROSIS            contaminated water.         |
|  Borrelia burgdorferi    dogs (+humans); LYME     tick-borne; expanding with  |
|                                                   tick range (file 04).       |
|  E. coli / Salmonella    neonatal scours;         calf/piglet diarrhea +      |
|                          food-borne               food-safety pathogens.      |
|  Mastitis pathogens      dairy cattle udder       (Strep, Staph, coliforms)   |
|  (Strep/Staph/coliform)  infection                #1 production-loss disease  |
|                                                   in dairy. (file 06)         |
+-------------------------------------------------------------------------------+
```

**Spore-formers** (anthrax, clostridia) deserve emphasis: their spores survive in soil and
carcasses for years to decades, so the control strategy is environmental and preventive
(don't open an anthrax carcass; vaccinate against clostridial diseases) rather than purely
therapeutic. Anthrax is also why you never necropsy a suspected case in the open — exposing
the spores reseeds the soil.

---

## Parasites — The Veterinary Workhorse

Parasitism is far more central to veterinary than to human medicine in the developed world.
The three sub-classes:

```
+------------------------------------------------------------------------------+
|                          PARASITE CLASSES                                    |
|                                                                              |
|  PROTOZOA (single-cell)    HELMINTHS (worms)       ARTHROPODS (ectoparasite) |
|  ----------------------    -----------------       ------------------------  |
|  Coccidia (Eimeria)        Roundworms (nematodes:  Fleas (also flea-borne    |
|    -> diarrhea in young     Toxocara, hookworm,     disease + tapeworm       |
|    livestock/pets           Dirofilaria=heartworm)  vector)                  |
|  Giardia (zoonotic GI)     Tapeworms (cestodes)    Ticks (vector for Lyme,   |
|  Toxoplasma (cat-          Flukes (trematodes:      anaplasma, babesia,      |
|    definitive host;         liver fluke)            ehrlichia, Rocky Mtn     |
|    risk in pregnancy)                               spotted fever)           |
|  Babesia (tick-borne,                              Mites (mange: Sarcoptes   |
|    RBC parasite)                                    =scabies, Demodex)       |
|                                                    Lice; myiasis (flystrike) |
+------------------------------------------------------------------------------+
```

### Heartworm (Dirofilaria immitis) — a parasite with an arthropod vector

A worth-knowing example because it ties a helminth to an arthropod and to drug toxicity:

```
   Mosquito bites infected dog -> ingests microfilariae
        -> larvae mature in the mosquito
        -> mosquito bites a new dog -> larvae enter
        -> adult worms grow in the PULMONARY ARTERIES and HEART
        -> heart failure, death if untreated.

   PREVENTION: monthly macrocyclic lactone (e.g. ivermectin-class) kills larvae.
   TREATMENT of established adult worms is risky (dying worms can embolize).
   COLLIE-TYPE BREEDS: an MDR1/ABCB1 gene mutation makes some herding breeds
   dangerously sensitive to high-dose ivermectin (neurotoxicity). Heartworm-
   preventive doses are safe; high deworming doses are not. (See file 08.)
```

### Why deworming dominates herd and pet medicine

Helminth burdens sap growth, fertility, and immunity in livestock, and anthelmintic
**resistance** is now a serious problem (parallel to antibiotic resistance) from decades of
blanket deworming. Strategic, refugia-preserving deworming has replaced calendar-based
blanket treatment — a direct analog to antimicrobial stewardship (`09-PUBLIC-HEALTH-ROLE.md`).

### Toxoplasma — the cat connection

Cats are the *definitive host* of Toxoplasma gondii (the only host in which it completes its
sexual cycle and sheds oocysts). This is the real basis of the advice that pregnant women
avoid handling cat litter — congenital toxoplasmosis can harm a fetus. The mechanism is
specific and worth getting right: the risk is fresh oocysts from cat feces (and undercooked
meat), not the mere presence of a cat. (Zoonosis detail in file 04.)

---

## Fungi — Smaller but Important

Fungal disease is less common but includes a few important entities:

| Disease | Agent | Note |
|---------|-------|------|
| **Ringworm** (dermatophytosis) | Microsporum, Trichophyton | NOT a worm — a fungus; zoonotic; common in cats, calves; classic ring-shaped skin lesion |
| **Aspergillosis** | Aspergillus mold | Air-sac and respiratory infection in birds (recall poorly vascularized air sacs, file 01); also nasal in dogs |
| **Valley fever** (coccidioidomycosis) | Coccidioides | Soil fungus in arid regions; dogs and humans both susceptible |
| **Cryptococcosis** | Cryptococcus | Cats especially; often via bird droppings; nasal/CNS |

Antifungal options are limited and often slow — another reason husbandry (dry housing,
ventilation) is the first line, especially for air-sac aspergillosis in birds.

---

## The Control Toolkit — Same Logic, Scaled to Populations

```
+-----------------------------------------------------------------------------+
|                    DISEASE CONTROL LAYERS                                   |
|                                                                             |
|   BIOSECURITY    quarantine new arrivals, control movement, disinfect,      |
|   (perimeter)    rodent/vector control, "all-in/all-out" housing.           |
|        |                                                                    |
|   VACCINATION    core vaccines (rabies, parvo/distemper for dogs; panleuk   |
|   (patching)     for cats) + risk-based non-core. Herd immunity at scale.   |
|        |                                                                    |
|   SURVEILLANCE   testing, reporting reportable diseases to authorities,     |
|   (detection)    necropsy/diagnostics. (file 09)                            |
|        |                                                                    |
|   STAMPING OUT   for the worst reportable diseases (FMD, HPAI, ASF):        |
|   (isolation)    cull + quarantine + movement ban to eradicate.             |
+-----------------------------------------------------------------------------+
```

Vaccination basics worth anchoring: vaccines split into **core** (recommended for nearly all
animals of a species because the disease is severe and/or zoonotic — e.g., **rabies** in dogs
and cats, **parvovirus and distemper** in dogs, **panleukopenia** in cats) and **non-core**
(given based on lifestyle and exposure risk — e.g., FeLV for outdoor cats, Lyme, Bordetella
"kennel cough"). The vaccine types themselves (live-attenuated, inactivated, subunit, recom-
binant, mRNA) follow the same taxonomy as human vaccines in `medicine/02-ANTIVIRALS-VACCINES.md`.

---

## Decision Cheat Sheet

| Pattern / clue | Suspect | Class |
|----------------|---------|-------|
| Unvaccinated puppy, bloody diarrhea + vomiting + low WBC | Parvovirus | Virus |
| Spongiform brain, long incubation, no fever, fatal | Prion (BSE/scrapie/CWD) | Prion |
| Cloven-hoofed, blisters on mouth/feet, explosive spread | Foot-and-mouth disease | Virus (reportable) |
| Cattle abortion storm + "undulant fever" in farmworkers | Brucellosis | Bacterium (zoonotic) |
| Sudden death in grazers, spore-former, don't open carcass | Anthrax | Bacterium (zoonotic) |
| Mass poultry die-off, neuro signs, fast | Avian influenza (HPAI) / Newcastle | Virus (reportable) |
| Dog cough/heart failure, mosquito exposure | Heartworm | Helminth (vectored) |
| Ring-shaped hairless skin lesion, contagious to owner | Ringworm | Fungus (zoonotic) |
| Air-sac infection in a pet bird | Aspergillosis | Fungus |
| ~100% fatal pig disease, no vaccine, no zoonosis | African swine fever | Virus |

---

## Common Confusion Points

### "Ringworm is a worm"

It is a fungus (dermatophyte). The name describes the ring-shaped skin lesion. It is zoonotic
and treated with antifungals, not dewormers.

### "Foot-and-mouth disease is the same as human hand-foot-mouth disease"

Completely unrelated. Animal FMD is an aphthovirus of cloven-hoofed livestock and is a
trade-halting catastrophe; human hand-foot-and-mouth is a coxsackievirus, usually a mild
childhood illness. Easy to confuse by name, never by biology.

### "African swine fever can infect people"

ASF is devastating to pigs but is not zoonotic — it does not infect humans. Its impact is
purely economic and on animal welfare. Contrast with swine influenza, which can be zoonotic.

### "If it has no cure, treatment is pointless"

Many of the worst agents (rabies once clinical, prions, ASF) have no cure — which is exactly
why the entire strategy shifts to *prevention*: vaccination, biosecurity, surveillance, and
stamping out. The control lever moves upstream of treatment. How these agents cross into
people is the subject of `04-ZOONOSES-AND-ONE-HEALTH.md`.
