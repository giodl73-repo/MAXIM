# Prospect Theory

## The Paper and Its Significance

Kahneman & Tversky (1979), "Prospect Theory: An Analysis of Decision under Risk," *Econometrica* 47(2): 263-291.

The most-cited paper in economics. As of 2024: ~80,000 citations. Published in *Econometrica* — the flagship theory journal — by two psychologists. Replaced expected utility theory as the dominant descriptive model of individual choice under risk. Kahneman received the 2002 Nobel Prize in Economics (Tversky died in 1996; Nobel not awarded posthumously).

The paper is remarkable for its combination of:
- Systematic empirical documentation (choice experiments)
- Elegant axiomatic structure
- Psychological interpretability
- Quantitative precision

## The Full Prospect Theory Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PROSPECT THEORY ARCHITECTURE                             │
│                                                                             │
│  A "prospect" is a lottery: {(x₁, p₁), ..., (xₙ, pₙ)}                       │
│                                                                             │
│  EVALUATION: V(prospect) = Σᵢ π(pᵢ) × v(xᵢ)                                 │
│                                                                             │
│  where:                                                                     │
│  v(x) = VALUE FUNCTION (defined on GAINS and LOSSES from a reference point) │
│  π(p) = PROBABILITY WEIGHTING FUNCTION (nonlinear probability perception)   │
│                                                                             │
│  TWO PHASES:                                                                │
│  EDITING: Frame, simplify, and code the prospect                            │
│  EVALUATION: Apply v(·) and π(·) to compute overall value                   │
└─────────────────────────────────────────────────────────────────────────────┘
```

## The Value Function

```
VALUE FUNCTION v(x):
  Defined over GAINS and LOSSES relative to a REFERENCE POINT (not final wealth).

  KEY PROPERTIES:
  1. Reference-dependence: evaluated relative to reference point (status quo,
     aspiration, expectation, prior state)
  2. S-shaped: concave in gains, convex in losses
  3. Loss aversion: steeper for losses than gains
  4. Diminishing sensitivity: in both directions from reference point

  STANDARD PARAMETRIC FORM (Tversky-Kahneman 1992, "Cumulative Prospect Theory"):

  v(x) = { x^α              if x ≥ 0  (gain domain)
          { -λ × (-x)^β     if x < 0  (loss domain)

  Typical estimates: α ≈ β ≈ 0.88, λ ≈ 2.25

  GRAPH:
  v(x)
    │        ●
    │      ●
    │    ●
    │  ●
    │●
  ──●────────────────────── x (gain/loss)
    │●
    │  ●
    │    ●●
    │       ●●●●   ← steeper slope (loss aversion λ ≈ 2.25)
    │

  KEY IMPLICATIONS:
  Concave in gains: risk-averse for moderate-probability gains
    (prefer $500 certain to 50/50 chance of $1000)
  Convex in losses: risk-seeking for moderate-probability losses
    (prefer 50/50 chance of losing $1000 to certain loss of $500)
  Loss aversion: the pain of losing $X exceeds the pleasure of gaining $X
  Diminishing sensitivity: $100 gain matters more from $0 than from $1000 baseline
```

## Loss Aversion — The Flagship Finding

```
LOSS AVERSION COEFFICIENT (λ):
  The ratio of marginal disutility of losses to marginal utility of gains.
  λ ≈ 1.5 to 2.5 across meta-analyses (Kahneman 1979 estimated ~2.25).
  Practical interpretation: losing $1 feels about as bad as gaining $2 feels good.

THE BASIC DEMONSTRATION:
  Gamble: 50/50 chance of winning $110 OR losing $100.
  Expected value: +$5 (positive).
  Most people REJECT this gamble.
  Break-even: people require roughly gain ≥ $200 to accept a loss of $100.
  This implies λ ≈ 2.

LOSS AVERSION IN ORGANIZATIONAL BEHAVIOR:
  Why employees resist layoffs even when they hurt few people:
  Survivors feel they "lost" job security; gains from remaining employed are taken as baseline.
  Why teams resist scope cuts even when rational:
  Cutting features = loss; keeping features = maintaining status quo.
  Why engineers keep working on failing projects (see also 04 sunk cost):
  Admitting failure = loss of investment; continuing = avoiding realized loss.
  Why performance reviews are so difficult:
  Any feedback below "perfect" is coded as a loss; people defend against it.
  WHY CHANGE IS HARD: change requires giving up current state (loss) for
  uncertain future state (gain). Expected value must be substantially positive
  for people to accept the loss framing. λ ≈ 2 means you need to offer ~2×
  the value to overcome the loss of giving up the current state.

ENDOWMENT EFFECT:
  Corollary of loss aversion.
  Kahneman, Knetsch & Thaler (1990): Cornell mug experiment.
  50% of participants randomly assigned a coffee mug.
  Trading: mug owners → WTA ~$7; non-owners → WTP ~$3.
  ~0% of trading (predicted by theory: ~50% should trade).
  Simply owning an object makes giving it up feel like a loss → WTA > WTP.
  Replication: very robust for "regular goods" (not trading objects, money itself).
```

## Probability Weighting

```
PROBABILITY WEIGHTING FUNCTION π(p):
  Decision weights are NOT equal to objective probabilities.
  π(p) ≠ p in general.

  KEY FEATURES:
  Overweighting of small probabilities: π(0.001) >> 0.001
    "small probabilities appear larger than they are"
  Underweighting of moderate-to-large probabilities: π(0.90) < 0.90
  Certainty and impossibility are distinct categories:
    π(1) = 1 (certainty is certain), π(0) = 0
    But: π(0.99) significantly less than 1 — certainty effect

  GRAPHICAL FORM:
  π(p)
  1.0│              ●
     │           ●
  0.5│        ●
     │     ●
  0.4│   ●
     │  ●
  0.2│ ●
     │●
  0  └────────────────── p
     0   0.2  0.4  0.6  0.8  1.0
  (Dashed line = π(p) = p, 45-degree diagonal)

  The curve crosses the 45-degree line around p ≈ 0.35-0.40.
  Below that: overweighted. Above: underweighted.

  TVERSKY-KAHNEMAN (1992) PARAMETRIC FORM:
  π(p) = p^γ / [p^γ + (1-p)^γ]^{1/γ}
  Typical γ ≈ 0.65 (both for gains and losses; some asymmetry found)

EXPLANATORY POWER:
  Why do people buy lottery tickets? (tiny probability → grossly overweighted)
  Why do people buy insurance? (tiny catastrophe probability → overweighted)
  → Risk-seeking for large-stakes, small-probability gambles
  → Both can be explained by probability weighting + loss aversion together.

  Why do people underinsure moderate risks?
  Moderate probability of loss: underweighted → undervalued → underinsured.
  "Probability neglect" for moderate risks is a public health problem
  (hurricane preparation, pandemic preparation, financial reserve).
```

## Framing Effects

```
FRAMING: The same objective situation described differently → different choices.

TVERSKY & KAHNEMAN (1981) — ASIAN DISEASE PROBLEM:
  600 people affected by disease.

  POSITIVE FRAME:
  A: 200 people saved for certain.
  B: 1/3 probability 600 saved, 2/3 probability nobody saved.
  CHOICE: 72% choose A (certain gain → risk averse)

  NEGATIVE FRAME:
  C: 400 people die for certain.
  D: 1/3 probability nobody dies, 2/3 probability 600 die.
  CHOICE: 78% choose D (certain loss → risk seeking)

  A ≡ C (mathematically): 200 saved ↔ 400 die (out of 600).
  B ≡ D: 1/3 chance all saved ↔ 1/3 chance nobody dies.
  Yet: 72% choose A (vs. C), 78% choose D (vs. C=A).

  MECHANISM: Reference point set by frame ("lives saved" vs. "deaths").
  Positive frame → gain domain → concave utility → risk aversion.
  Negative frame → loss domain → convex utility → risk seeking.

FRAMING IN ORGANIZATIONAL COMMUNICATION:
  "10% failure rate" vs. "90% success rate" for the same product → different WTP.
  "We need to find $10M in cuts" vs. "We need to defend $10M of investment"
    → different team dynamics, different resistance.
  Performance review: "exceeds expectations in 8 of 10 areas" vs.
    "falls short in 2 of 10 areas" → different employee reactions despite
    identical underlying assessment.
  Budget framing: "your department is getting +$2M" vs. "you're getting less
    than the 4 other departments who each got +$3M" → different motivation.
    Reference point determines gain vs. loss framing.
```

## Editing Phase Operations

```
EDITING PHASE (before evaluation):
  1. CODING: Classify outcomes as gains or losses relative to reference point.
     Reference point = current wealth, expectation, aspiration, social comparison.
  2. COMBINATION: Combine identical outcomes.
     {($100, 0.3), ($100, 0.2)} → {($100, 0.5)}
  3. SEGREGATION: Separate riskless component from risky.
     {($100, 0.8), ($200, 0.2)} → $100 for certain + {($0, 0.8), ($100, 0.2)}
     The sure $100 is coded as no-risk; extra $100 is the gamble.
  4. CANCELLATION: Cancel out common components across compared options.
     Allais problem: ignore the 89% component shared by both options.
  5. SIMPLIFICATION: Round probabilities; ignore small components.
  6. DOMINANCE DETECTION: Immediately reject dominated options.

  VIOLATIONS EXPLAINED:
  Combination + simplification can create preference reversals.
  Cancellation → isolation effect (see below).

ISOLATION EFFECT:
  People focus on the distinctive components of lotteries and ignore
  shared components.
  This creates apparent inconsistency: the same lottery presented differently
  (different decomposition) → different choices.
  Example: pre-game endowments in sequential gambles affect choice
  even though final payoffs are the same.
```

## Cumulative Prospect Theory (1992)

```
TVERSKY & KAHNEMAN (1992) REVISION:
  Original 1979 PT: applied π(p) to each probability independently.
  Problem: could violate first-order stochastic dominance (intransitive).

  CUMULATIVE PT:
  Apply π(·) to the CUMULATIVE distribution, not individual probabilities.
  This preserves stochastic dominance: if lottery A stochastically dominates
  B, CPT must rank A ≥ B.

  MECHANISM:
  Rank outcomes from worst to best.
  For gains: compute probability that payoff ≥ xᵢ.
  For losses: compute probability that payoff ≤ xᵢ.
  Apply weighting function to these cumulative probabilities.
  Decision weights w₊ᵢ, w₋ᵢ are differences in cumulated weights.

  KEY INSIGHT: The probability of the worst outcome in a lottery is overweighted.
  This is because the cumulative weighting applied to the tail of the distribution
  amplifies the decision weight of extreme negative outcomes.
  → Extreme downside risk is overweighted → excess risk aversion at the tails.
  Consistent with: overpricing of insurance, credit default swaps.
```

## Applications to Management and Org Behavior

```
LOSS AVERSION IN CHANGE MANAGEMENT:
  Kotter's research: 70% of major change initiatives fail.
  Behavioral explanation: net present value positive for the organization
  but individual employees face loss (disruption, uncertainty, status quo change).
  λ ≈ 2 means the perceived loss must be 2× overcompensated for neutral reaction.
  Practical implication: don't just communicate gains from change.
  REFRAME THE STATUS QUO AS A LOSS.
  "If we don't change, we will lose market share worth X" is more motivating
  than "if we change, we will gain market share worth X."

REFERENCE POINT MANAGEMENT:
  Expectations set reference points.
  Exceeding a milestone = gain (even if small absolute gain).
  Missing a milestone = loss (even if small absolute miss).
  Implication: be careful what targets you set. You cannot un-set a reference.
  A target that was set too high becomes the reference point; any miss is a loss.
  This is why ambitious-but-achievable targets > stretch goals for motivation
  (stretch goals that regularly fail → chronic loss experience → demoralization).

BONUS vs. SALARY IN COMPENSATION DESIGN:
  Prospect theory implications for incentive design:
  Bonus framing: $10K bonus for hitting target = gain (positive)
  Fine framing: salary $10K above base, lose $10K for missing target = loss
  Iso-incentive: same financial outcome. Different psychology.
  Loss framing is a stronger motivator (λ ≈ 2).
  BUT: loss framing increases stress, reduces intrinsic motivation, reduces trust.
  Tradeoff between short-term motivation and long-term engagement.
```

## Decision Cheat Sheet

| Prospect theory question | Prediction |
|---|---|
| Will people accept a symmetric 50/50 bet? | No, if loss > $X; need ~2× gain to compensate |
| Why does a person buy both lottery and insurance? | Prob. weighting: overweight small probs at both extremes |
| Why do teams fight scope cuts more than expected? | Loss aversion: cutting scope = loss; adding features = gain |
| Why is the "Asian Disease" problem susceptible to framing? | Gain frame → risk averse; loss frame → risk seeking |
| How to get an employee to accept a new role with uncertainty? | Frame rejection as loss (current path declining) not just new role as gain |
| What's the endowment effect? | Owning → loss aversion → WTA >> WTP for same good |
| Why is loss aversion strongest for small probabilities? | Probability weighting amplifies both extreme gains and extreme losses |

## Common Confusion Points

**Prospect Theory is descriptive, not normative**: PT describes how people actually choose. It does not say this is how people should choose. Expected utility theory (EU) is the normative standard. The Allais paradox shows EU is violated; PT models the violation. Being loss-averse is often not optimal, especially for decisions with repeated, independent outcomes (insurance at scale).

**Loss aversion ≠ risk aversion**: Risk aversion in EU theory = concave utility function (prefer certain outcome to fair gamble). Loss aversion = steeper value function for losses than gains at the reference point. You can have both, and they interact. Risk-seeking in the loss domain (gambling to avoid a sure loss) is loss aversion, not risk loving.

**Reference point is not always the status quo**: K-T assumed reference point = current status. But it can be: an expectation, an aspiration, a social comparison, a budget target, prior year's performance. The reference point is cognitively set and can be influenced by how options are framed. This is what makes framing effects powerful for communication and choice architecture.

**λ ≈ 2 is an average, not a constant**: Individual and context variation is large. Loss aversion is stronger for: high-stakes decisions, irreversible decisions, decisions in domains of prior loss, older individuals (some evidence). Loss aversion is weaker for: repeated decisions, expert traders, low-stakes, experienced consumers. The 2× is a useful heuristic, not a precise constant.
