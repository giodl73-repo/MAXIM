---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "09-METRICS-AND-ANALYTICS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:marketing:metrics-and-analytics
kind: guide
module: marketing
section: marketing
title: Metrics and Analytics
status: source-custody
source_custody: partial
current_path: marketing/09-METRICS-AND-ANALYTICS.md
canonical_path: marketing/09-METRICS-AND-ANALYTICS.md
backsource_ids: [proof-backfill:marketing:09-metrics-and-analytics, git-history:marketing:09-metrics-and-analytics]
concepts: [CAC, LTV, ROAS, funnel analysis, cohort analysis, MMM, MTA, attribution, incrementality]
root_concepts: [marketing metrics, unit economics]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Metrics and Analytics

## The Big Picture

This is where marketing proves it paid. The metrics layer converts campaigns into
**unit economics** — the cost to acquire a customer vs the value that customer
returns — and into the *did-it-work* question (attribution, incrementality). The
landscape, from spend to verdict:

```
+-------------------------------------------------------------------------+
|                    THE MARKETING ECONOMICS STACK                        |
|                                                                         |
|  SPEND            -> ACQUISITION    -> VALUE        -> VERDICT          |
|  -----               -----------       -----           -------          |
|  marketing $         CAC               LTV             LTV : CAC        |
|  + sales $           (cost to          (value a        ratio + payback  |
|                       acquire one)      customer        period          |
|                                         returns)                        |
|     |                    |                  |              |            |
|     v                    v                  v              v            |
|  .--------.          .--------.         .--------.    .-------------.   |
|  | ROAS   |          | FUNNEL |         | COHORT |    | ATTRIBUTION |   |
|  | revenue|          | per-   |         | retain |    | which spend |   |
|  | per $  |          | stage  |         | by     |    | gets credit?|   |
|  | spent  |          | yield  |         | cohort |    | MMM vs MTA  |   |
|  '--------'          '--------'         '--------'    '-------------'   |
|                                                            |            |
|                                                            v            |
|                                                    .---------------.    |
|                                                    | INCREMENTALITY |   |
|                                                    | what spend     |   |
|                                                    | CAUSED (A/B)   |   |
|                                                    '---------------'    |
|                                                                         |
|  The whole stack answers: are we acquiring customers profitably?        |
+-------------------------------------------------------------------------+
```

**Read left-to-right**: spend buys acquisitions at some CAC; those customers
return some LTV; the ratio and payback decide profitability; attribution and
incrementality decide *which spend* deserves the credit. The bridge: this is
**cost accounting + observability for the growth pipeline** — the same instinct as
cost-per-request and SLOs, applied to customers.

---

## CAC: Customer Acquisition Cost

The denominator of the whole model.

```
                 total sales + marketing spend (in a period)
   CAC  =  ---------------------------------------------------------
                 number of NEW customers acquired (same period)
```

| Subtlety | Why it matters |
|---|---|
| **Fully-loaded vs paid-media-only** | Include salaries, tools, content — not just ad spend — or CAC flatters |
| **Blended vs paid CAC** | Blended divides by *all* new customers (incl. organic); paid divides by paid-channel customers. Blended hides whether paid is working |
| **By channel / cohort** | Marginal CAC rises as you scale a channel (you exhaust the cheap audience first) |
| **Attribution-dependent** | Which channel gets credited changes per-channel CAC (see attribution below) |

The trap is **blended CAC masking a broken paid channel**: organic growth can hide
that your paid acquisition is unprofitable. Always look at *paid* CAC and
*marginal* CAC (the cost of the *next* customer), not just the blended average —
the same reason you watch p99 and marginal cost, not just the mean.

---

## LTV: Customer Lifetime Value

The numerator — the value a customer returns over their life. Several formulations;
here is the operating one.

```
  SIMPLE (steady-state):

            ARPA  x  gross margin %
   LTV  =  ---------------------------
                 churn rate

   ARPA = avg revenue per account (per period)
   churn = fraction of customers lost per period
   (1 / churn = expected customer lifetime in periods)

  EXAMPLE: $100/mo ARPA, 70% gross margin, 5% monthly churn
   lifetime = 1 / 0.05 = 20 months
   LTV = (100 x 0.70) / 0.05 = $1,400
```

