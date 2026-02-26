# Rawls: A Theory of Justice

## The Big Picture

```
+-----------------------------------------------------------------------+
|                    RAWLS' THEORY OF JUSTICE                            |
+-----------------------------------------------------------------------+
|                                                                       |
|  QUESTION: What principles of justice would rational persons          |
|  choose for their society?                                            |
|                                                                       |
|  METHOD: Original Position + Veil of Ignorance                       |
|  +-------------------------------------------------+                 |
|  | Persons behind a veil of ignorance do not know: |                 |
|  | - Their place in society                        |                 |
|  | - Their natural talents or abilities            |                 |
|  | - Their conception of the good                  |                 |
|  | - Their generation                              |                 |
|  | - Their psychological profile                   |                 |
|  +-------------------------------------------------+                 |
|                                                                       |
|  RESULT: Two principles of justice, lexically ordered:               |
|  1. Equal basic liberties (liberty principle)                        |
|  2. Fair equality of opportunity + difference principle              |
+-----------------------------------------------------------------------+
```

---

## The Original Position and Veil of Ignorance

```
THE ORIGINAL POSITION (Rawls 1971)
=====================================

WHAT IT IS:
  A hypothetical thought experiment, not an actual historical state.
  A device of representation: what principles would persons choose
  if they were choosing from behind a veil of ignorance about
  their own position in society?

WHAT THE VEIL CONCEALS:
  - Social position: rich/poor, high/low status
  - Natural talents: intelligence, strength, health
  - Conception of the good: what you value and want
  - Psychological profile: risk tolerance, envy, ambition
  - Historical facts about one's society
  - Generation: whether you're in the first, current, or future gen.

WHAT IS KNOWN BEHIND THE VEIL:
  - General facts of economics, psychology, sociology
  - How institutions work
  - The conditions that make justice necessary
  - What primary goods are (things any rational person wants
    regardless of their specific conception of the good:
    liberties, opportunities, income/wealth, social bases of self-respect)

THE POINT:
  The veil of ignorance ensures impartiality.
  You can't choose principles that favor YOUR position
  because you don't know your position.
  You choose from behind genuine uncertainty.
  This is a fairness constraint on the choice of principles.

MIT TCS BRIDGE:
  The original position is analogous to game theory under uncertainty.
  Rawls' parties choose maximin (maximize the minimum payoff).
  This is the correct strategy under uncertainty when:
  - Outcomes matter enormously
  - No rational basis for assigning probabilities
  - Can't accept a really bad outcome
  Rawls argues: justice involves all three conditions.
```

---

## The Two Principles of Justice

```
THE TWO PRINCIPLES (Final Formulation)
========================================

FIRST PRINCIPLE (Liberty Principle):
  "Each person has the same indefeasible claim to a fully adequate
  scheme of equal basic liberties, which scheme is compatible with
  the same scheme of liberties for all."

  BASIC LIBERTIES:
  - Freedom of thought and conscience
  - Political liberties (vote, run for office)
  - Freedom of association
  - Personal liberties (bodily integrity, rule of law)
  - Freedoms protected by the rule of law

  PRIORITY: This principle takes lexical priority over the second.
  No amount of economic benefit can justify restricting basic liberties.
  (Except by balancing against each other: free speech vs. privacy.)

SECOND PRINCIPLE (combines two sub-principles):
  Social and economic inequalities are just only if they satisfy:

  (a) FAIR EQUALITY OF OPPORTUNITY (FEO):
  Attached to positions and offices open to all under conditions
  of fair equality of opportunity.
  Not just formal equality (no legal barriers).
  Substantive equality: similar talents and willingness to use them
  should have similar life prospects regardless of social origin.
  Requires: public education, affirmative steps to counteract
  advantages of favorable social position.

  (b) DIFFERENCE PRINCIPLE:
  They are to be to the greatest benefit of the least-advantaged
  members of society.
  Inequalities are just ONLY IF they make the worst-off
  as well-off as possible.
  This is not equality of outcome -- inequalities are allowed.
  But: they must benefit the bottom of the distribution.
  (Pareto improvement relative to equality, directed at the bottom.)

LEXICAL ORDERING:
  First principle > FEO > Difference Principle.
  Liberty is not traded off for equality.
  Fair opportunity is not traded off for aggregate welfare.
  The difference principle applies within whatever is left.
```

---

## Maximin and the Rationale for the Difference Principle

```
MAXIMIN REASONING
==================

Why would parties in the original position choose the difference principle?

MAXIMIN STRATEGY:
  Choose the option whose worst possible outcome is best.
  Rational when:
  1. The stakes are high enough that a bad outcome is catastrophic.
  2. No rational basis for probability assignment.
  3. The gain from risking a better outcome is not worth the risk.

  In the original position:
  1. High stakes: you're choosing the basic structure of society.
     Being in the worst-off position is very bad.
  2. No rational basis for probability: you don't know how likely
     you are to be in any position.
     (Rawls rejects Harsanyi's equal probability assumption:
      there's no basis to assign equal or any specific probabilities.)
  3. Gains not worth risk: the least-advantaged position could be
     quite bad; the principle ensures it is as good as possible.

  Therefore: choose the principle that maximizes the minimum.
  = Difference principle.

RAWLS vs. HARSANYI:
  Harsanyi: behind the veil, assign equal probability to each position.
  Maximize expected utility.
  This gives average utilitarianism.

  Rawls: no rational basis for equal probability assignment.
  Use maximin.
  This gives the difference principle.

  The dispute is about decision theory under uncertainty.
  MIT TCS connection: this is decision theory applied to social choice.
```

