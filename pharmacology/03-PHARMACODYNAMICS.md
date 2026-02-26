# Pharmacodynamics: Dose-Response and EC50

## The Big Picture

Pharmacodynamics (PD) describes the relationship between drug concentration and the effect it produces. The dose-response curve is the central tool. It encodes potency, efficacy, and the therapeutic window in a single diagram.

```
+──────────────────────────────────────────────────────────────────+
|                  PHARMACODYNAMICS FRAMEWORK                      |
|                                                                  |
|  EFFECT (%) │ ───────────────── Emax (ceiling)                  |
|         100 │          ╭────────────────────────────────        |
|          75 │        ╱                                          |
|          50 │      ╱ ← EC50 (potency marker)                   |
|          25 │    ╱                                              |
|           0 │──╱────────────────────────────────────           |
|             └────────────────────────────────────────→         |
|                  [Drug] (log scale)                             |
|                                                                  |
|  KEY PARAMETERS                                                  |
|  EC50:   Concentration for 50% of Emax          → POTENCY      |
|  Emax:   Maximum achievable effect              → EFFICACY     |
|  TI:     TD50/ED50 or TD10/ED90                → SAFETY        |
|  Hill n: Steepness of curve                    → COOPERATIVITY |
+──────────────────────────────────────────────────────────────────+
```

---

## The Dose-Response Curve in Detail

```
SIGMOIDAL DOSE-RESPONSE (Emax model)
──────────────────────────────────────

  E(C) = Emax × Cⁿ / (EC50ⁿ + Cⁿ)

  E = effect at concentration C
  Emax = maximum effect
  EC50 = concentration producing 50% Emax
  n = Hill coefficient (steepness; n=1 for most drugs)

  ON LOG SCALE: symmetrical sigmoid with inflection at EC50
  ON LINEAR SCALE: rectangular hyperbola

LOG-SCALE CURVE READING
  ─────────────────────
  The log10-scale is canonical because:
  (1) EC50 falls at the midpoint of the sigmoid → easy to read
  (2) Useful range typically spans 3-4 log units (1000-10,000× dose range)
  (3) Doses expressed as mg/kg, μg/mL etc. are naturally log-distributed

  EFFECT%  │         ←n=1→                ←n=3→
      100  │     ╭──────────────────     ╭──────────
       50  │   ╱                        │
        0  │─╱──────────────────────────│──────────
           │       ↑                    ↑
           │      EC50 same EC50   Steep sigmoid
           │                       n>1: more switch-like
```

---

## Potency vs Efficacy

This distinction is tested constantly and confused constantly:

```
POTENCY
────────
  Defined by EC50: lower EC50 = more potent.
  Drug A (EC50 = 1 nM) is 1000× more potent than Drug B (EC50 = 1 μM).
  Potency does not tell you how strong the effect is — only how little is needed.

EFFICACY
──────────
  Defined by Emax: the maximum achievable response.
  Full agonist: Emax = 100% of possible response.
  Partial agonist: Emax < 100%.

CLINICAL RELEVANCE
  More potent drug → lower dose needed → fewer side effects at non-target sites?
    Not necessarily. Potency is only useful if it reduces absolute dose.
  Higher efficacy drug → can produce stronger effect.
    Important when maximum response matters (pain control, infection clearance).

EXAMPLE COMPARISON TABLE
  Drug        EC50      Emax      Classification
  ──────────  ─────────  ────────  ──────────────────
  Morphine    0.1 μM    100%      Full opioid agonist
  Fentanyl    0.001 μM  100%      Full agonist, 100× more POTENT
  Codeine     10 μM     80%       Partial agonist, less potent AND less efficacious
  Buprenorphine 0.001 μM 50%     Partial agonist, very potent but limited efficacy
```

---

## Therapeutic Index and Safety Window

```
THERAPEUTIC INDEX (TI)
───────────────────────

  TI = TD50 / ED50   (toxic dose 50% / effective dose 50%)

  ─────────────────────────────────────────────────────────────────
  DOSE:     │──────────────│──────────────────────│──────────────│
            0            ED50                    TD50           →
            ←   Below     →← Therapeutic window  →← Toxic       →
                effect

CLINICAL ALTERNATIVE: TI = TD10 / ED90 (more conservative)
  Dose that is toxic in 10% / dose effective in 90% of population.
  More relevant for safety in heterogeneous populations.

DRUG EXAMPLES
  Drug            TI (approx.)   Safety margin
  ─────────────   ─────────────  ──────────────────────────────
  Penicillin      > 100          Very wide; can give huge doses
  Digoxin         ~2             Narrow; toxic ≈ 2× therapeutic
  Warfarin        ~2-3           Narrow; requires INR monitoring
  Lithium         ~3             Narrow; tremor/seizure near therapeutic
  Phenytoin       ~2-5           Narrow; nonlinear kinetics
  Theophylline    ~2             Narrow; cardiac arrhythmia
  Acetaminophen   ~3             Narrow in overdose; hepatotoxic
  Aspirin         ~10            Moderate; tinnitus → overdose

NARROW TI DRUGS require:
  • Therapeutic drug monitoring (TDM)
  • Weight-based dosing
  • Renal/hepatic dose adjustment
  • Close clinical monitoring
  • Patient education about signs of toxicity
```