```
+-----------------------------------------------------------------+
|                  WHAT DRIVES LTV                                |
|                                                                 |
|  ARPA up       -> upsell, cross-sell, price (04)                |
|  MARGIN up     -> cost to serve down                            |
|  CHURN down    -> retention is the BIGGEST lever (1/churn       |
|                   is nonlinear: halving churn DOUBLES lifetime) |
|  EXPANSION     -> negative net churn (existing accounts grow    |
|                   faster than they leave) -> LTV can be huge    |
+-----------------------------------------------------------------+
```

Two refinements senior readers will want: (1) **discount future cash flows** — LTV
is a present value; far-future revenue is worth less, so a proper LTV discounts at
the cost of capital. (2) **Churn is the dominant, nonlinear lever** — because
lifetime is 1/churn, cutting churn from 5% to 2.5% *doubles* expected lifetime and
LTV. Retention beats acquisition for LTV, which is why cohort analysis (below)
matters more than any single campaign metric.

---

## The LTV:CAC Ratio and Payback Period

The two numbers that decide whether the business works.

```
+-----------------------------------------------------------------+
|              LTV : CAC  AND  PAYBACK                            |
|                                                                 |
|  LTV : CAC RATIO     how much value you get per $ of            |
|                      acquisition.                               |
|                                                                 |
|     < 1 : 1   losing money on every customer (stop)             |
|     ~ 1 : 1   break-even, no margin for ops/profit              |
|     ~ 3 : 1   the common HEALTHY benchmark for SaaS             |
|     > 5 : 1   possibly UNDER-investing in growth (spend more!)  |
|                                                                 |
|  CAC PAYBACK PERIOD  months to recover CAC from gross-margin    |
|                      contribution.                              |
|                                                                 |
|              CAC                                                |
|     = -----------------------------                             |
|        ARPA x gross margin (monthly)                            |
|                                                                 |
|     Healthy SaaS rule of thumb: < 12 months.                    |
|     Long payback strains cash even if LTV:CAC looks great.      |
+-----------------------------------------------------------------+
```

| Metric | Formula | Healthy benchmark | What it ignores |
|---|---|---|---|
| **LTV:CAC** | LTV / CAC | ~3:1 (SaaS) | *When* the cash returns (timing) |
| **CAC payback** | CAC / (ARPA x GM% per period) | < 12 months | Total lifetime value beyond payback |

The two metrics are complementary and you need *both*. A 5:1 LTV:CAC with a
36-month payback can *bankrupt* you on cash even though each customer is wildly
profitable eventually — you front the CAC today and collect for three years. This
is a **cash-flow-vs-NPV** distinction: LTV:CAC is the lifetime return; payback is
the cash-conversion speed. The bridge: it's the difference between "is this service
profitable per request" and "can we afford the capex to stand it up before the
revenue lands."

```
OLD WORLD                          UNIT-ECONOMICS ANALOG
-----------------------------      -------------------------------------
Cost per request / per unit        CAC (cost per acquired customer)
Lifetime value of a tenant         LTV (value per customer over life)
NPV of a capacity investment       LTV:CAC ratio (lifetime return)
Time to ROI / break-even           CAC payback period (cash speed)
Watch marginal, not just average   Marginal CAC, not blended CAC
```

---

## ROAS: Return on Ad Spend

The campaign-level efficiency metric.

```
                 revenue attributable to the ads
   ROAS  =  ----------------------------------------
                 cost of the ads

   ROAS = 4 (or "400%")  ->  $4 revenue per $1 spent.

   BREAK-EVEN ROAS depends on MARGIN, not revenue:
     break-even ROAS = 1 / gross margin %
     (50% margin -> need ROAS > 2 just to break even on COGS;
      and that's BEFORE the ad cost itself)
```

The constant error is treating **ROAS as profit**. ROAS is *revenue* per ad
dollar; profit requires netting out COGS (so break-even ROAS = 1/margin) and all
other costs. A 3x ROAS on a 30% margin product is *losing money*. ROAS is also
**attribution-dependent** — the revenue in the numerator is "attributed" revenue,
which means the attribution model (next section) silently sets the number. Two
teams can report different ROAS for the same campaign purely from attribution
choices.

---

## Funnel and Cohort Analysis

Two complementary lenses on the data.

