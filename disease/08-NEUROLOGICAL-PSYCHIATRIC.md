# 08 — Neurological & Psychiatric Disease

## Neurodegenerative, Epilepsy, Stroke, Mood, Psychosis

---

## Big Picture: CNS Disease Landscape

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    CNS DISEASE BY MECHANISM                             │
├──────────────────┬──────────────────────────────────────────────────────┤
│  PROTEIN         │  Alzheimer's (Aβ + tau)                              │
│  AGGREGATION     │  Parkinson's (α-synuclein)                           │
│  PROTEINOPATHIES │  ALS/FTLD (TDP-43, FUS)                              │
│                  │  Huntington's (polyQ)                                │
├──────────────────┼──────────────────────────────────────────────────────┤
│  EXCITABILITY    │  Epilepsy (GABA↓ / glutamate↑)                       │
│  DISORDERS       │  Migraine (CSD, CGRP)                                │
│                  │  Channelopathies (SCN1A, KCNQ2)                      │
├──────────────────┼──────────────────────────────────────────────────────┤
│  VASCULAR        │  Ischemic stroke (large vessel / cardioembolic /     │
│                  │    small vessel / cryptogenic)                       │
│                  │  Hemorrhagic stroke (ICH / SAH)                      │
│                  │  TIA (same mechanism, transient)                     │
├──────────────────┼──────────────────────────────────────────────────────┤
│  DEMYELINATING   │  MS (CNS — autoimmune; see 07-AUTOIMMUNE)            │
│                  │  GBS (PNS — post-infectious)                         │
│                  │  CIDP (chronic GBS equivalent)                       │
├──────────────────┼──────────────────────────────────────────────────────┤
│  PSYCHIATRIC /   │  Depression (monoamine/HPA)                          │
│  CIRCUIT-LEVEL   │  Schizophrenia (DA imbalance)                        │
│                  │  Bipolar (circuit dysregulation)                     │
│                  │  ADHD, ASD (neurodevelopmental)                      │
│                  │  Addiction (VTA-NAc plasticity)                      │
└──────────────────┴──────────────────────────────────────────────────────┘

Protein aggregation diseases share: normal protein → misfolded → seeding/spreading
Psychiatric disorders share: circuit-level dysfunction without overt structural lesion
```

---

## 1. Alzheimer's Disease

### Amyloid Cascade Hypothesis

```
APP (amyloid precursor protein)
      │
      ▼
β-secretase (BACE1) cleavage → sAPPβ + C99
      │
γ-secretase (presenilin 1/2) cleavage
      │
      ├─► Aβ40 (predominant, soluble)
      └─► Aβ42 (aggregation-prone, seed plaques)
              │
              ▼ oligomerization
        Aβ oligomers (synaptotoxic) ──► synaptic dysfunction (early)
              │
              ▼ plaque deposition
        Neuritic plaques ──► neuroinflammation (microglia/astrocytes)
              │
              ▼ tau secondary?
        Hyperphosphorylated tau → neurofibrillary tangles (NFTs)
              │
              ▼
        Neuron death → atrophy (hippocampus/entorhinal first)
```

**Key molecules:**
- **APP** mutations → familial AD (rare); Trisomy 21 → 3 copies → early AD
- **PSEN1/PSEN2** (γ-secretase components) → most common FAD mutations → ↑Aβ42/40 ratio
- **APOE ε4** allele → impairs Aβ clearance, promotes aggregation; 3–4× risk per allele
- **APOE ε2** — protective; ε3 — neutral

**Cholinergic hypothesis:** Basal nucleus of Meynert → neocortex/hippocampus; cholinergic neurons disproportionately lost → basis for AChEI therapy (donepezil, rivastigmine, galantamine). Memantine (NMDA antagonist) for moderate-severe.

**Biomarkers (ATN framework):**
```
A = Amyloid: CSF Aβ42↓ (deposited), PET amyloid+, plasma p-tau/Aβ42 ratio
T = Tau:     CSF p-tau↑, tau-PET
N = Neurodegeneration: FDG-PET hypometabolism (temporal-parietal), atrophy MRI
```

**Clinical staging:**
- Preclinical AD (biomarker+ / cognitively normal)
- MCI due to AD (objective impairment, daily function preserved)
- AD dementia (episodic memory → language/visuospatial → executive)

**New therapeutics:** Anti-Aβ mAbs (lecanemab/donanemab) — modest cognitive slowing in MCI/early AD; risk of ARIA (amyloid-related imaging abnormalities = microhemorrhage/edema).

---

## 2. Parkinson's Disease

### Basal Ganglia Circuit — Normal vs PD

```
NORMAL PATHWAY:
Cortex ──►  Striatum (caudate/putamen)
                 │
            ┌────┴────┐
            │         │
     Direct path:   Indirect path:
     D1 receptor    D2 receptor
     ↓ GPi/SNr      ↑ GPi/SNr
     ↓ inhibition   ↑ inhibition
     ↑ thalamus     ↓ thalamus
     ↑ cortex       ↓ cortex
         (movement facilitation)

