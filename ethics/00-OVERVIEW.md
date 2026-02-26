# Ethics — Landscape and Taxonomy

## The Big Picture

```
+-----------------------------------------------------------------------+
|                    ETHICS AS A DISCIPLINE                              |
+-----------------------------------------------------------------------+
|                                                                       |
|  METAETHICS              NORMATIVE ETHICS         APPLIED ETHICS     |
|  +------------------+    +------------------+     +---------------+  |
|  | What IS morality?|    | What SHOULD we   |     | How do these  |  |
|  | Are moral facts  |    | do? What makes   |     | theories apply|  |
|  | real?            |    | actions right    |     | to specific   |  |
|  | What is the      |    | or wrong?        |     | cases?        |  |
|  | meaning of moral |    |                  |     | AI ethics,    |  |
|  | terms?           |    | Consequentialism |     | bioethics,    |  |
|  | Realism vs.      |    | Deontology       |     | research      |  |
|  | anti-realism     |    | Virtue ethics    |     | ethics,       |  |
|  +------------------+    | Contractualism   |     | global justice|  |
|                          +------------------+     +---------------+  |
+-----------------------------------------------------------------------+
```

---

## The Fundamental Distinction: Is vs. Ought

```
HUME'S GUILLOTINE (1739)
==========================

Hume's observation: in arguments, people routinely move from
statements of fact ("is") to statements of value ("ought")
without justifying the transition.

"People suffer when harmed.    (IS -- factual)
Therefore you ought not harm. (OUGHT -- normative)"

The move from "is" to "ought" requires a BRIDGE:
an additional normative premise.

Without a bridge: the inference is invalid.
The is/ought gap is fundamental to ethics.

MORAL NATURALISM tries to bridge it:
"Suffering is bad" -- if "bad" = "causes pain" (a natural property),
then natural facts DO entail normative conclusions.
G.E. Moore's open question argument attacks this (see 01-METAETHICS.md).

MORAL NON-NATURALISM: The bridge is a sui generis normative fact.
Moral facts are not natural facts.

WHY IT MATTERS FOR AI:
  When we derive "AI should not deceive" from "deception causes harm":
  we need a bridge (e.g., utilitarianism, deontological rule).
  Different bridges give different conclusions.
  AI alignment is fundamentally a normative ethics problem.
```

---

## Major Normative Theories

```
NORMATIVE THEORY OVERVIEW
===========================

+------------------+------------------+------------------+------------------+
| CONSEQUENTIALISM | DEONTOLOGY       | VIRTUE ETHICS    | CONTRACTUALISM   |
+------------------+------------------+------------------+------------------+
| Core: The right  | Core: Some       | Core: Morality   | Core: Principles |
| action maximizes | actions are      | is about         | that rational    |
| overall good     | right/wrong      | character and    | people would     |
| (welfare,        | regardless of    | human            | agree to         |
| preference,      | consequences.    | flourishing.     | (Rawls,          |
| happiness).      | (Kant, Ross,     | (Aristotle,      | Scanlon).        |
|                  | Nozick)          | MacIntyre)       |                  |
+------------------+------------------+------------------+------------------+
| Decision         | Decision         | Decision         | Decision         |
| procedure:       | procedure:       | procedure:       | procedure:       |
| Calculate        | Apply the        | Ask: what would  | Ask: what        |
| consequences;    | relevant duty    | a person of good | principles could |
| choose action    | or rule; check   | character do?    | no one reasonably|
| with best        | for violations.  | What promotes    | reject?          |
| expected outcome.|                  | flourishing?     |                  |
+------------------+------------------+------------------+------------------+
| Key problem:     | Key problem:     | Key problem:     | Key problem:     |
| Can justify      | Conflicts        | Circularity:     | Who counts as    |
| rights           | between duties;  | "virtuous person"| "rational"?      |
| violations;      | absolute prohib- | defines virtue   | Original position|
| demandingness.   | itions seem      | but what is      | is idealized.    |
|                  | too strict.      | virtuous?        |                  |
+------------------+------------------+------------------+------------------+
```

---

## The Trolley Problem as Theory Discriminator

