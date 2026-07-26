---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-DIAGNOSTIC-TEST-INTERPRETATION.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:clinical-medicine:diagnostic-test-interpretation
kind: guide
module: clinical-medicine
section: clinical-medicine
title: Diagnostic Test Interpretation - Decision Theory for Testing Under Uncertainty
status: source-custody
source_custody: partial
current_path: clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION.md
canonical_path: clinical-medicine/03-DIAGNOSTIC-TEST-INTERPRETATION.md
backsource_ids: [mdloom-backfill:clinical-medicine:03-diagnostic-test-interpretation]
concepts: [diagnostic-decision-theory, likelihood-ratio, bayesian-updating, predictive-value, test-treatment-threshold, value-of-information]
root_concepts: [diagnostic-reasoning]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Diagnostic Test Interpretation — Decision Theory for Testing Under Uncertainty

**This guide owns** the *decision theory* of diagnostic testing: the 2×2 confusion
matrix as a belief-updating engine, likelihood ratios and odds-form Bayes, the
prevalence dependence of predictive values, what ROC/AUC does and does not reveal,
the **test and treatment thresholds** (the Pauker–Kassirer model), sequential and
correlated testing, the overtesting/incidentaloma cascade, and the value of
information a test carries. **It builds on** `02-DIFFERENTIAL-DIAGNOSIS` (which
supplies the *pretest probability* this guide updates) and assumes probability
fundamentals from `probability-statistics/`. **It explicitly defers** the *test
catalog itself* — which panels exist, reference ranges, analyte time-courses, and
X-ray/CT/MRI/US/PET physics — to `medicine/10-DIAGNOSTICS-IMAGING`; the *why a
result is what it is* (tissue/cell mechanism, lab-medicine method) to `pathology/`
(the lab-medicine method — how a result is generated and bounded — in
`pathology/08-LABORATORY-MEDICINE`; the tissue/cell mechanism in `pathology/01`–`07`
and the diagnosis reasoning in `pathology/10`); and population **screening programs** and
study-design mechanics to `public-health/`. The companion clinical-medicine guides this one leans on — the
clinical encounter (01), differential diagnosis (02), evidence appraisal (04), and
individual prevention/screening (09) — are complete and cross-referenced throughout;
`STATUS.md` holds the full 12-guide module manifest.

**Overlap note — `medicine/10 §11`.** `medicine/10-DIAGNOSTICS-IMAGING` §11
("Diagnostic Reasoning") carries a **compact** diagnostic-reasoning treatment
(Sn/Sp/PPV/NPV, likelihood ratios, an odds/Fagan update, prevalence dependence, a
worked example) sized for the diagnostics/imaging catalog. This guide is the **deeper
standalone decision-theory version** of that material: it owns the threshold model,
value of information, calibration, and the overtesting cascade at graduate depth. The
boundary is wired **both ways**: a **forward** pointer (this guide → `medicine/10`)
and a **reciprocal** pointer (`medicine/10 §11` → this guide) now exist. `medicine/10`
owns the test **catalog**, reference ranges, and imaging **physics**, plus the short
compact reasoning section; `clinical-medicine/03` owns the deep, standalone decision
theory. The two treatments are deliberately **layered** — a catalog-side quick
reference vs. the graduate-depth decision theory — not a duplication awaiting
reconciliation (see the wave architecture record).

> **This module is an educational reference about *how clinical medicine reasons and
> how care is organized* — the cognitive and system architecture of the discipline.
> It is *not* medical advice. It does not diagnose, does not give treatment, dosing,
> or procedure instructions, does not give emergency or first-aid instructions, and
> is *not a substitute* for evaluation by a licensed clinician. Worked cases are
> illustrative teaching vignettes showing *how a clinician thinks*, not what any
> reader should do. For personal concerns, appropriate care comes from qualified
> local professionals; emergencies are handled through local emergency services.**

*Per-guide banner: educational reference on diagnostic decision theory — not medical
advice, diagnosis, or a recommendation to obtain or forgo any test. Every numeric
value below is illustrative and dated/attributed where it names a real instrument.*

---

## The Big Picture: A Test Is a Belief-Update Operator, Not an Oracle

The novice mental model is "order test → test says yes/no → that is the answer." The
expert model is a control loop: a test is an *operator* that transforms a **prior
belief** (pretest probability) into a **posterior belief** (posttest probability),
and the only reason to run it is that the posterior might cross a **decision
threshold** that changes what happens next. If no result can cross a threshold, the
test is paid-for noise.

