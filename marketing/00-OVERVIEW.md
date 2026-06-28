---
maxim_schema: maxim.frontmatter.v1
id: maxim:marketing:overview
kind: guide
module: marketing
section: marketing
title: Marketing - Landscape Overview
status: source-custody
source_custody: partial
current_path: marketing/00-OVERVIEW.md
canonical_path: marketing/00-OVERVIEW.md
backsource_ids: [proof-backfill:marketing:00-overview, git-history:marketing:00-overview]
concepts: [marketing concept, marketing mix, 4 Ps, 7 Ps, STP, marketing funnel, AARRR]
root_concepts: [marketing]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Marketing — Landscape Overview

## The Big Picture

Marketing is one discipline pretending to be a dozen. The confusion is that
"marketing" names the *whole strategy* (who do we serve, how do we win) and a
*specific function* (the ads, the email, the website) at the same time. The
landscape below is the whole stack, top to bottom: from a market down to a
single tracked conversion.

```
+-------------------------------------------------------------------------+
|                        THE MARKETING STACK                              |
|                                                                         |
|  STRATEGY      Who do we serve, and how do we win?                      |
|  --------      market definition, segmentation, targeting, positioning  |
|       |        (borrows competitive analysis from strategy/economics)   |
|       v                                                                 |
|  THE MIX       The controllable levers (the "4 Ps", extended to 7)      |
|  -------        .---------. .---------. .---------. .-----------.       |
|                 | PRODUCT | |  PRICE  | |  PLACE  | | PROMOTION |       |
|                 '---------' '---------' '---------' '-----------'       |
|                 | what it | | what    | | where   | | how they  |       |
|                 | is/does | | costs   | | to buy  | | hear/buy  |       |
|                 '---------' '---------' '---------' '-----------'       |
|       |                                                                 |
|       v                                                                 |
|  EXECUTION     Campaigns, channels, creative, content, media buys       |
|  ---------     the day-to-day surface customers actually touch          |
|       |                                                                 |
|       v                                                                 |
|  MEASUREMENT   Did it work, and did it pay?                             |
|  -----------   funnels, CAC, LTV, ROAS, attribution, incrementality     |
+-------------------------------------------------------------------------+
```

**Read this top-down**: strategy decides *who and how*; the mix decides *what
levers*; execution *pulls the levers*; measurement *closes the loop*. Each layer
constrains the one below it. A brilliant ad (execution) for the wrong segment
(strategy) loses money — measurably.

This guide is the map. Each numbered guide drills into one layer.

---

## The Marketing Concept (and what it replaced)

The single most important idea in modern marketing is also the oldest debate:
*what orients the firm?* The field evolved through distinct orientations.

```
PRODUCTION ERA   "Make it cheap and available. Demand exceeds supply."
   |             Henry Ford: any color, as long as it's black.
   v
PRODUCT ERA      "Build the best product; customers will find it."
   |             Trap: the better-mousetrap fallacy.
   v
SELLING ERA      "We have inventory; push hard to move it."
   |             Marketing == aggressive sales + advertising.
   v
MARKETING ERA    "Start from the customer's need, work backward."
   |             Sense a need, design to it, deliver value profitably.
   v
SOCIETAL /       "Customer need + firm profit + societal well-being."
HOLISTIC ERA     Sustainability, ethics, long-term relationship value.
```

The **marketing concept** is the marketing-era idea: the firm achieves its goals
by being *more effective than competitors at creating, delivering, and
communicating customer value* to a chosen target market. The shift is from
**inside-out** (we have a thing, sell it) to **outside-in** (a customer has a
need, serve it).

```
OLD WORLD (you may recognize)        NEW FRAME
------------------------------       ----------------------------------------
"Ship the feature, then market it"   Market sizing/segment first, then build
Engineering-led roadmap              Customer-problem-led roadmap
"Build it and they will come"        Product-market fit is earned, measured
Sales pipeline = the funnel          Marketing owns the top of that funnel
```

If you have run a large engineering org, the bridge is exact: the marketing
concept is *requirements gathering with the whole market as the user*, plus a
profit constraint. Outside-in is the same instinct that says "don't build the
API the team finds elegant; build the one customers integrate."

---

## The Marketing Mix: 4 Ps and 7 Ps

The **marketing mix** is the set of controllable, tactical levers the firm
combines to produce the desired response in the target market. McCarthy's (1960)
**4 Ps** is the canonical taxonomy. Booms & Bitner (1981) extended it to **7 Ps**
for services, where the offering is intangible and produced/consumed at once.

| P | Question it answers | Examples of decisions |
|---|---|---|
| **Product** | What is the offering? | Features, quality, design, brand, packaging, service |
| **Price** | What does the customer give up? | List price, discounts, financing, tiers, elasticity |
| **Place** | Where/how do they get it? | Channels, coverage, logistics, retail vs direct |
| **Promotion** | How do they learn and get persuaded? | Advertising, sales, PR, digital, content |
| **People** *(7P)* | Who delivers it? | Staff, training, customer-facing skill (services) |
| **Process** *(7P)* | How is it delivered? | Service flow, queues, self-serve, onboarding |
| **Physical evidence** *(7P)* | What tangible cues signal quality? | Storefront, UI, packaging, documentation |

