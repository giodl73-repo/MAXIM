# Forensic and Medical Entomology

## The Big Picture

Forensic entomology uses insect succession patterns on remains to estimate postmortem interval (PMI). Medical entomology covers the insects and arachnids that cause disease — either as direct parasites or as vectors of pathogens. Together they represent the applied entomological interface with human welfare: one solves crimes, the other prevents death from disease.

```
ENTOMOLOGY-HUMAN WELFARE INTERFACE
=====================================

  FORENSIC ENTOMOLOGY            MEDICAL ENTOMOLOGY
  ====================           ===================
  Postmortem interval (PMI)      Vector-borne disease
  Crime scene analysis           Myiasis (larval infestation)
  Geographical origin            Ectoparasites
  Drug detection (insects)       Envenomation
  Child/elder neglect            Stored product pests
         |                              |
  Evidence: insect succession    Evidence: vector distribution,
  on corpse follows predictable  competence, capacity,
  thermal succession pattern     vectorial capacity formula
```

---

## Forensic Entomology: Postmortem Interval

### Decomposition Stages and Insect Succession

```
DECOMPOSITION STAGES AND INSECT SUCCESSION
============================================

FRESH (0-2 days): minimal insect activity
  First arrival: blowflies (Calliphoridae) within minutes to hours
  Lucilia sericata, Calliphora vicina (Europe/N. America)
  Chrysomya megacephala (tropical/subtropical)
  Phormia regina (carrion indicator, N. America)
  Oviposition: preferred: body orifices, wounds
  Eggs hatch: 12-30 hours (temperature dependent)

BLOAT (2-6 days): gas production; strong odor
  Continued Calliphoridae dominance
  First arrivals: Sarcophagidae (flesh flies; viviparous -- deposit larvae)
  Beetles begin: Staphylinidae, Histeridae (predators of fly larvae)
  Piophilidae (cheese skippers): later stages

ACTIVE DECAY (4-13 days): tissue rapidly consumed
  Calliphoridae larvae (maggot masses) dominate
  Maggot masses generate heat: interior of mass up to 10 C above ambient
    -> development rate in mass > development rate at ambient T
  Silphidae (burying beetles): Nicrophorus can relocate small carcasses
  Dermestidae (hide beetles): keratin feeders

DRY/REMAINS (13+ days): mostly dry tissue, bone, hair
  Dermestidae dominant: Dermestes maculatus, D. lardarius
  Tineidae (clothes moths): keratin
  Cleridae, Nitidulidae: late colonizers
  Arachnida: mites, pseudoscorpions
  Duration: months to years

+------------------------------------------------------------+
|  SUCCESSION IS WAVE-LIKE:                                  |
|  Each wave creates conditions for the next                 |
|  Predictable across temperate regions (with correction)    |
|  Tropical: faster; polar: arrested; aquatic: different     |
+------------------------------------------------------------+
```

### PMI Calculation Methods

```
PMI ESTIMATION METHODS
========================

METHOD 1: ACCUMULATED DEGREE HOURS (ADH)
  Most precise method for fresh remains
  Use: oldest/most developed life stage present

  Step 1: Collect oldest larvae; identify species
  Step 2: Determine developmental stage (instar, weight)
  Step 3: Laboratory rear voucher sample; record T
  Step 4: Calculate ADD (Accumulated Degree Days) to sampled stage
    ADD = sum((T_daily - T_base) * days)
    T_base = lower developmental threshold (Lucilia: 10 C typically)
  Step 5: Reconstruct temperature history at scene (weather station + correction)
  Step 6: PMI = ADD / average daily degree days

  Example:
    Found: 3rd instar Lucilia sericata larvae
    ADH from egg to 3rd instar = 1500 ADH (T_base 0 C)
    Scene average = 15 C/day -> 100 ADH/day
    PMI estimate = 1500/100 = 15 days + eclosion to oviposition lag

METHOD 2: SUCCESSION PATTERNS
  Use: when remains are older (weeks-months)
  Identify species present -> map to succession wave
  Less precise; cross-validate with other evidence
  Geographic calibration essential (succession differs by region)

METHOD 3: MOLECULAR CLOCK (larval gut contents)
  DNA from ingested gut material -> ID victim even from dispersed remains
  Mitochondrial DNA of larvae -> maternal lineage confirmation
  Drug/toxin detection in larvae: possible even when host tissue decomposed

COMPLICATING FACTORS:
  Burial: delays colonization; reduces T (insulate)
  Submersion: entirely different aquatic fauna
  Indoor: controlled T; different blow fly assemblages
  Covered: blankets, plastic -> access restriction
  Drugs in body: accelerate/delay development
    Morphine: accelerates Calliphora development
    Cocaine: stimulates fly development
    Heroin: inhibits development (depends on dose)
```