```
DIAGNOSTIC DECISION LOOP  (this guide owns the whole loop)
==========================================================================
  [ 02: DIFFERENTIAL ]      supplies the prior
        |  pretest probability  p0   (a NUMBER, however rough)
        v
  [ CHOOSE TEST ]  -- is any result able to cross a threshold? (Section 6-7)
        |            if NO -> model favors no test (value of information = 0)
        v
  [ RUN TEST ]  -- result R  (medicine/10 owns WHICH test + its Sn/Sp)
        |
        v
  [ UPDATE ]   post-odds = pre-odds x LR(R)          <-- Section 2
        |      the 2x2 (Section 1) is where LR comes from
        v
  [ POSTTEST PROBABILITY  p1 ]
        |
        v
  [ COMPARE TO THRESHOLDS ]                            <-- Section 5
     p1 < T_test  ......... below testing threshold  -> model favors no test
     T_test < p1 < T_treat  ................. -> model favors testing/observation
     p1 > T_treat ........ above treatment threshold -> model favors action (treat)
==========================================================================
  Read top-to-bottom: belief in, evidence applied, belief out, decision made.
  A "positive" result is not a diagnosis; it is a multiplier on the prior.
```

Three consequences follow immediately, and the rest of the guide is their
elaboration:

1. **The same result means different things to different patients**, because they
   start from different priors (Section 3, the prevalence effect).
2. **A test can be excellent and still worthless here**, if the patient's prior is
   already outside the "test zone" (Sections 5–7).
3. **Chaining tests multiplies evidence only if the tests are conditionally
   independent given disease status** — and most related tests are not, so the naive
   product can mislead in either direction (Section 6).

**Bridge (software).** This is exactly a Bayesian filter (Kalman/particle-filter
intuition): a prior state estimate, a noisy measurement with a known error model,
and a posterior that is the prior reweighted by the measurement likelihood. The
"error model" of a clinical test is its sensitivity/specificity; the "measurement
update" is multiplication in odds space; and the "controller" downstream only cares
whether the posterior crosses a setpoint.

---

## 1. The 2×2 as a Belief-Updating Engine

Every dichotomous test, compared against a reference standard ("truth"), produces a
2×2 contingency table. This is the ML confusion matrix with clinical names.

```
                          TRUTH (reference standard)
                     Disease +            Disease -
                 +-----------------+-----------------+
   TEST    +     |   TP            |   FP            |
  RESULT         |  true positive  | false positive  |
                 +-----------------+-----------------+
           -     |   FN            |   TN            |
                 |  false negative |  true negative  |
                 +-----------------+-----------------+
                   Sn = TP/(TP+FN)    Sp = TN/(TN+FP)    (down COLUMNS -> test property)
                   PPV = TP/(TP+FP)   NPV = TN/(TN+FN)   (across ROWS  -> test + prevalence)
```

| Metric | Formula | Reads across / down | Fixed by | Answers |
|---|---|---|---|---|
| Sensitivity (Sn) | TP/(TP+FN) | down the disease-**+** column | the test | of truly diseased, fraction the test catches |
| Specificity (Sp) | TN/(TN+FP) | down the disease-**−** column | the test | of truly well, fraction the test clears |
| PPV | TP/(TP+FP) | across the test-**+** row | test **and prevalence** | given a **+**, chance disease is real |
| NPV | TN/(TN+FN) | across the test-**−** row | test **and prevalence** | given a **−**, chance the patient is truly well |

**The load-bearing distinction:** Sn and Sp are **column** properties — computed
*within* a disease status, so they are (approximately) stable across populations and
are what studies report. PPV and NPV are **row** properties — they mix the columns in
the proportion the population supplies, so they **move with prevalence** (Section 3).
Confusing "the test is 95% accurate" (a test property) with "a positive means 95%
chance of disease" (a population-dependent posterior) is one of the common
test-interpretation errors; they are equal only at one specific prevalence.

**SpPin / SnNout** (the bedside heuristics, and their trap):

```
  High SPecificity, a Positive rules IN   (SpPin)   -- few FPs, so + is trustworthy
  High SEnsitivity, a Negative rules OUT  (SnNout)  -- few FNs, so - is trustworthy
```

These are *directional shortcuts*, not laws. A 99%-specific test still floods a
low-prevalence population with false positives in absolute number (Section 3), so
"SpPin" can fail exactly where screening happens. They are reminders of *which error a
test suppresses*, not permission to skip the arithmetic.

**Bridge (ML).** Sn = recall/TPR; Sp = TNR = 1−FPR; PPV = precision; the "screening
paradox" is the precision collapse every ML engineer has seen deploying a classifier
trained on a balanced set onto a rare-event production stream. Class imbalance in ML
*is* low prevalence in medicine.

---

## 2. Odds, Likelihood Ratios, and the Update Rule

Probabilities are awkward to update; **odds** are not, because Bayes' theorem is
*multiplicative* in odds. This is the engine room of the whole guide.

```
  odds(p)      = p / (1 - p)              prob -> odds
  p(odds)      = odds / (1 + odds)        odds -> prob

  Pretest odds  x  Likelihood Ratio  =  Posttest odds        (Bayes, odds form)
  -----------      -----------------     --------------
  what was           what the             what is
  believed           result is worth      believed now

  LR+ = Sn / (1 - Sp)  = TPR / FPR        (multiplier after a POSITIVE result)
  LR- = (1 - Sn) / Sp  = FNR / TNR        (multiplier after a NEGATIVE result)
```

