# Pharmacology — Landscape and Taxonomy

## The Big Picture

Pharmacology is the science of how drugs interact with biological systems — where "drug" means any chemical that alters a biological process. It bridges chemistry, physiology, and medicine.

```
+──────────────────────────────────────────────────────────────────+
|                  PHARMACOLOGY LANDSCAPE                          |
|                                                                  |
|  PHARMACOKINETICS (PK)        PHARMACODYNAMICS (PD)             |
|  "What the body does          "What the drug does               |
|   to the drug"                 to the body"                     |
|  ────────────────             ────────────────────              |
|  Absorption                   Receptor binding                  |
|  Distribution                 Signal transduction               |
|  Metabolism                   Dose-response                     |
|  Excretion                    EC50, Emax                        |
|  Half-life, Cmax              Therapeutic index                 |
|                                                                  |
|  PK/PD RELATIONSHIP                                              |
|  Drug concentration in plasma (PK) → Effect at target (PD)      |
|                                                                  |
+─────────────────────────────────────────────────────────────────+
|                DRUG DEVELOPMENT PIPELINE                         |
|                                                                  |
|  Target  → Lead   → Preclinical → Phase I → Phase II →          |
|  ID         discovery  testing      Safety    Efficacy           |
|               → Phase III → FDA review → Market → PV            |
|                  Large RCT          NDA/BLA      Surveillance    |
+──────────────────────────────────────────────────────────────────+
```

---

## Core Conceptual Axes

```
AXIS 1: SITE OF ACTION
  ┌─────────────────────────────────────────────┐
  │ Extracellular:  Receptors (GPCR, ligand-gated ions)        │
  │ Cell surface:   Enzymes, transporters, growth factor Rs     │
  │ Intracellular:  Nuclear receptors, intracellular enzymes    │
  │ Nucleic acid:   DNA intercalation, RNA-targeting            │
  └─────────────────────────────────────────────┘

AXIS 2: TYPE OF DRUG-TARGET INTERACTION
  Agonist:      Activates receptor → full or partial response
  Antagonist:   Blocks receptor → no activation
  Inverse agonist: Activates constitutively active receptor DOWNWARD
  Allosteric:   Binds non-active site → modulates activity indirectly

AXIS 3: REVERSIBILITY
  Reversible:   Drug-receptor complex dissociates; equilibrium dynamics
  Irreversible: Covalent bond; effect lasts until new protein synthesized

AXIS 4: PHARMACOKINETIC PROPERTIES
  Lipophilicity ↔ Aqueous solubility (Lipinski's rule of 5)
  First-pass metabolism (oral bioavailability)
  Protein binding (free drug fraction)
  Volume of distribution (tissue penetration)
```

---

## Drug Classes by Mechanism

```
+─────────────────────────────────────────────────────────────────+
|              MAJOR DRUG MECHANISMS                               |
|                                                                  |
|  RECEPTOR-ACTING                                                 |
|  ────────────────                                                |
|  GPCR agonists/antagonists: β-blockers, opioids, antipsychotics  |
|  Ion channel modulators:    calcium channel blockers, lidocaine  |
|  Nuclear receptor ligands:  steroids, thyroid hormone, retinoids |
|                                                                  |
|  ENZYME-INHIBITING                                               |
|  ─────────────────                                               |
|  ACE inhibitors: cardiovascular (lisinopril)                     |
|  COX inhibitors: anti-inflammatory (aspirin, ibuprofen)          |
|  Kinase inhibitors: cancer (imatinib/Gleevec)                    |
|  Protease inhibitors: HIV (ritonavir), HCV (boceprevir)          |
|  Acetylcholinesterase inhibitors: Alzheimer's (donepezil)        |
|                                                                  |
|  TRANSPORTER-TARGETING                                           |
|  ─────────────────────                                           |
|  SSRIs: block serotonin reuptake (fluoxetine/Prozac)             |
|  SNRIs: block serotonin + NE reuptake (venlafaxine)              |
|  Proton pump inhibitors: block H+/K+-ATPase (omeprazole)         |
|                                                                  |
|  DNA/RNA-TARGETING                                               |
|  ─────────────────                                               |
|  Alkylating agents: crosslink DNA (cyclophosphamide)             |
|  Topoisomerase inhibitors: unwind DNA (doxorubicin, CPT-11)      |
|  Antimetabolites: fake nucleotides (methotrexate, 5-FU)          |
|  Antisense / siRNA: RNA targeting                                |
+─────────────────────────────────────────────────────────────────+
```

