# Reasoning and Judgment — Cognitive Science

## The Big Picture

Humans are neither fully rational nor uniformly irrational. They use **heuristics** — fast, frugal inference rules that work well in most natural environments but produce systematic errors in carefully constructed laboratory (and real-world) situations.

```
+------------------------------------------------------------------+
|  THE JUDGMENT LANDSCAPE                                          |
+------------------------------------------------------------------+
|                                                                  |
|  Normative theory           Descriptive theory                   |
|  (what we should do)        (what we actually do)                |
|                                                                  |
|  Expected utility theory    Prospect theory                      |
|  Bayesian inference         Heuristics and biases                |
|  Logic                      Dual-process (S1/S2)                 |
|                                                                  |
|  The gap between these is the subject of this module.            |
|  The gap is not random noise — it is systematic and              |
|  theoretically interpretable.                                    |
+------------------------------------------------------------------+
```

**The founding insight** (Tversky & Kahneman 1974 *Science* paper): Human judgment under uncertainty relies on a limited number of heuristic principles, which reduce complex inferential tasks to simpler ones. These generally work well but sometimes lead to severe and systematic errors.

---

## The Wason Selection Task

The most replicated finding in cognitive psychology.

```
Four cards: [A] [K] [4] [7]
Each card has a letter on one side and a number on the other.
Rule: "If a card has a vowel on one side, it has an even number on the other"
Which card(s) must you turn over to test the rule?

Correct answer: A and 7
Common answer: A and 4  (~90% of university students get this wrong)
```

Why? The rule is a conditional P→Q. To falsify it you need: P true + Q false. So you need:
- Turn A (P=vowel): check whether Q=even on back
- Turn 7 (Q=odd, not-Q): check whether P=vowel on back — if it is, rule falsified
- K (not-P): irrelevant — rule says nothing about consonants
- 4 (Q=even): irrelevant — rule already satisfied whether vowel or not on back

People confuse **confirmation** (turn A) with **falsification** (turn 7). Confirmation bias is already present in abstract reasoning.

**Deontic version** (Griggs & Cox 1982; Cheng & Holyoak "pragmatic reasoning schemas"):
```
Rule: "If you are drinking alcohol, you must be over 21"
Cards: [drinking beer] [drinking cola] [age 25] [age 16]

~70% correct (beer, age 16)
```
Same logical structure, dramatically better performance when framed as a social contract with permission/violation structure. The brain is better at detecting cheaters than evaluating abstract propositions.

---

## Dual-Process Theory (Kahneman)

The organizing framework for the heuristics-and-biases program:

```
+------------------------------------------------------------------+
|  SYSTEM 1                      SYSTEM 2                          |
|  (Fast / Heuristic)            (Slow / Analytic)                 |
+------------------------------------------------------------------+
|  Automatic                     Effortful                         |
|  Unconscious                   Conscious                         |
|  Parallel                      Serial                            |
|  High capacity                 Low capacity                      |
|  Context-sensitive             Context-insensitive               |
|  Associative                   Rule-governed                     |
|  Emotional                     Logical                           |
|  "What you see is all          Checks and corrects S1            |
|  there is" (WYSIATI)           but often doesn't bother          |
+------------------------------------------------------------------+
|  Fast, intuitive judgments     Deliberate reasoning              |
|  Pattern recognition           Mathematical calculation          |
|  Expert skill                  Planning                          |
|  Emotional response            Following rules explicitly        |
+------------------------------------------------------------------+
```

**Important caveats**:
- System 1 / System 2 are labels for processes, not brain regions
- The terminology is debated (Evans uses Type 1/Type 2; Stanovich distinguishes further)
- S2 often *endorses* S1 output rather than correcting it — the "lazy controller"
- Expertise can move things from S2 to S1 (deliberate practice automates skill)

**WYSIATI** ("What You See Is All There Is"): S1 constructs the most coherent story from available information, ignoring what it doesn't know. This is fast and efficient but creates systematic errors when the framing is manipulated.

---

## Cognitive Bias Taxonomy

### Availability Heuristic
Frequency/probability estimated by *ease of retrieval from memory*.

```
Judging frequency by how easily examples come to mind.
Plane crash → memorable → overestimate aviation risk
Car accident → unremarkable → underestimate road risk
```
- After a dramatic news story, that cause of death seems more frequent
- People who can easily imagine a cancer diagnosis (smokers, family history) overestimate its probability

### Representativeness Heuristic
Probability assessed by *similarity to a prototype*.

**Base rate neglect**: A taxi cab is 85% green, 15% blue. A witness identifies a cab as blue (reliability: 80%). What probability that the cab was actually blue?

Bayesian answer: P(blue|identified blue) = (0.15 × 0.80) / (0.15×0.80 + 0.85×0.20) = 0.41 — still less than 50% blue despite the witness's identification. Most people ignore the base rate and report ~80%.