---

## Quantal Dose-Response: Population Variation

The curves above are for one patient. In a population:

```
QUANTAL (ALL-OR-NONE) DOSE-RESPONSE
──────────────────────────────────────
For a defined endpoint (e.g., "seizure stopped" or "patient died"):
  Each patient either responds or doesn't.
  The curve plots % of population responding vs dose.

  POPULATION VARIABILITY
  ─────────────────────
  Normally distributed sensitivity in population.
  → Sigmoid curve when plotted as % responding vs log(dose).

  ED50 = dose producing response in 50% of population.
  TD50 = dose producing toxicity in 50% of population.

  SOURCES OF VARIABILITY
  • Pharmacokinetic variation: CYP polymorphisms, renal function
  • Pharmacodynamic variation: receptor polymorphisms, disease state
  • Age and body composition
  • Drug interactions affecting concentration

CLINICAL INTERPRETATION
  Giving ED50 to a population: 50% will respond.
  To treat 90% of patients, need dose near ED90 (higher than ED50).
  But if TI is narrow, ED90 may be close to TD10.
  → Real clinical challenge: treat enough patients without harming outliers.
```

---

## Time-Dependent Pharmacodynamics

Not all drug effects are simply proportional to current concentration:

```
HYSTERESIS LOOPS
─────────────────
Concentration and effect are not in sync.

  CLOCKWISE HYSTERESIS (acute tolerance)
  Effect

    │     /---\  ← at same concentration,
    │    /     \    effect is LESS during the
    │   /       \   downward phase
    │──/─────────\──→ Concentration

  Drug tolerance develops rapidly. Common with opioids.

  COUNTER-CLOCKWISE HYSTERESIS (delayed effect)
  Effect

    │          /---\  ← effect lags behind concentration
    │         /     \    (buildup at effect site)
    │    /──/         \
    │───/──────────────→ Concentration

  Drug must reach effect site (which lags plasma).
  Warfarin: plasma levels peak quickly, but anticoagulant effect
  peaks 36-72 hours later (must wait for clotting factors to deplete).

LINK MODEL (effect compartment)
  Solves hysteresis by modeling effect-site concentration Ce:
    dCe/dt = k_e0 × (Cp - Ce)   where k_e0 = rate constant
  PD: effect vs Ce (no hysteresis)
  PK: Cp drives Ce with lag.
```

---

## Drug Tolerance and Dependence

```
TOLERANCE MECHANISMS
──────────────────────
  1. PHARMACOKINETIC tolerance:
     Drug induces its own metabolism (CYP induction).
     Carbamazepine (antiepileptic): induces CYP3A4 → faster clearance
     → therapeutic levels drop over time → dose escalation needed.

  2. PHARMACODYNAMIC tolerance:
     Receptor desensitization (Module 01).
     Receptor downregulation (fewer receptors).
     Counter-regulatory responses: compensatory systems activated.
     Opioids: μ-receptor internalization + counter-regulatory cAMP rebound.

  3. BEHAVIORAL tolerance:
     Learned compensatory behaviors.
     Alcohol tolerance: brain learns to function in presence of ethanol.

PHYSICAL DEPENDENCE vs ADDICTION
  Physical dependence: physiological adaptation; withdrawal on stopping.
  Addiction: compulsive use despite harm; reinforcement-driven.
  These are NOT the same:
    Patients on long-term opioids for pain are physically dependent
    (will have withdrawal if stopped abruptly) but usually not addicted.
    Addiction involves the reward circuitry; dependence is just adaptation.

WITHDRAWAL SYNDROMES (receptor upregulation phenomenon)
  Receptor upregulated during chronic antagonism/agonist reduction.
  Abrupt cessation → hyperactivation.
  β-blocker withdrawal: rebound tachycardia, hypertension, angina.
  Opioid withdrawal: diarrhea, cramps, tachycardia, agitation.
  Alcohol withdrawal: seizures (GABA receptor downregulated).
```

---

## Engineering Bridge: PD as Transfer Function and Control Theory

Pharmacodynamics is the input-output model of the drug-target-effect system. PK/PD integration is applying system dynamics to a biology pipeline.