---

## Medical Entomology: Vector-Borne Diseases

### The Epidemiological Framework

```
VECTOR COMPETENCE AND CAPACITY
=================================

VECTORIAL CAPACITY (Macdonald formula, mosquitoes):
  C = m * a^2 * b * p^n / (-ln p)

  m = mosquito density per human
  a = biting rate (bites/mosquito/day)
  b = proportion of bites that result in infection (competence)
  p = daily survival probability
  n = extrinsic incubation period (EIP, days)
  (-ln p) = mortality rate

  KEY INSIGHT: survival (p) enters as p^n -- small increases in survival
  or decreases in EIP disproportionately increase transmission
  -> Malaria control: target adult mosquito longevity (insecticide)
                      or reduce EIP (Plasmodium development in mosquito)

REPRODUCTIVE NUMBER:
  R0 (vector-borne) = vectorial capacity x intrinsic transmission parameters
  R0 > 1: epidemic spreads
  Goal of control: drive R0 < 1
  Reduce m (mosquito density), reduce a (biting), increase p^-n (shorten EIP),
  reduce b (vaccine -> reduce b in human host)
```

### Major Disease Vectors

```
MOSQUITOES (Culicidae) -- MOST DEADLY ARTHROPOD CLASS
=======================================================

Anopheles spp. (>100 vector species):
  Pathogen: Plasmodium falciparum/vivax/malariae/ovale
  Disease: MALARIA -> ~200-250M cases/yr; >600,000 deaths/yr (mostly <5 yr Africa)
  Transmission: females only; obligate blood meal for egg maturation
  EIP: 10-21 days depending on T; threshold ~16 C for P. falciparum
  Control: ITNs (insecticide-treated nets), IRS (indoor residual spraying)
           ACTs (artemisinin combination therapy); RTS,S vaccine
  Key species: A. gambiae s.s. (Africa; highly anthropophilic),
               A. stephensi (South Asia; urban), A. darlingi (Amazon)

Aedes aegypti:
  Pathogens: dengue (4 serotypes), Zika virus, yellow fever, chikungunya
  Disease: dengue ~400M infections/yr; 100M symptomatic; 20,000 deaths
           Zika: 2015-2016 pandemic; microcephaly; Guillain-Barre
           Yellow fever: vaccine preventable; ~90,000 deaths/yr
  Anthropophilic: breeds in small water containers in peridomestic habitat
  Distribution: all tropical/subtropical regions; expanding poleward
  Control: container reduction (source reduction); Wolbachia biocontrol;
           sterile insect technique (Oxitec self-limiting strain)

Aedes albopictus (tiger mosquito):
  Competent vector: dengue, chikungunya, Zika, EEE, WNV
  Cold-hardy: established temperate Europe, N. America
  Breeds in tires, cemetery vases, tree holes; more cryptic than Ae. aegypti

Culex quinquefasciatus/pipiens:
  Pathogen: West Nile Virus (WNV), lymphatic filariasis (Wuchereria bancrofti)
  Bird-human bridge: Culex bites infected bird -> human spillover
  WNV: neuroinvasive in ~1% infected humans; N. America endemic since 1999
```

