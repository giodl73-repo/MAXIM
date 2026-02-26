# CNS Pharmacology: Neurotransmitters and Targets

## The Big Picture

CNS pharmacology targets the chemical signaling systems of the brain. Each major neurotransmitter system has distinct anatomy, receptor types, and drugs that modulate it. The blood-brain barrier is an additional PK constraint.

```
+──────────────────────────────────────────────────────────────────+
|              CNS PHARMACOLOGY LANDSCAPE                          |
|                                                                  |
|  MAJOR NEUROTRANSMITTER SYSTEMS AND TARGET DRUG CLASSES          |
|                                                                  |
|  DOPAMINE      → Antipsychotics, ADHD drugs, Parkinson's drugs   |
|  SEROTONIN     → Antidepressants, antiemetics, triptans          |
|  NOREPINEPHRINE → Antidepressants (SNRIs), ADHD drugs            |
|  GABA          → Anxiolytics, anesthetics, anticonvulsants       |
|  GLUTAMATE     → Anesthetics (ketamine), NMDA modulators         |
|  ACETYLCHOLINE → Alzheimer's drugs, muscle relaxants             |
|  OPIOID PEPTIDES → Analgesics, addiction drugs                   |
|                                                                  |
|  BLOOD-BRAIN BARRIER (BBB)                                       |
|  All CNS drugs must cross: lipophilic, small, non-P-gp-substrate  |
|  Or use active transporters (L-dopa transporter for dopamine)    |
+──────────────────────────────────────────────────────────────────+
```

---

## The Blood-Brain Barrier

```
BBB STRUCTURE AND FUNCTION
────────────────────────────
  Brain capillary endothelial cells joined by TIGHT JUNCTIONS.
  No fenestrations (unlike peripheral capillaries).
  Surrounded by astrocyte end-feet.
  Expresses P-glycoprotein (P-gp) efflux pump on luminal side.

  FACTORS FOR CNS PENETRATION
  Good:                          Bad:
  Low MW (< 400-450 Da)         Large MW (antibodies, peptides)
  High lipophilicity (logP > 1)  Low lipophilicity (aminoglycosides)
  Low plasma protein binding     High P-gp substrate activity
  Unionized at physiologic pH    Ionized at physiologic pH

  CLINICAL IMPLICATIONS
  Most antibiotics: poor CNS penetration
    → Exception: chloramphenicol, metronidazole, fluoroquinolones
    → For bacterial meningitis: need drugs with CNS penetration
       PLUS inflamed BBB (meningitis increases permeability)

  L-DOPA STRATEGY FOR PARKINSON'S
    Dopamine itself cannot cross BBB.
    L-dopa (precursor) uses amino acid transporter → crosses BBB.
    Once in brain: decarboxylated → dopamine.
    Given with carbidopa (peripheral decarboxylase inhibitor)
    → prevents L-dopa → dopamine conversion OUTSIDE brain.
    → More L-dopa reaches brain; less peripheral dopamine side effects.
```

---

## Dopamine System

```
DOPAMINE PATHWAYS
──────────────────
  Pathway           Origin                Destination         Function
  ──────────────────────────────────────────────────────────────────────
  Mesolimbic        VTA                   Nucleus accumbens   Reward, motivation
                                          (limbic system)     ADDICTION target
  Mesocortical      VTA                   Prefrontal cortex   Cognition, working memory
                                                              NEGATIVE symptoms in SCZ
  Nigrostriatal     Substantia nigra      Striatum            Motor control
                                                              MOVEMENT; Parkinson's
  Tuberoinfundibular Hypothalamus         Pituitary           Prolactin inhibition
                                                              Side effect: hyperprolactinemia

DOPAMINE RECEPTORS
  D1/D5 (Gs): ↑cAMP → activation. Prefrontal function.
  D2/D3/D4 (Gi): ↓cAMP → inhibition. Reward, motor, antipsychotic target.

ANTIPSYCHOTICS (D2 antagonists)
  Typical antipsychotics (1st gen): Haloperidol, chlorpromazine
    Strong D2 blockade → treats positive symptoms (psychosis)
    BUT: blocks nigrostriatal → EPS (extrapyramidal symptoms)
         blocks tuberoinfundibular → hyperprolactinemia
         blocks muscarinic, histamine → anticholinergic, sedation

  Atypical antipsychotics (2nd gen): Clozapine, olanzapine, quetiapine
    D2 blockade PLUS 5-HT2A blockade (and others)
    Fewer EPS; improved negative symptoms
    New side effects: metabolic syndrome, weight gain (clozapine)
    Clozapine: most effective but agranulocytosis risk (1%) → CBC monitoring

PARKINSONS PHARMACOLOGY (dopamine replacement)
  L-dopa + carbidopa (Sinemet): gold standard
  Dopamine agonists: pramipexole, ropinirole (bypass neuronal conversion)
  MAO-B inhibitors: selegiline, rasagiline (slow dopamine breakdown)
  COMT inhibitors: entacapone (block peripheral L-dopa metabolism)
```