**Conjunction fallacy** (Linda problem, Tversky & Kahneman 1983):
```
Linda is 31, single, outspoken, very bright. Majored in philosophy.
Concerned about discrimination and social justice.

Rank probability:
(A) Linda is a bank teller
(B) Linda is a bank teller and is active in the feminist movement

85% of subjects rank B as more probable than A — violating the
conjunction rule P(A∩B) ≤ P(A).
```
Explanation: Linda matches the feminist prototype, so the conjunction feels more representative. The "and" should *lower* probability, not raise it.

**Gambler's Fallacy**: After HHHHHH, next flip is "due" to be T. No — each flip is independent. The representativeness of a sequence is confused with the probability of individual outcomes.

### Anchoring Effect
Initial value influences subsequent estimates even when irrelevant.

```
Subjects spin a wheel (rigged to land on 10 or 65).
Then: "What percentage of African countries are in the UN?"
High anchor (65): median estimate 45%
Low anchor (10): median estimate 25%
```
Anchoring persists even when subjects know the anchor is random. The first number serves as a starting point; adjustment is typically insufficient.

**Engineering implication**: Estimates generated first in a planning meeting anchor subsequent estimates. This is the planning fallacy's cousin.

### Framing Effect
The same information described differently leads to different choices.

```
Disease program options:
GAIN FRAME: A = 200 people saved; B = 1/3 chance 600 saved, 2/3 chance 0 saved
→ 72% choose A (risk-averse for gains)

LOSS FRAME: A = 400 people die; B = 1/3 chance nobody dies, 2/3 chance 600 die
→ 78% choose B (risk-seeking for losses)

These are mathematically identical. Choice flips based on framing.
```

### Other Key Biases

| Bias | Description | Engineering Example |
|------|-------------|-------------------|
| **Confirmation bias** | Seek/interpret evidence consistent with existing belief | Debug by testing only expected behavior paths |
| **Sunk cost fallacy** | Weight prior irrecoverable costs in future decisions | Keep rewriting bad code because "we've already spent 3 months" |
| **Planning fallacy** | Underestimate time/cost of future projects; ignore outside view | Project estimates — see below |
| **Overconfidence** | Confidence exceeds accuracy; 90% CI intervals too narrow | "This will take 2 weeks" |
| **Hindsight bias** | "I knew it all along" after the fact | Post-mortems: "Of course the system would fail that way" |
| **Status quo bias** | Prefer current state; change requires extra justification | "We've always done it this way" |
| **Automation bias** | Over-trust automated outputs; under-monitor | Trust code review tools uncritically |
| **Dunning-Kruger** | Unskilled overestimate competence; experts underestimate (often misrepresented: the original paper showed both, replication contested) | |

**Planning fallacy** (Kahneman & Tversky 1979):
- Inside view: estimate based on specific features of this project → optimistic
- Outside view: estimate based on statistical base rate of similar projects → accurate
- Fix: explicitly ask "How long did similar projects take?" before adding task-specific adjustments

---

## Prospect Theory (Kahneman & Tversky 1979)

Nobel Prize 2002. Replaces expected utility theory as the descriptive model of choice under uncertainty.

**Four components**:

### 1. Reference Dependence
Utility is defined relative to a **reference point** (usually the status quo), not absolute wealth.
- A gain of $100 from $0 feels different from being at $100 and losing $0.
- The same objective state can be a gain or loss depending on reference point.

### 2. Loss Aversion
Losses hurt approximately **twice as much** as equivalent gains feel good.

```
UTILITY
  |     /
  |    /
  |   /   <-- gains (concave -- diminishing returns)
  |  /
  | /
  |/_____________________ WEALTH relative to reference point
   \
    \   <-- losses (convex -- diminishing returns for losses too)
     \
      \  Loss of $100 ≈ emotional impact of gain of $200
```

**~2:1 ratio** (varies by domain, but loss aversion is robust).

Applications:
- Endowment effect: once you own something, you demand more to give it up than you'd pay to acquire it
- Status quo bias: losses from changing > gains, so no change preferred
- Insurance: overpay for small-loss coverage (loss aversion dominates)

### 3. Diminishing Sensitivity
Marginal value diminishes as you move away from the reference point in either direction. The difference between $0 and $100 is felt more strongly than between $1000 and $1100.

### 4. Probability Weighting
Objective probabilities are distorted:
```
Probability    Weight
0              0
Very low       Higher than actual (overweight small probs)
0.1-0.9        Lower than actual (underweight medium probs)
Very high      Lower than actual (underweight near-certainties)
1.0            1.0

Result:
  Lottery tickets (very low prob big win) — overvalued
  Insurance (very low prob big loss) — also overvalued
  Near-certain outcomes feel more certain than they are
  (certainty effect)
```

---

**Formal note for the mathematically inclined**: The probability weighting function pi(p) is a nonlinear distortion of the objective probability measure. The precise claim is that humans evaluate gambles using V = sum[pi(p_i) * v(x_i)] rather than E[u(x)] = sum[p_i * u(x_i)]. The weighting function pi is an inverted-S: concave near 0 (overweight small p), convex near 1 (underweight near-certainties), with a fixed point around p ~ 0.35. This violates the independence axiom of expected utility theory. Cumulative Prospect Theory (Tversky & Kahneman 1992) fixes a technical problem: original PT can violate stochastic dominance. CPT uses rank-dependent integration — weights are applied to cumulative probabilities rather than individual outcomes, preserving monotonicity of the preference ordering while retaining the empirical predictions.

