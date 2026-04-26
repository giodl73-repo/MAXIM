# Underdetermination and the Duhem-Quine Thesis: Theory Choice, Holism

## The Big Picture

Underdetermination is the thesis that evidence never uniquely determines which theory to believe. There will always, in principle, be multiple theories consistent with all available evidence. This threatens both Popperian falsificationism (what exactly is falsified?) and scientific realism (if multiple theories explain the same data, which one is true?).

```
+------------------------------------------------------------------+
|               UNDERDETERMINATION — TWO LEVELS                    |
+------------------------------------------------------------------+
|                                                                  |
|  LEVEL 1: DUHEM'S PROBLEM (weak underdetermination)             |
|  Theories tested only in conjunction with auxiliaries.          |
|  Anomaly targets: core + auxiliaries (can't tell which)         |
|  → Theory choice underdetermined by experiment alone            |
|                                                                  |
|  LEVEL 2: UNDERDETERMINATION PROPER (strong)                    |
|  Even in principle, multiple inequivalent theories can          |
|  match all possible observational data.                         |
|  → Theory choice underdetermined by all possible evidence       |
|                                                                  |
+------------------------------------------------------------------+
|                                                                  |
|  QUINE'S HOLISM (connects levels 1 and 2)                        |
|  No statement faces experience alone — "web of belief"           |
|  No analytic/synthetic distinction → any statement revisable     |
|  → Underdetermination is pervasive, not isolated                 |
|                                                                  |
+------------------------------------------------------------------+
```

---

## Duhem's Problem (1906)

Pierre Duhem, in *The Aim and Structure of Physical Theory* (1906), made the observation that has shaped all subsequent epistemology of science:

**A physical hypothesis cannot be tested in isolation. It is always tested in conjunction with a whole system of hypotheses.**

```
EXAMPLE: Testing Newton's inverse-square law

  APPARENTLY YOU'RE TESTING:
  H: F = G(m1 · m2)/r²

  BUT ACTUALLY YOU'RE TESTING:
  H  (gravitational law)
  + A1 (Newtonian mechanics N1-N3)
  + A2 (telescope optics are accurate)
  + A3 (no significant atmospheric refraction)
  + A4 (calibrated clocks)
  + A5 (observer locations measured accurately)
  + A6 (no undiscovered masses nearby)
  + ...

  If prediction fails, modus tollens says:
  NOT (H ∧ A1 ∧ A2 ∧ A3 ∧ A4 ∧ A5 ∧ A6)

  But this is consistent with revising ANY of H, A1, A2, ...
  You cannot isolate H as the culprit.
```

### Duhem's Conclusion

The scientist has a **logical choice** when facing an anomaly: revise any component of the tested conjunction. There is no purely logical constraint that says the core hypothesis must take the hit.

Duhem was more conservative than Quine's later generalization: he thought there were good scientific reasons (internal coherence, external agreement) that guide which component to revise — just not *logical* reasons. The choice requires **good taste (bon sens)**.

---

## Quine's Holism

### Two Dogmas of Empiricism (1951)

W.V.O. Quine's 1951 paper demolished the two central tenets of logical positivism:
1. **The analytic/synthetic distinction**: no sharp line between truths of meaning and truths of fact
2. **Reductionism**: no statement can be reduced to immediate experience in isolation

Quine's positive thesis: **the web of belief**. Our beliefs form a web; they face experience collectively, not sentence by sentence:

```
+------------------------------------------------------------------+
|                    QUINE'S WEB OF BELIEF                         |
+------------------------------------------------------------------+
|                                                                  |
|                PERIPHERY (empirical beliefs)                    |
|   observable facts, measurement reports, experimental results   |
|                                                                  |
|          CENTER (mathematics, logic, core science)              |
|   deep theoretical commitments, mathematical structure          |
|   → insulated from peripheral observations by layers of belief  |
|                                                                  |
|  Experience impinges at the periphery.                          |
|  Force of recalcitrant experience propagates inward.            |
|  Which beliefs to revise is underdetermined:                    |
|  → Can always protect any belief by revising peripheral ones    |
|  → Even logic is revisable (quantum logic for QM anomalies?)    |
|                                                                  |
+------------------------------------------------------------------+
```

