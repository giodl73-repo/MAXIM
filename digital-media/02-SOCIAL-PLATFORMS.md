# Social Media Platforms: Architecture, Algorithm, Feed Design, Network Effects

## The Big Picture

```
SOCIAL PLATFORM ARCHITECTURE TAXONOMY
=======================================

BY GRAPH STRUCTURE:
+------------------------------------------------------------------+
|  BROADCAST ASYMMETRIC       SOCIAL GRAPH SYMMETRIC              |
|  (Twitter/X, Substack)      (Facebook, LinkedIn)                |
|                                                                  |
|  A -> B (one way)            A <-> B (mutual)                    |
|  Follower != following        Friend = bidirectional             |
|  Public by default            Privacy controls important         |
|  Designed for:               Designed for:                      |
|    publishing to audience      maintaining relationships         |
|                                                                  |
|  INTEREST GRAPH               EPHEMERAL                          |
|  (TikTok, YouTube)            (Snapchat, Stories)               |
|                                                                  |
|  No social graph needed        Content disappears                |
|  Platform infers interests      Reduces permanence anxiety        |
|  from behavior                 Designed for:                    |
|  Designed for:                  casual, frequent posting         |
|    content discovery                                             |
+------------------------------------------------------------------+

HYBRID: Most platforms combine these
  Instagram: social graph (mutual) + interest graph (Explore)
  LinkedIn: social graph + broadcast (following) + interest graph
  Reddit: anonymous interest graph + community social
```

---

## Feed Algorithm Anatomy

The feed algorithm is the central mechanism of every social platform. It determines what content users see and in what order.

### Signal Types

```
FEED RANKING SIGNALS
=====================

ENGAGEMENT SIGNALS (user behavior on content):
  Positive:
    Watch time / read time        <- highest weight (most honest)
    Shares / reposts              <- strong intent signal
    Saves / bookmarks             <- high intent
    Clicks                        <- medium intent
    Likes / reactions             <- low intent (cheap to produce)
    Comments                      <- mixed (negative comments exist)

  Negative:
    "Not interested in this"      <- explicit negative signal
    Hide post / block creator     <- strong negative
    Skip quickly / scroll past    <- implicit negative
    Report                        <- very strong negative

RELATIONSHIP SIGNALS:
  How often do you interact with this poster?
  Do you have a close relationship? (mutual follows, DMs)
  Do you always read this person's content?

CONTENT SIGNALS:
  Post format (video vs. image vs. text)
  Topical category (platform may favor certain topics)
  Recency (how new is the post?)
  Velocity (how fast is it accumulating engagement?)

ACCOUNT SIGNALS:
  Creator's historical performance
  Account type (personal vs. page vs. brand)
  Advertiser status (pays for promotion)
```

### Platform-Specific Weighting

```
PLATFORM ALGORITHM PRIORITIES (approximate, documented)
========================================================

TWITTER/X (chronological + algorithmic):
  Original: purely chronological
  2022-2023: algorithmic "For You" feed default
  Signals: replies, reposts, likes, but also:
    "content you engage with in first 30 min of day"
    topic/interest inference
  Elon Musk era: subscription tier (X Premium) gets
    algorithmic boost -> pay-to-rank for some signals

FACEBOOK (social graph + engagement):
  Weight: friends and family content > pages > ads
  "Meaningful interactions": comments and shares
    outrank passive likes
  Video: longer watch time heavily weighted
  Controversy: engagement-optimized news feed was
    found to increase political polarization
    (internal research leaked 2021)

TIKTOK (interest graph, no social required):
  New user: immediate interest graph inference
  Each video: shown to a small cohort; if engagement high,
    shown to larger cohort (pool expansion model)
  Watch time: primary signal; watch 100% = strong positive
  "Completion rate" = watches to end without skipping
  NO social graph required to see popular content
  -> Most powerful discovery algorithm currently available

INSTAGRAM:
  Feed: social graph (friends, following)
  Explore: interest graph (algorithmic discovery)
  Reels: TikTok-style interest graph
  Two separate algorithms within one app
```

