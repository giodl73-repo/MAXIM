# Heuristics and Biases

## The Heuristics Research Program

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    HEURISTICS LANDSCAPE                                     │
│                                                                               │
│  TVERSKY & KAHNEMAN (1974) "Science" paper:                                 │
│  Three heuristics: Representativeness, Availability, Anchoring              │
│  These are cognitive shortcuts for making probability judgments.            │
│  Under most conditions: fast, adequate.                                     │
│  Under certain conditions: systematic, predictable errors.                  │
│                                                                               │
│  KEY DISTINCTION:                                                           │
│  K-T view: Heuristics are error-prone shortcuts                             │
│  Gigerenzen view: Heuristics are ecologically rational tools                │
│  BOTH are empirically supported in their domains.                           │
│                                                                               │
│  MODERN SYNTHESIS:                                                          │
│  Heuristics work well when:                                                 │
│    - Environment has regularities matching heuristic structure              │
│    - Task is familiar, domain expertise is present                          │
│    - Decision speed matters more than precision                             │
│  Heuristics fail when:                                                      │
│    - Environment is decontextualized (lab tasks)                            │
│    - Statistical reasoning required (base rates, conditional probability)   │
│    - Incentives conflict with heuristic defaults                            │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Representativeness Heuristic

```
MECHANISM:
  Judge the probability of event A given information B by asking:
  "How much does B resemble/represent the typical A?"
  Substitute "how similar is this to the prototype?" for "what is the probability?"

CLASSIC DEMONSTRATION — LINDA PROBLEM (Tversky & Kahneman 1983):
  "Linda is 31 years old, single, outspoken, and very bright. She majored in
   philosophy. As a student, she was deeply concerned with issues of
   discrimination and social justice, and also participated in antinuclear
   demonstrations."

  Rank in order of probability:
  A. Linda is a bank teller.
  B. Linda is a bank teller AND is active in the feminist movement.

  85-90% of subjects rank B > A — the CONJUNCTION FALLACY.
  P(A ∩ B) ≤ P(A) always (by probability theory).
  The conjunction cannot be more probable than either constituent.
  But B "represents" the description better → judged more probable.

BASE RATE NEGLECT:
  When given:
  - Prior probability (base rate): P(H) = 0.01 (1% of population has disease X)
  - Likelihood: P(positive test | H) = 0.95, P(positive test | not H) = 0.05

  Correct answer by Bayes: P(H | positive) = 0.95×0.01 / (0.95×0.01 + 0.05×0.99)
                          = 0.00950 / (0.00950 + 0.04950) = 0.161

  Most people ignore the 1% base rate and respond ~95%.
  The representativeness heuristic: "the test is 95% accurate → positive result
  means ~95% chance of disease." Base rate is discarded.

  KAHNEMAN-TVERSKY FINDING: When case description is vivid and specific,
  base rates are discounted. When no description is given, base rates are used.

GAMBLER'S FALLACY:
  "The roulette has come up red 5 times in a row → black is due."
  Representativeness: a sequence of random coin flips should "look random"
  (alternating). A long run of heads doesn't represent randomness.
  Therefore: perceive that tails is more likely after heads.
  WRONG: each flip is independent; past outcomes don't affect future.

HOT HAND FALLACY (opposite direction):
  "He's made 6 shots in a row — he's on a hot hand. Pass to him."
  Opposite error: past runs of success predict future success.
  Gilovich, Vallone & Tversky (1985): no statistical hot hand in basketball.
  BUT: Miller & Sanjurjo (2018) found a statistical artifact in GVT's test.
  Current evidence: weak hot hand may exist in some sports contexts.
```

## Availability Heuristic

