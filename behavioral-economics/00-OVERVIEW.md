# Behavioral Economics — Landscape Overview

## The Challenge to Homo Economicus

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   BEHAVIORAL ECONOMICS LANDSCAPE                             │
│                                                                               │
│  NEOCLASSICAL MODEL             BEHAVIORAL ECONOMICS                         │
│  (Homo economicus)              (Homo sapiens)                               │
│  ─────────────────────          ─────────────────────────────────────────   │
│  Unlimited cognitive capacity   Bounded rationality (Simon)                  │
│  Stable, coherent preferences   Reference-dependent preferences              │
│  Perfect information processing Systematic cognitive shortcuts               │
│  Pure self-interest             Social preferences (fairness, reciprocity)   │
│  Exponential time discounting   Hyperbolic/quasi-hyperbolic discounting      │
│  Consistent risk preferences    Loss aversion; probability weighting         │
│  Fungible wealth accounts       Mental accounts (non-fungible categories)    │
│                                                                               │
│  THE BEHAVIORAL RESEARCH PROGRAM (1969-present):                            │
│  IDENTIFY systematic deviations from the standard model                     │
│  EXPLAIN mechanisms (psychological/neural)                                   │
│  PREDICT where and when deviations occur                                     │
│  APPLY to policy, product design, institutional design                      │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- @editor[bridge/P2]: Missing explicit old-world bridge — the opening diagram contrasts Homo economicus vs. Homo sapiens but doesn't frame the bridge in terms the learner owns: classical optimization theory (LP, convex optimization, rational agents from AI) maps to EU theory; behavioral economics is the empirical study of where these optimization assumptions break down in human systems. Any senior engineer coming from formal methods or optimization theory needs this framing -->
## The Research Lineage

```
TIMELINE:
  1944: von Neumann-Morgenstern — Expected utility theory formalized
  1953: Allais Paradox — first systematic violation of EU theory
  1961: Ellsberg Paradox — ambiguity aversion (risk ≠ uncertainty)
  1955: Simon — bounded rationality, satisficing, cognitive limits
  1974: Tversky & Kahneman — "Judgment Under Uncertainty: Heuristics and Biases"
  1979: Kahneman & Tversky — Prospect Theory (Science, most cited economics paper)
  1980: Thaler — Mental Accounting
  1981: Kahneman, Knetsch & Thaler — Endowment effect
  1986: Thaler — Anomalies column in JEP (documenting deviations from rationality)
  1988: Loomes & Sugden — Regret theory
  1991: Fehr et al. — Ultimatum game experiments → social preferences
  1994: Loewenstein & Prelec — Quasi-hyperbolic discounting
  1999: Thaler & Benartzi — Save More Tomorrow (SMarT) — first practical intervention
  2002: Kahneman Nobel Prize (in Economics, though a psychologist)
  2003: BIT (Behavioural Insights Team) equivalent programs begin
  2008: Thaler & Sunstein — "Nudge" (popularization, choice architecture)
  2013: Shiller Nobel; behavioral finance legitimized
  2017: Thaler Nobel Prize
  2021: Card (related empirical work) Nobel Prize

SCHOOLS:
  Heuristics and Biases program (K-T): systematic mapping of cognitive errors
  Ecological rationality (Gigerenzen): heuristics as adaptive tools, not errors
  Behavioral finance (Shiller, Thaler): asset pricing anomalies from behavior
  Mechanism design / behavioral economics: policy applications
```

## Key Findings Map

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    CORE FINDINGS TAXONOMY                                    │
│                                                                               │
│  RISK & UNCERTAINTY              SOCIAL BEHAVIOR                             │
│  ─────────────────────           ───────────────────────────                │
│  Loss aversion (λ ≈ 2)           Inequity aversion (Fehr-Schmidt)           │
│  Probability weighting           Reciprocal altruism                        │
│  Ambiguity aversion              Trust and cooperation                      │
│  Framing effects                 Social norms and conformity                │
│  Overconfidence                  Reputation effects                         │
│                                                                               │
│  COGNITIVE SHORTCUTS             TIME & DECISIONS                           │
│  ─────────────────────           ───────────────────────────                │
│  Availability heuristic          Present bias / β-δ model                   │
│  Representativeness              Hyperbolic discounting                     │
│  Anchoring and adjustment        Projection bias                            │
│  Affect heuristic                Hot-cold empathy gap                       │
│  Attribute substitution          Procrastination                            │
│                                                                               │
│  REFERENCE POINTS & ACCOUNTS     CONTEXT EFFECTS                           │
│  ─────────────────────────────   ───────────────────────────                │
│  Mental accounting               Default effects                            │
│  Sunk cost fallacy               Choice overload (Paradox of choice)        │
│  Endowment effect                Decoy effect (asymmetric dominance)        │
│  House money effect              Contrast effects                           │
│  Payment decoupling              Scarcity and social proof                  │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Bounded Rationality — Herbert Simon's Framework