---

## Reflective Equilibrium Method

```
REFLECTIVE EQUILIBRIUM (RAWLS' METHOD)
========================================

See also: 00-OVERVIEW.md (brief treatment).

PROCEDURE:
  1. Collect considered moral judgments (about specific cases).
  2. Propose principles that systematize them.
  3. Test principles against further cases.
  4. If conflict: revise principles OR revise considered judgments.
  5. Reach wide reflective equilibrium including background theories.

WHY IT'S THE RIGHT METHOD (Rawls argues):
  Neither pure theory (from first principles) nor pure intuition works.
  Pure theory can lead anywhere if premises are wrong.
  Pure intuition may be biased, parochial, unreflective.
  RE is iterative: responsive to both theory and intuition.

COHERENTISM IN ETHICS:
  RE is the ethical analog of coherentism in epistemology.
  Beliefs are justified by their coherence with a web of beliefs.
  Moral beliefs are justified by their coherence with principles
  and background theories.

OBJECTION:
  RE allows starting points to influence endpoint.
  Different starting intuitions --> different stable equilibria.
  No guarantee of convergence to moral truth.

RAWLS' RESPONSE:
  Wide RE includes background theories of justice, psychology,
  and the nature of persons.
  These constrain the equilibrium more tightly.
  Also: this method is appropriate for the nature of moral knowledge.
  We don't have better access to moral truth than through this process.
```

---

## Rawls vs. Nozick vs. Utilitarianism

```
RAWLS vs. MAJOR ALTERNATIVES
==============================

RAWLS vs. UTILITARIANISM:
  Utilitarianism: maximize aggregate welfare.
  Could justify violating individual rights if sum is high enough.
  Could justify slavery if it maximizes aggregate utility.

  Rawls: THE SEPARATENESS OF PERSONS.
  "Individuals are distinct and separate. The life of each is not
  combined with others to yield a larger whole."
  You cannot trade off one person's life or rights against
  aggregate gains for others.
  The difference principle is the utilitarian principle corrected
  for the separateness of persons.

  Rawls specifically: utilitarian reasoning is what you get
  when you forget you're distributing to distinct persons.
  "Each member of society has an inviolability that even the
  welfare of society as a whole cannot override."

RAWLS vs. NOZICK:
  Nozick: entitlement theory. Justice = just acquisition + transfer.
  Taxation for redistribution = forced labor.
  Difference principle is not a constraint on voluntary exchange.

  Rawls: the difference principle governs the BASIC STRUCTURE
  of society (constitution, laws, background institutions).
  It doesn't govern individual transactions.
  Within a just basic structure, voluntary exchange is fine.

  NOZICK'S WILT CHAMBERLAIN ARGUMENT:
  Start from a just distribution D1.
  Each of 1 million fans pays Chamberlain 25 cents voluntarily.
  Result D2: Chamberlain has $250,000 more.
  Each fan has 25 cents less.
  D2 arose from D1 by free transactions.
  Each transaction was voluntary.
  How can D2 be unjust if D1 was just and transitions were free?

  RAWLS' RESPONSE:
  The question isn't whether individual transactions were voluntary.
  It's whether the background structure -- tax law, property law,
  inheritance rules -- is just.
  Nozick ignores institutional background.
  A just background structure is the precondition for
  individual transactions to have their claimed legitimacy.
```

---

## Political Liberalism

```
RAWLS: "POLITICAL LIBERALISM" (1993)
======================================

REVISION OF "A THEORY OF JUSTICE":
  ATJ assumed comprehensive liberal doctrine (a full conception
  of the good based on autonomy and rational reflection).
  But: citizens of liberal democracies hold diverse comprehensive
  doctrines (religious, secular, philosophical).
  A state committed to one comprehensive doctrine is not liberal.

PROBLEM OF STABILITY:
  How can a pluralistic society agree on principles of justice
  when citizens hold different comprehensive doctrines?

FREESTANDING POLITICAL CONCEPTION:
  Justice as fairness as a POLITICAL conception -- not a comprehensive
  doctrine about the good life.
  It is a conception that can be endorsed from within different
  comprehensive doctrines for different reasons.

OVERLAPPING CONSENSUS:
  Citizens endorse justice as fairness from within their own
  comprehensive doctrines:
  - Catholics support it on Catholic grounds.
  - Secular liberals support it on Kantian grounds.
  - Rawlsian liberals support it on rational contractor grounds.
  The overlapping consensus sustains the conception without
  requiring agreement on comprehensive doctrine.

PUBLIC REASON:
  In political discourse, citizens should offer reasons that
  all reasonable citizens can accept.
  Not: argue from within your own comprehensive doctrine.
  "My religion says this law should hold" is not public reason.
  "This law protects basic freedoms all citizens have claim to" is.

  This limits what can count as a justification in democratic politics.
  Controversial in practice (religious arguments in politics?).
```