---

## Virality Mechanics

```
VIRALITY MODEL
===============

BASIC REPRODUCTION NUMBER (R0 analogy):
  If each piece of content gets shared by >1 person on average,
  it can spread exponentially (viral)
  If <1, it decays
  R0 > 1 = viral potential; R0 < 1 = organic decay

VIRALITY FACTORS:
  1. EMOTIONAL RESONANCE:
     Strong emotion (anger, awe, fear, amusement)
     drives sharing behavior
     Jonah Berger (Contagious, 2013): STEPPS framework
       Social currency (makes sharer look good)
       Triggers (environmental cues that prompt recall)
       Emotion (high-arousal emotions, not low-arousal)
       Public (visible social proof)
       Practical value (useful to recipient)
       Stories (narrative container)

  2. NETWORK POSITION:
     Content shared by high-degree nodes (influencers)
     reaches more users per share
     One share from an account with 1M followers =
     1,000 shares from accounts with 1,000 followers

  3. FRICTION:
     Platforms that minimize sharing friction
     (one-tap retweet vs. multi-step) increase volume
     Twitter's RT button increased sharing 10x over quote-tweet

  4. ALGORITHM AMPLIFICATION:
     Platform algorithms detect early engagement velocity
     and amplify content that is gaining momentum
     This creates winner-take-all dynamics:
     trending content gets exponentially more distribution
```

---

## Network Effects

```
NETWORK EFFECTS TAXONOMY
=========================

DIRECT NETWORK EFFECTS:
  Value to each user increases as total users increase
  Classic example: telephone (worthless if only one person has one)
  Social platforms: more friends -> more reason to join
  Formula: Metcalfe's Law: value ~ n^2 (pairs of users)
  This is why dominant platforms are almost impossible to displace:
    each marginal user makes the platform MORE valuable for all others

INDIRECT NETWORK EFFECTS:
  Value increases because of complementary users
  Platform + two distinct user groups (two-sided market)
  eBay: more sellers -> more buyers -> more sellers
  Facebook: more users -> more advertisers -> better ad product -> more users
  Social platforms: users + advertisers as two sides

DATA NETWORK EFFECTS:
  More users -> more data -> better algorithm -> better product -> more users
  TikTok: more watch-time data -> better recommendation -> longer sessions
  Google: more searches -> better search -> more searches
  This is a harder-to-replicate moat than pure social graph

SAME-SIDE vs. CROSS-SIDE:
  Same-side: more sellers -> better for buyers (only)
  Cross-side: more of one type benefits the other type
  Social platforms: same-side primary (more friends = better)
  Also cross-side: more users = more advertiser revenue
```

---

## Platform Lock-In Mechanisms

```
LOCK-IN STRATEGIES
===================

SOCIAL GRAPH LOCK-IN:
  Your followers are on this platform
  Moving to another platform means losing them (unless they follow)
  The cost of switching = the cost of rebuilding your audience

DATA PORTABILITY LIMITS:
  Platforms rarely offer complete data export
  Even with export, the data is not directly importable elsewhere
  Your posts, engagement history, connections: hard to transfer
  This is a deliberate anti-competitive design choice

IDENTITY LOCK-IN:
  Your username, handle, and URL are platform-specific
  @username on Twitter ≠ @username on Mastodon
  Brands have invested in platform-specific identities

CONTENT FORMAT LOCK-IN:
  Platform-native formats (Stories, Reels, Spaces) don't transfer
  Algorithmic advantage for native formats discourages export

HABIT LOCK-IN:
  Users return to where they already have established routines
  The default is the existing platform; switching requires effort

REGULATORY RESPONSE:
  EU Digital Markets Act (DMA, 2023):
    Designated "gatekeepers" must allow data portability
    Must allow interoperability with third-party services
    First enforcement: Apple, Google, Meta, Amazon, Microsoft
  ActivityPub (open standard): attempts to solve social graph lock-in
    (Mastodon, Pixelfed, PeerTube use this)
```