A likelihood ratio is *how many times more often this result is seen in disease than
in health*. It is a pure property of the test at a given cutoff (like Sn/Sp), it does
**not** depend on prevalence, and — crucially — it **composes** (Section 6) and
**generalizes past yes/no** to multilevel or continuous results (each result band
gets its own LR = fraction-of-diseased-with-that-band ÷ fraction-of-well-with-that-
band). That is why sophisticated diagnosticians think in LRs, not Sn/Sp: Sn/Sp force
a binary cutoff and discard the information that "strongly positive" beats "barely
positive."

**Interpretive bands** (rules of thumb; attribute and date when printed —
Jaeschke, Guyatt & Sackett, *JAMA* 1994; McGee, *J Gen Intern Med* 2002):

| LR+ | effect on probability | LR− | effect on probability |
|---|---|---|---|
| >10 | large increase (often decisive) | <0.1 | large decrease (often decisive) |
| 5–10 | moderate increase | 0.1–0.2 | moderate decrease |
| 2–5 | small increase | 0.2–0.5 | small decrease |
| 1–2 | minimal / rarely useful | 0.5–1 | minimal / rarely useful |
| **1** | **useless — result changes nothing** | **1** | **useless** |

A test whose LR is near 1 is diagnostic theater: it produces a number without moving
belief. McGee's mental-math shortcut for those without a nomogram: LRs of 2/5/10 add
roughly **+15/+30/+45 percentage points** to a *mid-range* pretest probability, and
0.5/0.2/0.1 subtract roughly the same — a useful sanity check that also exposes why
the same LR barely moves an extreme prior (the percentage-point change shrinks near
0 and 1 even though the *odds* multiply identically).

**Bridge (information theory / CS).** In log space the update is *additive*:
log-posterior-odds = log-prior-odds + log LR. That log LR is the "weight of evidence"
(Good/Turing); a diagnostic workup is a running log-odds accumulator, and each test
contributes a signed number of bits. This is identical to a naïve-Bayes classifier
summing feature log-likelihoods — with the same fatal assumption (independence) that
Section 6 attacks.

---

## 3. Predictive Values Depend on Prevalence — The Screening Paradox

PPV and NPV are just the posttest probabilities after a positive or negative result,
so they inherit the prior. Writing PPV out with Bayes makes the prevalence term
explicit (p = prevalence):

```
              Sn * p
  PPV = ----------------------------
        Sn * p  +  (1 - Sp)(1 - p)

              Sp (1 - p)
  NPV = ----------------------------
        Sp (1 - p)  +  (1 - Sn) p
```

**Worked demonstration (illustrative).** Hold the test fixed at an excellent
**Sn = 99%, Sp = 95%** (so LR+ = 0.99/0.05 = 19.8) and vary only prevalence:

| Prevalence | PPV (after +) | NPV (after −) | Per 10,000 tested: TP / FP |
|---|---|---|---|
| 50% | 95.2% | 99.0% | 4950 / 250 |
| 10% | 68.8% | 99.9% | 990 / 450 |
| 1% | 16.7% | 99.99% | 99 / 495 |
| 0.1% | 1.9% | ~100% | ~10 / ~500 |

At 0.1% prevalence, the *same* near-perfect test makes **~98% of its positives
false** — not because the test degraded, but because there are ~500 false positives
(5% of the ~9990 well people) chasing only ~10 true positives. This is the screening
paradox, and it is why a positive screening result is a *prompt for a confirmatory
test* rather than a diagnosis. The claim is quantitative, not absolute: **low
prevalence raises the false-positive share, but does not by itself guarantee that most
positives are false** — that outcome depends jointly on prevalence *and* LR+, and a
strong enough LR+ holds PPV above 50% even for an uncommon condition (the 10% row
above already sits at 68.8%). Symmetrically, NPV is nearly perfect at low prevalence
for a trivial reason: almost everyone is well, so "the patient is well" is almost
always right.

**The decision-useful takeaways:**

- **PPV/NPV are uninterpretable without the prevalence they were computed at.** A
  vendor's "PPV 95%" is a claim about *their* study population's base rate, not
  necessarily another clinic's.
- **Prevalence is the pretest probability of the population being tested.** In a
  symptomatic clinic it is high; in asymptomatic screening it is low; for one patient
  it is whatever the differential (guide 02) estimated. Same test, different math.
- **Spectrum matters too.** Sn/Sp are only *approximately* prevalence-independent;
  they drift with disease **spectrum** (sicker cohorts inflate Sn) and referral
  filtering (**spectrum bias / verification bias**), so a test measured in a tertiary
  center can underperform in primary care even before prevalence is considered.
- **Screening pathways vary.** The "confirm every positive with a second test" design
  is *common*, not universal — programs differ in sequence, interval, and triage, and
  which pathway fits a population is a program-design question owned by
  `public-health/`, not a fixed rule.

---

## 4. ROC / AUC — What It Buys and What It Hides