```
MECHANISM:
  Judge the probability or frequency of an event by the ease with which
  examples come to mind.
  Substitute "how easily can I think of an example?" for "how common is this?"

CAUSES OF HIGH AVAILABILITY (independent of true frequency):
  - Recency: recent events come to mind more easily
  - Vividness: dramatic events are more memorable
  - Personal experience: direct experience > statistical report
  - Media coverage: coverage ≠ frequency
  - Emotional salience: emotionally engaging events are recalled better

RISK PERCEPTION DISTORTIONS:
  People OVERESTIMATE:
    Death from plane crashes (recent, dramatic, media coverage)
    Death from terrorism (vivid, media)
    Death from shark attacks, tornadoes, fireworks
  People UNDERESTIMATE:
    Death from car accidents (boring, common, not newsworthy)
    Death from heart disease (gradual, not dramatic)
    Death from diabetes, stroke (invisible, slow)
    Death from smoking (very high but normalized)

  The gap between objective risk and perceived risk is large and systematic.
  Slovic (1987): risk perception = f(dread risk, unknown risk, not frequency).
  "Dread" (uncontrollable, catastrophic, inequitable) > pure frequency.

AVAILABILITY BIAS IN ORGANIZATIONAL DECISION-MAKING:
  Teams recall recent failures more easily → overly risk-averse after recent loss.
  Teams recall recent successes → overconfident after recent wins.
  "Availability cascade" (Kuran & Sunstein): when an event gets media coverage,
    it becomes more available → perceived as more risky → more coverage → cycle.
    COVID-19 early: availability cascade → panic purchases, supply disruption.
  Post-incident bias: after a major system outage, all subsequent architectural
    decisions weighted heavily against the type of failure that just occurred,
    potentially creating blind spots for other failure types.

WITHIN TEAMS:
  Shared information is more available than unshared information.
  "Hidden profile" problem: teams spend most time discussing what everyone
    already knows; unique private information (possessed by one person) is
    less likely to surface and be used in decision.
  Solution: structured information sharing; pre-mortems; devil's advocate roles.
```

## Anchoring and Adjustment

```
MECHANISM:
  When making an estimate under uncertainty, start from an initial value
  (the "anchor") and adjust toward a final estimate.
  Adjustment is typically INSUFFICIENT → final estimates remain biased
  toward the initial anchor.

ANCHORING WITH ARBITRARY NUMBERS:
  Tversky & Kahneman (1974) wheel experiment:
  Spin a rigged wheel that stops at 10 or 65 (randomly assigned to subjects).
  Then ask: "What percentage of African countries are in the UN?"
  Median answer: 25 (wheel 10) vs. 45 (wheel 65).
  The wheel number (completely irrelevant) shifts estimates by 20 points.

ANCHORING IN REAL CONTEXTS:
  Salary negotiation:
    First offer serves as anchor; final settlement tracks first offer.
    Evidence: whichever party makes the first offer does better.
    Implication: make the first offer; make it specific (rounded numbers
    invite counter-anchoring; precise numbers signal information).
  Legal damages:
    Judges given random sentencing suggestions anchor to those suggestions.
    Experienced professionals, not just naive subjects.
  Real estate:
    Listing price is the anchor; buyers' offers track listing prices.
  Product pricing:
    "Was $99 — now $69!" → $99 is the anchor; $69 feels like a deal.
    "Suggested retail price: $149 — your price: $79"

CROSS-ANCHORING IN NEGOTIATIONS:
  Both parties set anchors. The party whose anchor was accepted as the
  reference point has the structural advantage.
  High anchor + information about why: better than just high anchor.
  Defensible anchors are more credible than arbitrary ones.
  But credibility isn't required for the anchoring effect to occur
  (the wheel experiment used obviously arbitrary numbers).

ADJUSTMENT MECHANISM:
  Why is adjustment insufficient?
  1. Adjustment terminates when an acceptable value is reached (satisficing).
  2. The anchor determines the direction of search; search stops at first
     acceptable value in that direction → biased.
  3. Anchor activates semantically related information; adjustment is
     anchored in the semantic field of the initial value.
```

## Affect Heuristic