```
+------------------------------------------------------------------+
|  4 Ps = FIRM'S VIEW          4 Cs = CUSTOMER'S VIEW (Lauterborn) |
|  ------------------          ----------------------------------- |
|  Product            <----->  Customer solution / need            |
|  Price              <----->  Cost to the customer (total)        |
|  Place              <----->  Convenience of access               |
|  Promotion          <----->  Communication (two-way)             |
|                                                                  |
|  Same four levers, restated outside-in. The 4 Cs is the          |
|  marketing concept applied to the mix itself.                    |
+------------------------------------------------------------------+
```

Note: **for software/SaaS, the 7 Ps fit better than the 4 Ps.** Your "product" is
intangible, delivery *is* the experience (Process), the support org *is* part of
the product (People), and the UI/docs are the Physical evidence. A pure-goods
4 P frame under-describes a platform business.

---

## STP: Segmentation, Targeting, Positioning

Before you touch the mix, strategy answers three sequential questions. **STP** is
the spine of marketing strategy — covered in depth in `02-SEGMENTATION-TARGETING.md`.

```
+-----------------------------------------------------------------+
|                   STP: THE STRATEGY SEQUENCE                    |
|                                                                 |
|  1. SEGMENTATION    Divide the heterogeneous market into        |
|     ------------    homogeneous subgroups.                      |
|     "Not everyone is the same customer."                        |
|              |                                                  |
|              v                                                  |
|  2. TARGETING       Choose which segment(s) to serve, by        |
|     ---------       attractiveness x fit with our strengths.    |
|     "We cannot profitably serve everyone."                      |
|              |                                                  |
|              v                                                  |
|  3. POSITIONING     Decide the distinct place we occupy in      |
|     -----------     the target's mind, vs alternatives.         |
|     "Why us, in one sentence they'd repeat."                    |
+-----------------------------------------------------------------+
```

STP is **divide -> choose -> differentiate**. It is the strategy layer; the mix is
the tactics that *deliver* the chosen positioning. The bridge: this is sharding
a workload (segmentation), choosing which shards to optimize for (targeting), and
defining your service's contract/SLA vs competitors (positioning).

---

## The Funnel (and AARRR)

The **marketing/purchase funnel** models the customer's journey as a narrowing
sequence of stages, with drop-off at each. The classic hierarchy-of-effects
funnel and the growth-oriented **AARRR** ("pirate metrics", Dave McClure, 2007)
are two framings of the same pipeline.

```
+-----------------------------------------------------------------+
|  CLASSIC FUNNEL              AARRR (growth / SaaS)              |
|  --------------              ----------------------             |
|                                                                 |
|   AWARENESS                   ACQUISITION   how they arrive     |
|      \      (do they know)        |                             |
|   INTEREST                    ACTIVATION    first "aha" value   |
|      \      (do they care)        |                             |
|   DESIRE                      RETENTION     do they come back   |
|      \      (do they want)        |                             |
|   ACTION                      REVENUE       do they pay         |
|      \      (do they buy)         |                             |
|   [LOYALTY]                   REFERRAL      do they tell others |
|                                                                 |
|  Each stage is a CONVERSION RATE. The funnel is a pipeline      |
|  with per-stage yield. Multiply stages -> end-to-end yield.     |
+-----------------------------------------------------------------+
```

**This is a data pipeline with stage-level yield, exactly like a distributed
job.** If 100k see an ad, 10% click (10k), 20% sign up (2k), 15% activate (300),
40% pay (120), your end-to-end conversion is 0.12%. Optimizing the funnel is
optimizing the *bottleneck stage* — the same throughput logic as queueing
theory. Cohort and funnel analysis (in `09-METRICS-AND-ANALYTICS.md`) are the
instrumentation.

```
OLD WORLD                          MARKETING FUNNEL
-----------------------------      -------------------------------------
Request pipeline / middleware      Awareness -> ... -> Action stages
Per-stage error/drop rate          Per-stage conversion rate
Bottleneck = slowest stage         Bottleneck = lowest-converting stage
Cohort of requests over time       Cohort of users by acquisition date
A/B flag rollout                   A/B test of a funnel-stage change
```

---

## How Marketing Connects to Neighboring Fields

Marketing imports heavily. It does not re-derive these — it applies them.

