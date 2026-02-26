# Pharmacokinetics: ADME

## The Big Picture

Pharmacokinetics (PK) describes the time course of drug concentration in the body. It answers: how much drug reaches the target, when, and for how long? ADME is the four-process framework: Absorption, Distribution, Metabolism, Excretion.

```
+──────────────────────────────────────────────────────────────────+
|                  PHARMACOKINETIC LANDSCAPE                       |
|                                                                  |
|  [DOSE administered]                                             |
|       │                                                          |
|       v Absorption (A)                                           |
|  [Drug in systemic circulation] ── Plasma concentration-time   |
|       │                            curve: Cmax, Tmax, AUC       |
|       v Distribution (D)                                         |
|  [Drug in tissues / bound to proteins]                           |
|       │                                                          |
|       v Metabolism (M) — mainly liver CYP enzymes               |
|  [Drug → Metabolites] (active or inactive)                      |
|       │                                                          |
|       v Excretion (E) — mainly kidney, some bile               |
|  [Drug / metabolites eliminated]                                 |
|                                                                  |
|  MASTER EQUATION: Concentration(t) = f(A, D, M, E, dose, time)  |
+──────────────────────────────────────────────────────────────────+
```

---

## Absorption

```
ORAL ABSORPTION
────────────────
  1. Disintegration of tablet/capsule
  2. Dissolution into GI fluid
  3. Transport across intestinal epithelium:
     • Passive diffusion (most drugs, lipophilic)
     • Active transport (amino acid-like drugs, methotrexate)
     • P-glycoprotein efflux (pumps drug BACK into gut)

FACTORS AFFECTING ABSORPTION
  Factor           High absorption         Low absorption
  ────────────     ─────────────────────   ─────────────────────
  Lipophilicity    Moderate (logP 1-3)     Too low (hydrophilic)
                                           Too high (stays in membrane)
  Molecular weight Low (<500 Da)           High (> 500 Da: Lipinski)
  Ionization       Unionized form          Fully ionized
  GI pH            pKa near physiologic    Very acidic or very basic drugs
  Food             Variable (usually ↓)    Some drugs ↑ with food (fat-soluble)
  P-gp efflux      P-gp substrate → ↓      P-gp inhibitor → ↑ absorption

ROUTES OF ADMINISTRATION
  Route           F (bioavailability)   Onset    Use case
  ─────────────   ──────────────────    ─────    ─────────────────────
  IV (intravenous) 100%                Seconds  Emergencies, precise dosing
  IM               75-100%            Minutes   Vaccines, depot formulations
  SC               75-100%            15-30 min Insulin, biologics
  Oral             10-100%            30-90 min Most chronic medications
  Sublingual       70-90%             2-5 min   Nitrates, buprenorphine
  Inhaled          10-80%             Seconds   Asthma, anesthetics
  Transdermal      ~100% (slow)       Hours-days Hormones, nicotine, fentanyl
  Rectal           50-80%             Minutes   When oral not possible
```

---

## Bioavailability and First-Pass Metabolism

```
BIOAVAILABILITY (F)
────────────────────
  F = fraction of administered dose reaching systemic circulation unchanged

  F_oral = F_absorption × (1 - F_first-pass)

  FIRST-PASS METABOLISM
  Drugs absorbed from GI tract enter portal circulation → liver.
  Liver CYP enzymes metabolize drug before it reaches systemic circulation.

  HIGH first-pass drugs (oral bioavailability < 20%):
    Morphine: F = 25% (extensive first-pass → IV morphine 4× more potent)
    Nitroglycerin: F = < 5% (must be sublingual or transdermal)
    Lidocaine: F = 35% (cannot be used orally for arrhythmia)
    Propranolol: F = 25% (accounts for in dose selection vs IV)

  STRATEGIES TO BYPASS FIRST-PASS
  • Sublingual: drug → systemic veins directly (nitroglycerin)
  • Transdermal: bypasses gut and liver entirely
  • Rectal: lower rectum → systemic veins (partial bypass)
  • Prodrug: designed to survive first-pass, activated elsewhere
    Codeine → morphine (CYP2D6 in liver after systemic distribution)
```

---

## Distribution