```
MECHANISM:
  Judgments and decisions are influenced by the overall emotional valence
  (good/bad feeling) associated with an object or action.
  Substitute "how do I feel about this?" for "what is the probability/value?"

DISCOVERED BY: Slovic, Finucane, Peters & MacGregor (2002).
  Builds on earlier "somatic marker hypothesis" (Damasio) — emotions guide
  decision by providing fast signals.

RISK-BENEFIT AFFECT LINK:
  In reality: risk and benefit of activities often positively correlated
    (nuclear power: high potential benefit AND high risk).
  In perception: risk and benefit judgments are negatively correlated.
  If people have positive affect toward X: low risk, high benefit.
  If negative affect toward X: high risk, low benefit.
  Information that changes affect (positive story about nuclear power)
  SIMULTANEOUSLY reduces perceived risk AND increases perceived benefit.
  → Single underlying dimension (affect) drives both.

PRACTICAL IMPLICATIONS:
  Brand reputation affects risk tolerance: "Microsoft product" vs. "generic
  product" — same feature, different risk perception due to affect.
  Prior relationships affect contract negotiation risk perception.
  User trust in a product affects tolerance for UX friction.
  Leader trust: low-affect leader's risky proposal → higher resistance than
  high-affect leader's identical proposal.

AFFECT HEURISTIC AND EXPERT JUDGMENT:
  Experts are not immune. Experts show affect heuristic effects in their
  domain expertise areas. The heuristic affects both novices and experts,
  though experts may have more calibrated base affects.
```

## Other Key Cognitive Biases

```
OVERCONFIDENCE:
  Three forms:
  1. Overprecision: confidence intervals too narrow
     "90% confidence interval" tasks: calibrated response covers ~50% of answers
  2. Overplacement: "I'm better than average" (illusory superiority)
     ~80% of drivers think they're above average (impossible; ~50% must be below)
  3. Overestimation: absolute performance overestimated
     Actually less common than the other two; sometimes underconfidence in hard tasks

  PLANNING FALLACY (Kahneman & Tversky 1979):
  Plans are too optimistic: underestimate time, cost, risk.
  Boston Big Dig: $2.8B estimated → $14.6B actual (5.2× overrun).
  Sydney Opera House: $7M estimated → $102M actual (14.6× overrun).
  NHS IT system (UK, 2002): £2.3B estimated → £10B spent before cancellation.
  Pattern: 100% of large software/infrastructure projects exceed estimates.
  Explanation: inside view (focus on THIS project's unique features) vs. outside
  view (reference class: how long do similar projects actually take?).
  FIX: Reference class forecasting (Kahneman & Lovallo): look at base rates for
  the reference class. "Distribution of actual costs / estimated costs for
  similar infrastructure projects" → build in a multiplier.

STATUS QUO BIAS (Samuelson & Zeckhauser 1988):
  Preference for the current state, even when alternatives are better.
  Mechanism: changing involves risk; status quo has zero regret (it's the default).
  Loss aversion: change = giving up current state (loss) + uncertainty of new state.
  Implication: default settings matter enormously (see 07-NUDGE).

CONFIRMATION BIAS:
  Search for, interpret, favor, and recall information confirming existing beliefs.
  Not discussed in K-T 1974 paper; developed separately.
  Organizational implications: teams stop searching after confirming evidence found;
  dissenting views not sought; post-mortem less useful if leader's hypothesis is
  confirmed first.
  FIX: Pre-mortem (imagine the project failed — what went wrong?); structured
  adversarial collaboration; red teams; designated devil's advocate.
```

## Ecological Rationality — When Heuristics Win