### Quine's Key Claims

1. **No statement is immune to revision** — not even logic or mathematics. We could (in extreme circumstances) revise the law of excluded middle to handle quantum mechanics.

2. **No statement faces the tribunal of experience alone** — every statement is embedded in the web; its "empirical content" is inseparable from the content of neighboring beliefs.

3. **The analytic/synthetic distinction collapses** — there is no principled way to separate "true by meaning" from "true by fact." Carnap's foundation evaporates.

4. **Underdetermination is pervasive** — any web of beliefs can be adjusted to accommodate any observation by making adjustments elsewhere.

---

## Underdetermination Proper: The Strong Thesis

Beyond Duhem-Quine holism, there is a stronger claim: even given all possible observable data, multiple inequivalent theories can account for it equally well.

### The Observational Equivalence Argument

Two theories T1 and T2 are **empirically equivalent** if they make exactly the same observational predictions. The claim: for every theory T, there exists at least one empirically equivalent rival T* that is genuinely inequivalent in its theoretical commitments.

**Poincaré's geometric conventionalism** is the classic case:
- Euclidean geometry + complex optical laws can describe physical space
- Non-Euclidean geometry + simple optical laws can describe the same physical space
- Both predict identical observational results
- No experiment can distinguish them — you adjust the physics to compensate for the geometry

Similarly:
- Newtonian mechanics in absolute space vs. Newtonian mechanics in various non-inertial frames (before GR)
- Quantum mechanics in different formulations (Heisenberg matrix vs. Schrödinger wave, before establishing their equivalence)
- Einstein's special relativity vs. Lorentz's ether theory: same predictions, different ontology

---

## Responses to Underdetermination

### Response 1: Theoretical Virtues as Tie-Breakers

