# Mental Accounting

## Thaler's Mental Accounting Framework

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MENTAL ACCOUNTING ARCHITECTURE                           │
│                                                                             │
│  STANDARD ECONOMIC VIEW:                                                    │
│  Money is perfectly fungible. $1 from salary = $1 from bonus = $1 from      │
│  gambling winnings = $1 found on street. Same $1 → same purchasing power.   │
│                                                                             │
│  REALITY (Thaler 1980, 1985, 1999):                                         │
│  People maintain SEPARATE MENTAL ACCOUNTS for money.                        │
│  Accounts have:                                                             │
│    - Implicit labels (food budget, entertainment, savings, "windfall")      │
│    - Non-fungibility: money in one account not freely transferred to another │
│    - Different psychological "prices" for spending                          │
│    - Different loss aversion across accounts                                │
│                                                                             │
│  MENTAL ACCOUNTING PHENOMENA:                                               │
│  ├── Sunk cost fallacy    (past costs affect future decisions)              │
│  ├── House money effect   (windfall gains spent differently from earned)    │
│  ├── Payment decoupling   (credit cards decouple pain of payment)           │
│  ├── Budgeting effects    (mental budget categories constrain spending)     │
│  ├── Transaction utility  (pleasure/displeasure from the deal itself)       │
│  └── Hedonic framing      (how to combine gains/losses to maximize utility) │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Sunk Cost Fallacy

```
SUNK COST:
  A cost that has already been incurred and cannot be recovered.
  Standard economics: sunk costs are IRRELEVANT to future decisions.
  Only future costs and benefits should determine current choice.
  Rational rule: if marginal benefit > marginal cost going forward, continue.

SUNK COST FALLACY:
  Continuing or escalating commitment to a course of action because of
  prior investment (time, money, reputation), even when the marginal
  calculation says stop.

MECHANISM (Thaler's interpretation):
  The sunk cost is in a mental account labeled "investment in project X."
  The account is "open" as long as project X continues.
  Abandoning the project "closes" the account with a loss crystallized.
  Continuing allows hope of eventual gain that would "close" the account positively.
  Loss aversion → extreme reluctance to close accounts at a loss.

DEMONSTRATIONS:
  Thaler (1980) theater ticket example:
  You paid $100 for a theater ticket. The day of the show, you feel ill.
  You wouldn't go if the ticket were free. But you go anyway "to not waste" the ticket.
  The $100 is gone either way. Your well-being is higher staying home.
  Rational action: stay home.

  Sports season tickets: fans attend games in terrible weather because "I already paid."
  If the ticket were free, they'd stay home.

ORGANIZATIONAL SUNK COST FALLACY:
  Large software projects: continue after cost overruns because "we've invested too much."
  Unsuccessful acquisitions: continue integrating/supporting acquired company
    long after ROI is clearly negative to avoid "admitting" the acquisition was wrong.
  Weapons systems, infrastructure: political reluctance to cancel due to sunk investment.

TECHNICAL DEBT AS HYPERBOLIC SUNK COST:
  Taking on technical debt is often framed as "we've already built it this way."
  Sunk cost fallacy: the effort to build it that way is already spent.
  The relevant question: what's the marginal cost of carrying this debt forward
  vs. marginal cost of refactoring NOW?
  Sunk costs should not enter this calculation — but they do.

DEBIASING:
  Actively separate sunk costs from future projections.
  Ask: "If we were starting fresh today with this information, would we start this project?"
  If no: the sunk cost fallacy is at work.
  Pre-commitment "kill criteria": define in advance the objective conditions under which
  the project will be canceled. Avoids post-hoc rationalization.
```

## House Money Effect

```
HOUSE MONEY EFFECT (Thaler & Johnson 1990):
  Windfall gains (unexpected) are held in a separate mental account
  labeled something like "extra" or "house money."
  This money feels different from "earned" money → spent more freely
  → more risk-taking with it.

EXPERIMENTAL EVIDENCE:
  Give subjects a prior gain before a gambling task.
  Subjects who received a prior gain → more risk-taking in subsequent bet.
  Prior gain "cushions" against subsequent loss (loss doesn't hurt as much
  because the loss is absorbed by the prior gain in the same mental account).

  Gamble after gaining $30: more likely to accept bet with negative EV.
  Gamble after losing $30: less likely to accept bet (prior loss depletes mental account).

REAL-WORLD APPLICATIONS:
  Stock market: investors take more risk with unrealized gains
    (profits "play with house money") than with principal.
  Casino behavior: winnings spent more freely than initial stake.
  Bonus spending: employee bonuses often spent on discretionary items
    ("windfall money") vs. salary going to fixed expenses.
  Sales commission: quarterly windfall commissions → discretionary big purchases.

INVESTMENT IMPLICATION:
  Mental separation of "invested capital" vs. "market gains" is economically
  irrational. $1 of unrealized capital gain has the same purchasing power as
  $1 of principal. But behavioral investors treat them differently → suboptimal
  portfolio management (hold winners too long because gains are "house money").
```