```
GIGERENZEN'S FAST-AND-FRUGAL HEURISTICS:

  TAKE-THE-BEST HEURISTIC:
  Task: Choose between two options on some criterion (which city is larger?)
  Strategy:
  1. List cues ordered by validity (correlation with criterion).
  2. Check the most valid cue first. Does it discriminate (one option yes, other no)?
     If yes → choose the option that cue favors. STOP.
     If no (both yes or both no) → move to next cue.
  3. Continue until discriminating cue found.

  PERFORMANCE:
  Take-the-best vs. multiple regression on 20+ data sets:
  Out-of-sample prediction: Take-the-best equals or beats regression in ~63% of cases.
  Why? Regression overfits in small-N settings. Take-the-best uses fewer parameters
  → less sampling error → better generalization.
  This is the bias-variance tradeoff from statistical learning: simpler models
  can generalize better than complex ones when data is scarce.
  Connection to statistics-applied/: L1 regularization (Lasso) is the formal
  version of "use fewer predictors" — same principle.

  RECOGNITION HEURISTIC:
  "If you recognize option A but not option B, infer that A scores higher
  on the criterion."
  Performance: can outperform much more complex models in environments
  where recognition correlates with the criterion.
  Example: German city populations — American students, knowing less about
  Germany, use recognition heuristic → outperform Germans (who know more
  cities but must reason more carefully).
  Counter-intuitive: less knowledge → better judgment in this environment.
```

## Replication Status

```
REPLICATION OF HEURISTICS/BIASES FINDINGS:
  Core findings (robust replicators):
  - Anchoring effects: very robust (Maniadis et al. 2014 meta-analysis confirms)
  - Conjunction fallacy (Linda problem): robust
  - Framing effects: robust
  - Loss aversion: robust (see 02)
  - Endowment effect: robust for normal goods
  - Default/status quo effects: very robust (large N field studies)

  Weaker or mixed replication:
  - Planning fallacy magnitude: real but smaller than lab studies suggest
  - Hot hand controversy: ongoing debate
  - Priming effects (unrelated to heuristics/biases core): largely failed replication
  - Ego depletion: largely failed replication
  - "Unconscious thought" theory: largely failed replication

  OVERALL ASSESSMENT:
  The core K-T program — representativeness, availability, anchoring, loss
  aversion — is well-replicated and robust. Peripheral extensions (priming,
  depletion) are not. The field over-extended in the 2000s-2010s with too many
  small-N studies on weak phenomena. Return to basics: the core is solid.
```

## Decision Cheat Sheet

| Heuristic question | Error condition | Debiasing strategy |
|---|---|---|
| Representativeness | Linda problem; base rate neglect; hot hand / gambler's fallacy | Explicitly compute P(A∩B); seek base rates; ask "what is the reference class?" |
| Availability | Risk perception distorted by vivid/recent events | Ask "what's the actual incidence rate?"; use actuarial data |
| Anchoring | Salary, pricing, legal, estimation tasks | Make the first offer; use reference class for estimation; challenge anchors explicitly |
| Affect heuristic | Risk-benefit link distorted by affect | Separate risk and benefit judgments; use structured assessments |
| Overconfidence | Project estimates too narrow/optimistic | Reference class forecasting; de Bondt intervals; red team |
| Status quo bias | Staying with bad default | Reframe status quo as active loss; compare to reference class performance |
| Confirmation bias | Evidence search stops early; disconfirming evidence ignored | Pre-mortem; adversarial collaboration; structured devil's advocate |

## Common Confusion Points

**Heuristics and biases are not the same thing**: A heuristic is a strategy. A bias is the systematic error that results when a heuristic is applied in the wrong environment. The availability heuristic doesn't always produce bias — in environments where ease-of-recall correlates with frequency (many natural environments), it's a fine heuristic. The bias arises when recall is distorted by recency, media, or salience independent of frequency.

**The planning fallacy is not stupidity**: People planning their own projects use an "inside view" (this project is special, we know what we're doing) rather than an "outside view" (base rate for similar projects). This is rational from a certain perspective — you do have more information about your specific project. The error is overweighting that specific information and underweighting the base rate.

**Base rate neglect is not universal**: People use base rates when no case-specific information is available. They neglect base rates when given vivid case descriptions. The heuristic is applied when both base rate AND case description are available; the case description captures attention. The bias is context-specific.

**Gigerenzen is not pro-irrationality**: He argues heuristics are rational in natural environments. He fully accepts that heuristics can produce errors in decontextualized lab tasks. His target is the overgeneralization of lab findings to real-world decision-making, not the existence of cognitive limitations.
