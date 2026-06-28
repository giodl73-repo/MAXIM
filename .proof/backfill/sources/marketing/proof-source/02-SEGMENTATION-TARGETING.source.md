---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-SEGMENTATION-TARGETING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:marketing:segmentation-targeting
kind: guide
module: marketing
section: marketing
title: Segmentation, Targeting, and Positioning
status: source-custody
source_custody: partial
current_path: marketing/02-SEGMENTATION-TARGETING.md
canonical_path: marketing/02-SEGMENTATION-TARGETING.md
backsource_ids: [proof-backfill:marketing:02-segmentation-targeting, git-history:marketing:02-segmentation-targeting]
concepts: [segmentation, targeting, positioning, STP, perceptual map, value proposition]
root_concepts: [segmentation, positioning]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# Segmentation, Targeting, and Positioning (STP)

## The Big Picture

STP is the **strategy spine** of marketing: divide the market, choose whom to
serve, and decide how to be perceived. Everything in the mix (`04`-`06`) is
downstream of these three choices. The landscape, left to right:

```
+-------------------------------------------------------------------------+
|                            STP PIPELINE                                 |
|                                                                         |
|  1. SEGMENTATION       2. TARGETING          3. POSITIONING             |
|  ---------------       ------------          --------------             |
|  one heterogeneous     of the segments,      for the chosen target,     |
|  market                pick which to serve   define a distinct place    |
|        |                      |               in their mind             |
|        v                      v                     |                   |
|  .----------.          .----------.                 v                   |
|  | seg A    |  score   | seg A *  | <-pick   .--------------------.     |
|  | seg B    |  each on | seg B    |          | "For [target] who  |     |
|  | seg C    | -attract | seg C *  | <-pick   |  [need], [brand]   |     |
|  | seg D    | -fit     | seg D    |          |  is the [category] |     |
|  '----------'          '----------'          |  that [benefit],   |     |
|                                              |  because [reason]" |     |
|  DIVIDE                CHOOSE                 '--------------------'    |
|                                              DIFFERENTIATE              |
+-------------------------------------------------------------------------+
```

**Read left-to-right**: segmentation is *analysis* (carve up reality), targeting
is *a decision* (where to spend), positioning is *a design* (the claim you make
and must deliver). The bridge: this is workload sharding (segment), capacity
allocation (target), and a service contract / SLA differentiated from competitors
(position).

---

## Step 1: Segmentation — Bases for Dividing a Market

Segmentation groups buyers who respond similarly to a given marketing mix. The
art is choosing the **basis** — the variable(s) you cut on. Four families,
roughly in order of how *actionable* vs how *deep* they are.

```
+-----------------------------------------------------------------+
|                  SEGMENTATION BASES                             |
|                                                                 |
|  DEMOGRAPHIC      age, income, gender, education, occupation,   |
|  (easy to        family size. Easy to measure + target.         |
|   measure)       Weak link to actual wants.                     |
|       |                                                         |
|  GEOGRAPHIC      region, climate, urban/rural, country.         |
|       |          Combines with demo -> "geodemographic".        |
|       |                                                         |
|  PSYCHOGRAPHIC   lifestyle, values, personality, attitudes.     |
|       |          Stronger link to wants. Harder to measure.     |
|       |          (e.g. VALS framework.)                         |
|       |                                                         |
|  BEHAVIORAL      usage rate, occasion, benefits sought,         |
|  (closest to     loyalty status, readiness. Often the BEST      |
|   the money)     predictor of response. Needs data.             |
+-----------------------------------------------------------------+
```

| Basis family | Example variables | Strength | Weakness |
|---|---|---|---|
| **Demographic** | Age, income, gender | Easy to measure, easy to buy media against | Weakly predicts wants |
| **Geographic** | Region, climate, density | Operationally simple, logistics-aligned | Coarse |
| **Psychographic** | Lifestyle, values (VALS), personality | Predicts wants and message resonance | Hard to measure/buy |
| **Behavioral** | Usage rate, benefits sought, loyalty, occasion | Best predictor of *response* | Needs usage data |

**Benefit segmentation** (a behavioral cut on "what benefit do you seek") and
**usage-rate segmentation** (the 80/20 / heavy-user rule) are the two that most
directly tie to revenue. The "heavy half" — often ~20% of buyers driving ~80% of
volume — is frequently the real target.

### What makes a segment *useful* (the criteria)

A segment you can act on must pass five tests (Kotler):