PARKINSON'S — dopamine depleted from SNpc:
Direct path weakened + Indirect path excessive
→ GPi overactive → thalamus inhibited → cortex under-driven
→ BRADYKINESIA, rigidity, difficulty initiating movement
```

**Pathology:**
- Loss of dopaminergic neurons in **substantia nigra pars compacta (SNpc)**
- Remaining neurons contain **Lewy bodies** — α-synuclein + ubiquitin aggregates
- Braak staging: pathology begins in olfactory bulb/dorsal vagus (stage 1–2) → SNpc (3–4) → neocortex (5–6)
- α-synuclein may spread cell-to-cell (prion-like mechanism)

**Cardinal motor features (TRAP):**
- **T**remor at rest (4–6 Hz, "pill-rolling"), ↓ with action
- **R**igidity (lead-pipe; cogwheel = rigidity + tremor)
- **A**kinesia/bradykinesia (micrographia, hypomimia, shuffling gait)
- **P**ostural instability (late sign)

**Non-motor features:** REM sleep behavior disorder (often precedes motor), anosmia, constipation, autonomic dysfunction, depression, dementia (Parkinson's dementia vs DLB).

**Genetics:**
| Gene | Inheritance | Protein | Notes |
|------|-------------|---------|-------|
| SNCA (PARK1) | AD | α-synuclein | Triplication → more severe |
| LRRK2 | AD | LRRK2 kinase | Most common familial PD |
| PINK1/Parkin | AR | Mitophagy pathway | Young onset; no Lewy bodies |
| GBA | Risk factor | Glucocerebrosidase | 5–10× risk; lysosomal dysfunction |

**Treatment:**
```
LEVODOPA/CARBIDOPA — gold standard
  Levodopa crosses BBB → converted to DA in SNpc residual neurons
  Carbidopa blocks peripheral DOPA decarboxylase → ↓ nausea/↑ CNS delivery
  Long-term: wearing off, dyskinesia, on-off fluctuations

DOPAMINE AGONISTS (pramipexole, ropinirole, rotigotine)
  Direct D2/D3 agonism; adjunct or monotherapy (young onset)
  Risk: impulse control disorders

MAO-B INHIBITORS (selegiline, rasagiline): ↓ DA catabolism
COMT inhibitors (entacapone): ↓ peripheral L-DOPA breakdown