For a continuous test (a troponin level, a risk score), every possible cutoff gives
one (FPR, TPR) point; sweeping the cutoff traces the **ROC curve**, and the area
under it (**AUC / c-statistic**) is the probability that a random diseased patient
scores higher than a random well one — a threshold-free measure of **discrimination
(ranking)**.

```
  TPR 1 |          ____------  AUC = P(score_diseased > score_well)
 (Sn)   |      _--                = 0.5 chance-line, 1.0 perfect
        |    /        each POINT = one cutoff choice
        |  /          moving along curve = trading Sn <-> Sp
        | /
      0 +-------------------- 1   FPR (1 - Sp)
```

**What ROC/AUC is good for:** comparing two tests' intrinsic ranking ability
independent of any single cutoff, and visualizing the Sn↔Sp trade so an operating
point can be chosen for a stated purpose (rule-out point = high Sn, upper-left;
rule-in point = high Sp).

**What AUC hides — the limitations that matter for a decision:**

| Limitation | Why it bites |
|---|---|
| **Ignores prevalence** | AUC is computed within-class (like Sn/Sp), so it says nothing about PPV in the target population. A 0.90-AUC test can still be mostly false positives when rare. |
| **Ignores the cost asymmetry** | AUC weights a false positive and a false negative equally; real decisions do not. A miss of a lethal treatable disease ≠ an over-call. |
| **Discrimination ≠ calibration** | AUC only ranks. A model can rank perfectly yet output probabilities that are systematically wrong (e.g., all doubled). Acting on the *number* needs **calibration** (predicted vs observed), which AUC never checks. |
| **Insensitive to clinically relevant gains** | Adding a strong new marker to a good model often barely moves AUC even when it reclassifies real patients — hence reclassification/net-benefit measures. |
| **One number flattens the curve** | Two tests with equal AUC can cross; one is better in the rule-out region, the other in rule-in. The average hides the region actually in use. |

**The modern successors** (name them; they answer "does using this test do more good
than harm at *the operative* threshold?"): **calibration plots** (is a predicted 20% observed
20%?), **reclassification** (NRI/IDI — with well-known caveats), and especially
**decision curve analysis (DCA)** — **net benefit** across the range of threshold
probabilities a reasonable person might hold. DCA folds in the cost asymmetry that
AUC discards and directly answers whether the test beats "treat all" and "treat
none." When a paper reports only AUC, the load-bearing question — *net benefit at the
threshold that governs the decision* — is unanswered.

**Bridge (ML).** Everything here is the precision/recall-vs-ROC debate and the
"calibrated probabilities vs. good AUC" problem from production ML, plus
cost-sensitive learning. DCA is the clinical analogue of an expected-utility /
cost-curve evaluation rather than a rank-only metric.

---

## 5. Test and Treatment Thresholds — The Pauker–Kassirer Model

Updating belief is only half the job; the clinician must decide **what belief justifies
action**. The threshold model (Pauker & Kassirer, *NEJM* 1975 for the treatment
threshold; *NEJM* 1980, "The Threshold Approach to Clinical Decision Making," for the
test/test-treatment thresholds) makes this explicit and is the intellectual core of
this guide.

**Step 1 — the treatment threshold, from harms and benefits only.** Let **B** = net
benefit of treating a patient who truly has the disease, and **H** = net harm of
treating a patient who does *not*. In the model, treatment is favored when the
expected utility of treating exceeds not treating:

```
  favor Rx if   p * B  >  (1 - p) * H
  =>  favor Rx if   p/(1-p) > H/B      (threshold ODDS = harm/benefit ratio)
  =>  treatment threshold   p* = H / (H + B)
```

The threshold is **pure value judgment made quantitative**: a dangerous treatment
(large H) pushes p\* up — the model demands near-certainty before it favors acting; a
safe, highly beneficial treatment (small H, large B) pushes p\* down — the model
favors treating on suspicion. A miss of a lethal but treatable disease makes the "harm
of *not* treating the diseased" huge, which is the same as a large B, driving p\*
toward zero. **There is no universal threshold**; it is a function of the specific
outcomes.

**Step 2 — add the test, and its own harm, to get two more thresholds.** A test is
worth doing only in a *middle band* of pretest probability:

```
  PROBABILITY OF DISEASE   0% ------------------------------------> 100%
                     T_test                         T_treat
                       |                              |
                (testing thr.)             (test-treatment thr.)
   +-----------------+------------------------------+-----------------+
   |  MODEL: NO TEST |   MODEL: TEST (a result can  |  MODEL: TREAT   |
   | MODEL: NO TREAT |   cross treatment threshold  |  (no test)      |
   +-----------------+------------------------------+-----------------+
     below T_test: even a POSITIVE stays under p*  -> model favors no test
     above T_treat: even a NEGATIVE stays over p*  -> model favors treating, no test
     between: a result can cross p*                -> model favors testing
```

Ignoring the test's own risk, the two flanking thresholds are just "what pretest
probability makes a positive (or negative) result land exactly on p\*":

```
  T_test   solves   odds(T_test)  * LR+ = odds(p*)   =>  odds(T_test)  = odds(p*)/LR+
  T_treat  solves   odds(T_treat) * LR- = odds(p*)   =>  odds(T_treat) = odds(p*)/LR-
```

