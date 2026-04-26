# Rational Choice — Critique and Alternatives

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│              RATIONAL CHOICE THEORY — LANDSCAPE AND CRITIQUE                │
│                                                                               │
│  LAYER 1: THE FORMAL BASELINE                                               │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Expected Utility Theory (vNM 1944):                                        │
│  EU(L) = Σᵢ pᵢ × U(xᵢ)    [axioms: completeness, transitivity,              │
│                              continuity, independence]                        │
│  Representation theorem: axioms ⟺ exists U s.t. agent maximizes EU          │
│  This is the formal spec. Behavioral critique = finding where               │
│  actual human choices violate the axioms.                                   │
│                                                                               │
│  LAYER 2: SYSTEMATIC VIOLATIONS (empirical falsification of the axioms)     │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Allais Paradox (1953):       Violates INDEPENDENCE axiom                   │
│    Certainty effect — 100% probability is categorically different from 99%  │
│  Ellsberg Paradox (1961):     Violates SUBJECTIVE PROBABILITY axiom         │
│    Ambiguity aversion — known vs unknown probabilities treated differently  │
│  Preference reversals (1979): Violates TRANSITIVITY + COMPLETENESS          │
│    Price vs choice reversal — preferences are context-dependent             │
│  WTA ≫ WTP:                   Violates WEALTH EQUIVALENCE assumption        │
│    Endowment effect — owning something changes its subjective value         │
│                                                                               │
│  LAYER 3: THEORETICAL ALTERNATIVES                                          │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Savage (1954):   Subjective EU — handle uncertainty via subjective probs   │
│    Ellsberg violates this too (sure-thing principle)                        │
│  Simon (1955):    Bounded rationality — optimization infeasible; satisficing │
│  Maximin EU:      Handle ambiguity by maximizing worst-case EU              │
│  Robust opt.:     Uncertainty set instead of single distribution            │
│                                                                               │
│  LAYER 4: PROSPECT THEORY PREVIEW (full treatment in 02-PROSPECT-THEORY)    │
│  ─────────────────────────────────────────────────────────────────────────  │
│  Loss aversion: U(−x) ≈ −2 × U(x)   (losses feel ~2× as bad as gains)     │
│  Probability weighting: π(p) ≠ p     (overweight small; underweight large)  │
│  Reference dependence: utility = f(Δ from reference, not absolute wealth)   │
│  Diminishing sensitivity: concave in gains, convex in losses                │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Expected Utility Theory — The Baseline

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    EXPECTED UTILITY THEORY (vNM 1944)                       │
│                                                                               │
│  A rational agent facing a lottery L = {(x₁, p₁), (x₂, p₂), ..., (xₙ, pₙ)}  │
│  selects the option maximizing expected utility:                              │
│                                                                               │
│  EU(L) = Σᵢ pᵢ × U(xᵢ)                                                      │
│                                                                               │
│  AXIOMS (vNM):                                                              │
│  1. Completeness:     ∀A,B: A ≽ B or B ≽ A (always comparable)              │
│  2. Transitivity:     A ≽ B and B ≽ C → A ≽ C                               │
│  3. Continuity:       ∃p s.t. A ~ pB + (1-p)C (no lexicographic pref)       │
│  4. Independence:     If A ≽ B, then pA+(1-p)C ≽ pB+(1-p)C for all C, p     │
│                       (mixtures preserve preference order)                    │
│                                                                               │
│  THEOREM: Preferences satisfy these axioms iff they can be represented      │
│  by a utility function U: outcomes → ℝ such that lotteries are ranked       │
│  by expected utility.                                                         │
│                                                                               │
│  The representation theorem is the formal justification for EU theory.      │
│  Behavioral economics asks: do people's preferences satisfy these axioms?   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## The Allais Paradox (1953)

Maurice Allais's direct challenge to the independence axiom:

```
ALLAIS'S CHOICE PROBLEMS:

PROBLEM 1: Choose between:
  A: $1M with certainty
  B: $5M with probability 10%
     $1M with probability 89%
     $0  with probability 1%

PROBLEM 2: Choose between:
  C: $1M with probability 11%, $0 with probability 89%
  D: $5M with probability 10%, $0 with probability 90%

TYPICAL RESPONSES:
  Most people choose A over B (take the sure $1M, avoid the 1% chance of $0)
  Most people choose D over C (take the 10% chance of $5M)

WHY THIS VIOLATES INDEPENDENCE:
  Both problems can be written as:
  Problem 1: 0.89 × ($1M) + 0.11 × [A'] vs. 0.89 × ($1M) + 0.11 × [B']
  Problem 2: 0.89 × ($0)  + 0.11 × [A'] vs. 0.89 × ($0)  + 0.11 × [B']

  where A' = $1M with certainty, B' = {$5M: 10/11, $0: 1/11}

  Independence axiom: since the common 89% component changes only
  between $1M and $0, the preference between A' and B' should be
  independent of the common component.
  Therefore: A ≻ B ↔ C ≻ D (and similarly A ≺ B ↔ C ≺ D).
  But people choose A ≻ B AND D ≻ C → violates independence.

INTERPRETATION:
  "Certainty effect": 100% probability is overweighted vs. 99% (near-certainty).
  The shift from 11% to 10% (Problem 2) feels like proportional shift.
  The shift from 100% to 89% (Problem 1) feels like a qualitative loss of certainty.
  → Probability weighting is non-linear near 0 and 1.
  → This is captured in Prospect Theory (see 02-PROSPECT-THEORY).
```