DBS (deep brain stimulation): STN or GPi targets; reduces motor fluctuations
```

---

## 3. ALS (Amyotrophic Lateral Sclerosis)

**Pathophysiology:** Combined upper motor neuron (UMN) + lower motor neuron (LMN) degeneration.

```
UMN (corticospinal): spasticity, hyperreflexia, Babinski+, weakness
LMN (anterior horn/bulbar): weakness, atrophy, fasciculations, hyporeflexia
Combination = ALS (El Escorial criteria)
```

**Molecular mechanisms:**
- **Glutamate excitotoxicity:** ↑ synaptic glutamate → excessive AMPA/NMDA activation → Ca²⁺ overload → mitochondrial dysfunction → ROS → death
- **Protein aggregation:** TDP-43 (nuclear RNA-binding protein) mislocalizes to cytoplasm → cytoplasmic inclusions (>97% of ALS)
- **RNA processing defects:** FUS, ALS2, SETX mutations
- **Axonal transport failure**
- **Neuroinflammation:** activated microglia → TNF-α, IL-1β

**Genetic ALS (~10%):**
| Gene | % familial ALS | Mechanism |
|------|---------------|-----------|
| C9orf72 | ~40% | GGGGCC hexanucleotide repeat → RNA foci, DPR proteins |
| SOD1 | ~20% | Misfolded Cu/Zn SOD → toxic gain of function |
| TDP-43 | ~5% | Nuclear → cytoplasmic redistribution |
| FUS | ~5% | RNA processing protein aggregation |

**Treatment:**
- **Riluzole:** blocks presynaptic glutamate release; ~3 month survival extension
- **Edaravone:** free radical scavenger; modest benefit early-stage
- **Tofersen** (antisense oligonucleotide): SOD1-ALS; ↓ neurofilament light chain
- Median survival 2–5 years; respiratory failure usually cause of death

---

## 4. Huntington's Disease

**Genetics:** CAG trinucleotide repeat in **HTT** gene (chromosome 4)
```
Normal: <26 repeats
Intermediate: 27–35 (may expand in next generation)
Reduced penetrance: 36–39
Full penetrance: ≥40 repeats
Juvenile HD: >55–60 repeats (rigid Westphal variant)
```

**Anticipation:** CAG repeats tend to expand in transmission, especially paternal; earlier onset in subsequent generations.

**Polyglutamine toxicity:**
- Expanded polyQ tract → mutant huntingtin (mHTT) aggregates
- Loss of interaction with BDNF → striatal neuron (medium spiny neurons) vulnerability
- mHTT interacts aberrantly with transcription factors, disrupts mitochondria/proteasome
- Striatal atrophy → caudate head (seen on MRI as ventricular "boxing glove" appearance)

**Clinical triad:**
1. **Chorea** (involuntary writhing movements; early)
2. **Psychiatric** (depression, irritability, obsessive features; often precede motor)
3. **Dementia** (subcortical pattern: executive dysfunction, slowed processing)

**Genetic testing:** Direct mutation testing (polyQ repeat PCR); 100% penetrance if ≥40. Predictive testing: major ethical issues (pre-symptomatic disclosure, insurance implications).

**Treatment:** No disease-modifying therapy. Tetrabenazine/valbenazine (VMAT2 inhibitor) for chorea. Antipsychotics for psychiatric symptoms.

---

## 5. Epilepsy

### Seizure Classification (ILAE 2017)

```
SEIZURE ONSET
      │
  ┌───┴───┐
Focal    Generalized    Unknown
  │           │
  ├── Aware   ├── Motor (tonic-clonic, myoclonic, tonic, atonic, clonic)
  └── Impaired├── Non-motor (absence — 3 Hz spike-wave)
  awareness   └── Unknown

Focal → Bilateral: Focal onset → bilateral tonic-clonic (old "secondarily generalized")