---

## Serotonin System

```
SEROTONIN (5-HT) RECEPTORS
────────────────────────────
  5-HT1A:  Gi; autoreceptor; anxiolytic target (buspirone)
  5-HT2A:  Gq; psychedelic target; antipsychotic target (blockade)
  5-HT3:   Ion channel; antiemetic target (ondansetron)
  5-HT4:   Gs; GI motility target (prokinetics)

ANTIDEPRESSANTS: THE REUPTAKE TRANSPORTER CASCADE
  Presynaptic terminal releases 5-HT → binds postsynaptic receptor.
  Serotonin reuptake transporter (SERT) clears 5-HT from synapse.
  Antidepressants block SERT → ↑ synaptic 5-HT.

  DRUG CLASS    MECHANISM               EXAMPLES
  ─────────────────────────────────────────────────────────────────
  SSRIs         SERT inhibitor          Fluoxetine, sertraline, escitalopram
  SNRIs         SERT + NET inhibitor    Venlafaxine, duloxetine
  TCAs          SERT + NET + multiple   Amitriptyline, nortriptyline
                off-targets
  MAOIs         MAO inhibitor           Phenelzine, tranylcypromine
                → ↓5-HT degradation     (irreversible; tyramine reaction)

SEROTONIN SYNDROME
  Caused by excess serotonergic activity (SSRI + MAOI, or SSRI + tramadol)
  Triad: mental status change + neuromuscular abnormalities + autonomic instability
  Mechanism: overstimulation of 5-HT1A and 5-HT2A receptors
  Severe cases: hyperthermia, clonus, rhabdomyolysis, death
  Treatment: stop serotonergic drugs; cyproheptadine (5-HT antagonist)
  Distinguished from NMS (neuroleptic malignant syndrome, dopamine-related).

ANTIEMETICS
  Ondansetron: 5-HT3 antagonist → blocks vagal afferents in gut + CTZ
  Used for: chemotherapy-induced nausea, post-op nausea
  5-HT3 is the key emesis receptor in vagal afferents.
```

---

## GABA System

```
GABA: BRAIN'S PRIMARY INHIBITORY NEUROTRANSMITTER
──────────────────────────────────────────────────
  GABA_A: Ligand-gated Cl⁻ channel → hyperpolarization → inhibition
  GABA_B: GPCR (Gi) → ↓cAMP + ↑K+ channels → slower inhibition

DRUGS ACTING ON GABA_A
  Drug Class       Site                 Effect           Examples
  ───────────────  ────────────────     ─────────────    ─────────────────────
  Benzodiazepines  BZD site (allosteric) ↑Cl- influx    Diazepam, lorazepam
                                        frequency        Alprazolam, midazolam
  Barbiturates     Barbiturate site     ↑Cl- influx     Phenobarbital, thiopental
                                        duration         (can fully activate alone!)
  General          Various sites        Enhance GABA    Propofol, etomidate
  anesthetics                          at high doses
  Neurosteroids    Neurosteroid site    ↑Cl- influx     Brexanolone (postpartum depression)
  Z-drugs          BZD site (ω₁ select) Selective for   Zolpidem, zaleplon
                                        sleep circuits
  Flumazenil       BZD site            Competitive      Reverse BZD overdose
                                        antagonist

CRITICAL DIFFERENCE: BZDs vs BARBITURATES
  BZDs: Allosteric modulator. REQUIRE GABA to be present.
        Cannot fully activate GABA_A alone.
        CEILING EFFECT → safe in overdose alone.
  Barbiturates: Can activate GABA_A WITHOUT GABA.
                No ceiling effect → lethal in overdose.
  This is why BZDs replaced barbiturates as anxiolytics.

GABA_B DRUGS
  Baclofen: GABA_B agonist → muscle relaxant, alcohol/opioid withdrawal
  Gabapentin/pregabalin: NOT GABA agonists despite names!
    Actually block α2δ subunit of voltage-gated Ca²⁺ channels
    → Reduce neurotransmitter release → anticonvulsant, neuropathic pain
```

