# Causation and Explanation: Hempel DN Model, Causal Mechanisms, Interventionism

## The Big Picture

Two questions that look similar but are distinct: (1) What is causation? (2) What is scientific explanation? They come apart — you can explain without citing causes (some DN explanations), and you can identify causes without explaining (regularity theory). The modern answer to both involves causal structure: explanation is usually explanation by causal mechanism, and causation is analyzed via counterfactuals or interventions.

```
+------------------------------------------------------------------+
|            THEORIES OF EXPLANATION AND CAUSATION                |
+------------------------------------------------------------------+
|                                                                  |
|  MODELS OF EXPLANATION:                                          |
|  +------------------+  +-------------------+  +---------------+ |
|  |  DN MODEL        |  |  CAUSAL-MECHANICAL|  |  PRAGMATIC    | |
|  |  (Hempel)        |  |  (Salmon)         |  |  (van Fraassen| |
|  |  Deduction from  |  |  Explanation via  |  |  Explanation  | |
|  |  laws + conds.   |  |  causal processes |  |  relative to  | |
|  |                  |  |  and conserved    |  |  interests and| |
|  |                  |  |  quantities       |  |  contrast classes|
|  +------------------+  +-------------------+  +---------------+ |
|                                                                  |
|  THEORIES OF CAUSATION:                                          |
|  +------------------+  +-------------------+  +---------------+ |
|  |  REGULARITY      |  |  COUNTERFACTUAL   |  |  INTERVENTIONIST|
|  |  (Hume)          |  |  (Lewis)          |  |  (Woodward)   | |
|  |  C causes E =    |  |  C causes E =     |  |  C causes E = | |
|  |  Cs regularly    |  |  if C had not     |  |  ideal interv.|  |
|  |  followed by Es  |  |  occurred, E would|  |  on C changes | |
|  |                  |  |  not have occurred|  |  E            | |
|  +------------------+  +-------------------+  +---------------+ |
|                                                                  |
|  CAUSAL BAYES NETS:                                              |
|  Graph structure encodes conditional independence; do-calculus  |
|  distinguishes observation (P(E|C)) from intervention (P(E|do(C)))|
|                                                                  |
+------------------------------------------------------------------+
```

---

## Hempel's Deductive-Nomological (DN) Model

### The Model

Carl Hempel (1948, with Oppenheim) proposed that scientific explanation is deduction from laws plus initial conditions:

```
DEDUCTIVE-NOMOLOGICAL STRUCTURE:

  L1, L2, ..., Lk     (laws of nature)
  C1, C2, ..., Cm     (initial conditions / antecedent conditions)
  ─────────────────── (deductive entailment)
  E                   (explanandum: the phenomenon to be explained)

EXAMPLE: Why did the mercury rise when heated?
  L1: For any substance with high thermal expansion coefficient,
      an increase in temperature produces volume expansion
  L2: Mercury has a high thermal expansion coefficient
  C1: The mercury was heated (temperature increased)
  ─────────────────────────────────────────────────
  E:  The mercury expanded (rose in the tube)
```

The **explanandum** is the phenomenon to be explained. The **explanans** is the set of sentences (laws + conditions) that does the explaining. The model requires the explanans to *entail* the explanandum.

### Hempel's Requirements

1. The explanandum must be a logical consequence of the explanans
2. The explanans must contain at least one law
3. The explanans must have empirical content (testable)
4. The sentences of the explanans must be true

---

## Problems with the DN Model

### 1. The Asymmetry Problem (Flagpole)

```
FLAGPOLE ARGUMENT:

  Observation: A flagpole of height H casts a shadow of length S
  given sun at angle θ.

  DN EXPLANATION 1 (correct):
  L:  Law of rectilinear propagation of light + geometry
  C1: Pole height H, sun at angle θ
  ─────────────────────────
  E:  Shadow length S = H/tan(θ)     ← GOOD explanation

  DN EXPLANATION 2 (problematic):
  L:  Same optical laws
  C1: Shadow length S, sun at angle θ
  ─────────────────────────
  E:  Pole height H = S · tan(θ)     ← "Explains" pole height!

  But shadow does not CAUSE or explain the pole's height.
  The pole causes the shadow. DN model gets the direction wrong.
  Asymmetry in causation is not captured by symmetric deduction.
```

### 2. The Irrelevance Problem

```
BIRTH CONTROL PILLS AND PREGNANCY:

  L:  No man who takes birth control pills gets pregnant
  C:  John takes birth control pills
  ────────────────────────────────
  E:  John does not get pregnant

  This is a valid DN explanation. But John's taking birth
  control pills is IRRELEVANT to his not getting pregnant.
  The real explanation is: John is male.

  DN model cannot filter irrelevant factors from explanatory ones.
```