```
VOLUME OF DISTRIBUTION (Vd)
────────────────────────────
  Vd = Dose / C₀  (where C₀ = plasma concentration at time 0)

  Vd is not a real volume — it is a pharmacokinetic construct:
  "What volume would be needed for the drug to have plasma concentration C₀?"

  LOW Vd:   Drug stays in plasma (protein-bound or hydrophilic)
  HIGH Vd:  Drug concentrates in tissues

  VALUES
  Vd = 3-5 L:     Plasma only (large proteins, heparin)
  Vd = 15 L:      Extracellular fluid (aminoglycosides)
  Vd = 40 L:      Total body water (ethanol)
  Vd = 200 L:     Extensive tissue binding (digoxin: 600 L/kg)
  Vd = 3,500 L:   Amiodarone (60 L/kg × 70 kg body weight)

PROTEIN BINDING
────────────────
  Most drugs bind plasma proteins (mainly albumin, α1-acid glycoprotein).
  Only UNBOUND ("free") drug crosses membranes and produces effect.

  Protein binding fraction fb = 0.95 means 95% bound, 5% free.

  DISPLACEMENT INTERACTIONS
  Drug A and Drug B compete for albumin binding.
  Drug B displaces Drug A → free Drug A suddenly ↑ → toxicity.
  Example: warfarin (99% bound) displaced by aspirin → bleeding risk.

TISSUE DISTRIBUTION FACTORS
  Lipophilicity: crosses membranes, distributes widely
  Molecular size: < 500 Da cross most membranes
  Ionization: unionized form crosses membranes (Henderson-Hasselbalch)
  P-gp: pumps drugs out of CNS, intestine, tumor cells
  Blood-brain barrier: tight junctions limit CNS entry
```

---

## Metabolism

```
PHASE I METABOLISM (functionalization)
────────────────────────────────────────
Adds or unmasks polar functional group (-OH, -NH₂, -SH, -COOH).
Usually makes drug more water-soluble for excretion.

  Reactions: Oxidation, reduction, hydrolysis
  Main enzyme: CYP450 (cytochrome P450) family in liver

  CYP enzyme    % of drugs metabolized    Examples
  ──────────────  ────────────────────────  ────────────────────────────
  CYP3A4          ~50%                     Statins, calcium channel blockers
  CYP2D6          ~25%                     Antidepressants, opioids, antipsychotics
  CYP2C9          ~15%                     NSAIDs, warfarin, phenytoin
  CYP2C19         ~10%                     PPIs, clopidogrel, antiepileptics
  CYP1A2          ~5%                      Caffeine, theophylline, clozapine

PHASE II METABOLISM (conjugation)
───────────────────────────────────
Conjugates Phase I product with large polar molecule → highly water-soluble.
Usually inactivates drug; sometimes activates.

  Reactions: Glucuronidation, sulfation, acetylation, glutathione conjugation
  Enzymes: UGT (glucuronyl transferase), SULT (sulfotransferase), NAT (acetyltransferase)

  Example:
    Morphine (active) → morphine-6-glucuronide (M6G, more active)
                      → morphine-3-glucuronide (M3G, antagonist/neurotoxic)
    This explains why morphine is long-acting despite short half-life.
```

---

## Excretion

```
RENAL EXCRETION (primary route for most drugs/metabolites)
───────────────────────────────────────────────────────────
Three processes:

  GLOMERULAR FILTRATION
    All unbound drug is filtered at glomerulus.
    Rate = GFR × free fraction of drug in plasma.
    GFR ≈ 120 mL/min in healthy adults.
    Reduced in renal disease → drug accumulates → dose adjust.

  TUBULAR SECRETION
    Active transport: OCT (organic cation transporter), OAT (anion transporter)
    Can exceed filtration → clearance > GFR.
    Penicillin cleared at ~600 mL/min (5× GFR).
    Drug interactions at transporters: probenecid blocks penicillin secretion.

  TUBULAR REABSORPTION
    Lipophilic drugs reabsorbed back into blood.
    Ionized drugs (in acidic/basic urine) are NOT reabsorbed → faster excretion.
    Urinary pH manipulation: treat aspirin overdose with sodium bicarbonate
    → alkalinize urine → ionize salicylate → trap in urine → faster excretion.

HEPATIC EXCRETION (bile)
  Liver → bile → small intestine → excretion in feces.
  ENTEROHEPATIC RECIRCULATION:
    Drug from bile is reabsorbed from intestine → back to liver → cycle.
    Extends duration of action.
    Estrogen in oral contraceptives undergoes enterohepatic recirculation.
    Antibiotics disrupting gut flora → break cycle → ↓contraceptive effectiveness.

OTHER ROUTES
  Lungs: volatile anesthetics, ethanol (breath test)
  Sweat, saliva: minor; forensic importance
  Breast milk: important for drug safety in lactation
```

---

## Key PK Parameters