---

## Glutamate System

```
GLUTAMATE: BRAIN'S PRIMARY EXCITATORY NEUROTRANSMITTER
─────────────────────────────────────────────────────────
RECEPTORS
  AMPA (ionotropic): Fast excitatory transmission; Na+ influx
  NMDA (ionotropic): Ca²+ influx; requires BOTH glutamate + glycine
                     Mg²+ blocks channel at rest (voltage-dependent)
                     Long-term potentiation (LTP) → memory
  Kainate (ionotropic): Na+ influx; epilepsy role
  mGluR (metabotropic): Modulate transmission; various effects

NMDA ANTAGONISTS (clinical drugs)
  Ketamine: Dissociative anesthetic; NMDA channel blocker
            Anesthesia at high doses; rapid-acting antidepressant at low doses
            Subanesthetic ketamine = first new mechanism for depression in decades
            Esketamine (Spravato): FDA-approved intranasal for treatment-resistant depression
            Mechanism: may activate mTOR signaling in prefrontal cortex → synaptogenesis

  Memantine: Low-affinity, voltage-dependent NMDA antagonist
             At pathological [glutamate] (as in Alzheimer's): blocks channel
             At physiological [glutamate]: less blocking → normal signaling preserved
             Used for moderate-severe Alzheimer's; modest symptomatic benefit

  Phencyclidine (PCP/angel dust): Potent NMDA antagonist
             At high doses: psychosis indistinguishable from schizophrenia
             → NMDA hypofunction hypothesis of schizophrenia.
```

---

## Opioid System

```
OPIOID RECEPTORS AND DRUGS
────────────────────────────
  RECEPTOR    G-PROTEIN   ANALGESIA  RESPIRATORY  EUPHORIA   PHYSICAL
  TYPE                               DEPRESSION              DEPENDENCE
  ─────────────────────────────────────────────────────────────────────
  μ (mu)      Gi           +++        +++          +++        +++
  κ (kappa)   Gi           ++         +            - (dysphoric) +
  δ (delta)   Gi           +          +            +           +
  NOP/ORL-1   Gi           +/-        -            -           -

DRUG CHART
  Drug                  Receptor           Classification
  ──────────────────    ────────────────   ─────────────────────────────
  Morphine              μ full agonist     Gold standard analgesic
  Fentanyl              μ full agonist     100× more potent; IV/patch/lozenge
  Heroin (diacetylmorphine) μ full agonist Prodrug → morphine; high euphoria
  Methadone             μ full agonist     Long t½; NMDA antagonist; addiction rx
  Buprenorphine         μ partial agonist  Ceiling effect; addiction treatment
  Naloxone (Narcan)     μ antagonist       Reversal of overdose; short-acting
  Naltrexone            μ antagonist       Long-acting; addiction maintenance
  Codeine               Prodrug → morphine CYP2D6 dependent (see Module 04)
  Tramadol              μ weak agonist     Also SNRI; CYP2D6 for active metabolite
                        + SNRI activity

RESPIRATORY DEPRESSION — THE LETHAL MECHANISM
  μ-opioid receptors in brainstem respiratory centers → ↓ rate and depth.
  All μ-agonists cause this; it's dose-dependent.
  Tolerance develops to analgesia but NOT fully to respiratory depression.
  Opioid overdose: triad of miosis, coma, respiratory depression.
  Reversal: naloxone (IV/IM/IN); may need repeated doses for fentanyl.
```

---

## Cholinergic System