---

## The ADME Cycle

```
ORAL DRUG JOURNEY
─────────────────

  [Tablet/capsule]
       │
       v  Dissolution in stomach/intestine
  [Free drug in GI lumen]
       │
       v  Absorption through intestinal epithelium
  [Portal blood]
       │
       v  First-pass metabolism in liver (CYP enzymes)
  [Systemic circulation]   ← Cmax, Tmax measured here
       │
       ├─→ Distribution: plasma protein binding, tissue distribution
       │    Vd = how widely distributed
       │
       ├─→ Metabolism: liver CYP enzymes → metabolites (active or inactive)
       │    T½ = half-life
       │
       └─→ Excretion: kidney (filtration/secretion), bile, sweat, lungs
            Clearance = rate of removal

F (bioavailability) = fraction of dose reaching systemic circulation
F_oral = F_absorption × F_first-pass = often 10-80% depending on drug
```

---

## Therapeutic Index and Safety Window

```
THERAPEUTIC INDEX (TI)
───────────────────────
  TI = TD50 / ED50

  ED50 = dose effective in 50% of population
  TD50 = dose toxic in 50% of population

  High TI (e.g., penicillin, TI > 100): wide safety margin
  Low TI (e.g., warfarin, digoxin, TI < 10): narrow safety margin

  ←─ Safe ──→ ← Therapeutic window → ← Toxic ─→
  ____________|_______________________________|____________
              ED10                            TD10

  The narrower the window, the more precise the dosing must be.
  Low TI drugs require blood level monitoring.
```

---

## Module Map

| Module | Core Concepts |
|--------|--------------|
| 01-RECEPTOR-THEORY | Receptor types, affinity, agonism, antagonism, efficacy |
| 02-PHARMACOKINETICS | ADME, half-life, volume of distribution, clearance, bioavailability |
| 03-PHARMACODYNAMICS | Dose-response curve, EC50, Emax, therapeutic index, efficacy vs potency |
| 04-CYP-METABOLISM | CYP450 enzymes, inducers, inhibitors, drug-drug interactions |
| 05-CNS-PHARMACOLOGY | Neurotransmitter systems, BBB, psychopharmacology |
| 06-CARDIOVASCULAR | Antihypertensives, antiarrhythmics, heart failure drugs, statins |
| 07-CHEMOTHERAPY | Mechanism classes, combination therapy, resistance |
| 08-DRUG-DEVELOPMENT | Discovery pipeline, preclinical, phases I-III, regulatory approval |
| 09-PERSONALIZED | Pharmacogenomics, SNPs, CYP variants, precision dosing |

---

## Key Numbers to Internalize

| Parameter | Typical Values | Notes |
|-----------|---------------|-------|
| Therapeutic drug concentration | ng/mL to μg/mL | Varies widely |
| Oral bioavailability | 10–100% | First-pass limited |
| Protein binding (typical drug) | 70–99% | Free fraction = active |
| Volume of distribution | 0.04–100 L/kg | Plasma → 0.04; high-tissue → >10 |
| Half-life | Minutes to weeks | Determines dosing interval |
| Renal clearance max | ~GFR = 120 mL/min | + secretion can exceed this |
| CYP3A4 fraction of drugs metabolized | ~50% | Most important CYP |

---

## Engineering Bridge: Pharmacology as Systems Engineering

The drug development pipeline and PK/PD framework map directly onto systems engineering and software release processes.