```
+-----------------------------------------------------------------+
|         FUNNEL (cross-section)   vs   COHORT (longitudinal)     |
|                                                                 |
|  FUNNEL = conversion by STAGE    COHORT = behavior over TIME    |
|  ------------------------------  ------------------------------ |
|   visit    100,000               group users by SIGNUP MONTH:   |
|     |  10%                                                      |
|   signup    10,000               cohort  m0   m1   m2   m3      |
|     |  20%                       Jan     100%  60%  45%  40%    |
|   activate   2,000               Feb     100%  65%  50%  47%    |
|     |  15%                       Mar     100%  70%  58%  ...    |
|   pay          300                                              |
|                                  -> is RETENTION improving      |
|   where is the bottleneck        cohort over cohort?            |
|   STAGE? -> fix the worst        -> does the curve FLATTEN      |
|   per-stage yield                (a retained core) or -> 0?     |
+-----------------------------------------------------------------+
```

**Funnel analysis** is a *cross-sectional* view — conversion rate per stage right
now — and it localizes the bottleneck (the lowest-yield stage is where to invest,
exactly like the slowest stage in a pipeline). **Cohort analysis** is a
*longitudinal* view — group users by acquisition date and track them over time —
and it answers the questions funnels can't: is retention improving for newer
cohorts, and does the retention curve *flatten* (you have a sticky core) or decay
to zero (you have a leaky bucket no acquisition can fill). The bridge: funnels are
per-stage throughput; cohorts are *retention curves by release*, like tracking
each deploy's user base over time. You need both: the funnel says *where* it
leaks, the cohort says *whether it's getting better*.

---

## Attribution: Who Gets the Credit?

Customers touch many channels before converting. **Attribution** assigns credit
for the conversion across those touches — and it silently determines CAC, ROAS,
and budget decisions. There is no objectively "true" attribution model; each is a
*rule*, and the rule changes the answer.

```
+-----------------------------------------------------------------+
|              ATTRIBUTION MODELS                                 |
|              (journey: display -> search -> email -> BUY)       |
|                                                                 |
|  LAST-TOUCH     100% to the LAST touch (email).                 |
|                 Simple; over-credits bottom-funnel.             |
|                                                                 |
|  FIRST-TOUCH    100% to the FIRST touch (display).              |
|                 Over-credits top-funnel awareness.              |
|                                                                 |
|  LINEAR         equal credit to all touches (25% each).         |
|                                                                 |
|  TIME-DECAY     more credit to touches NEARER the conversion.   |
|                                                                 |
|  POSITION-BASED 40% first, 40% last, 20% middle (U-shaped).     |
|                                                                 |
|  DATA-DRIVEN    model-estimated credit (e.g. Shapley-value      |
|                 style) from many journeys. Best, data-hungry.   |
|                                                                 |
|  THE PROBLEM: these are RULES, not truth. They distribute a     |
|  fixed credit by assumption -> different budgets, same data.    |
+-----------------------------------------------------------------+
```

| Model | Credit rule | Bias |
|---|---|---|
| **Last-touch** | All to final touch | Over-credits closers (search/email) |
| **First-touch** | All to first touch | Over-credits awareness |
| **Linear** | Equal to all | Ignores that touches differ in impact |
| **Time-decay** | More to recent touches | Still assumption-driven |
| **Position-based (U)** | 40/40/20 | Arbitrary weights |
| **Data-driven** | Modeled (Shapley-like) | Best, but needs lots of journey data |

The deep point: **all attribution is correlational** — it divides up credit among
observed touches by an assumed rule, but it cannot tell you what would have
happened *without* the touch. That counterfactual is what you actually want, and
only experiments give it (incrementality, below).

---

## MMM vs MTA vs Incrementality

The three families for answering "what did our marketing actually drive," with a
sharp distinction in what they can claim.

```
+-----------------------------------------------------------------+
|         MMM   vs   MTA   vs   INCREMENTALITY                    |
|                                                                 |
|  MMM (marketing mix modeling)                                   |
|   top-down regression: model SALES ~ spend by channel +         |
|   price + seasonality + macro, on aggregate time-series.        |
|   + privacy-proof (no user tracking), captures offline +        |
|     long-term/brand effects                                     |
|   - coarse, can't do user-level, correlational (confounds)      |
|                                                                 |
|  MTA (multi-touch attribution)                                  |
|   bottom-up: stitch USER-LEVEL touch journeys, assign credit.   |
|   + granular, per-channel/creative                              |
|   - needs cross-site tracking (DYING, see 08), still            |
|     correlational                                               |
|                                                                 |
|  INCREMENTALITY (experiments)                                   |
|   randomized holdout / geo test: show ads to A, not to B,       |
|   measure the LIFT.                                             |
|   + CAUSAL - the real "did it work"                             |
|   - costs forgone exposure, needs scale + design                |
|                                                                 |
|  GOLD STANDARD: experiments. MMM + MTA inform; experiments      |
|  CONFIRM. As tracking dies (08), MMM + experiments rise.        |
+-----------------------------------------------------------------+
```