## The Ellsberg Paradox (1961)

Daniel Ellsberg's challenge distinguishes risk from uncertainty:

```
ELLSBERG'S SETUP:
  Urn contains 90 balls: 30 RED, 60 BLACK or YELLOW (unknown split).

PROBLEM 1: Choose between:
  A: Win $100 if RED drawn
  B: Win $100 if BLACK drawn

  MOST PEOPLE CHOOSE A (known 1/3 probability over unknown black probability)

PROBLEM 2: Choose between:
  C: Win $100 if RED or YELLOW drawn
  D: Win $100 if BLACK or YELLOW drawn

  MOST PEOPLE CHOOSE D (known 2/3 probability over unknown red+yellow)

INCONSISTENCY:
  Choice A implies: P(Red) > P(Black)
  Choice D implies: P(Red) + P(Yellow) < P(Black) + P(Yellow)
    → P(Red) < P(Black)
  These two preferences are contradictory under any subjective probability.

ELLSBERG PARADOX = AMBIGUITY AVERSION:
  People prefer known probabilities (risk) over unknown probabilities (ambiguity).
  Risk: probability distribution known (a dice, a known urn).
  Uncertainty (Knightian): probability distribution unknown.
  Ambiguity aversion: people pay a premium to face risk rather than uncertainty.

FORMAL MODELS:
  Maximin expected utility (Gilboa-Schmeidler): maximize worst-case EU.
  Choquet expected utility: capacity (non-additive measure) instead of probability.
  Robust optimization: maximize subject to worst-case distribution in an ambiguity set.

ORGANIZATIONAL APPLICATION:
  Strategy under Knightian uncertainty — you don't know the probability
  distribution of outcomes. Classical EU analysis doesn't apply.
  Options: robust strategies (perform well across scenarios), real options
  (preserve flexibility), scenario planning.
  This is different from risk management (known distribution).
```

## Savage's Subjective Expected Utility

```
SAVAGE (1954): SUBJECTIVE EU
  Extends vNM to handle uncertainty by allowing subjective probabilities.
  Agents act as-if they have a subjective probability distribution over states.
  Axioms: add "sure-thing principle" (version of independence for uncertainty).

  The sure-thing principle:
  If you prefer A over B in every state of the world, you prefer A over B.

  Ellsberg paradox violates the sure-thing principle:
  State S1 (30 Red, 60 Yellow, 0 Black):
    P1 state: A wins with 1/3, B wins with 0 → prefer A
  State S2 (30 Red, 0 Yellow, 60 Black):
    P1 state: A wins with 1/3, B wins with 2/3 → prefer B
  Person flip-flops depending on state — but doesn't know which state
  they're in. The sure-thing principle doesn't require knowing;
  Ellsberg preferences can't be consistent with any coherent probability.
```

## Revealed vs. Stated Preferences

```
REVEALED PREFERENCE (Samuelson 1938):
  Observe choices to infer preferences.
  If agent chooses A when B was available, A ≽ B.
  Strong axiom of revealed preference (SARP): transitivity of revealed preferences.
  Advantage: preferences revealed by actual behavior; no hypothetical bias.

STATED PREFERENCE:
  Ask people what they prefer / how much they value X.
  Contingent valuation (CVM): "how much would you pay for clean air?"
  WTP (willingness to pay) vs. WTA (willingness to accept) divergence.

  WTA ≠ WTP: ANOMALY
  Standard theory: for modest wealth effects, WTA ≈ WTP.
  Empirical: WTA typically 2-7× WTP for the same good.
  Kahneman, Knetsch & Thaler (1990): endowment effect explains WTA > WTP.
  Once you own something, losing it is worse than gaining it by the same amount.
  → Loss aversion (Prospect Theory) explains the gap.

PREFERENCE REVERSALS:
  Grether & Plott (1979): A game has high probability of small win ($);
    B game has low probability of larger win ($$).
  Subjects: prefer A in choice, but price B higher.
  Playing the game they prefer and pricing the one they value more → reversal.
  Violates the assumption that preferences are stable and complete.
```