---

## Moderation at Scale

```
CONTENT MODERATION SYSTEMS
============================

SCALE PROBLEM:
  Facebook: ~100 billion pieces of content per day
  YouTube: 500 hours of video uploaded per minute
  Human review at this scale: impossible for all content
  -> Hybrid: automated + human

AUTOMATED MODERATION:
  Hash-based: PhotoDNA (Microsoft) compares against database
    of known CSAM and terrorist content
    Exact match: high precision, cannot detect variations
  Perceptual hashing: near-match detection (slight crops, recolors)
  NLP classifiers: text classification for hate speech, spam
  Computer vision: image/video classifiers
  Velocity detection: detect coordinated inauthentic behavior

HUMAN REVIEW:
  Scale: ~40,000 contractors globally (Facebook/Meta estimate)
  Regions: mostly outsourced to lower-cost markets (Philippines, Kenya)
  Workflow: automated system flags -> human reviews -> decision
  Psychological cost: significant; moderators exposed to extreme content
  Labor issues: TIME investigation (2023) documented Facebook Kenya
    contractors (Sama) earning <$2/hr reviewing torture, murder, rape

POLICY CHALLENGES:
  Satire vs. harassment (context required)
  Political speech (legitimate debate vs. incitement)
  Medical misinformation (consensus vs. debate)
  Geographic variation (what is legal speech varies by country)
  The "Streisand effect": banning content amplifies it

EFFECTIVENESS:
  Proactive detection (before reports): improving with AI
  False positive rate: 10-15% for automated systems
  Appeals: most platforms have review; most users don't appeal
  Adversarial evolution: bad actors adapt to detection methods
```

---

## Decision Cheat Sheet

| Platform | Graph type | Algorithm priority | Content type |
|----------|-----------|-------------------|--------------|
| Twitter/X | Broadcast asymmetric | Engagement velocity | Text + images |
| Facebook | Social graph | Meaningful interactions (comments) | Mixed |
| TikTok | Interest graph | Watch time / completion | Short video |
| Instagram | Social + interest (Explore) | Engagement + time | Image + video |
| LinkedIn | Professional social | Relevance + engagement | Professional |
| YouTube | Interest graph | Watch time | Long + short video |
| Reddit | Anonymous interest communities | Upvotes + community rules | Text + links |

| Concept | Meaning |
|---------|---------|
| Direct network effect | More users -> more valuable to each user |
| Indirect network effect | Two-sided market: each side benefits from the other |
| Data network effect | More data -> better algorithm -> more users |
| R0 > 1 | Viral: each post gets >1 share on average |
| Filter bubble | Algorithmic personalization reduces diverse info exposure |

---

## Common Confusion Points

**TikTok's algorithm does not primarily use your social graph.** It infers interests from watch behavior. A new account with no followers can see viral content immediately. This is fundamentally different from Facebook's friend-graph model.

**Engagement rate and reach are different.** Engagement rate = interactions / impressions. Reach = total unique users who saw the content. A post can have low reach but high engagement rate (small but engaged audience) or high reach and low engagement rate (broad but uninterested audience).

**Platform algorithms do not favor organic content out of altruism.** They favor content that keeps users on the platform longer. If that is organic content, organic wins. When paid content keeps users longer (or organic content is throttled to drive advertising), the algorithm reflects that.

**Lock-in is structural, not accidental.** Social platforms are designed to make leaving expensive. The social graph portability gap is not a technical limitation — it is a business decision.

**Moderation at scale is a labor problem, not just a technology problem.** Automated systems handle volume; human judgment handles nuance. The hidden human cost of content moderation is a significant ethical issue in the industry.