STATUS EPILEPTICUS: ≥5 min continuous seizure OR ≥2 seizures without recovery
```

**Pathophysiology:**
- **GABA↓:** reduced inhibitory tone; GABAa = Cl⁻ channel; GABAb = K⁺ channel / ↓cAMP
- **Glutamate↑:** enhanced AMPA/NMDA-mediated excitation
- **Abnormal burst firing:** Na⁺ channel slow inactivation failure → repetitive firing
- **Channelopathies:**
  - SCN1A (Nav1.1) loss → Dravet syndrome (febrile+ afebrile seizures, treatment-resistant)
  - KCNQ2/3 (Kv7) loss → neonatal seizures
  - GABRB3 (GABAa β3) → childhood absence

**Antiseizure medications — mechanisms:**
| Mechanism | Drugs |
|-----------|-------|
| Na⁺ channel block (use-dependent) | Phenytoin, carbamazepine, oxcarbazepine, lamotrigine, lacosamide |
| GABA enhancement | Phenobarbital (GABA-A), benzodiazepines (GABA-A), vigabatrin (GABA-T inhibitor), tiagabine (GABA reuptake) |
| Ca²⁺ channel block (T-type) | Ethosuximide (absence only), valproate |
| NMDA antagonism | Felbamate (partial), ketamine (acute) |
| SV2A ligand (synaptic vesicle) | Levetiracetam, brivaracetam |
| K⁺ channel opener | Ezogabine (Kv7) |
| AMPA antagonism | Perampanel |

**Status epilepticus management (time-critical):**
```
0–5 min:    BZD — lorazepam IV 0.1 mg/kg (or IM midazolam/buccal)
5–20 min:   BZD again if not stopped
20–40 min:  2nd line — fosphenytoin / valproate / levetiracetam IV
40+ min:    Refractory SE → propofol/midazolam/pentobarbital infusion (EEG monitoring)
```

---

## 6. Stroke (Detailed)

*(Overview in 05-CARDIOVASCULAR-DISEASE.md; here: mechanisms and imaging)*

### Arterial Territories

```
Anterior circulation (ICA):
  ACA ──► medial frontal/parietal (leg > arm weakness, abulia)
  MCA ──► lateral cortex (contralateral face + arm > leg, aphasia if dominant)
    Superior division: Broca's (motor aphasia, intact comprehension)
    Inferior division: Wernicke's (fluent aphasia, poor comprehension)