### 3. The Problem of Statistical Explanation

For phenomena explained by statistical laws, you cannot deductively entail the explanandum. Hempel developed the **Inductive-Statistical (IS) model** for this case: explanation shows that the explanandum was highly probable given the laws and conditions. But:

- High probability ≠ explanation. A man's recovery from a cold in 7 days is highly probable whether or not he took aspirin. Aspirin doesn't explain the recovery even if it makes it slightly more probable.

---

## Wesley Salmon's Causal-Mechanical Model

Salmon (1984) responded to DN's failures by making causal process central to explanation.

### Causal Processes and Causal Interactions

- **Causal process**: a connected sequence of events with genuine causal continuity (a moving billiard ball, a light ray, a person walking)
- **Causal interaction**: an intersection of processes that produces persistent changes in both (billiard ball collision; wave hitting a rock)
- **Pseudo-process**: apparent process without genuine causal transmission (shadow, moving spotlight on a screen)

The distinction: a causal process can transmit a mark (if you paint part of the ball, the paint persists). A pseudo-process cannot (if you intersect a shadow at one point, the mark doesn't persist downstream).

Salmon later moved to the **conserved quantity** approach: causal processes transmit conserved quantities (energy, momentum, charge). Explanation consists in tracing the causal-mechanical pathways that transmit these quantities to the phenomenon.

---

## Counterfactual Analysis of Causation (Lewis)

David Lewis (1973) proposed the most influential counterfactual theory:

**C causes E** if and only if:
1. C and E both occurred
2. If C had not occurred, E would not have occurred (under the nearest possible world where C is absent)

```
POSSIBLE WORLDS SEMANTICS:

  Actual world:  C occurs, E occurs

  Nearest possible world where C doesn't occur:
  → E also doesn't occur → C caused E (counterfactual dependence)

  OR:
  → E still occurs → C did NOT cause E

  EXAMPLE:
  My flipping the light switch (C) causes the light to go on (E).
  In the nearest world where I don't flip: light stays off.
  → Counterfactual dependence → C caused E

  PROBLEM: PREEMPTION
  Two assassins, A and B. A shoots first and kills the victim.
  B would have shot if A hadn't.

  Does A cause the death? Yes.
  Counterfactual test: if A hadn't shot, B would have.
  The victim STILL DIES. No counterfactual dependence.
  → Lewis's test incorrectly says A didn't cause the death.
```

Lewis responded with increasingly complex extensions (causal chains, transitivity of dependence). The preemption, overdetermination, and late preemption cases are still actively debated.

---

## Interventionism (Woodward)

James Woodward, *Making Things Happen* (2003), proposes the most influential current theory of causation.

### The Core Idea

**X causes Y** if and only if: there is a possible **ideal intervention** on X that would change Y (or the probability distribution of Y) while holding everything else fixed.

An **ideal intervention** on X with respect to Y:
1. Directly affects X (and not Y except through X)
2. "Surgically" sets X without correlating with other causes of Y
3. Blocks any backdoor paths from X to Y

```
INTERVENTIONIST STRUCTURE:

  X ────────────────────→ Y   (X causes Y)

  Intervention I sets X to value x':
  I ──→ X = x' ──────────→ Y changes
        (all other causes of Y unchanged by I)

  If Y changes when I manipulate X: X causes Y.
  If Y doesn't change: X doesn't cause Y (or is not on the right path).
```

### Why Interventionism Is Attractive

1. **Solves the asymmetry problem**: Pole height and shadow length. Can you intervene on shadow length to change pole height? No — you can't reach into the shadow and pull up the pole. Asymmetry is built into the interventionist account.

2. **Connection to scientific practice**: Randomized controlled trials (RCTs) are precisely attempts to implement ideal interventions (random assignment = breaking confounders; controlled administration = surgical manipulation of the treatment variable).

3. **Handles the irrelevance problem**: Birth control pills and male pregnancy. Intervening on pill consumption (randomly assigning pills to men) doesn't change the probability of pregnancy. So pills don't cause non-pregnancy in men.

---

## Causal Bayes Nets and the do-Calculus (Pearl)

Judea Pearl (2000) provides a formal machinery for causal inference.

### The Causal Graph

A directed acyclic graph (DAG) where edges represent direct causal relationships. The **Markov condition**: each variable is conditionally independent of its non-descendants given its parents.

```
EXAMPLE: Smoking and Cancer

     Smoking ────────→ Cancer
        |                 ↑
        |                 |
        └──→ Yellow fingers → (none — confound illustrates)

Actually:
  Genotype ──→ Smoking
  Genotype ──→ Cancer
  Smoking  ──→ Cancer

  DAG:
  Genotype → Smoking → Cancer
      |               ↑
      └───────────────┘

  Observational data: P(Cancer | Smoking) is high.
  Is this causal?
  Confounded: Genotype causes both.
```

### Observation vs. Intervention

Pearl's crucial distinction:

- **Observational query**: P(Cancer | Smoking = high) — what probability of cancer if we select smokers?
- **Interventional query**: P(Cancer | do(Smoking = high)) — what probability of cancer if we *force* someone to smoke?

The **do-operator** models ideal intervention: do(Smoking = high) means setting Smoking = high by intervention, cutting all arrows *into* Smoking in the graph. This removes the effect of confounders.

```
ADJUSTING FOR CONFOUNDERS (do-calculus):

  Original graph: Genotype → Smoking → Cancer
                  Genotype ──────────→ Cancer

  After do(Smoking = high):
  Genotype → [Smoking = high set by intervention] → Cancer
  Genotype ──────────────────────────────────────→ Cancer
  But arrow Genotype → Smoking is CUT (smoking is set by us)

  Now: P(Cancer | do(Smoking)) no longer confounded by Genotype.
  This is what RCTs implement physically.

BACKDOOR CRITERION:
  A set of variables Z blocks all backdoor paths from X to Y.
  Conditioning on Z makes observational = interventional.
  → Can estimate causal effects from observational data
    if you have measured the right confounders.
```

---

## Probabilistic Causation

J.L. Mackie and Patrick Suppes developed probabilistic approaches to causation:

**INUS conditions** (Mackie): C is an **I**nsufficient but **N**ecessary part of an **U**nnecessary but **S**ufficient condition for E.

Example: A house fire. The fire was caused by a short circuit. But:
- The short circuit alone wasn't sufficient (needed oxygen, dry material)
- The whole conjunction (short + oxygen + dry material) was sufficient but unnecessary (arson would also suffice)
- The short circuit was an insufficient but necessary part of this particular sufficient condition

This captures the intuition that a cause "makes a difference" in context, without requiring it to be sufficient or necessary on its own.

---

## Multiple Realizability and Causation (Special Sciences)

Jerry Fodor (1974): Mental states are **multiply realizable** — the same mental state (pain) can be physically implemented in many ways (C-fiber firing in humans, different mechanism in octopuses). If mental states reduce to physical states, and physical states are species-specific, then there are no species-independent physical laws of psychology.

Consequence for causation: Is it the mental state or the physical implementation that causes behavior? Fodor argues mental-level causation is irreducible — there are genuinely causal laws at the level of psychology (stimulus → response) that are not derivable from neuroscience.

This connects to Woodward's interventionism: intervening on the mental-level description can be more predictively powerful than intervening on the physical-level description, when the former is implemented in multiple physical ways.

---

## Decision Cheat Sheet

| Question | Answer |
|----------|--------|
| What is the DN model? | Explanation = deduction from laws + initial conditions; explanandum follows logically from explanans |
| What is the flagpole problem? | Shadow length DN-"explains" pole height, but direction is wrong: DN has no asymmetry |
| What is the counterfactual theory? | Lewis: C causes E iff if C had not occurred, E would not have occurred (nearest possible world) |
| What is the interventionist theory? | Woodward: C causes E iff ideal intervention on C changes E; connects causation to manipulation |
| What is the do-operator? | Pearl: do(X=x) models intervention — sets X by cutting all arrows into X in the causal graph |
| What is backdoor criterion? | A set Z that blocks all non-causal paths from X to Y, enabling observational identification of causal effect |
| What is multiple realizability? | Same functional state can have multiple physical implementations; grounds mental-level causation |

---

## Common Confusion Points

**Correlation ≠ causation and the do-operator makes this precise**: P(Y|X) = conditional probability given observed X value. P(Y|do(X)) = probability given intervened X value. These are different. The gap = confounding. The do-calculus formalizes exactly what informal statisticians mean by "controlling for confounders."

**DN model is not completely wrong**: For certain idealized cases — simple physical processes where causation and laws align neatly — the DN model gives the right answer. The problems are with edge cases (asymmetry, irrelevance) that reveal the model is missing something.

**Counterfactual theory ≠ interventionist theory**: Both use "what if" reasoning. Lewis's account focuses on possible worlds; Woodward's on physical interventions. Woodward's is more empirically grounded; Lewis's is more metaphysically general.

**Causal Bayes nets require a causal assumption**: The DAG structure must be specified; the arrows are not statistically derived — they encode causal assumptions. The statistical tests (conditional independence) check whether the assumed structure is consistent with data, not whether the assumed causation is correct.