The **full** Pauker–Kassirer model then subtracts the test's *own* morbidity/risk
(and cost) from the value of testing, which **raises T_test and lowers T_treat** —
narrowing the "test" zone. A risky test must buy more decision-change to be worth it;
a zero-risk, cheap test has a wide test zone. This is why "would the result change
management?" is the correct first question, and it is formally the **value of
information** (Section 7).

**Bridge (systems).** p\* is a decision boundary with **asymmetric misclassification
costs**; T_test/T_treat are the region where acquiring another feature has positive
expected value net of its acquisition cost — precisely active-learning /
value-of-information gating, or a guard that refuses to pay for a probe that cannot
flip the branch it feeds.

---

## Fully Worked Case with Sensitivity Analysis (illustrative)

A clinician is weighing a single condition **D** in one patient. All numbers are
invented for teaching; no real test or condition is named (the *catalog* lives in
`medicine/10`).

**Inputs.**
- Pretest probability from the differential (guide 02): **p0 = 0.10**.
- Dichotomous marker **M**: **Sn = 0.90**, **Sp = 0.85**.
- Treatment for D: moderate harm-to-benefit ratio **H/B = 0.25** → treatment
  threshold **p\* = 0.25/1.25 = 0.20 (20%)**.

**Derived test weights.**
```
  LR+ = 0.90 / (1 - 0.85) = 0.90 / 0.15 = 6.0
  LR- = (1 - 0.90) / 0.85 = 0.10 / 0.85 = 0.1176
```

**Update from p0 = 0.10  (pretest odds = 0.10/0.90 = 0.1111).**
```
  If M POSITIVE:  post-odds = 0.1111 x 6.0    = 0.6667  -> p1 = 0.6667/1.6667 = 0.400 (40.0%)
  If M NEGATIVE:  post-odds = 0.1111 x 0.1176 = 0.01307 -> p1 = 0.01307/1.0131 = 0.013 (1.3%)
```

**Decision, read against p\* = 20% (as model states, not advice).**
```
  Pretest 10%  is BELOW p* (20%)        -> with no test, the model favors NO treatment.
  M positive -> 40% ( > 20% )           -> crosses p*; the model now favors treating.
  M negative -> 1.3% ( < 20% )          -> stays under p*; the model still favors no treat.
  Only the POSITIVE branch changes the favored action (no-treat -> treat); the negative
  branch just confirms the baseline. At least one branch crosses p*, so M is
  decision-relevant here -- but the decision flips in ONE direction, not both.
```

**Where are the thresholds for this test?** (no-test-risk version, using
odds(p\*) = 0.20/0.80 = 0.25):
```
  T_test  : odds = 0.25 / LR+  = 0.25 / 6.0    = 0.04167 -> p = 4.0%
  T_treat : odds = 0.25 / LR-  = 0.25 / 0.1176 = 2.125   -> p = 68.0%
  => TEST ZONE = 4% to 68% pretest probability. The vignette's 10% sits inside the
     zone, so the model favors testing.
```

**Sensitivity analysis.** The model's favored move is only as stable as its inputs.
Varying one input at a time from the base case:

*A. Varying the pretest probability (test fixed, p\* = 20%, T_test–T_treat = 4%–68%):*

| Pretest p0 | post-+ (×6.0) | post-− (×0.118) | Model-favored move |
|---|---|---|---|
| 3% | 15.6% | 0.36% | below T_test (4%) → no test, no treat (even a + stays under p*) |
| 10% (base) | 40.0% | 1.3% | in zone → test (only + crosses p*) |
| 50% | 85.7% | 10.5% | in zone → test (baseline treat; only − would drop under p*) |
| 75% | 94.7% | 26.1% | above T_treat (68%) → treat, no test (even a − stays over p*) |

*B. Varying the treatment threshold via harm/benefit (pretest fixed at 10%; the branch
posteriors are unchanged — post-+ = 40.0%, post-− = 1.3% — only p\* and the zone move).
Because odds(p\*) = p\*/(1−p\*) = H/B, the zone edges are T_test = odds(p\*)/LR+ and
T_treat = odds(p\*)/LR−, recomputed for each threshold. Both branches are tested against
the recomputed p\*:*

| H/B | p\*=H/(H+B) | odds(p\*) | T_test–T_treat | baseline @10% | post-+ 40.0% | post-− 1.3% | Which branch changes the action |
|---|---|---|---|---|---|---|---|
| 0.05 (very safe Rx) | 4.76% | 0.05 | 0.83%–29.8% | 10% > p* → treat | 40% > p* → treat (same) | 1.3% < p* → **no treat (flip)** | **negative** flips; testing is NOT moot |
| 0.25 (base) | 20% | 0.25 | 4.0%–68.0% | 10% < p* → no treat | 40% > p* → treat (flip) | 1.3% < p* → no treat (same) | **positive** flips |
| 1.0 (harm=benefit) | 50% | 1.0 | 14.3%–89.5% | 10% < p* → no treat | 40% < p* → no treat (same) | 1.3% < p* → no treat (same) | **neither** — 10% is below T_test (14.3%), no result crosses p* |