```
SIMON'S CONTRIBUTION (1955, 1957, 1978 Nobel Prize — Economics):
  The classical model assumes optimization: find the best option.
  Simon's diagnosis: humans face:
  1. Incomplete information
  2. Cognitive capacity limits
  3. Time constraints
  4. Complexity of real problems

  SATISFICING: Find a "good enough" option (satisfy + suffice).
  Stop searching when the first option exceeding a threshold is found.
  Aspiration level: threshold above which options are "acceptable."
  Aspiration levels update over time with experience.

  PROCEDURAL vs. SUBSTANTIVE RATIONALITY:
  Substantive: outcome is objectively optimal
  Procedural: process follows reasonable decision rules
  Simon argues: only procedural rationality is achievable.
  Standard economics assumes substantive; behavioral economics studies procedural.

  ORGANIZATIONAL IMPLICATIONS (directly relevant to VP-level leadership):
  Simon's boundedly rational organizations:
  - Decisions are made by bounded agents with local information
  - Organizational hierarchy = decomposition of complex decisions into
    bounded subproblems manageable by individuals
  - Routines and SOPs = codified satisficing rules that work well on average
  - Innovation = disrupting routines that no longer work
  - Information processing bottlenecks = the key constraint on org. performance
```

## Ecological Rationality (Gigerenzen's Counter-View)

```
GIGERENZEN'S CHALLENGE TO THE HEURISTICS-AND-BIASES PARADIGM:

  K-T/Kahneman view: heuristics are shortcuts that PRODUCE ERRORS.
  The lab experiments reveal biases — systematic deviations from rationality.

  Gigerenzen's view: heuristics are ECOLOGICALLY RATIONAL.
  They evolved/developed because they work well in natural environments.
  The K-T lab tasks are decontextualized, stripped of natural cues.

  FAST AND FRUGAL HEURISTICS:
  Gigerenzen's ABC research group identified families of heuristics:
    Take-the-best: rank cues by validity; use the first discriminating cue.
    Recognition heuristic: recognize one option but not another → choose recognized.
    Tallying (equal weighting): count positives; ignore cue validity differences.
    1/N rule: divide equally among N options.

  WHEN HEURISTICS OUTPERFORM OPTIMIZATION:
  In environments with:
  - Few data points (parameter estimation error dominates model fit)
  - High uncertainty (model structure uncertain)
  - Correlated cues (adding more cues doesn't help)
  - Need for robustness across environments
  Heuristics often match or beat complex optimization models.
  Classic result: equal weighting (1/N) beats Markowitz mean-variance
  portfolio optimization out-of-sample in most financial datasets.

  RESOLUTION: The K-T and Gigerenzen programs are complementary.
  K-T identifies conditions where heuristics fail (systematic biases).
  Gigerenzen identifies conditions where heuristics succeed (natural environments).
  Both are empirically valid. The policy implications differ:
  K-T: design institutions to compensate for biases.
  Gigerenzen: design environments to match heuristic capabilities.
```

## System 1 / System 2 Framework