## Payment Decoupling

```
PAIN OF PAYING:
  Spending money is mildly aversive — it creates a "pain of paying."
  The strength of pain depends on the SALIENCE of the payment.
  More salient payment → more pain → more restraint on spending.

DECOUPLING:
  Separating the payment in time or salience from the consumption experience.
  Less salient payment → less pain → more spending.

CREDIT CARDS:
  Pay now: cash payment at point of purchase → maximum salience → maximum pain.
  Pay by check: slightly decoupled.
  Pay by credit card: payment delayed; abstract; maximum decoupling → minimum pain.
  Result: people spend more (on average ~15-30% more in field studies) when paying
  by credit card vs. cash.

  Prelec & Simester (2001): willingness to pay for tickets to sold-out event:
  Credit card bidders: 2× higher bids than cash bidders.
  Same person, same good, different payment mechanism.

AMAZON ONE-CLICK / IN-APP PURCHASES:
  Remove every friction in the payment process.
  Stored credit card + single click = maximum decoupling.
  Children and in-app purchases: extreme case. Zero perceived pain.
  Regulatory response: FTC enforcement on misleading in-app purchase design.

TAX WITHHOLDING AND MENTAL ACCOUNTING:
  Payroll tax withholding: taxes taken before pay hits your account.
  Tax refund: psychologically "found money" (windfall), not "return of overpayment."
  Most Americans prefer refunds even though this is an interest-free loan to government.
  Mental accounting: withheld taxes in "government's account"; refund is unexpected gain.
  Non-withheld taxes (self-employed, quarterly estimates): equivalent total taxes
  paid, but more painful because writing a check is salient. Self-employed report
  greater tax resentment than employees with similar effective rates.

PRODUCT DESIGN:
  Subscription models: annual upfront payment → single painful payment, then free.
  Monthly auto-renewal: small, recurrent, low-salience → consumers don't cancel.
  The "forgetting tax": consumers paying for unused subscriptions = decoupled payment.
  Gym memberships: paid upfront → sunk cost + decoupled. Members rarely cancel.
  Netflix / SaaS: monthly billing → low-salience → low churn (by design).
```

## Transaction Utility and the Acquisition Utility

```
THALER (1985) — TWO-COMPONENT UTILITY:

  ACQUISITION UTILITY: The pleasure/pain from the good itself.
    = Consumer surplus: V(good) − P(price paid)
    Standard economic measure.

  TRANSACTION UTILITY: The pleasure/pain from the "deal."
    = P(reference price) − P(price paid)
    where reference price = what the consumer believes the good should cost.
    If price paid < reference price → positive transaction utility (good deal!)
    If price paid > reference price → negative transaction utility (bad deal!)

  TOTAL UTILITY = Acquisition utility + Transaction utility

IMPLICATIONS:
  A consumer might buy a good with negative acquisition utility if the
  transaction utility is positive enough.
  Example: You see a shirt priced "$200, marked down to $75."
    If you wouldn't normally pay $75 for this shirt (V < $75):
    Acquisition utility < 0.
    But: reference price anchor = $200; transaction utility = $200 - $75 = $125.
    If transaction utility > |acquisition utility|: buy even though V < P.
    "I saved $125!" (on something you didn't need)

  SILVER LINING IN PRICING:
  High reference price + moderate discount:
    Large positive transaction utility can drive purchase decisions.
    Retail "was/now" pricing exploits this.
  Luxury goods: high transaction utility from buying above one's usual category.
  "Good deal" framing can make irrational purchases feel rational.

REFERENCE PRICE FORMATION:
  Where do reference prices come from?
  - Usual market price (category knowledge)
  - Listed "suggested retail price" (SRP)
  - Competitor pricing
  - Prior purchases of same good
  - Stated anchor/comparison in ad copy
  All are malleable to influence by the seller.
```