Boyd, Quine himself, and others: scientists choose theories by non-empirical virtues:
- **Simplicity** (Occam's Razor): prefer theories with fewer ontological commitments
- **Explanatory power**: prefers theories that unify disparate phenomena
- **Coherence** with background knowledge
- **Fruitfulness**: theories that generate new research programs
- **Precision** of predictions

These virtues are not arbitrary aesthetic preferences — they have epistemic justification. Simpler theories with greater explanatory scope are more likely to be true given our background knowledge.

### Response 2: The Problem is Not So Bad in Practice

Most alleged empirically equivalent theories are underdetermined only relative to current technology. Ether theory vs. SR became distinguishable with more precise measurements. Strong underdetermination requires theories that are equivalent relative to all *possible* observations in principle — a much higher bar.

Laudan and Leplin (1991): the empirical equivalence of two theories at time t does not entail their equivalence at all future times. Novel evidence breaks apparent equivalences. This response works against the historical examples but does not address the in-principle argument.

### Response 3: Holism Cuts Both Ways (Quine)

Quine himself argued that underdetermination, while genuine, is not paralyzing. The web of belief is conservative: we make the minimal revisions needed to accommodate new experience. **Pragmatic virtues** — simplicity, familiarity, fecundity — guide revision. These are rational constraints even if not purely logical ones.

---

## The No Free Lunch Connection

The No Free Lunch theorem (Wolpert and Macready, 1997) in machine learning is the mathematical cousin of underdetermination:

```
NO FREE LUNCH THEOREM:
  For any learning algorithm A and any cost function C:
  If we average over all possible cost functions (problem distributions),
  all algorithms perform equally.

  → No algorithm is universally better than random search.
  → Algorithm choice requires prior commitment to a class of problems.
  → "All algorithms equal" over all problems uniformly.

PHILOSOPHICAL PARALLEL TO UNDERDETERMINATION:
  For any observation data D:
  Multiple theories fit D equally well.
  → Theory choice requires prior commitments (theoretical virtues).
  → "All theories equal" given data alone.

  No Free Lunch = underdetermination in machine learning.
  Regularization = operationalized Occam's Razor.
  Prior in Bayesian learning = theoretical virtues.
```

---

## Underdetermination and the Analytic/Synthetic Boundary

Quine's collapse of the analytic/synthetic distinction is the most radical form of underdetermination: it means that even the distinction between what a theory says "by meaning" and what it says "about the world" is itself underdetermined. There is no fact of the matter about whether a definition is merely analytic.

Consequences:
- Mathematical truths are not protected from revision by their "analyticness" — they are just much more firmly embedded in the web
- The positivist program of reducing science to observation via logical connections collapses
- Theory and observation are not separable layers — they interpenetrate throughout

---

## Implications for Scientific Realism

Underdetermination is the anti-realist's main weapon (see 06-SCIENTIFIC-REALISM.md):

```
ANTI-REALIST ARGUMENT FROM UNDERDETERMINATION:

  P1: For any theory T about unobservables (electrons, fields),
      there exists an empirically equivalent rival T* with
      different claims about unobservables.

  P2: Empirical equivalence means no possible observation
      can favor T over T*.

  P3: We should only believe what is warranted by evidence.

  C:  We cannot be warranted in believing T rather than T*.
      → We cannot warrant beliefs about unobservables.
      → Scientific anti-realism about unobservables.

REALIST RESPONSE:
  P2 is false: in practice theories become distinguishable.
  P3 is false: theoretical virtues (simplicity, explanatory power)
  provide non-observational warrant.
  Or: structural realism — believe the mathematical structure,
  not the specific nature of the unobservables.
```

---

## Model Selection in ML — Underdetermination Made Practical

The underdetermination problem is the philosophical foundation of the model selection problem in machine learning:

```
DATA D = {(x1,y1), ..., (xn,yn)}

For any finite data set, infinitely many models fit perfectly.
(Any function passing through all points — Runge's phenomenon)

UNDERDETERMINATION: data alone does not determine which model.

RESPONSES (parallel to philosophy):
  Regularization = Occam's Razor (prefer simpler models)
  Cross-validation = use held-out data (expand the evidence set)
  Bayesian priors = encode theoretical virtues formally
  Minimum description length = information-theoretic simplicity
  Structural risk minimization (Vapnik) = bound generalization error

ALL OF THESE ARE WAYS OF BREAKING UNDERDETERMINATION
by importing prior commitments that data alone cannot justify.
```

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is Duhem's problem? | Theories tested only in conjunction with auxiliaries; anomaly cannot uniquely target the core hypothesis |
| What is Quine's holism? | No statement faces experience alone; whole web of belief faces experience collectively |
| What is the Two Dogmas argument? | Quine: analytic/synthetic distinction is not principled; reductionism of meaning to experience fails |
| What is strong underdetermination? | Even all possible evidence leaves multiple inequivalent theories tied; choice requires non-empirical virtues |
| How do realists respond? | Theoretical virtues (simplicity, scope, coherence) are epistemic, not merely aesthetic; empirical equivalence is often only temporary |
| What is the No Free Lunch connection? | NFL theorem is underdetermination in learning theory: data alone doesn't determine algorithm choice; regularization = Occam's Razor |
| What is Poincaré's example? | Euclidean geometry + complex optics vs. non-Euclidean + simple optics: identical observational predictions, different theoretical commitments |

---

## Common Confusion Points

**Duhem's problem vs. strong underdetermination**: Duhem's problem is that a single anomaly doesn't uniquely target the core hypothesis (auxiliary-revision escape). Strong underdetermination is that even complete data doesn't uniquely determine theory. These are distinct claims with different implications.

**Holism is not skepticism**: Quine's web of belief does not say we cannot know anything. It says there is no privileged class of incorrigible claims. Scientific knowledge is still possible — just revisable throughout, not just at the periphery.

**Simplicity as epistemic vs. aesthetic**: Is Occam's Razor a preference for pretty theories or an epistemic norm? The realist needs simplicity to be epistemically justified — connected to truth, not just ease. Boyd argues simple theories are better confirmed given background knowledge. Whether this fully answers the challenge is contested.

**Underdetermination applies to models in ML**: If you see colleagues agonizing over regularization parameters, feature engineering, and prior selection — they are navigating the practical consequences of underdetermination. The philosophy is not abstract.