```
  PHARMACODYNAMICS              CONTROL THEORY / SIGNAL PROCESSING
  ──────────────────────────────────────────────────────────────────────
  Dose-response sigmoid         Saturating nonlinear transfer function:
  E = Emax·Cⁿ/(EC50ⁿ+Cⁿ)       Logistic / Hill function. Same shape as
                                a sigmoid activation function in ML, or
                                a soft saturation in nonlinear control.
                                Linear range: C << EC50 (→ E ≈ Emax·C/EC50,
                                first-order linear gain).
                                Saturated range: C >> EC50 (→ E ≈ Emax,
                                zero-order saturation plateau).

  Hill coefficient n            Steepness / cooperativity:
  n = 1: standard Hill          n controls slope at EC50. n > 1 produces
  n > 1: positive cooperativity a steeper, more switch-like dose-response.
                                In control: a high-n Hill function is
                                close to a Heaviside step — an approximation
                                to a threshold comparator.

  Effect compartment (ke0)      First-order lag (low-pass filter):
  d[Ce]/dt = ke0([C]-[Ce])      Ce(s) = C(s) × ke0/(s + ke0).
  (link model)                  Introducing a first-order lag between plasma
                                concentration and effect-site concentration.
                                The phase lag explains clockwise hysteresis:
                                for the same C on the way up vs. down, Ce
                                is lower on the ascending arm (lag) and
                                higher on the descending arm.

  Clockwise hysteresis          Phase lag in feedback: effect lags
  (tolerance / acute effect)    concentration → on the C-E phase plot,
                                the trajectory is clockwise (C rises before
                                E does). Counter-clockwise hysteresis →
                                counter-direction: E rises BEFORE C, which
                                signals active metabolite accumulation or
                                sensitization.

  PK/PD cascade                 Cascade transfer function:
  E(t) = PD[PK(t, dose, route)] H_total(s) = H_PK(s) × H_PD(Ce).
                                PK provides the impulse response (distribution
                                + elimination); PD is the static or dynamic
                                output nonlinearity. Predicting optimum
                                dosing regimen = finding input drive to
                                maintain output within therapeutic band.

  AUC/MIC ratio (antibiotics)   Energy delivery metric:
                                Total drug exposure (AUC) relative to
                                minimum inhibitory concentration (MIC) is
                                the time-integrated "signal above threshold"
                                — analogous to a signal-to-noise ratio
                                integrated over time.
  ──────────────────────────────────────────────────────────────────────
```

---

## PK/PD Modeling

```
PK/PD INTEGRATION
──────────────────
PK provides C(t): concentration vs time.
PD provides E(C): effect vs concentration.
Together: E(t) = PD[PK(t, dose, route)]

SIMPLE CASE (no hysteresis)
  E(t) = Emax × C(t)ⁿ / (EC50ⁿ + C(t)ⁿ)
  Combine with C(t) = (F × D / Vd) × e^{-k_el × t}

CLINICAL USES
  • Dose selection: what dose achieves E > threshold for sufficient time?
  • Dosing interval: how long before effect drops below therapeutic?
  • Population PK/PD: model between-subject variability
  • AUC/MIC (antibiotics): target attainment analysis

ANTIBIOTIC PD CLASSIFICATION
  Time-dependent killing (penicillin, cephalosporin):
    Effect correlates with TIME above MIC.
    Goal: frequent dosing or continuous infusion.
    %T>MIC ≥ 40-50% of dosing interval.

  Concentration-dependent killing (aminoglycosides, fluoroquinolones):
    Effect correlates with Cmax/MIC or AUC/MIC.
    Goal: once-daily high doses.
    Target: Cmax/MIC ≥ 8-12 (aminoglycosides).
```

---

## Decision Cheat Sheet

| PD Concept | Parameter | Clinical Reading |
|------------|-----------|-----------------|
| Drug A more potent than Drug B | EC50_A < EC50_B | Smaller dose needed for A |
| Drug A has greater efficacy | Emax_A > Emax_B | Stronger maximum effect from A |
| Drug has narrow TI | TD50/ED50 < 10 | Requires TDM, careful dosing |
| Dose-response is steep | Hill n > 2 | Small dose change → large effect change |
| Effect lags concentration | Counter-clockwise hysteresis | Allow time for effect-site equilibration |
| Tolerance developing | Tolerance mechanisms | May need dose escalation or tolerance breaks |
| Antibiotic needs high peak | Concentration-dependent PD | Once-daily dosing (aminoglycosides) |
| Antibiotic needs sustained level | Time-dependent PD | Frequent dosing or continuous infusion |

---

## Common Confusion Points

**"EC50 is the effective dose — same as ED50?"**
EC50 is for a single patient or in vitro system: the concentration for 50% of maximum effect. ED50 is for a population: the dose producing a defined response in 50% of patients. EC50 is a PD parameter; ED50 is a clinical parameter that reflects PK (getting drug to target) + PD (response at target).

**"Bigger maximum effect always better?"**
No. Sometimes you want partial agonism. Buprenorphine's ceiling effect on respiratory depression is actually desirable in treating opioid addiction — prevents overdose. Partial agonists are also safer in overdose for anxiolytics and other CNS drugs.

**"TI = 2 sounds terrifying — how does warfarin get approved?"**
Because dosing is titrated individually. Warfarin isn't given at a fixed dose — it's adjusted based on INR (international normalized ratio, a measure of anticoagulation). The narrow TI means you need lab monitoring, not that the drug is inherently too dangerous to use. TI is a useful screening concept; individualized dosing adjusts for population variability.