```
THE TROLLEY PROBLEM (Philippa Foot, 1967; Judith Jarvis Thomson, 1985)
=======================================================================

FOOTBRIDGE TROLLEY (TRACK VARIANT):
  A runaway trolley is heading toward 5 people.
  You can pull a lever to divert to a sidetrack where 1 person is.
  Do you pull the lever?

  CONSEQUENTIALIST: Yes. 5 lives saved vs. 1 lost.
  DEONTOLOGIST: Complicated. You're the proximate cause; but
                using someone as a means? (The 1 is not your means.)
                Most deontologists: Yes (doctrine of double effect).
  VIRTUE ETHICIST: What would a person of practical wisdom do?
                   Probably yes.

FOOTBRIDGE VARIANT (Thomson):
  A trolley is heading toward 5 people.
  You are on a footbridge above the track with a large man.
  If you push the large man off the bridge, he will stop the trolley.
  The 5 are saved; the man dies.
  Do you push?

  CONSEQUENTIALIST: Yes. Same math: 5 > 1.
  DEONTOLOGIST: No. You are using the man as a MEANS to saving others.
                This violates the Humanity Formula.
                He is not a threat; he is an innocent bystander.
  VIRTUE ETHICIST: What kind of person pushes someone to their death?
                   No.

MAJORITY INTUITION:
  Pull the lever: 85% yes.
  Push the man: 85% no.
  SAME MATH. DIFFERENT INTUITIONS.

  GREENE'S DUAL-PROCESS INTERPRETATION:
  Fast, emotional system (System 1): "Don't push people!"
  Slow, deliberative system (System 2): "5 > 1 logically."
  Footbridge variant engages System 1 more strongly (personal contact).
  This suggests moral intuitions are partly psychological artifacts,
  not purely rational moral judgments.
```

---

## Reflective Equilibrium (Rawls)

```
RAWLS' METHOD: REFLECTIVE EQUILIBRIUM (1971)
==============================================

PROBLEM: Neither pure theory nor pure intuition is reliable.
  Pure theory (from first principles): may give counterintuitive results.
  Pure intuition: may reflect bias, culture, limited perspective.

REFLECTIVE EQUILIBRIUM:
  Start with intuitions about particular cases.
  Propose general principles to explain the intuitions.
  Apply principles to new cases.
  If principles give unacceptable results: revise principles.
  If intuitions conflict with well-supported principles: revise intuitions.
  Continue until coherent (in equilibrium).

  CASE        PRINCIPLE
  (intuition) <--------> (theory)
     ^                       ^
     |    reflective         |
     +----> equilibrium <----+

ANALOGY (MIT TCS connection):
  This is similar to the process in formal methods:
  You have a formal specification (principles) and test cases (intuitions).
  When they conflict, you revise either the spec or reclassify the test case.
  Rawls' method is the ethical analog of test-driven specification.

LIMITATIONS:
  No guarantee of converging to truth.
  Coherent theory can still be systematically biased.
  (Historically: many coherent theories defending slavery, etc.)
  Rawls: requires "wide" reflective equilibrium including
  background theories of justice, politics, and person.
```

---

## Moral Psychology: How We Actually Make Moral Judgments

```
HAIDT'S MORAL FOUNDATIONS THEORY (2001, 2012)
===============================================

Jonathan Haidt: "The Righteous Mind"
Moral reasoning is mostly post-hoc rationalization of intuitive judgments.

SIX MORAL FOUNDATIONS:
  1. CARE/HARM: evolved care for children, aversion to suffering
  2. FAIRNESS/RECIPROCITY: evolved cooperation, cheater detection
  3. LOYALTY/BETRAYAL: coalition formation, in-group solidarity
  4. AUTHORITY/SUBVERSION: respect for hierarchy and tradition
  5. SANCTITY/DEGRADATION: disgust system applied to purity
  6. LIBERTY/OPPRESSION: resistance to bullying and coercion

  LIBERALS (US): emphasize Care and Fairness.
  CONSERVATIVES (US): weight all six.
  This explains why liberals and conservatives talk past each other:
  they're using different moral vocabularies.

GREENE'S DUAL-PROCESS MODEL:
  Two systems for moral judgment:
  System 1 (fast, automatic, emotional): generates intuitive judgments.
    Outputs: "DON'T DO IT" (deontological-ish)
    Evolved for personal interactions.
  System 2 (slow, deliberate, rational): reasoning about consequences.
    Outputs: cost-benefit calculations (utilitarian-ish)
    Recruited for abstract cases.

  Trolley problem: footbridge variant engages System 1 (personal).
  Track variant: more abstract, engages System 2 more.
```

---

## Ethics and Decision Theory (MIT TCS Bridge)