```
TSETSE FLIES (Glossina) -- SLEEPING SICKNESS
==============================================

G. morsitans, G. fuscipes, G. palpalis:
  Pathogen: Trypanosoma brucei gambiense (chronic; W/C Africa)
            Trypanosoma brucei rhodesiense (acute; E Africa)
  Disease: Human African Trypanosomiasis (HAT) / sleeping sickness
  Viviparity: deposits single larva; unique among flies
  Both sexes blood-feed
  Distribution: sub-Saharan Africa (tsetse belt); ~10M km^2
  Control: Sterile Insect Technique (SIT): Zanzibar eradication ~1997
           Deltamethrin-treated targets + cattle treatment (pour-on)

Chagas (for comparison -- Reduviidae, not Diptera):
  Vector: Triatoma infestans, Rhodnius prolixus (assassin bugs)
  Pathogen: Trypanosoma cruzi
  Disease: Chagas disease (~6-7M infected; C/S America)
  Transmission: NOT bite -- vector defecates near bite; host rubs in feces
```

```
SANDFLIES -- LEISHMANIASIS
===========================

Phlebotomus (Old World), Lutzomyia (New World):
  Pathogen: Leishmania spp. (~20 species)
  Disease: cutaneous (~1M cases/yr), visceral (kala-azar, ~0.1M/yr)
  Distribution: tropical/subtropical; expanding with climate change
  Control: insecticide spraying; ITNs (fine mesh needed for tiny sandfly)
           No vaccine approved for humans (2025)
```

```
BLACKFLIES -- RIVER BLINDNESS
===============================

Simulium damnosum complex (Africa), S. ochraceum (Americas):
  Pathogen: Onchocerca volvulus (filarial nematode)
  Disease: Onchocerciasis (river blindness); ~21M infected; ~1M vision loss
  Aquatic larvae: fast-flowing rivers (Simulium breeding habitat)
  Control: Ivermectin (Mectizan donation program) + Bti aerial spraying
  OCP (Onchocerciasis Control Programme): 1974-2002;
    ~300,000 cases prevented; 25M ha agricultural land freed
```

```
TICKS -- LYME, TBE, RMSF
==========================

Arachnida (not insects) but canonically in medical entomology:

Ixodes scapularis/ricinus (black-legged tick):
  Borrelia burgdorferi s.l. -> Lyme disease (~400,000 cases/yr USA)
  Anaplasma, Babesia, tick-borne encephalitis virus (in Europe)
  3-host life cycle: larva, nymph, adult each feed once
  Nymph most dangerous: small, long-feeding, preferred timing

Dermacentor variabilis (American dog tick):
  Rickettsia rickettsii -> Rocky Mountain Spotted Fever (RMSF)

Control: tick checks; repellents (DEET, picaridin); landscape management
         Acaricides; deer population management
```

---

## Myiasis: Larval Infestation of Living Tissue

```
MYIASIS TYPES
==============

OBLIGATE MYIASIS:
  Larvae require living host tissue
  Cochliomyia hominivorax (New World screwworm fly):
    Females lay eggs in wounds of warm-blooded animals
    Larvae bore into living tissue; can kill cattle in days
    USDA eradication by SIT: North/Central America (1966-1991)
    Eradication sustained by sterile male releases at Panama isthmus
    Cost-benefit: eradication cost ~$750M; saves ~$1B/yr indefinitely

  Dermatobia hominis (human botfly):
    Female captures other insects (mosquitoes, ticks)
    Glues eggs to captured insect -> eggs transfer to host during bloodfeed
    Larva develops in subcutaneous tissue; 5-10 weeks; painful but benign
    Removal: suffocate with occlusive dressing -> larva exits

  Oestrus ovis (sheep nasal botfly):
    Larvae in nasal passages, sinuses of sheep; can infect humans

FACULTATIVE MYIASIS:
  Normally saprophagous larvae; opportunistically infest neglected wounds
  Calliphora, Lucilia: blowflies in wounds of elderly/infirm
  Can be therapeutic: medicinal maggots (Lucilia sericata)
    Maggots: secrete serine proteases -> debride necrotic tissue only
    Approved as Class II medical device (US FDA, 2004)
    Effective for diabetic foot ulcers, MRSA wounds
```