```
HALF-LIFE (t½)
────────────────
  t½ = 0.693 × Vd / CL

  Time for plasma concentration to halve.
  After 5 half-lives: ~97% eliminated (clinically "cleared").
  Time to steady state: 5 half-lives of dosing.

  t½ depends on BOTH Vd and clearance:
    High Vd + same CL → longer t½ (drug stored in tissues)
    High CL + same Vd → shorter t½

CLEARANCE (CL)
───────────────
  CL = Rate of elimination / Plasma concentration
  Units: mL/min or L/hr

  Hepatic clearance: CL_H = Q_H × (CL_int / (Q_H + CL_int))
    Q_H = hepatic blood flow (~1,500 mL/min)
    CL_int = intrinsic clearance (CYP capacity)

  High extraction drugs: CL ≈ Q_H (blood flow limited)
    → Highly sensitive to blood flow changes
  Low extraction drugs: CL ≈ CL_int × f_unbound
    → Sensitive to enzyme induction/inhibition and protein binding

AREA UNDER THE CURVE (AUC)
  AUC = ∫₀^∞ C(t) dt = F × Dose / CL
  AUC proportional to total drug exposure.
  Bioequivalence: compare AUC and Cmax of test vs reference formulation.

STEADY STATE CONCENTRATION (Css)
  Css,avg = (F × Dose) / (CL × τ)   where τ = dosing interval
  Achieved after ~5 × t½.
  Loading dose: Ld = Vd × Css,target (to reach steady state immediately)
```

---

## One-Compartment vs Two-Compartment Models

```
ONE-COMPARTMENT MODEL
──────────────────────
Drug distributes instantaneously to all tissues.
C(t) = C₀ × e^{-k_el × t}     (monoexponential decay)
k_el = CL / Vd = 0.693 / t½

  LOG(C)
    │ \
    │  \  Slope = -k_el = -0.693/t½
    │   \
    │    \
    └──────────────────→ time

TWO-COMPARTMENT MODEL
──────────────────────
Central compartment (plasma + highly perfused organs) +
Peripheral compartment (muscle, fat, poorly perfused).
Drug distributes between compartments + is eliminated.

C(t) = A × e^{-αt} + B × e^{-βt}

  LOG(C)
    │ \
    │  ╲   α phase (distribution)
    │   ╲
    │    ┖────── β phase (elimination)
    │            slope = -β
    └──────────────────→ time

  α phase: rapid initial decline (distribution into tissues)
  β phase: slower terminal decline (elimination)
```

---

## PK Monitoring and Drug Level Interpretation

```
PEAK AND TROUGH LEVELS
───────────────────────
  Peak (Cmax): Sample 30-60 min after end of IV infusion, or at Tmax for oral.
               Reflects efficacy (need above MIC for antibiotics).
  Trough (Cmin): Sample just before next dose (at steady state).
                 Reflects toxicity avoidance (aminoglycosides, vancomycin).

THERAPEUTIC DRUG MONITORING (TDM) DRUGS
  Drug           Target Range          Reason for TDM
  ──────────────  ───────────────────   ─────────────────────────────
  Vancomycin      15-20 μg/mL trough   Nephrotoxicity; resistance prevention
  Aminoglycosides Peak 5-10 μg/mL      Toxicity at high trough; efficacy at peak
  Phenytoin       10-20 μg/mL          Narrow TI; nonlinear kinetics
  Digoxin         0.5-2 ng/mL          Narrow TI; toxicity (arrhythmia)
  Cyclosporine    100-400 ng/mL        Immunosuppression; nephrotoxicity
  Lithium         0.6-1.2 mEq/L        Narrow TI; neurological toxicity
  Warfarin        INR 2-3              Variable response; PT/INR preferred
```

---

## Decision Cheat Sheet

| PK Question | Parameter | Formula |
|-------------|-----------|---------|
| How long does drug stay in body? | Half-life t½ | 0.693 × Vd / CL |
| How broadly does drug distribute? | Vd | Dose / C₀ |
| How fast is drug removed? | Clearance CL | Rate/Concentration |
| How much drug reached circulation? | Bioavailability F | AUC_oral / AUC_IV |
| How long to reach steady state? | 5 × t½ | — |
| What loading dose to reach target quickly? | Loading dose | Vd × Css_target |
| Effect of hepatic impairment? | CL_H → ↓ | Dose reduction for high-extraction |
| Effect of renal impairment? | CL_renal → ↓ | Dose reduction for renally cleared |

---

## Common Confusion Points

**"t½ is constant — does drug always disappear at the same rate?"**
t½ is constant for first-order kinetics (rate proportional to concentration). Most drugs follow first-order. But at saturating concentrations (phenytoin, ethanol), elimination is zero-order (fixed amount per time) — t½ becomes concentration-dependent and dose-dependent. Ethanol: ~10 mL/hr regardless of concentration — relevant to overdose management.

**"High protein binding = drug is safer?"**
No. High protein binding means most drug is inactive (free fraction is tiny). It also means displacement interactions can suddenly increase free drug dramatically. And it means only the unbound drug distributes and is eliminated — affecting Vd and clearance. High binding is neither safe nor dangerous by itself.

**"Lipophilic drug = good CNS penetration?"**
Partly. High lipophilicity helps cross the blood-brain barrier. But highly lipophilic drugs also bind heavily to tissues/plasma proteins. The BBB also expresses P-glycoprotein (P-gp), which pumps many lipophilic drugs OUT of the CNS. Both P-gp substrate status and lipophilicity determine CNS penetration.