```
ACETYLCHOLINE RECEPTORS
────────────────────────
  Nicotinic (nAChR):  Ionotropic (Na+/Ca²+); skeletal muscle NMJ, ganglia
  Muscarinic (mAChR): GPCR (M1-M5); heart, smooth muscle, glands, CNS

DRUGS
  Acetylcholinesterase inhibitors (↑ synaptic ACh):
    Physostigmine: CNS penetrating; anticholinergic toxicity reversal
    Neostigmine:   Quaternary; no CNS; reversal of neuromuscular blockade
    Donepezil, rivastigmine: Alzheimer's disease (symptomatic only)
    Pyridostigmine: myasthenia gravis

  Muscarinic antagonists:
    Atropine:       ↑HR, mydriasis, dry, bronchodilation
    Scopolamine:    Motion sickness (CNS muscarinic)
    Ipratropium:    Bronchodilator (COPD); doesn't cross BBB
    Oxybutynin:     Overactive bladder (M3 selectivity)
    Benztropine:    Parkinson's; drug-induced EPS

  Nicotinic blockers (NMJ):
    Succinylcholine: Depolarizing; for rapid sequence intubation
    Rocuronium/vecuronium: Non-depolarizing; reversed by sugammadex

ALZHEIMER'S PHARMACOLOGY
  Cholinergic hypothesis: loss of ACh neurons in hippocampus/cortex.
  Approach 1: AChE inhibitors (donepezil, rivastigmine, galantamine)
    → Modest symptomatic improvement; don't slow progression.
  Approach 2: Memantine (NMDA antagonist) for moderate-severe.
  Approach 3 (newer): Anti-amyloid antibodies
    Lecanemab, donanemab: slow progression by ~35%; ARIA (brain edema) risk.
```

---

## Decision Cheat Sheet

| Drug Class | Neurotransmitter | Receptor Target | Main Clinical Use |
|------------|-----------------|-----------------|------------------|
| SSRIs/SNRIs | Serotonin (±NE) | SERT blockade | Depression, anxiety |
| Typical antipsychotics | Dopamine | D2 blockade | Psychosis |
| Atypical antipsychotics | Dopamine + serotonin | D2 + 5HT2A block | Psychosis + fewer EPS |
| Benzodiazepines | GABA | GABA_A (BZD site) | Anxiety, sedation, seizures |
| Opioids (full agonist) | Opioid peptides | μ-receptor | Analgesia |
| Buprenorphine | Opioid peptides | μ-partial agonist | Addiction treatment |
| Naloxone | Opioid peptides | μ-antagonist | Overdose reversal |
| L-dopa + carbidopa | Dopamine | Dopamine precursor | Parkinson's |
| Memantine | Glutamate | NMDA antagonist | Alzheimer's (moderate-severe) |
| AChE inhibitors | ACh | Prevents ACh breakdown | Alzheimer's (mild-moderate) |

---

## Common Confusion Points

**"If benzodiazepines and barbiturates both enhance GABA — why is one safer?"**
BZDs require GABA to be present — they amplify GABA-A receptor activity allosterically. Without GABA, no effect. This creates a ceiling. Barbiturates can directly gate the channel in absence of GABA — no ceiling — respiratory depression at high doses. This is why BZD overdose alone rarely kills; barbiturate overdose can.

**"SSRIs take 2-6 weeks to work — isn't that because levels take 2-6 weeks to build?"**
No. SSRI levels reach steady state in 5 half-lives (5-7 days). The 2-6 week delay is neuroplastic: gradual 5-HT receptor downregulation, synaptogenesis, and hippocampal neurogenesis. The fast pharmacokinetic effect is not the mechanism — the slow neuroplastic adaptation is. This is why ketamine (different mechanism, direct NMDA blockade → mTOR → synaptogenesis) works in hours, not weeks.

**"Why is naloxone short-acting but fentanyl isn't?"**
Naloxone half-life is 30-90 minutes. Fentanyl's half-life is 2-4 hours. In fentanyl overdose, naloxone wears off before fentanyl does → patient re-narcoticizes. Standard practice: give naloxone, observe 4-6 hours minimum, may repeat doses or use continuous IV infusion. With synthetic opioids (carfentanil), multiple large doses of naloxone may be needed.