---

## Envenomation

```
INSECT VENOM SYSTEMS
======================

HYMENOPTERA (most medically significant):
  Bees: Apis mellifera venom
    Major proteins: Phospholipase A2, Melittin, Hyaluronidase, Apamin
    Melittin (50% dry venom weight): membrane-disrupting peptide
    IgE-mediated anaphylaxis: ~50 deaths/yr in US (anaphylactic shock)
    Mass envenomation (>50 stings): direct toxicity; hemolysis; renal failure

  Wasps/Hornets: Vespula, Polistes
    Venom: wasp kinins, phospholipase, hyaluronidase
    Vespa mandarinia: large venom volume; multiple stings; hospitalization

  Ants: formicic acid (Formica), alkaloid venom (Solenopsis)
    Solenopsis invicta (fire ant): piperidine alkaloids + Sol i II protein
    Lesions: sterile pustules; anaphylaxis possible

LEPIDOPTERA:
  Lonomia obliqua (Brazil): hemotoxic caterpillar
    Larval spines inject toxin -> coagulopathy -> hemorrhage; deaths reported
  Hylesia spp.: adult scales cause urticaria (lepidopterism)

HEMIPTERA:
  Reduviidae (assassin bugs): bite; painful but not typically dangerous
  Triatoma: bite vector for Chagas

COLEOPTERA:
  Paederus (rove beetles): pederin toxin on cuticle
    Contact -> vesicant dermatitis; "Nairobi fly" dermatitis
    Pederin more toxic than cobra venom on molar basis (different mode)
```

---

## Vector Control Strategies

```
VECTOR CONTROL TOOLKIT
========================

INSECTICIDE-BASED:
  Indoor Residual Spraying (IRS): spray walls/ceilings with residual insecticide
    Resting mosquitoes contact insecticide -> die before completing EIP
    DDT (controversial but effective), Bendiocarb, Pirimiphos-methyl
  Insecticide-Treated Nets (ITN/LLIN): pyrethroid-impregnated
    Physical barrier + insecticidal effect
    LLIN (long-lasting): impregnated in fiber; 3-5 year life
    ~1.5B LLINs distributed; malaria mortality halved 2000-2015

BIOLOGICAL:
  Wolbachia (wMel strain in Aedes aegypti):
    Maternally inherited intracellular bacteria
    Blocks dengue/Zika/chikungunya replication in mosquito
    Cytoplasmic incompatibility -> self-spreading through population
    Field releases: World Mosquito Programme, ~15 countries
    ~77% dengue reduction in Yogyakarta, Indonesia (RCT 2020)

  Sterile Insect Technique (SIT):
    Mass-rear; irradiate males to sterilize
    Release: mate with wild females -> no offspring -> population crash
    Requirements: flooded release (10:1 sterile:wild); species specificity
    Successes: screwworm eradication, tsetse in Zanzibar

GENETIC APPROACHES (emerging):
  Gene Drive:
    CRISPR-based drive biases inheritance -> suppresses population
    Anopheles gambiae: doublesex gene drive; female-killing in cage trials
    Regulatory: contained trials only (2025); open release pending
  Self-limiting Aedes aegypti (Oxitec):
    OX513A male: daughters die, sons survive + continue spreading lethal allele
    Open releases in several countries; conditional FDA approval (US)

ENVIRONMENTAL:
  Source reduction: remove standing water (Aedes containers)
  Larval habitat management: drain swamps (malaria); pit privy (Culicidae)
  Window screens + air conditioning: reduces indoor exposure
```

---

### Engineering Bridges

Vectorial capacity is a structured sensitivity analysis of disease transmission probability. The formula:

