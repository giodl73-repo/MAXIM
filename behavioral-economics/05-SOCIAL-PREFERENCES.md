# Social Preferences

## Beyond Self-Interest

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    SOCIAL PREFERENCES LANDSCAPE                              │
│                                                                               │
│  STANDARD MODEL: U_i(x) = f(x_i)  — utility depends only on OWN payoff     │
│                                                                               │
│  SOCIAL PREFERENCES: U_i(x) = f(x_i, x_{-i}, context, history)             │
│  Utility depends on:                                                         │
│    - Own payoff x_i                                                          │
│    - Others' payoffs x_{-i}  (inequity aversion)                            │
│    - Whether payoff was fairly obtained  (procedural fairness)               │
│    - Whether others cooperated  (reciprocity)                               │
│    - Identity/group membership  (in-group favoritism)                       │
│    - Social norms in context  (what's appropriate here?)                    │
│                                                                               │
│  EXPERIMENTAL METHODS:                                                       │
│  Ultimatum Game, Dictator Game, Trust Game, Public Goods Game,              │
│  Prisoner's Dilemma variants — all run with real money stakes                │
└─────────────────────────────────────────────────────────────────────────────┘
```

<!-- @editor[bridge/P2]: No bridge from classical game theory (Nash equilibrium, subgame perfection) to behavioral game theory — the learner has MIT TCS background and would orient faster with an explicit "standard game theory predicts X via backward induction; here's where human subjects diverge" framing before the experiments -->
## Ultimatum Game

```
ULTIMATUM GAME (Güth et al. 1982):
  Two players: Proposer and Responder.
  Stake: $100 (or equivalent).
  Proposer: offers some split (e.g., $70/$30).
  Responder: accepts → both receive the split; rejects → both receive $0.

  STANDARD PREDICTION (self-interested players):
  Proposer offers $1 (minimum), Responder accepts ($1 > $0).
  By backward induction: Responder accepts any positive offer.

  EMPIRICAL REALITY:
  Most common offer: 40-50% (Proposer keeps 50-60%)
  Mean offer: ~40-45% of the stake
  Rejection rate for offers < 20%: ~50-80%
  Rejection rate for offers < 10%: >90%

  Players reject money rather than accept "unfair" offers.
  They sacrifice real money to punish unfair Proposers.
  This is COSTLY PUNISHMENT → purely other-regarding behavior.

  CROSS-CULTURAL VARIATION:
  Henrich et al. (2001): ultimatum game in 15 small-scale societies.
  Wide variation in modal offer: 26% (Machiguenga, Amazon) to 57% (Lamalera, Indonesia).
  Variation correlates with: market integration, cooperation in production.
  NO society shows offers near 0% or acceptance of near-0 offers.
  → Fairness norms exist everywhere but their content varies significantly.
```

## Dictator Game

```
DICTATOR GAME (Kahneman, Knetsch & Thaler 1986):
  Same as ultimatum but Responder has no power to reject.
  Proposer dictates the split; Responder takes whatever is offered.

  STANDARD PREDICTION: Proposer keeps everything ($100, $0 to Responder).

  EMPIRICAL REALITY:
  Mean offer: ~20-30% of stake to Responder.
  Mode: often at 0% or 50% (bimodal distribution).
  Some give 50% (strong equality norm).
  Most give something > 0 (altruistic transfers).

  INTERPRETATION: Reveals altruistic giving without strategic considerations.
  Unlike ultimatum (where generosity could be strategic), dictator game
  generosity is "pure" altruism.

CAVEATS:
  Experimenter effect: people give more when they feel observed.
  Hoffman et al.: increasing anonymity → less giving. Near-complete anonymity → ~10% give.
  Levitt & List (2007): field settings show less altruism than lab.
  List (2006): "take" frame (can take from Responder) → much less giving.
  Awareness: DG giving is context-sensitive; reduced in non-laboratory settings.

  LESSON: Social preferences are real but sensitive to context, anonymity, and norms.
```

## Fehr-Schmidt Inequity Aversion Model

```
FEHR-SCHMIDT (1999) MODEL:
  Utility depends on own payoff MINUS penalty for inequality.

  U_i(x) = x_i − α_i × max(x_j − x_i, 0) − β_i × max(x_i − x_j, 0)

  where:
  x_i = own payoff, x_j = other player's payoff (j ≠ i)
  α_i = disadvantageous inequality aversion (hurt when behind)
  β_i = advantageous inequality aversion (discomfort when ahead)

  PARAMETER CONSTRAINTS:
  α_i > 0:          Dislike being paid LESS than others (behind is bad)
  0 ≤ β_i < 1:      Some discomfort at being paid MORE (ahead is discomforting)
  β_i < α_i:        Disadvantageous inequality hurts more than advantageous
                    ("It's worse to get less than others than to get more")

  ESTIMATED EMPIRICAL PARAMETERS:
  About 30% of population: α ≈ 0, β ≈ 0 (pure self-interest)
  About 30%: α ≈ 0.6, β ≈ 0.25 (mild inequity aversion)
  About 30%: α ≈ 1, β ≈ 0.5 (strong inequity aversion)
  About 10%: β > 0.5 (very strong inequity aversion — near Rawlsian)

  ORGANIZATIONAL APPLICATIONS:
  Pay transparency: when employees know peers' salaries, β effects activate.
  Employees in identical roles → strong equality norm.
  If one person makes substantially more: those making less feel α hurt.
  If one person makes much more AND knows others make less: β effect activates.
  Internal equity matters as much as absolute pay level.

EVIDENCE IN ORGANIZATIONS:
  Card et al. (2012): UC pay revealed to employees below median → reduced job satisfaction.
  Employees above median: no change. Consistent with α >> β.
  Implication: pay transparency → morale gains for top earners, losses for below-median.
  Reduces overall satisfaction if distribution is right-skewed (as most are).
```

## Reciprocity

```
RECIPROCITY — TYPES:
  POSITIVE RECIPROCITY: If X does something nice for Y → Y wants to reciprocate.
    Warm glow from helping someone who helped you.
  NEGATIVE RECIPROCITY: If X does something mean to Y → Y wants to punish X.
    Anger from being mistreated → costly punishment.

EXPERIMENTAL EVIDENCE — PUBLIC GOODS GAME:
  N players each given $100.
  Each can contribute 0-100 to a public pool.
  Pool doubles and is equally divided.
  Pure self-interest: contribute $0 (Nash equilibrium).
  Nash prediction: free riding → public goods underprovision.

  EMPIRICAL FINDING:
  Round 1: average contribution ~50% of endowment.
  Successive rounds (without communication): contributions DECLINE toward zero.
  Why? Non-contributors (free riders) observed → contributers reduce contributions
  in anger at being exploited.
  With punishment option: contributors punish free riders (even at personal cost).
  With punishment: contributions stay high (conditional cooperation maintained).

  CONDITIONAL COOPERATION: Most people are conditional cooperators.
  They contribute if others contribute; reduce contribution if others free ride.
  This is NOT pure altruism — it's reciprocal.
  A small fraction (<30%) are unconditional free riders; they bring down cooperation.

RABIN'S FORMAL RECIPROCITY MODEL (1993):
  Fairness equilibrium: strategy is justified by the belief that the other
  player intends kindness/unkindness toward you.
  Kind intent → reciprocate kindly; unkind intent → punish.
  This creates multiple equilibria: full cooperation if everyone believes
  everyone else will cooperate; full defection if everyone believes defection.
  The belief → self-fulfilling prophecy.
  Social context and shared expectations determine which equilibrium is reached.
```

## Trust Game (Berg, Dickhaut & McCabe 1995)

```
TRUST GAME:
  Two players, Sender and Receiver.
  Sender given $10. Can send 0-10 to Receiver.
  Amount sent is TRIPLED (by experimenter).
  Receiver can send any amount back to Sender.

  STANDARD PREDICTION: Sender sends $0 (Receiver will return nothing).
  EMPIRICAL REALITY:
    Mean amount sent: ~$5 (50% of endowment)
    Mean amount returned: ~$3-4 (less than tripled amount, but positive)

  INTERPRETATION:
  Senders trust Receivers to return value → trust is placed.
  Receivers reciprocate trust → social equilibrium above Nash.
  Economic theory of trust: credible commitment + punishment + reputation.
  Experimental finding: trust and reciprocity operate even without these.

  WITHIN-ORGANIZATION TRUST:
  Managers who extend autonomy and trust to employees:
  → Employees reciprocate with higher effort and commitment (positive reciprocity).
  → This is NOT based on incentive contracts but on the trust itself.
  "Gift exchange" (Akerlof 1982): employers offer above-market wages as "gift"
  → employees reciprocate with above-minimum effort.
  Evidence: above-market wages predict higher productivity, lower shirking.
  Efficiency wages: paying more than the market-clearing wage is rational
  if it elicits reciprocal effort that exceeds the wage premium.

  ORGANIZATIONAL TRUST DAMAGE:
  Betrayal aversion (Bohnet & Zeckhauser 2004):
  Loss from betrayal by a trusted person > same loss from an impersonal mechanism.
  Layoffs, broken promises, surveillance of trusted employees →
  destroys reciprocity more than the immediate cost suggests.
  Trust is asymmetric to build and destroy: slow to build, fast to destroy.
```

## Social Norms and Cooperation

```
INJUNCTIVE vs. DESCRIPTIVE NORMS:
  Injunctive: what people OUGHT to do (moral prescription)
  Descriptive: what people ACTUALLY do (observed behavior)

  Cialdini et al. (1990): both influence behavior but in different ways.
  Descriptive norm ("Most guests reuse their towels") → conformity.
  Injunctive norm ("Please help us save the environment by reusing") → weaker effect.
  Descriptive norms leverage social proof / conformity.

  NORM CONFLICT:
  When injunctive and descriptive norms diverge: "Don't litter" (injunctive) in
  a heavily littered environment → descriptive norm (littering is normal here)
  can INCREASE littering relative to a clean environment.
  Implication: keeping an environment clean is its own positive externality.

  ORGANIZATIONAL NORMS:
  "This is how we do things here" = injunctive + descriptive norm bundled.
  New employees rapidly adopt team norms (descriptive conformity).
  When the norm is "ship on time" or "don't cut corners" → self-enforcing.
  When the norm is "it's okay to miss deadlines" → also self-enforcing.
  Leadership shapes norms through visible behavior (you are the descriptive norm
  for your organization — what you do, not what you say, is the norm).

  SOCIAL SANCTIONING:
  Norms sustained by:
  1. Internalization: people believe the norm is right.
  2. Shame/guilt: anticipated negative self-evaluation.
  3. Social sanction: others will punish deviance.
  All three operate in real organizations; relative weight varies by culture.
```

## In-Group/Out-Group Effects

```
MINIMAL GROUP PARADIGM (Tajfel 1970):
  Assign people to groups on a trivially arbitrary basis (flip of a coin,
  stated art preference). No interaction, no prior relationship.
  Result: people IMMEDIATELY favor in-group members in resource allocation.
  Even the most arbitrary categorization creates us/them effects.

APPLICATIONS:
  Team identity: naming teams, shared rituals → in-group favoritism.
  Team competition: useful for performance in some contexts;
  dysfunctional in cross-team collaboration.
  Hiring: interviewers favor candidates similar to themselves
  (alma mater, interests, demographic similarity).
  Code reviews: more critical of out-group members' code.
  "No true Scotsman" argument in team culture debates.

  Cross-functional teams often fail because team identity is weaker than
  functional department identity. People identify more with their department
  than with the cross-functional project team.
```

## Decision Cheat Sheet

| Social preference question | Finding | Implication |
|---|---|---|
| Will employees accept a clearly unfair pay offer? | Ultimatum game: ~50-80% reject offers < 20% | Internal pay equity matters for morale and retention |
| How much weight should managers give to procedural fairness? | Fehr-Schmidt: α ≈ 0.5+ for most; process matters | Fair process acceptance even of bad outcomes |
| Will a team free-ride on a shared project? | Conditional cooperation: most cooperate if others do | Visible contribution tracking; punishment of free-riding |
| Will employees reciprocate trust with effort? | Trust game + efficiency wages: yes | Autonomy and above-market wages elicit reciprocal effort |
| Does pay transparency hurt morale? | Card et al.: below-median employees reduce satisfaction | Transparency has equity benefits but morale costs for below-median |
| How are organizational norms sustained? | Internalization + shame + social sanction | Leaders model behavior; maintain clean environments |
| Why do cross-functional teams underperform? | Minimal group paradigm + competing identities | Shared team identity building; reduce departmental identity salience |

## Common Confusion Points

**Inequity aversion ≠ pure egalitarianism**: Fehr-Schmidt model allows β < 1 — people are somewhat uncomfortable being ahead but don't require perfectly equal outcomes. In fact, many people accept large inequality if it's perceived as deserved (performance-based). The key is perceived fairness of the process and proportionality, not strict equality.

**Ultimatum game results aren't universal**: Cross-cultural variation is real and significant (Henrich et al.). Western undergraduate lab subjects are WEIRD (Western, Educated, Industrialized, Rich, Democratic). Fairness norms vary significantly across societies. Don't generalize US university samples to global workforces without caution.

**Reciprocity requires correct attribution of intent**: Rabin's model depends on perceived intent (kind vs. unkind). The same outcome delivered with different framing (system failure vs. deliberate policy) elicits different reciprocal responses. Organizational communication about why something is happening affects whether negative outcomes trigger resentment (negative reciprocity) or acceptance.

**Social preferences and incentives interact**: Strong financial incentives can crowd out intrinsic motivation and social preferences. Frey (1997): adding payment for tasks previously done for free can reduce effort. Gneezy & Rustichini (2000): adding fines for late daycare pickup increased late pickups (fine reframed the norm from social obligation to market transaction). Incentive design must account for how incentives affect the social and normative context.