```
+-----------------------------------------------------------------+
|                  WHAT MARKETING BORROWS                         |
|                                                                 |
|  economics/          ---> demand curves, price elasticity,      |
|                           market structure, consumer surplus    |
|                                                                 |
|  behavioral-         ---> framing, loss aversion, anchoring,    |
|  economics/               defaults/nudges, mental accounting    |
|                                                                 |
|  statistics-         ---> sampling, hypothesis tests, A/B       |
|  applied/                 design, regression, conjoint          |
|                                                                 |
|  media-studies/      ---> media effects, attention, reach,      |
|                           two-step flow, framing in messages    |
|                                                                 |
|  organizational-     ---> strategy (5 forces, positioning),     |
|  behavior/                change management, org alignment      |
+-----------------------------------------------------------------+
```

| Question | Field that owns the theory | Marketing's job |
|---|---|---|
| Why does demand fall as price rises? | `economics/` | Pick the profit-max price |
| Why do defaults change behavior? | `behavioral-economics/` | Design the default that converts |
| Is this A/B lift real? | `statistics-applied/` | Run the test, ship the winner |
| How do five forces shape rivalry? | strategy (`organizational-behavior/05`) | Position to avoid the worst force |

A useful framing: **economics and behavioral economics give marketing its model
of the customer; statistics gives it its method; strategy gives it its game
board.** Marketing is the discipline that *acts* on all three to move a real
buyer.

---

## Porter's Five Forces vs the Marketing Mix

A frequent confusion: people treat Porter's **Five Forces** and the marketing
**mix** as competing frameworks. They operate at different altitudes and answer
different questions.

```
+-----------------------------------------------------------------+
|  FIVE FORCES (Porter)            MARKETING MIX (McCarthy)       |
|  --------------------            -----------------------        |
|  ALTITUDE: industry              ALTITUDE: the firm's offer     |
|  ASKS: is this industry          ASKS: given we compete here,   |
|    structurally attractive?        how do we configure our      |
|                                    offer to win customers?      |
|                                                                 |
|  The five forces:                The four levers:               |
|   - Rivalry among competitors     - Product                     |
|   - Threat of new entrants        - Price                       |
|   - Threat of substitutes         - Place                       |
|   - Buyer power                   - Promotion                   |
|   - Supplier power                                              |
|                                                                 |
|  OUTPUT: where to play +         OUTPUT: how to configure the   |
|  how much profit pool exists      offer in the chosen arena     |
+-----------------------------------------------------------------+
```

Five Forces is a **strategy/industry-analysis** tool (it lives more naturally in
`organizational-behavior/05-STRATEGY.md` and `economics/` on market structure).
The marketing mix is a **tactical configuration** tool. Use Five Forces to decide
*whether and where* to compete; use STP to decide *whom*; use the mix to decide
*how*. They stack, they do not compete.

---

## Decision Cheat Sheet

| I want to... | Use / read |
|---|---|
| Decide which markets are worth entering | Five Forces (strategy) + market sizing |
| Decide whom to serve and how to be seen | STP — `02-SEGMENTATION-TARGETING.md` |
| Understand why a customer buys (or doesn't) | `01-CONSUMER-BEHAVIOR.md` + `behavioral-economics/` |
| Configure the offer (the levers) | The mix: `04`, `05`, `06` |
| Set a price | `04-PRODUCT-AND-PRICE.md` (+ elasticity from `economics/`) |
| Build a brand that compounds | `03-BRANDING.md` |
| Reach and persuade at scale | `05-ADVERTISING-AND-PROMOTION.md`, `08-DIGITAL-MARKETING.md` |
| Get the product to buyers | `06-CHANNELS-AND-DISTRIBUTION.md` |
| Learn what's actually true | `07-MARKET-RESEARCH.md` (+ `statistics-applied/`) |
| Know if it paid | `09-METRICS-AND-ANALYTICS.md` |

---

## Common Confusion Points

### "Marketing is just advertising/the brand team"

Advertising is one element (Promotion) of one layer (Execution). The strategy
layer — who we serve, how we win, what we charge — is where most of the value and
most of the failures live. Calling marketing "the ads" is like calling
engineering "the deploys."

### "The 4 Ps are outdated"

The *labels* predate the internet; the *decisions* are timeless. Every business
still decides what the offering is, what it costs, where to get it, and how
people hear about it. Digital changed the tactics inside each P, not the
existence of the P. For services/software, reach for the 7 Ps.

### "STP and the funnel are the same thing"

STP is **strategy** (a one-time-ish choice of who/how, revisited periodically).
The funnel is **operations** (the ongoing flow of a chosen audience toward
purchase). STP decides whose funnel you are filling.

### "Marketing and sales are the same"

Marketing typically owns the top and middle of the funnel (awareness ->
consideration) and the strategy/positioning; sales owns the bottom (the close),
especially in B2B with high-touch deals. The handoff point (the "MQL -> SQL"
boundary) is a perennial org-design fight — and a measurement problem, covered in
`09`.

### "Strategy (Five Forces) and the mix are alternatives"

They are different altitudes. Five Forces analyzes the *industry*; the mix
configures *your offer*. You use both, in sequence: analyze the arena, choose the
segment, then configure the mix to win it.