The corrected reading: at **H/B = 0.05** the baseline shifts to "treat," and it is the
**negative** branch that carries the decision — a negative drives 10% → 1.3%, which
falls below the recomputed p\* = 4.76% and would spare treatment, so testing is *not*
moot and the 10% patient still sits inside the recomputed test zone (0.83%–29.8%). At
**H/B = 1.0** the pretest 10% falls *below* T_test (14.3%): even a positive (40%)
cannot reach p\* = 50%, so no branch crosses and the test genuinely loses its purpose.
Only the base case flips on the positive branch, and no case flips in both directions.

*C. Varying test quality (pretest 10%, p\* = 20%): drop Sp to 0.70 → LR+ = 0.90/0.30 = 3.0
(LR− = 0.10/0.70 = 0.143):*
```
  post-+ = odds 0.1111 x 3.0   = 0.333  -> 25.0%  (still over p* = 20%, margin now thin)
  post-- = odds 0.1111 x 0.143 = 0.0159 -> 1.6%   (still well under p*)
  T_test rises to odds 0.25/3.0 = 0.083 -> 7.7%, shrinking the useful test zone.
  The vignette's 10% still sits in-zone, so the model favors testing -- but a weaker
  test narrows the band in which that holds.
```

**Reading of the analysis.** The model's favored move is *robust* to pretest
probability across a wide band (4–68% at the base threshold) but *fragile* to the
value structure — and the fragility is **asymmetric**, so it must be read
branch-by-branch. Lowering p\* (a safe treatment) shifts the baseline to "treat" and
makes the **negative** branch decision-relevant: a negative can still fall below the
recomputed p\* (as at H/B = 0.05, where 1.3% < 4.76%), so testing is *not* automatically
moot. Raising p\* (a dangerous treatment) can push the pretest below T_test so that
*no* result crosses p\* and the test truly loses its purpose (H/B = 1.0). The favored
move is a function of *consequences*, not of the test's specs alone. This is why a
decision-quality workup states its pretest estimate and its threshold *before*
ordering, and reads a result as a threshold-crossing event rather than a verdict.

### Two contrasting contexts (transport limits, illustrative)

The same marker **M** (Sn = 0.90, Sp = 0.85, so LR+ = 6.0, LR− = 0.1176) behaves
differently as the *context* changes. Nothing below is advice; each line is a model
state for a hypothetical clinician in a fictional setting.

**Context 1 — asymptomatic screening, low prevalence.** A screening population has
pretest p0 = 0.5%. Read against the base treatment threshold p\* = 20% (T_test = 4%):
```
  odds0   = 0.005/0.995   = 0.00503
  post-+  = 0.00503 x 6.0  = 0.0302 -> p = 2.9%   (a POSITIVE stays far under p* = 20%)
  0.5% is BELOW T_test (4%) -> even a positive cannot cross p* in this setting
  => the model favors NOT using M as a standalone decision test here; a positive is at
     best a prompt for a separate confirmatory step (Section 6).
```
Roughly 97% of M's positives would be false at this base rate — the screening paradox
in situ. The transport limit: an instrument that is decision-relevant in a symptomatic
clinic can be decision-irrelevant in a screening population, purely because the prior
moved.

**Context 2 — symptomatic referral clinic, enriched prevalence.** A pre-filtered
referral stream has pretest p0 = 45% (the funnel of guide 08 raised the prior). Read
against the same p\* = 20%:
```
  odds0   = 0.45/0.55      = 0.818
  post-+  = 0.818 x 6.0     = 4.91  -> p = 83.1%   (stays above p*: treat)
  post--  = 0.818 x 0.1176  = 0.096 -> p =  8.8%   (drops BELOW p* = 20%)
  baseline 45% > p* -> treat; the NEGATIVE branch is the one that changes the action.
  => the model favors testing, but here as a rule-OUT: the decision-relevant branch is
     the negative -- the mirror image of the base case, where the positive carried it.
```
Same test, opposite job. Which branch matters is a property of the *population's
prior*, not of the instrument.

**Resource overlay.** In a low-resource setting the marker M may itself carry real
cost, delay, or access burden. In the full threshold model that test harm **raises
T_test and lowers T_treat**, narrowing the test zone, and the confirmatory step that
would rescue a screening positive may not exist. A testing architecture that is sound
where labs and follow-up are abundant does not automatically transport to where they
are scarce — a limit this module flags rather than universalizes.

---

## 6. Sequential and Correlated Testing

Real workups chain tests. In **odds space** the update is just repeated
multiplication — *if the tests are conditionally independent given disease status*:

```
  post-odds = pre-odds x LR_1 x LR_2 x ... x LR_n      (ONLY if independent | status)
```

**Serial (sequential) vs parallel strategies:**