```
  PHARMACOLOGY                  SYSTEMS ENGINEERING / SOFTWARE PARALLEL
  ──────────────────────────────────────────────────────────────────────
  Drug development pipeline     Software release pipeline:
    Target identification       → Requirements definition
    Lead discovery              → Architecture / proof-of-concept
    Preclinical testing         → Unit + integration testing
    IND filing                  → Design review gate
    Phase I (safety)            → Alpha / internal testing
    Phase II (efficacy signal)  → Beta / limited rollout
    Phase III (confirmatory RCT)→ GA candidate / staged rollout
    FDA review                  → Compliance certification / audit
    Post-marketing surveillance → Production monitoring / incident response
    REMS programs               → Privileged access controls

  PK (pharmacokinetics)         System state evolution:
    One-compartment model: C(t) = C₀·e^{-k_el·t}
    → First-order linear system, exponential decay to zero.
    Two-compartment model: biexponential
    → Two-pole transfer function; fast central pool, slow peripheral.
    Volume of distribution Vd   → Total buffer capacity
    Clearance CL                → Drain rate
    Half-life t½ = 0.693·Vd/CL → System time constant

  PD (pharmacodynamics)         Transfer function / input-output model:
    E = Emax·Cⁿ/(EC50ⁿ + Cⁿ)
    → Hill/sigmoidal: a saturating nonlinear transfer function.
    Identical in form to a logistic activation function or a
    Hill-type cooperative binding curve in control systems.
    EC50 is the half-saturation point (operating point of the system).

  PK/PD link model              Cascade model with lag:
  (effect compartment)          Effect lags behind plasma concentration
                                → first-order lag system (low-pass filter).
                                Hysteresis loops (E vs. C clockwise vs.
                                counterclockwise) distinguish absorption
                                lag (counter-clockwise) from tolerance
                                (clockwise).

  CYP enzyme induction/inhibition Shared resource contention:
  (drug-drug interactions)      CYP3A4 is a shared processing pool.
                                Inhibitor = job holding the thread pool;
                                victim substrate = starved job waiting for
                                worker. Inducer = autoscaling (spinning up
                                more workers). DDI risk = priority inversion.

  Therapeutic index TI = TD50/ED50  Safety margin = (failure threshold) /
                                (operating level). Narrow TI drugs (warfarin,
                                digoxin) require tight control — analogous
                                to systems with small stability margins that
                                need closed-loop feedback (drug level monitoring).
  ──────────────────────────────────────────────────────────────────────
```

---

## Decision Cheat Sheet

| Question | Pharmacology Concept | Key Parameter |
|----------|---------------------|---------------|
| How potent is drug A vs B? | Pharmacodynamics | EC50 (lower = more potent) |
| How big a maximum effect? | Pharmacodynamics | Emax / Efficacy |
| How long until drug clears? | Pharmacokinetics | Half-life (t½) |
| How widely distributed in tissues? | Pharmacokinetics | Volume of distribution (Vd) |
| How safe is the therapeutic dose? | Both | Therapeutic index (TI = TD50/ED50) |
| Will drug A affect drug B levels? | CYP metabolism | Enzyme induction/inhibition |
| Why isn't oral drug working? | Pharmacokinetics | Bioavailability (F), first-pass |
| Genetic variation in drug response? | Pharmacogenomics | CYP polymorphisms, HLA typing |

---

## Common Confusion Points

**"Efficacy vs potency — they sound the same"**
Efficacy = maximum effect achievable. Potency = how much drug is needed to get a given effect (EC50). A drug can be highly potent (tiny doses work) but have low efficacy (ceiling effect). Morphine has high efficacy (full agonist); buprenorphine has lower efficacy (partial agonist) but is more potent (lower EC50).

**"Receptor affinity vs binding — same?"**
Affinity = thermodynamic measure of how tightly drug binds receptor (Kd = equilibrium dissociation constant). Binding = the event. High affinity = low Kd (binds tightly, dissociates slowly). Affinity doesn't tell you what happens after binding (agonist vs antagonist vs allosteric).

**"Why does distribution affect half-life?"**
Half-life = 0.693 × Vd / Clearance. High Vd = drug stored in tissues = slow elimination = long half-life. Amiodarone has enormous Vd (60 L/kg) and a half-life of 40-55 days. Meaning: after stopping amiodarone, it takes months to leave the body.