## Bounded Rationality — Simon's Program

```
SIMON'S CENTRAL ARGUMENT:
  Optimization requires:
  (a) knowing all alternatives
  (b) knowing all consequences
  (c) ability to compute the optimum
  None of these hold in practice.

COGNITIVE LIMITS:
  Working memory: 7 ± 2 chunks (Miller 1956)
  Attention: serial, not parallel for complex tasks
  Time: decisions are time-constrained
  Information: vast amounts unavailable or too costly to acquire

SATISFICING:
  Set an aspiration level (minimum acceptable outcome).
  Search until finding an option exceeding the aspiration level.
  Stop. No need to find the best option — "good enough" is chosen.

  FORMAL MODEL:
  Let A = aspiration level, V(x) = value of option x.
  Search options x₁, x₂, ... in sequence.
  Choose first xᵢ with V(xᵢ) ≥ A.
  Aspiration level adjusts: A↑ if many options exceed it; A↓ if none do.

  This predicts: decisions depend on search order, anchors, and experience.
  A job candidate seen second looks better/worse relative to one seen first.
  The reference point = current aspiration level.

ADAPTIVE TOOLBOX (Gigerenzen):
  Humans use different heuristics adapted to different domains.
  The "toolbox" of heuristics is selected based on:
  - Social (norms, imitation) learning
  - Individual trial-and-error
  - Evolution (for very basic heuristics)
  Heuristics are matched to environment structure.
  This explains why heuristics can be "rational" in their native environments.
```

## Prospect Theory Preview — What EU Misses

```
SYSTEMATIC VIOLATIONS OF EU:

1. LOSS AVERSION: Losses feel about 2× as bad as equivalent gains.
   Standard utility: U is only defined over final wealth levels.
   Reality: people code outcomes as gains/losses relative to a reference point.

2. PROBABILITY WEIGHTING: People overweight small probabilities,
   underweight moderate-to-high probabilities.
   Standard EU: probabilities enter linearly.
   Reality: π(0.01) > 0.01; π(0.90) < 0.90 in typical tasks.

3. REFERENCE DEPENDENCE: Utility depends on change from reference point,
   not final wealth level.
   Standard EU: U defined on absolute wealth.
   Reality: $1M gained from $1M baseline feels different from
            $1M as final wealth after $500K loss.

4. DIMINISHING SENSITIVITY: Marginal utility decreases from reference point
   in both directions (unlike standard concave utility which only applies to gains).
   A $100 gain matters more from $0 than from $1,000 gain.
   A $100 loss matters more from $0 than from $1,000 loss.

These failures motivate Prospect Theory (see 02-PROSPECT-THEORY).
```

## Decision Cheat Sheet

| EU critique question | Core violation | Relevant phenomenon |
|---|---|---|
| Why do people turn down gambles even when EU says accept? | Loss aversion | Risk aversion stronger in loss domain |
| Why do people buy lottery tickets AND insurance? | Probability weighting | Overweight small probabilities |
| Why can't we agree on a price for uncertain assets? | Ellsberg / ambiguity aversion | WTA/WTP divergence |
| Why do A ≻ B and D ≻ C at same time? | Allais / independence violation | Certainty effect |
| Why do people take a certain $1M over 89% chance of $1M + 10% of $5M? | Certainty effect (risk aversion at certainty boundary) | Independence axiom violation |
| Why are preferences unstable? | Preference reversals | Context-dependent value |
| How do real organizations decide? | Bounded rationality / satisficing | Sequential search, aspiration levels |

## Common Confusion Points

**Risk vs. uncertainty vs. ambiguity**: Risk = known probability distribution (flipping a fair coin). Uncertainty/ambiguity = unknown probability distribution (new market, tail risk). Standard EU theory handles risk but struggles with ambiguity. Ellsberg paradox = ambiguity aversion. Most real strategic decisions involve ambiguity, not pure risk.

**Independence axiom is not intuitive**: The independence axiom says: if you prefer A over B, adding a common lottery "backdrop" to both should preserve that preference. Algebraically sensible; psychologically violated because people treat the certainty/near-certainty component differently. The Allais paradox is a controlled demonstration of this violation.

**Bounded rationality ≠ irrationality**: Simon's argument is not that people are irrational. It's that optimization is computationally infeasible in realistic environments, and satisficing is a sensible response to that constraint. Satisficing with reasonable aspiration levels often produces nearly-optimal outcomes at far lower cognitive cost.

**WTA > WTP is not confusion or inconsistency**: The endowment effect (WTA >> WTP) is robust and has been replicated many times in field and lab. It reflects loss aversion in the Prospect Theory sense: losing an owned good is coded as a loss, which is psychologically more costly than the gain from acquiring it. It's not measurement error.