| Strategy | Rule | Net effect | Use when |
|---|---|---|---|
| **Serial** (test, then test) | act on second test only if first is positive | ↑ specificity, ↓ sensitivity, fewer tests | ruling **in**; test 2 is costly/risky; confirming a screen |
| **Parallel** (test both now) | positive if *either* is positive | ↑ sensitivity, ↓ specificity | ruling **out** fast; acute setting; can't wait |

Serial testing is the confirmatory pattern behind many screening pathways: a high-Sn
cheap screen (SnNout) followed by a high-Sp confirmatory test (SpPin) on the positives
— the combination beats either alone and rescues PPV from the screening paradox.
Screening designs vary (Section 3), so this is a common architecture, not the only one.

**Conditional independence is the load-bearing assumption — and the naive product can
err in *either* direction.** The chained multiplication is valid **only** when the
tests are *conditionally independent given disease status* — independent among the
diseased **and** independent among the non-diseased. Tests that measure *related biology* — two inflammatory markers, two imaging views of
the same process, a symptom and a sign with a shared cause — usually violate this.
The bias direction depends on the **joint conditional distributions in both strata**
(disease present and disease absent), not on a single informal label such as
"positively correlated." **There is no universal inequality** between the true joint
LR and the product of marginal LRs.

```
  post-odds = pre-odds x LR_A x LR_B    (VALID ONLY if conditionally independent | status)
  dependence in either status stratum -> bias direction requires the joint distributions
  no universal inequality holds between LR_combined and (LR_A x LR_B)
```

The disciplined response is to estimate the evidence from the **joint result pattern**,
not from separate multipliers: use a **validated joint conditional model** (a rule fit
on the pair/panel, whose coefficients already absorb the dependence) or an
**empirically estimated combined LR** (the likelihood ratio of the *joint* result,
measured directly on data). Adding a fourth marker "confirming" the same pathway then
buys little — its information is already priced in — and **repeating the same test** is
the limiting case of positive dependence, maximally correlated with itself. When the
underlying state is static, a repeat mostly probes analytic noise rather than new
biology; but when the state can genuinely change over time, a repeat can measure **real
temporal change** (a trend, a rise, a response) — a different purpose from re-confirming
a fixed value, and one where serial measurements do carry new information.

**Bridge (ML).** This is naïve Bayes' independence assumption: summing marginal
log-likelihoods for dependent features can misstate the joint evidence in either
direction because the class-conditional joint distributions are missing. A validated
joint model is the ML analogue of an empirically estimated combined LR.

---

## 7. Overtesting, Incidentaloma Cascades, and Value of Information

The threshold model implies a discipline the culture often violates: **a test that
cannot change management is not worth ordering.** Violating it is not free — it
launches cascades.

**The base-rate + spectrum failure that starts it:** testing low-pretest-probability
patients ("pan-scan," reflexive panels, screening the worried-well) drives PPV down,
so a large share of positives can be false (Section 3). Each false positive is not an
endpoint but a *branch* into more testing.

```
  THE TESTING CASCADE  (an incidentaloma is the seed)
  broad test on low-prior patient
        |  finds an unexpected, probably-benign lesion (an "incidentaloma")
        v
  follow-up imaging  --> ambiguous  --> more imaging / short-interval surveillance
        |                                   |
        v                                   v
  biopsy / invasive test  -----------> procedural harm, anxiety, cost, labeling
        |
        v
  often ends where it began (benign) -- but now with harm done and a "patient" made
```

Incidentalomas are common precisely because high-resolution tests see *everything*,
and the population base rate of small benign findings is high. Structured response
frameworks exist to *dampen* the cascade by pre-committing to size/feature-based
follow-up (named, dated, and owned as catalogs by `medicine/10` and radiology
bodies — this guide owns only the *reasoning* that a follow-up algorithm is a
threshold policy that trades a tiny cancer-miss risk against large overdiagnosis
harm).

**Value of Information (VOI): the formal "would it change management?" test.** The
question before ordering is what the *expected* improvement in decision quality is, net
of the test's harm and cost:

```
  A test has POSITIVE value of information only if:
    (1) at least one plausible result crosses a decision threshold (Section 5), AND
    (2) the expected gain from those threshold-crossings
            EXCEEDS the test's own harm + cost + downstream cascade risk.

  If the action is identical for every possible result -> VOI = 0 -> model favors no test.
```

VOI reframes the whole guide as a stopping rule: evidence is acquired only
while the expected value of the next observation exceeds its cost — the clinical
instance of the **expected value of sample information** from decision analysis, and
the direct cousin of active learning's "is this label worth its acquisition cost?"
Overtesting is what happens when a system optimizes "rule out everything" or "reassure
by scanning" instead of expected net benefit.

**Bridge (systems).** The cascade is a **retry storm / cache-miss amplification**: a
cheap speculative probe whose false hit triggers an expensive, self-amplifying fan-out
of downstream work. VOI-gating is the circuit breaker: don't issue the probe unless
its result can change the branch, and budget for the amplification when it can't.

---

## Reader Tasks (answerable from this guide)