## Bounded Rationality (Simon 1955)

Herbert Simon's alternative to classical economic rationality:
- Humans don't *optimize* — they **satisfice** (find solutions that are "good enough")
- The search process stops when a threshold of acceptability is met
- This is rational given real cognitive constraints (limited time, limited memory, limited computation)

**Reasons for boundedness**:
1. **Limited information**: We never have all relevant information
2. **Limited computational capacity**: Optimization is often NP-hard
3. **Limited time**: Decisions must be made under time pressure

**The "fast and frugal heuristics" program** (Gigerenzen et al.): An alternative to the Kahneman framing. Heuristics are not *biases* — they are *ecologically rational* strategies that work well in the environment for which they evolved. "Less is more": in uncertain environments, simple rules often outperform complex optimization.

**The debate**: Kahneman: heuristics cause systematic errors; we should correct for them. Gigerenzen: heuristics are adaptive; the errors only appear in artificial lab conditions. Both have good evidence. The resolution depends on the specific task and environment.

---

### The Lazy Controller Problem — Does System 2 Actually Correct?

The textbook story is that S2 monitors S1 and intervenes when S1's output is wrong. The empirical picture is worse.

**The bat-and-ball problem** (Frederick 2005):
```
A bat and a ball cost $1.10 in total.
The bat costs $1.00 more than the ball.
How much does the ball cost?

Intuitive (S1) answer: $0.10
Correct (S2) answer:   $0.05  (ball=0.05, bat=1.05, total=1.10)

Result: ~80% of students at top universities (MIT, Princeton)
give the wrong answer. Even among those who get it right,
many report the intuitive answer "felt right" first.
```

**Stanovich's "cognitive miser" framework**: S2 is not a vigilant monitor — it is a lazy endorser. The default is to accept S1's output. S2 intervenes only when:
1. The problem is explicitly flagged as requiring calculation
2. The S1 output produces an obvious contradiction
3. The person has high "need for cognition" (trait-level disposition to think carefully)

**Why this matters**: The dual-process model is not S1-makes-errors / S2-corrects-them. It is S1-makes-judgments / S2-usually-rubber-stamps-them. The engineering implication is that checklists, pre-mortems, and structured decision protocols work *because they force S2 engagement* — not because people naturally exercise S2 oversight. Without procedural forcing functions, S2 rationalizes rather than overrides.

## Decision Cheat Sheet

| Phenomenon | What's happening | Correction strategy |
|------------|-----------------|-------------------|
| Availability bias | Vivid/recent examples inflate probability estimates | Ask for base rate statistics; use outside view |
| Representativeness | Category match overrides base rate | Force yourself to compute base rates explicitly |
| Anchoring | First number distorts all subsequent estimates | Deliberate "de-anchoring": generate independent estimate first |
| Framing effect | Gain vs loss presentation flips choice | Reframe the same problem both ways; check if choice changes |
| Confirmation bias | Seeking confirming evidence | Pre-mortems; adversarial collaboration; red team |
| Planning fallacy | Inside view is too optimistic | Reference class forecasting; distribution of similar project outcomes |
| Sunk cost | Counting irrecoverable costs | Ask: "If we hadn't spent anything yet, would we proceed?" |
| Loss aversion | Losses dominate decision-making | Reframe as opportunity cost; compute expected value explicitly |

---

## Common Confusion Points

**Dual-process ≠ two brain regions**: System 1 is not the limbic system; System 2 is not the frontal lobe. These are functional descriptions of process types, not anatomical structures. Most cognitive neuroscientists use the terminology cautiously.

**Heuristics ≠ always wrong**: Availability heuristic is accurate when memory retrieval frequency correlates with world frequency (common situations). It fails in specific cases (dramatic rare events). Same with representativeness. The bias appears when the heuristic is applied outside its domain of validity.

**Prospect theory doesn't predict all choices**: It's a descriptive model of risky choice in simple gambles. It handles framing, loss aversion, and probability weighting well. It struggles with: multi-attribute choices, sequential decisions, social preferences, and ambiguity (where probabilities themselves are unknown — Ellsberg paradox → requires Choquet expected utility or ambiguity aversion models).

**Wason task ≠ test of general intelligence**: PhDs from top universities fail the abstract version at the same rate as everyone else. The task tests a specific competence (formal conditional logic), not general reasoning ability. Deontic versions reveal domain-specific competence (social contracts) that doesn't transfer to abstract form.

**Cross-reference**: For the neural bases of decision-making (dopamine, orbitofrontal cortex, amygdala), see `neuroscience/03-COGNITION-COMPUTATION.md`. Prospect theory links to finance — see `finance/02-DERIVATIVES.md` for risk-neutral pricing and `finance/04-RISK-MODELS.md` for behavioral risk measures.