---

## Rawls and AI Ethics

```
RAWLSIAN FAIRNESS IN ALGORITHMIC DECISION-MAKING
==================================================

The Rawlsian criterion applied to algorithms:
  A just algorithm is one that makes no member of society worse off
  by virtue of membership in the least-advantaged group.

  RAWLSIAN FAIRNESS CRITERION (algorithmic version):
  The algorithm should be designed to be most beneficial to the
  least-advantaged affected group.

  Compare to other fairness criteria:
  +----------------------------+----------------------------------+
  | Criterion                  | Definition                       |
  +----------------------------+----------------------------------+
  | Rawlsian maximin           | Maximize worst-off outcome       |
  | Equal accuracy             | Same error rate across groups    |
  | Demographic parity         | Equal positive rates             |
  | Equalized odds             | Equal TPR and FPR                |
  | Calibration                | Same predicted probabilities     |
  +----------------------------+----------------------------------+

  Chouldechova's impossibility: these cannot all be satisfied when
  base rates differ across groups.
  Rawlsian lens: we should give priority to the worst-off
  group's error rate, not aggregate accuracy.

FAIR EQUALITY OF OPPORTUNITY IN AI:
  Facial recognition systems that are more accurate for white faces
  than Black faces: violate fair equality of opportunity.
  Similar talent (e.g., in hiring) should have similar prospects
  regardless of social origin.
  If an algorithm proxies race through zip code, it violates FEO.

VEIL OF IGNORANCE THOUGHT EXPERIMENT FOR AI DESIGN:
  Design an algorithm under a veil of ignorance about which
  group you'd be in.
  What error rates would you accept not knowing if you were
  in the high-risk or low-risk group?
  This is a practical design heuristic.
```

---

## Decision Cheat Sheet

| Concept | Definition | Where in Rawls |
|---|---|---|
| Original position | Hypothetical choice situation for deriving principles | A Theory of Justice, ch. 3 |
| Veil of ignorance | Remove knowledge of one's position to ensure impartiality | ATJ, ch. 3 |
| Primary goods | Things any rational person wants: liberties, opportunities, income, self-respect | ATJ, ch. 5 |
| First principle | Equal basic liberties; lexically prior | ATJ, §11 |
| Fair equality of opportunity | Similar talents have similar prospects regardless of origin | ATJ, §14 |
| Difference principle | Inequalities just only if they benefit the worst-off | ATJ, §13 |
| Maximin | Strategy: maximize the worst possible outcome | ATJ, §26 |
| Reflective equilibrium | Method: iterate between principles and considered judgments | ATJ, §9 |
| Separateness of persons | Can't trade off across persons like across time | ATJ, §5 |
| Overlapping consensus | Diverse doctrines agree on political conception | Political Liberalism |
| Public reason | Political justifications must be acceptable to all reasonable citizens | Political Liberalism |

---

## Common Confusion Points

**"Rawls wants equal outcomes for everyone."**
Rawls does NOT argue for equal outcomes. The difference principle allows inequalities — it just requires that any inequality benefit the worst-off group. A surgeon who earns more than an average worker can be consistent with the difference principle if the inequality is needed to incentivize medical training and results in better healthcare for the poor.

**"The veil of ignorance is unrealistic — people can't forget who they are."**
It's a hypothetical thought experiment, not a description of an actual choice. The veil is a device for testing the impartiality of principles: would you endorse this principle if you didn't know your position? If not, it may reflect bias toward your own position. The unrealism is intentional.

**"The difference principle = trickle-down economics."**
No. The difference principle says inequalities must actively benefit the worst-off. Trickle-down theory says benefits for the wealthy passively trickle down. The difference principle is an evaluative standard requiring institutions to be arranged so the worst-off actually benefit — this often requires active redistribution and equal opportunity programs.

**"Rawls' political liberalism means religious arguments can't influence policy."**
Public reason applies to citizens' arguments in fundamental political matters (constitutional essentials). Religious persons can be motivated by faith. But when offering justifications in the public square, they should also offer reasons accessible to citizens who don't share their faith. The restriction is on justificatory form, not on motivation or outcome.

**"Maximin is an irrational decision procedure."**
Maximin is irrational in standard decision theory when you have well-defined probabilities and the stakes aren't extreme. Rawls argues: behind the veil of ignorance, probabilities are not well-defined (there's no basis for equal or any probability assignment), and the stakes are extremely high (life prospects). Under these conditions, maximin is a reasonable strategy. This is a specific argument about the specific features of the original position, not a general endorsement of maximin reasoning.