1. **Compute a posttest probability.** Given pretest 15% and a result with LR+ = 8,
   convert to odds (0.176), multiply (1.41), convert back (**58.5%**) — and state
   whether that clears a stated treatment threshold. (Sections 2, 5.)
2. **Decide test vs. treat vs. defer.** Given a pretest probability, a test's LR+/LR−,
   and a treatment threshold p\*, locate the patient in the T_test–T_treat band and
   justify testing, treating, or doing neither. (Section 5 + worked case.)
3. **Explain why a great test is useless here.** Take Sn = 99%, Sp = 95% and show,
   with the per-10,000 table, why its positives are mostly false at 0.1% prevalence —
   and what that implies for screening the asymptomatic. (Section 3.)
4. **Diagnose an ROC overclaim.** Given a paper reporting only "AUC 0.88," name the
   three questions AUC leaves unanswered (prevalence/PPV, cost asymmetry, calibration)
   and what analysis (DCA/net benefit) the reasoning would demand instead. (Section 4.)
5. **Catch a correlated-test error and a cascade.** Identify where multiplying two
   dependent-test LRs can misstate evidence in either direction, and trace how a low-prior broad scan seeds an
   incidentaloma cascade with zero value of information. (Sections 6–7.)

---

## Decision Cheat Sheet

| Scenario | What the model does | Why (this guide) |
|---|---|---|
| A "positive result" is reported | reads it against the **pretest probability first**, then multiplies odds by LR+ | a result is a multiplier, not a verdict (§2) |
| Only Sn/Sp are reported | converts to **LR+ = Sn/(1−Sp), LR− = (1−Sn)/Sp** | LRs compose and handle result strength (§2) |
| A PPV is quoted | reads it as **prevalence-dependent** ("at what prevalence?") | PPV moves with the base rate (§3) |
| Screening the asymptomatic | expects a **large false-positive share**; a confirmatory serial test is the common design | screening paradox; SnNout→SpPin (§3, §6) |
| Two tests compared by AUC alone | looks for **calibration + net benefit (DCA)** at the operative threshold | AUC ignores prevalence, costs, calibration (§4) |
| Whether to order at all | locates the pretest in the **T_test–T_treat** band | outside the band, no result can change management (§5, §7) |
| Setting the treatment threshold | derives **p\* = H/(H+B)** from this treatment's harm/benefit | threshold is a value judgment made explicit (§5) |
| Chaining several tests | multiplies LRs **only under conditional independence given status**; otherwise reads a **validated joint model / empirical combined LR** | dependence can misstate evidence in either direction; no universal inequality applies (§6) |
| An incidental finding appears | treats follow-up as a **threshold policy** and checks **VOI** | dampens the cascade; no test if VOI = 0 (§7) |
| Repeating the same test on a static state | reads a repeat as mostly **analytic noise** (a repeat over time can still track real change) | a test is maximally correlated with itself (§6) |

---

## Common Confusion Points

**"The test is 95% accurate, so a positive means 95% chance of disease."** No — that
conflates a column property (test accuracy) with a row property (posttest
probability). They coincide only at one specific prevalence; at low prevalence a
positive can be *mostly* false despite a 95%+ test (§3). "Accuracy" itself is a
prevalence-weighted blend of Sn and Sp and is nearly useless as a single number.

**"Sensitivity tells me the chance I have the disease if I test positive."** No —
sensitivity is P(test+ | disease), computed among the *already diseased*. The chance
of disease given a positive is PPV = P(disease | test+), the reverse conditional. Swapping
the direction of the conditional is the "prosecutor's fallacy" in clinical dress.

**"Higher AUC means the better test for my patient."** Not necessarily. AUC is
average ranking ability across all thresholds; two tests can have equal AUC yet one
is better for ruling out and the other for ruling in, and neither AUC nor a good
ranking guarantees the *probabilities are calibrated* enough to act on (§4).

**"More tests mean more certainty."** Only if each adds *conditionally independent*
information above its harm and cost. Conditionally dependent tests break the naive
product and can misstate the evidence in either direction (§6); low-value tests seed cascades
(§7). Past the threshold, additional testing can *lower* decision quality by
generating false positives and incidentalomas.

**"A likelihood ratio near 1 is still a little bit useful."** Effectively no. LR ≈ 1
means the result is seen about equally in disease and health, so it multiplies the
odds by ~1 and moves belief negligibly — ordering it is cost and cascade risk with no
informational return (§2, §7).

**"Pretest probability is unknowable, so this is all theoretical."** The estimate is
rough, but the *machinery is robust to roughness* — the sensitivity analysis (worked
case) shows the test decision is stable across a wide pretest band. What is *not*
optional is committing to a number and a threshold before ordering; "I'll know it when
I see it" is how base rates get ignored (§5).

**"This tells me which test to order for my symptoms."** It does not, and it must not:
this is the *theory of interpretation*, not advice. The catalog of real tests, their
reference ranges, and imaging physics live in `medicine/10`; whether any test is
appropriate for a specific person is a clinical decision made by a licensed clinician
with that person in front of them.