```
  MEASURABLE     can you size and describe it?
  SUBSTANTIAL    is it big/profitable enough to serve?
  ACCESSIBLE     can you reach it with media + channels?
  DIFFERENTIABLE  does it respond DIFFERENTLY from other segments?
  ACTIONABLE     can you actually design a mix for it?
```

If two "segments" respond identically to your mix, they are not two segments —
they are one. Differentiability is the test most often failed.

```
OLD WORLD                          SEGMENTATION ANALOG
-----------------------------      -------------------------------------
Clustering / cohort analysis       Behavioral segmentation
Sharding a workload by key         Choosing a segmentation basis
"Is this partition meaningful?"    Differentiable + substantial criteria
Feature flags by user cohort       Targeting different mixes per segment
```

---

## Step 2: Targeting — Choosing Whom to Serve

Score each segment on **attractiveness** (size, growth, profitability,
competitive intensity) x **fit** (does it match our strengths and objectives).
Then choose a *coverage strategy*.

```
+-----------------------------------------------------------------+
|                  TARGETING STRATEGIES                           |
|                                                                 |
|  UNDIFFERENTIATED   One mix for the whole market.               |
|  (mass)             Ignores segment differences. Cheap, but     |
|                     vulnerable to focused rivals.               |
|                                                                 |
|  DIFFERENTIATED     A separate mix per chosen segment.          |
|  (segmented)        Higher reach + share, higher cost.          |
|                     (e.g. an auto maker with many models.)      |
|                                                                 |
|  CONCENTRATED       One mix, one segment. Deep focus.           |
|  (niche)            Great for small firms; risk = all eggs,     |
|                     one basket.                                 |
|                                                                 |
|  MICRO /            Mix tailored to individuals or micro-       |
|  ONE-TO-ONE         segments. Enabled by data + digital.        |
|                     (personalization at scale.)                 |
+-----------------------------------------------------------------+
```

The **segment-attractiveness x company-fit grid** is the decision tool:

```
+-----------------------------------------------------------------+
|                       |  HIGH attract.   |  LOW attract.        |
|  ---------------------+------------------+--------------------  |
|  HIGH company fit     |  TARGET (core)   |  maybe (cash cow)    |
|  ---------------------+------------------+--------------------  |
|  LOW company fit      |  build / partner |  AVOID               |
|                       |  or skip         |                      |
+-----------------------------------------------------------------+
```

Targeting is a **portfolio capital-allocation decision**: finite budget across
segments with different expected returns. The same logic as allocating headcount
across bets — concentrate where attractiveness *and* fit are both high; avoid
the bottom-right.

---

## Step 3: Positioning — Owning a Place in the Mind

**Positioning** (Ries & Trout) is the distinct, valued place your offering
occupies in the target customer's mind *relative to alternatives*. It is not what
you do to the product — it is what you do to the *prospect's perception*.

### The positioning statement (the canonical template)

```
+-----------------------------------------------------------------+
|  POSITIONING STATEMENT TEMPLATE                                 |
|                                                                 |
|  For   [target segment]                                         |
|  who   [statement of need / opportunity],                       |
|  the   [brand]                                                  |
|  is a  [product category / frame of reference]                  |
|  that  [key benefit / point of difference],                     |
|  unlike [primary competitive alternative],                      |
|  because [reason to believe / proof].                           |
+-----------------------------------------------------------------+
```

Three of these clauses are load-bearing:

| Clause | Name | Why it matters |
|---|---|---|
| "...is a [category]" | **Frame of reference** | Sets the competitors you're compared against |
| "...that [benefit]" | **Point of difference (POD)** | Why choose you over the frame |
| (implicit) must-haves | **Points of parity (POP)** | Table-stakes you must match to be in the frame |

**Points of parity vs points of difference** is the most useful distinction. POPs
are what you must have to be *considered at all* (a CRM must store contacts); PODs
are why you *win* (it auto-enriches them). Neglecting POPs is the classic failure
— a brilliant POD on a product that fails table stakes still loses.

---

## Perceptual Maps

A **perceptual map** plots brands in a space of the two attributes customers care
about most. It reveals crowding, gaps (open positions), and your move.