## Hedonic Framing — Combining Gains and Losses

```
THALER'S FOUR CASES (based on Prospect Theory value function shape):

  Case 1: SEPARATE GAINS (Silver Lining Principle)
    Two separate gains feel better than one combined gain.
    v($100) + v($50) > v($150) because v is concave in gains.
    "You won $100 on Monday AND $50 on Tuesday" better than "you won $150 once."
    IMPLICATION: When delivering good news, separate them.
    "Here's your $5K bonus... and separately, here's a $2K project completion bonus."

  Case 2: COMBINE LOSSES (Don't Salt the Wound)
    One combined loss feels better than two separate losses.
    v(-$150) > v(-$100) + v(-$50) because v is convex in losses (diminishing sensitivity).
    IMPLICATION: When delivering bad news, combine it.
    "Two bad things happened today: X and Y." Better than "X happened yesterday, Y today."

  Case 3: COMBINE SMALL LOSS WITH LARGE GAIN (Silver Lining)
    If gain is much larger than loss: combine.
    v($150 − $10) better than v($150) + v(-$10) if the $10 loss is "erased" by the gain.
    The small loss is absorbed into the gain domain (net gain feels better than
    celebrating gain separately and mourning small loss separately).

  Case 4: SEPARATE SMALL GAIN FROM LARGE LOSS (Don't Compound Misery)
    If large loss with small gain: separate them.
    v(-$150) + v($10) better than v(-$140).
    The $10 gain provides some consolation that would be lost if netted against the large loss.
    IMPLICATION: When there's a large loss, a small silver lining feels better separated.
    "We missed targets by $5M... but on the positive side, the product quality scores
    set a new record." Don't net these.

PRACTICAL HEDONIC FRAMING FOR LEADERS:
  Good news day: "Two great things to share..." → separate
  Bad news day: "There are a couple of difficult things together..." → combine
  Large loss + small win: "I know this quarter was very hard... I also want to note
    [specific silver lining]" → separate silver lining
  Small loss within large gain: combine into the overall success narrative
```

## Decision Cheat Sheet

| Mental accounting question | Phenomenon | Application |
|---|---|---|
| Why does the team refuse to kill a losing project? | Sunk cost fallacy (open loss account) | Pre-commit kill criteria; reframe as "starting fresh" |
| Why do employees spend bonuses on luxuries? | House money effect (windfall account) | Frame bonuses as part of total compensation for savings goals |
| Why does subscription revenue have lower churn? | Payment decoupling (low pain of paying) | Use annual subscriptions for retention; highlight savings |
| Why does a "$75 marked from $200" sell even at V < $75? | Transaction utility (positive deal feeling) | Reference price anchoring in pricing strategy |
| Best way to deliver two pieces of good news? | Hedonic framing (separate gains) | Deliver separately across time |
| Best way to deliver multiple bad news at once? | Hedonic framing (combine losses) | Combine; don't drag out bad news |
| Why is cash more restrictive than credit card? | Payment decoupling (salience of payment) | Use cash for budget discipline; card for smooth purchase |

## Common Confusion Points

**Sunk cost fallacy vs. commitment**: Not all persistence is sunk cost fallacy. Strategic commitment (burning ships, pre-commitment) can be rational game-theoretically. The distinction: sunk cost fallacy = continuing because of past investment despite negative marginal calculation. Rational commitment = building credibility by constraining future options when the commitment itself changes others' behavior.

**House money effect is not the same as risk tolerance**: Risk tolerance is a stable individual trait. The house money effect is context-specific: the same person takes more risk with windfall gains but not after losses. It's an account-specific, situational phenomenon, not a fundamental change in risk preferences.

**Mental accounting is not always irrational**: Thaler himself acknowledges that mental accounting serves useful self-control functions. Having a "savings account" that you don't raid for consumption is irrational from pure fungibility but smart for self-control. A "vacation fund" that resists consumption pressure preserves long-term well-being. Mental accounts = behavioral commitments to future self.

**Transaction utility exploitation is not always manipulation**: Providing good value AND clearly communicating the deal is transactional utility that's earned. The manipulation concern arises when reference prices are fabricated ("suggested retail price" that was never the real price), not when genuine value is communicated clearly.