```
ETHICS AND FORMAL DECISION THEORY
====================================

Your MIT math/TCS background maps directly onto formal ethics:

DECISION THEORY:
  Rational choice under uncertainty.
  Expected utility maximization: E[U] = sum_i P(outcome_i) * U(outcome_i)
  Consequentialism is essentially decision theory applied to morality.

  OBJECTION: Utility functions can encode any values including bad ones.
  Decision theory is a FORMAL TOOL; it doesn't specify WHAT to maximize.
  Ethics specifies what goes in the utility function.

MECHANISM DESIGN (Hurwicz, Maskin, Myerson -- Nobel 2007):
  Design systems/institutions that align individual incentives with
  social goals.
  This is deontology-adjacent: design rules that produce good outcomes
  regardless of individual utility.

SOCIAL CHOICE THEORY (Arrow 1951):
  Arrow's Impossibility Theorem: No voting procedure satisfies
  all of: unanimity, independence of irrelevant alternatives,
  non-dictatorship.
  Moral implication: there is no "perfect" procedure for aggregating
  individual preferences into social decisions.
  Consequentialism (aggregate welfare) must grapple with this.

THE ALIGNMENT PROBLEM AS FORMAL ETHICS:
  AI alignment = formal specification of human values.
  Goodhart's Law: when a measure becomes a target, it ceases to be
  a good measure. (Reward hacking in RL.)
  Inverse reinforcement learning: infer the reward function from behavior.
  But: behavior can reflect biased values.
  Constitutional AI (Anthropic): specify principles; let AI critique itself.
  All of these are practical engineering attempts to solve
  the is/ought problem computationally.
```

---

## Field Map

```
ETHICS GUIDE MAP
=================

01-METAETHICS.md        Realism, anti-realism, expressivism, error theory
                        What IS morality? Semantic and metaphysical questions.

02-CONSEQUENTIALISM.md  Bentham, Mill, Singer, effective altruism
                        Maximize good outcomes. Population ethics.

03-DEONTOLOGY.md        Kant's categorical imperative, Ross, Nozick, rights
                        Duty-based constraints; means/ends; rights as side constraints.

04-VIRTUE-ETHICS.md     Aristotle, eudaimonia, phronesis, Stoics, MacIntyre
                        Character over rules; human flourishing.

05-RAWLS.md             Original position, veil of ignorance, difference principle
                        Contractarian justice; fairness as foundational.

06-APPLIED-ETHICS.md    Bioethics, professional ethics, end-of-life
                        Principlism, specific case analysis.

07-RESEARCH-ETHICS.md   Nuremberg, Helsinki, Belmont, IRBs
                        Historical atrocities that built the framework.

08-AI-ETHICS.md         Alignment, fairness impossibility, governance, GDPR
                        The ethics most directly relevant to VP at Microsoft/Azure.

09-GLOBAL-JUSTICE.md    Cosmopolitanism, poverty, climate justice, migration
                        What do we owe people far away?
```

---

## Decision Cheat Sheet

| Level | Question | Key concept | See |
|---|---|---|---|
| Metaethics | Are moral facts real? | Realism vs. anti-realism | 01 |
| Normative | What should I maximize? | Consequentialism, utilitarianism | 02 |
| Normative | What duties do I have? | Categorical imperative, rights | 03 |
| Normative | What kind of person should I be? | Virtue, eudaimonia | 04 |
| Normative | What is a just society? | Rawls, veil of ignorance | 05 |
| Applied | Healthcare decisions | Principlism, autonomy | 06 |
| Applied | Research involving humans | Nuremberg Code, IRBs | 07 |
| Applied | AI systems | Alignment, fairness, governance | 08 |
| Applied | Global poverty, climate | Cosmopolitanism | 09 |

---

## Common Confusion Points

**"Ethics is just opinions."**
This is the position of moral relativism, which is one metaethical position — not obviously correct. Moral realists think there are mind-independent moral facts. Even anti-realists (expressivists, error theorists) can say that some moral claims are better-supported than others, some arguments more valid, some positions more coherent. The fact that ethics is contested doesn't mean all positions are equally defensible.

**"You can derive ethics from facts about human nature."**
This is moral naturalism. G.E. Moore's open question argument is the standard challenge: for any natural property F, it always seems coherent to ask "but is F-ness good?" This suggests that "good" is not identical to any natural property. Naturalists have responses, but the argument is serious.

**"The trolley problem is too unrealistic to be useful."**
Thought experiments are unrealistic by design — to isolate the relevant variables. The trolley problem isolates the question: does the means/ends distinction matter morally when consequences are otherwise identical? This is a real question that arises in genuine cases (self-driving car algorithms, triage, military ethics). The unrealism is a feature that makes the variable isolation possible.

**"Rawls' veil of ignorance is about economics."**
The original position is a general device for deriving principles of justice. The difference principle (inequalities are just only if they benefit the least advantaged) has economic implications, but the method applies to any domain: political liberties, access to offices, distribution of rights. It's a method for impartial reasoning, not an economic theory.

**"AI ethics is just compliance with regulations."**
Compliance is the minimum floor. The substantive questions — what should AI systems be designed to do, how to handle tradeoffs between fairness and accuracy, what counts as harm, who should govern AI, what obligations exist to affected populations — are genuinely philosophical and require engaging with normative ethics, not just checking legal boxes.