| Approach | Direction | Granularity | Causal? | Privacy |
|---|---|---|---|---|
| **MMM** | Top-down (aggregate regression) | Channel-level | No (correlational) | Robust (no user data) |
| **MTA** | Bottom-up (user journeys) | Touch-level | No (correlational) | Fragile (needs tracking) |
| **Incrementality** | Experiment (holdout/geo) | Test-level | **Yes (causal)** | Robust |

The thread tying this guide to `07-MARKET-RESEARCH.md`: **only a randomized
experiment establishes causation.** MMM and MTA are sophisticated *correlational*
estimates — useful for allocation, but confounded. Incrementality testing
(randomized holdouts, geo experiments) is the same A/B machinery from `07`, applied
to whole channels, and it is the only method that answers the counterfactual "what
sales would *not* have happened without this spend." As cross-site tracking erodes
(`08`), the industry is converging on **MMM for breadth + experiments for truth**,
with MTA shrinking.

---

## Decision Cheat Sheet

| I want to know... | Use |
|---|---|
| Can we acquire profitably? | LTV:CAC (aim ~3:1) *and* payback (< ~12 mo) |
| Is our paid channel actually working? | Paid + marginal CAC (not blended) |
| Where is the funnel leaking? | Funnel analysis — fix the lowest-yield stage |
| Is retention improving? | Cohort analysis — do curves flatten or decay? |
| The biggest lever on LTV | Reduce churn (lifetime = 1/churn, nonlinear) |
| Is a campaign efficient? | ROAS — but compare to break-even (1/margin), not to 1 |
| Which channel gets credit? | Attribution — pick a model, know it's a rule not truth |
| Allocate budget across channels (privacy-safe) | MMM |
| Per-touch/creative detail | MTA (where tracking still exists) |
| What spend *actually caused* sales | Incrementality experiment (the only causal answer) |

---

## Common Confusion Points

### "ROAS is profit"

ROAS is *revenue* per ad dollar. Profit requires subtracting COGS (break-even ROAS
= 1/gross margin) and the ad cost itself. A 3x ROAS on a 30% margin loses money.
Never read ROAS as profitability without the margin.

### "Blended CAC tells us if acquisition is healthy"

Blended CAC divides by *all* new customers, including organic — so strong organic
growth can hide an unprofitable paid channel. Look at *paid* CAC and *marginal* CAC
(cost of the next customer), which rises as you scale and exhaust cheap audiences.

### "High LTV:CAC means spend freely"

You also need the **payback period**. A great LTV:CAC with a long payback consumes
cash faster than it returns it and can bankrupt a growing company. LTV:CAC is
lifetime return; payback is cash speed. Both must be healthy.

### "Our attribution model tells us the true channel contribution"

Every attribution model is an *assumption* that divides a fixed credit by a rule
(last-touch, linear, U-shaped). None observes the counterfactual. Two models give
two different "truths" from identical data. For real causal credit, run an
incrementality test.

### "MTA is more rigorous than MMM because it's user-level"

Granular is not the same as causal. Both MMM and MTA are correlational; MTA's
granularity comes with heavy dependence on cross-site tracking that is being
deprecated (`08`). The causal method is experiments. Granularity buys detail, not
truth.

### "Lower churn and higher acquisition are equally good for growth"

Because lifetime = 1/churn, reducing churn is *nonlinear* — halving churn doubles
lifetime and LTV, and compounds across the whole base, while acquisition adds
linearly and re-incurs CAC each time. For most subscription businesses, retention
is the higher-leverage growth lever. The cohort curve flattening is the metric to
watch.

### "We measured a lift, so the campaign worked"

A lift versus your own past is confounded by seasonality, price, and everything
else that changed. A lift versus a *randomized holdout* (incrementality) is causal.
The discipline is the same as not trusting a before/after deploy comparison without
a control — hold out a group and measure the difference.