```
  C = (m × a² × b × p^n) / (-ln p)

  m = mosquito density relative to humans
  a = daily biting rate on humans (host preference × biting rate)
  b = probability of infection transmission per infective bite
  p = daily survival probability of mosquito
  n = extrinsic incubation period (days from infection to infectiousness)
```

The p^n term is the key: it measures the probability that a mosquito survives the entire extrinsic incubation period and becomes infective. For malaria (n ≈ 10–12 days), a change in daily survival from p = 0.90 to p = 0.80 reduces p^n by a factor of 0.90^11 / 0.80^11 = 0.314 / 0.086 ≈ 3.6× — mosquito lifespan is the most sensitive parameter by far. This is the kind of sensitivity analysis done in reliability engineering: which parameter most affects MTBF? Vectorial capacity reveals that interventions targeting mosquito survival (insecticide-treated nets, indoor residual spraying) have dramatically higher impact per unit cost than interventions targeting biting rate alone.

The R₀ threshold for epidemic spread (R₀ > 1 sustains transmission; R₀ < 1 leads to extinction) is the epidemic threshold in a network contagion model. R₀ is the expected number of secondary cases per primary case in a fully susceptible population — equivalent to the branching factor in a tree of contagion. For vector-borne diseases, R₀ = C × (1/recovery rate), so the vectorial capacity analysis directly predicts epidemic potential. This threshold concept maps to the critical point in network percolation theory: below the threshold, an outbreak is subcritical and dies out; above it, an outbreak can become a large-scale epidemic. The same threshold mathematics governs fault propagation in distributed systems: if the cascade branching factor > 1, a single failure propagates to the whole system.

## Decision Cheat Sheet

| Disease | Vector | Pathogen | Key control |
|---------|--------|----------|-------------|
| Malaria | Anopheles spp. | Plasmodium spp. | LLINs + IRS + ACTs |
| Dengue/Zika | Aedes aegypti | Flavivirus | Container removal; Wolbachia |
| Yellow fever | Aedes aegypti | Flavivirus | Vaccine (17D) |
| West Nile | Culex pipiens | Flavivirus | Larval control; surveillance |
| Lyme disease | Ixodes scapularis | Borrelia burgdorferi | Tick checks; habitat modification |
| Chagas | Triatoma spp. | Trypanosoma cruzi | Housing improvement; spraying |
| Onchocerciasis | Simulium spp. | Onchocerca volvulus | Ivermectin + Bti |
| Sleeping sickness | Glossina spp. | Trypanosoma brucei | SIT; deltamethrin targets |
| PMI estimation | Calliphoridae | - | ADH method; degree-day accumulation |

---

## Common Confusion Points

**PMI vs time since death**: PMI (postmortem interval) starts at death. "Time since death" is the same thing. Insect-based PMI gives the minimum time (oviposition lag adds 1-6 hours from death to first egg). The actual PMI may be longer if colonization was delayed.

**Vector competence vs capacity**: Competence = can the mosquito actually replicate and transmit the pathogen (intrinsic, per-mosquito)? Capacity = how many secondary cases does one infectious case generate through vectors (population-level, includes density, survival, biting rate)? A competent vector with low density has low capacity.

**DDT ban and malaria**: DDT was banned from agricultural use by the Stockholm Convention (2001) but is permitted for disease vector control (IRS for malaria). Several African countries use DDT for IRS. The debate over DDT is more nuanced than "banned globally."

**Wolbachia is not genetic engineering**: Wolbachia is a naturally occurring intracellular bacterium found in ~40-60% of insect species. Introducing wMel Wolbachia into Aedes aegypti (which normally lacks it) is a microbiome intervention, not a transgenic modification. Regulatory pathways differ from GMO releases.

**Flesh flies vs blowflies**: Sarcophagidae (flesh flies) deposit larvae directly (viviparous); Calliphoridae (blowflies) oviposit eggs. Both are significant in forensic succession. Sarcophagidae often arrive first or in parallel with Calliphoridae; can complicate PMI estimation because their developmental biology is less well-studied.