```
DUAL PROCESS THEORY (Kahneman "Thinking, Fast and Slow"):

  SYSTEM 1 ("Fast"):              SYSTEM 2 ("Slow"):
  ────────────────────────────    ─────────────────────────────
  Automatic, effortless           Deliberate, effortful
  Fast                            Slow
  Emotional, intuitive            Logical, analytical
  Associative                     Rule-based
  Unconscious                     Conscious
  Context-sensitive               Abstract
  Hard to override                Can override System 1
  Ancient (evolutionary)          Newer (prefrontal cortex)

  EXAMPLES:
  System 1: Face recognition, driving on empty road, "2+2=",
            automatic threat response, gut feeling about person
  System 2: 17 × 24 = ?, reading a contract, tax filing,
            deliberate statistical reasoning, chess analysis

  MOST BEHAVIORAL ECONOMIC BIASES = System 1 dominates
  in situations where System 2 should be engaged.

  CAVEAT (Gigerenzen again): System 1 is not simply "dumb."
  Expert intuition is System 1 operating with deep pattern matching.
  A chess grandmaster's instant move evaluation is System 1;
  it is often correct. A cardiologist's clinical intuition is System 1;
  it often outperforms checklists.

  ORGANIZATIONAL PARALLEL: Heuristics and routines in organizations
  are collective System 1 processes. When they work, they work fast
  and consistently. When they fail (environment changed), they fail
  systematically. Behavioral change in orgs = getting System 1 to update.
```

## Module Map

| Module | Core Question | Key Tools |
|---|---|---|
| 01-RATIONAL-CHOICE-CRITIQUE | When does rational choice fail? | Allais, Ellsberg, bounded rationality |
| 02-PROSPECT-THEORY | How do people evaluate outcomes under risk? | S-curve, loss aversion, probability weighting |
| 03-HEURISTICS-BIASES | What cognitive shortcuts cause systematic error? | Availability, representativeness, anchoring |
| 04-MENTAL-ACCOUNTING | How do people categorize and track money? | Sunk cost, house money, payment decoupling |
| 05-SOCIAL-PREFERENCES | Do people care about more than their own payoff? | Ultimatum game, Fehr-Schmidt, reciprocity |
| 06-INTERTEMPORAL-CHOICE | Why do people fail at long-term decisions? | Hyperbolic discounting, β-δ model |
| 07-NUDGE-CHOICE-ARCHITECTURE | How can defaults and framing guide choices? | Default effects, EAST framework, libertarian paternalism |
| 08-MARKET-ANOMALIES | How does behavior create asset pricing puzzles? | Equity premium, disposition effect, momentum |
| 09-APPLICATIONS-POLICY | How do governments use behavioral insights? | SBST, BIT, organ donation, tax compliance |
| 10-APPLICATIONS-PRODUCT-UX | How do products use behavioral patterns (for good and ill)? | Dark patterns, variable schedules, ethical design |

## Decision Cheat Sheet

| Behavioral question | Module |
|---|---|
| Why do employees resist organizational change? | 02 (loss aversion), 05 (reciprocity), 04 (status quo bias) |
| How to design a retirement savings program? | 06 (present bias), 07 (defaults), 09 (auto-enrollment) |
| Why do engineers keep working on failing projects? | 04 (sunk cost fallacy) |
| Why are performance reviews so fraught? | 02 (loss aversion), 05 (fairness/inequity aversion) |
| How to write a product pricing page? | 07 (anchoring, framing), 04 (payment decoupling) |
| Is this product feature manipulative or helpful? | 10 (dark pattern taxonomy, ethical design criteria) |
| Why doesn't better information always change behavior? | 01 (bounded rationality), 03 (affect heuristic) |
| How to structure incentive programs fairly? | 05 (inequity aversion), 02 (framing of gains vs. losses) |

## Common Confusion Points

**Behavioral economics doesn't say people are stupid**: The core finding is that people are systematically human — predictably biased in specific, documentable ways. These patterns are often adaptive in everyday environments. The issue arises when environments change but cognitive defaults don't update.

**Heuristics are not the same as biases**: A heuristic is a cognitive strategy. A bias is a systematic deviation from a normative standard. The same heuristic can be valuable in one environment (ecological rationality) and misleading in another. The distinction between "heuristic as adaptive tool" and "heuristic as bias" depends on the environment.

**Replication crisis context**: Much behavioral economics research from the 1970s-2000s has faced replication challenges. Priming effects (subliminal cues affecting behavior), ego depletion, power poses — many did not replicate at scale. Core findings (loss aversion, hyperbolic discounting, anchoring, default effects) are among the most robust. Be appropriately skeptical of single-study, small-N claims.

**Behavioral insights ≠ manipulation**: The same behavioral architecture principles apply to nudges toward better outcomes (default enrollment in retirement savings) and dark patterns in product design (confusing unsubscribe flows). The tool is neutral; the ethics depends on who benefits and whether users have meaningful alternatives.