Posterior circulation (vertebrobasilar):
  PCA ──► occipital (contralateral homonymous hemianopia)
  PICA ──► lateral medulla (Wallenberg: ipsilat face, contralat body, Horner's, dysphagia)
  Basilar ──► locked-in syndrome (bilateral corticospinal), cerebellar
  SCA ──► cerebellar (ataxia, nausea)
  AICA ──► lateral pons (ipsilat face + hearing loss, contralat body)
```

### Imaging Time Courses

```
DWI (diffusion-weighted MRI): bright within minutes (cytotoxic edema)
ADC map: dark (restricted diffusion) — confirms acute ischemia
FLAIR: bright at 6–12 h (vasogenic edema replaces cytotoxic)
CT: normal initially; hypodense at 6–24 h; hyperdense MCA sign = clot

PENUMBRA concept:
  Core (dead): CBF <10 mL/100g/min → irreversible injury in minutes
  Penumbra (salvageable): CBF 10–20 mL/100g/min → dies if untreated

  DWI-PWI mismatch = penumbra = target for intervention
```

**Treatment:**
- **tPA (alteplase):** 0–4.5 h from onset; contraindications: BP >185/110, prior ICH, recent surgery
- **Tenecteplase** (single IV bolus): non-inferior, preferred in some guidelines
- **Mechanical thrombectomy:** large vessel occlusion (ICA/proximal MCA); 0–24 h if salvageable penumbra (DAWN/DEFUSE-3 criteria)
- Secondary prevention: antiplatelet (aspirin ± clopidogrel), anticoagulation (AF), statin, BP control

### Hemorrhagic Stroke

```
ICH (intracerebral hemorrhage):
  HTN: putamen (most common), thalamus, pons, cerebellum
  CAA: lobar hemorrhages (elderly, APOE ε4)
  Management: BP control (SBP <140 target), neurosurgery if cerebellar (>3cm)

SAH (subarachnoid hemorrhage):
  Cause: ruptured saccular aneurysm (berry aneurysm) — MCA bifurcation most common
  Presentation: "thunderclap" — worst headache of life (sentinel bleed in 30%)
  Diagnosis: CT non-contrast (subarachnoid blood) → if neg, LP (xanthochromia >2h)
  Treatment: coiling vs clipping; nimodipine (prevent vasospasm → delayed ischemia)
  Complications: rebleeding, vasospasm (day 4–14), hydrocephalus, hyponatremia (SIADH/CSW)
```

---

## 7. Guillain-Barré Syndrome (GBS)

**Mechanism:** Post-infectious (C. jejuni, CMV, EBV, HIV, influenza, COVID-19) immune attack on peripheral nerve.

```
Molecular mimicry: Campylobacter LOS (lipooligosaccharide)
  mimics gangliosides (GM1, GD1a, GQ1b) on nerve membrane
  → anti-ganglioside antibodies → complement activation → demyelination/axonal injury
```

**Variants:**
| Variant | Target | Features |
|---------|--------|---------|
| AIDP (85%) | Myelin/Schwann cell | Ascending weakness, areflexia |
| AMAN | GM1/GD1a (axonal) | Axonal damage, poorer recovery |
| Miller Fisher (MFS) | GQ1b | Ophthalmoplegia, ataxia, areflexia |

**Clinical:** Ascending flaccid paralysis over 2–4 weeks; autonomic instability (BP lability); respiratory failure (30% need ventilation).

**CSF:** Albuminocytologic dissociation — protein ↑↑, cells normal (typically <10 WBC).

**EMG:** Demyelinating (↑ latency, ↓ conduction velocity) vs axonal pattern.

**Treatment:** IVIg (2g/kg) or plasmapheresis — equivalent; NOT steroids (worsen). Supportive care critical (respiratory monitoring, autonomic management).

---

## 8. Headache Disorders

### Classification

```
PRIMARY (no structural cause):
  ├── Migraine (± aura)
  ├── Tension-type (most common overall)
  └── Trigeminal autonomic cephalalgias (TACs):
        ├── Cluster headache
        ├── Paroxysmal hemicrania
        └── SUNCT/SUNA

SECONDARY (structural/systemic cause):
  SAH ("worst headache of life")
  Meningitis (fever + nuchal rigidity)
  IIH (pseudotumor cerebri)
  Temporal arteritis (>50yo, jaw claudication, ESR↑↑)
  Cervicogenic, medication overuse (rebound)
```

### Migraine — Trigeminovascular Pathway

```
Trigger (hormonal/stress/sleep/food/sensory)
      │
      ▼
Cortical spreading depression (CSD) — aura
  Wave of neuronal/glial depolarization at ~3–5 mm/min
  Spreading oligemia → hyperemia
      │
      ▼
Trigeminal nerve activation
  Releases CGRP, substance P → meningeal vessel dilation/inflammation
      │
      ▼
Trigeminal nucleus caudalis (dorsal horn equivalent) → thalamus → cortex
      │
Throbbing head pain (pulsatile, unilateral, nausea/vomiting, photo/phonophobia)
```

**CGRP (calcitonin gene-related peptide):** Potent vasodilator; released at trigeminal terminals → key target.
- **Triptans** (sumatriptan, rizatriptan): 5-HT1B/D agonists → vasoconstriction + ↓ CGRP release
- **Gepants** (ubrogepant, rimegepant): CGRP receptor antagonists; safe in CV disease
- **Ditans** (lasmiditan): 5-HT1F agonist; no vasoconstriction; CNS side effects
- **Anti-CGRP mAbs** (erenumab → receptor; fremanezumab/galcanezumab → ligand): Monthly SC injection for prevention

**Cluster headache:** Trigeminal autonomic reflex; circadian rhythm suggests hypothalamic involvement. Attacks: periorbital, ipsilateral lacrimation/rhinorrhea/Horner's, excruciating, 15–180 min. 100% O₂ + SC triptan for acute; verapamil, lithium, melatonin for prevention.

---

## 9. Depression

### Monoamine Hypothesis + HPA Dysregulation

```
MONOAMINE HYPOTHESIS (original, still useful):
  ↓ Serotonin (5-HT) in synapse → depression
  ↓ Norepinephrine (NE) → depression + cognitive/energy symptoms
  ↓ Dopamine (DA) → anhedonia, motivation deficits

  Evidence: reserpine (VMAT2 inhibitor → depletes monoamines) → depression
  Problem: antidepressants ↑ monoamines in hours but clinical effect takes weeks
           → hypothesis incomplete; downstream neuroplasticity changes more important

HPA AXIS DYSREGULATION:
  Chronic stress → ↑ CRH → ↑ ACTH → ↑ cortisol
  ↑ Cortisol → hippocampal volume loss (glucocorticoid neurotoxicity)
  Impaired GR feedback → hypercortisolism persists

NEUROPLASTICITY / BDNF HYPOTHESIS (modern):
  Depression: ↓ BDNF → synaptic loss in hippocampus/PFC
  Antidepressants → ↑ BDNF (via CREB phosphorylation) → synaptogenesis
  Ketamine: NMDA block → immediate AMPA/BDNF signaling → rapid antidepressant
```

**Treatment ladder:**

```
1st line: SSRI (fluoxetine/sertraline/escitalopram) or SNRI
           MAO: block 5-HT/NE reuptake transporter (SERT/NET)
           Onset: 2–4 weeks for full effect

2nd line: Augmentation (add bupropion/mirtazapine/lithium/atypical antipsychotic)
           Switch SSRI to SNRI or TCA

Treatment-resistant (≥2 adequate trials):
  Ketamine/esketamine (NMDA antagonist → AMPA/BDNF → rapid effect)
  ECT (electroconvulsive therapy): most effective antidepressant; ↑ BDNF/hippocampal neurogenesis
  TMS (transcranial magnetic stimulation): DLPFC target
  MAOIs (irreversible — tyramine-free diet required)
  Psilocybin (investigational — serotonergic; neuroplasticity)
```

---

## 10. Schizophrenia

### Dopamine Imbalance Model

```
MESOLIMBIC pathway (VTA → NAc/limbic):
  DA HYPERACTIVITY → positive symptoms
  Hallucinations (auditory most common), delusions, thought disorganization

MESOCORTICAL pathway (VTA → PFC):
  DA HYPOACTIVITY → negative symptoms + cognitive impairment
  Flat affect, alogia, avolition, anhedonia
  Working memory deficits (DLPFC)

TUBEROINFUNDIBULAR pathway (hypothalamus → anterior pituitary):
  D2 blockade by antipsychotics → ↑ prolactin → galactorrhea/sexual dysfunction

NIGROSTRIATAL pathway (SNpc → striatum):
  D2 blockade → EPS (extrapyramidal symptoms: parkinsonism/dystonia/akathisia/TD)
```

**Glutamate hypothesis (complementary):**
- NMDA receptor hypofunction → disinhibition of glutamatergic projection neurons
- PCP/ketamine model: NMDA antagonists reproduce positive + negative + cognitive symptoms
- Explains mesocortical DA hypoactivity (GABA interneuron failure → DA disinhibition in mesolimbic)

**Antipsychotics:**
| Class | Mechanism | EPS risk | Metabolic | Examples |
|-------|-----------|---------|-----------|---------|
| 1st gen (typical) | D2 block (high affinity) | ↑↑ | Low | Haloperidol, chlorpromazine |
| 2nd gen (atypical) | D2 + 5-HT2A block | ↓ | ↑ (clozapine/olanzapine) | Clozapine, olanzapine, quetiapine, risperidone |
| 3rd gen | Partial D2 agonist | Very low | Low | Aripiprazole, brexpiprazole, cariprazine |

**Clozapine:** Most effective antipsychotic (treatment-resistant); agranulocytosis risk (1–2%) → mandatory ANC monitoring (REMS program).

**Tardive dyskinesia (TD):** D2 supersensitivity after chronic block → involuntary orofacial movements; treat with VMAT2 inhibitors (valbenazine, deutetrabenazine).

---

## 11. Addiction

### Reward Circuit

```
Natural reward (food/sex/social): ─────────────────────┐
Drug reward: cocaine/amphetamine (↑ DA via DAT block)   │
             opioids (↑ DA via μ-opioid on VTA GABA)    ▼
             alcohol/nicotine/cannabis
                                            VTA (ventral tegmental area)
                                                 │
                                      ┌──────────┘
                                      │ Dopamine release
                                      ▼
                         NAc (nucleus accumbens) — reward
                         PFC — decision-making, impulse control
                         Amygdala — cue association, craving
                         Hippocampus — context memory
```

**Neuroplasticity of addiction (ΔFosB model):**
```
Acute drug use: ↑ FosB (rapidly degraded)
Repeated exposure: ΔFosB (truncated isoform, stable) accumulates in striatum
ΔFosB → transcriptional changes:
   ↑ GluA2 (AMPA subunit) → synaptic potentiation in NAc
   ↑ CREB → ↓ reward sensitivity (tolerance)
   ↑ CDK5 → spine morphology changes

ΔFosB persists weeks after cessation → long-term sensitization → craving/relapse
```

**Opioid system:**
- μ receptors: euphoria, analgesia, respiratory depression, constipation
- Tolerance: receptor desensitization/internalization (GRK/β-arrestin2)
- Physical dependence: LC noradrenergic hyperactivity during withdrawal (↑ cAMP rebound)
- **Naltrexone:** μ antagonist; blocks reward; OUD + alcohol use disorder
- **Methadone/buprenorphine:** OUD MAT; buprenorphine = partial μ agonist + κ antagonist; ceiling on respiratory depression; Suboxone (+ naloxone to deter IV misuse)
- **Naloxone:** rapid reversal of acute OD; short half-life < fentanyl

---

## Decision Cheat Sheet

| Disease | Hallmark Pathology | Key Gene/Mechanism | Disease-Modifying Rx? |
|---------|-------------------|-------------------|----------------------|
| Alzheimer's | Aβ plaques + NFTs | APOE ε4 risk; PSEN1 FAD | Anti-Aβ mAbs (lecanemab) |
| Parkinson's | Lewy bodies (α-synuclein) | LRRK2, PINK1/Parkin | No (L-DOPA symptomatic) |
| ALS | TDP-43 inclusions | C9orf72, SOD1 | Riluzole (modest) |
| Huntington's | Striatal atrophy | CAG ≥40 (HTT) | No |
| Epilepsy | Neuronal hyperexcitability | SCN1A, KCNQ2 | AEDs (seizure control, not disease) |
| GBS | Demyelination (PNS) | Post-infectious (anti-ganglioside) | IVIg/plasmapheresis |
| Migraine | CSD + CGRP | Trigeminovascular | Anti-CGRP mAbs (prevention) |
| Depression | ↓ BDNF, HPA activation | — | SSRI/SNRI/ketamine/ECT |
| Schizophrenia | DA imbalance | — | Antipsychotics (symptom control) |

---

## Common Confusion Points

**AD amyloid vs tau — which causes disease?**
Amyloid seeding is upstream (driver per cascade hypothesis); tau spread correlates better with clinical severity. Both required; drugs targeting amyloid help only pre-symptomatic/early stage.

**PD tremor vs Essential tremor:**
PD = resting tremor (disappears with action), asymmetric. ET = action/postural tremor, bilateral, often head/voice, alcohol responsive, no rigidity/bradykinesia.

**UMN vs LMN signs (ALS has both):**
UMN: spasticity, hyperreflexia, Babinski+, weakness. LMN: flaccidity, fasciculations, atrophy, hyporeflexia. ALS uniquely has both simultaneously.

**Seizure vs epilepsy:**
A seizure is an event; epilepsy is ≥2 unprovoked seizures (or 1 with high recurrence risk). Febrile seizures ≠ epilepsy.

**SSRI mechanism latency:** SSRIs block SERT immediately → ↑ synaptic 5-HT. But antidepressant effect takes 2–4 weeks because downstream receptor desensitization (5-HT1A autoreceptor) and BDNF-mediated neuroplasticity take time. Ketamine bypasses this (hours).

**Schizophrenia — why atypicals help negative symptoms?**
5-HT2A blockade disinhibits mesocortical DA (via 5-HT2A on pyramidal neurons) → modest ↑ prefrontal DA → some negative symptom benefit. But mesocortical improvement limited.

**Triptans contraindicated in CAD/stroke:** Triptans are vasoconstrictors (5-HT1B). Use gepants in vascular disease. Cluster headache with triptans: safe short-term; high-flow O₂ 100% is first choice.

**Addiction: dependence ≠ addiction:** Physical dependence (tolerance + withdrawal) is an expected pharmacological adaptation; occurs with opioids prescribed for legitimate pain. Addiction = compulsive use despite harm + craving + loss of control. Can have dependence without addiction.