```
+-----------------------------------------------------------------+
|                  PERCEPTUAL MAP (illustrative)                  |
|                                                                 |
|                      HIGH PRICE                                 |
|                          |                                      |
|            Brand-L  o    |    o  Brand-P                        |
|         (luxury,         |       (premium,                      |
|          niche)          |        broad)                        |
|                          |                                      |
|  SIMPLE -----------------+------------------ FEATURE-RICH       |
|                          |                                      |
|            Brand-V  o    |        . . . . . . <- OPEN GAP       |
|         (value,          |        (rich + cheap:                |
|          basic)          |         unoccupied)                  |
|                          |    o  Brand-M                        |
|                      LOW PRICE                                  |
|                                                                 |
|  The dotted gap is a candidate position: feature-rich but       |
|  affordable. Is it empty because it's an opportunity, or        |
|  because it's economically impossible? That is the question.    |
+-----------------------------------------------------------------+
```

Perceptual maps are usually built empirically — from survey ratings reduced by
**multidimensional scaling (MDS)** or factor analysis, or derived from **conjoint**
(`07`). The axes are the *customer's* salient dimensions, not yours. An "empty"
quadrant is a hypothesis to test, not a guaranteed opportunity — it may be empty
because no one wants it or because it can't be delivered profitably.

```
OLD WORLD                          PERCEPTUAL MAP ANALOG
-----------------------------      -------------------------------------
2D projection of a feature space   2D map of brands on key attributes
Dimensionality reduction (PCA)     MDS / factor analysis on ratings
Finding an underserved partition   Finding an open positioning gap
Differentiated API contract        Differentiated brand position
```

---

## Differentiation: The Basis of a Defensible Position

A position must rest on a real **differentiator**. Sources (Kotler/Treacy-Wiersema):

| Differentiation source | What it competes on | Risk |
|---|---|---|
| **Product** | Features, performance, design, durability | Copyable; feature wars |
| **Service** | Support, delivery, ease, onboarding | Costly to sustain |
| **Channel** | Coverage, convenience, expertise | Channel power shifts |
| **People** | Skill, culture of the staff | Hard to scale |
| **Image/brand** | Perception, status, trust | Slow to build, fragile |
| **Price/operations** | Lowest cost (operational excellence) | Margin compression |

The three classic **value disciplines** (Treacy & Wiersema): *operational
excellence* (best total cost), *product leadership* (best product), *customer
intimacy* (best total solution). Pick one to lead on; be merely competent on the
others. Trying to lead on all three is the position that fails — it is Porter's
"stuck in the middle."

---

## Decision Cheat Sheet

| I want to... | Do this |
|---|---|
| Decide how to cut the market | Test bases against the 5 criteria; prefer behavioral if data exists |
| Find the segment that drives revenue | Usage-rate (heavy-half) + benefit segmentation |
| Choose which segments to serve | Score attractiveness x fit; pick high/high, avoid low/low |
| Decide mass vs niche | Undifferentiated if scale > segment value; concentrated if focused/small |
| Write a positioning statement | Use the For/who/is-a/that/unlike/because template |
| Avoid losing on table stakes | Map points of parity *before* pushing your point of difference |
| Find an open position | Build a perceptual map; test whether the gap is opportunity or void |
| Pick a basis to differentiate on | Choose ONE value discipline; be competent on the rest |

---

## Common Confusion Points

### "Segmentation and targeting are the same step"

Segmentation is *analysis* — it produces groups regardless of your intent.
Targeting is a *decision* — which of those groups gets your money. You can
segment a market 100 ways; you target a handful.

### "More, finer segments are always better"

Finer segmentation raises cost (separate mixes, smaller media buys, more SKUs)
and can split a market below the *substantial* threshold. Segment until the
incremental response gain stops paying for the incremental cost — the same
diminishing-returns calculus as over-sharding a system.

### "Positioning is a tagline"

A tagline *expresses* a position; the position is the strategic choice of frame,
POD, and POP. You can have a great tagline on no position (and you'll be
forgettable) — or a strong position with a mediocre tagline (and you'll still win
the consideration set).

### "An empty quadrant on the map is automatically an opportunity"

Maybe — or it may be empty because customers don't want that combination, or it's
not deliverable at a profit. The gap is a *hypothesis*; validate demand (`07`)
before you build to fill it.

### "We can be all three value disciplines"

You can't lead on all three; resources and operating models conflict (lowest-cost
operations vs high-touch customer intimacy pull opposite directions). Lead on one,
hold parity on the rest. This *is* Porter's generic-strategy warning against being
stuck in the middle.

### "Points of difference are what matter; parity is boring"

Parity points are *gating* — fail them and your brilliant differentiator never
gets evaluated, because you're not in the frame of reference. Secure parity
first, then differentiate.
