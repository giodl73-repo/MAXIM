# Misinformation: Viral Spread, Prebunking, Fact-Checking, Platform Policy

## The Big Picture

```
MISINFORMATION TAXONOMY
=========================

+------------------------------------------------------------------+
|  TAXONOMY (First Draft, Claire Wardle & Hossein Derakhshan)      |
|                                                                  |
|  DIS-INFORMATION:            False + intentional to harm         |
|  MIS-INFORMATION:            False + NOT intentional to harm     |
|  MAL-INFORMATION:            TRUE + intentional to harm          |
|                              (reveals private information;       |
|                               true dirt on political opponent)   |
|                                                                  |
|  INFORMATION DISORDER:                                           |
|  All three types, overlapping, creating:                         |
|  - Confusion (can't tell what's true)                            |
|  - Overabundance of information (firehose)                       |
|  - Deliberate weaponization of all three                         |
+------------------------------------------------------------------+

WHY THE TAXONOMY MATTERS FOR INTERVENTION:
  Misinformation: education + correction effective
  Disinformation: requires detecting intent + actor attribution
  Malinformation: source may be technically true; can't "fact-check"
  Different types require different platform policies
```

---

## Viral Spread Mechanics

### MIT Twitter Study: False News Spreads Faster

```
VOSOUGHI, ROY, ARAL (2018) — Science
======================================

"The Spread of True and False News Online"
  Authors: Soroush Vosoughi, Deb Roy, Sinan Aral (MIT)
  Data: all fact-checked Twitter content 2006-2017
        ~126,000 rumor cascades
        Verified claims from: Snopes, PolitiFact, FactCheck.org
        3 million accounts, 4.5 million tweets

KEY FINDING:
  False news spreads significantly faster, farther, deeper,
  and more broadly than true news
  FALSE news: 70% more likely to be retweeted than true
  TRUE news: takes 6x longer to reach 1,500 people
  FALSE news: reaches any depth of retweet cascade faster

WHAT CAUSED THE DIFFERENCE?:
  NOT bots (removing suspected bots from analysis
    didn't change results)
  NOT account age or follower count
  CAUSE: novelty + emotional content
    False news was more novel (by linguistic analysis)
    False news evoked more: fear, disgust, surprise
    True news evoked more: anticipation, joy, trust
    "People prefer to share content that makes them
     feel something strong, especially surprise and disgust"

SCOPE LIMITATION:
  Twitter data only; may not generalize to all platforms
  Fact-checked claims are not representative of all false claims
  (Fact-checkers select newsworthy, checkable claims)
```

---

## Why False Content Spreads

```
PSYCHOLOGICAL MECHANISMS OF MISINFORMATION SPREAD
===================================================

1. NOVELTY (the main driver per MIT study):
   Novel claims are more memorable and more shareable
   True news tends to be incrementally novel
   False news can be extremely novel (no factual constraint)
   Novelty activates curiosity + sharing instinct

2. EMOTIONAL AROUSAL:
   High-arousal emotions (fear, anger, disgust) drive sharing
   Low-arousal emotions (sadness, contentment) do not
   False news can optimize for emotional impact
   True news is constrained by what actually happened

3. IDENTITY PROTECTIVE COGNITION (Dan Kahan):
   People evaluate information for identity-consistency
   not for epistemic accuracy
   "Does this confirm my group's view of the world?"
   -> Share if yes; scrutinize if no
   -> Bypasses accuracy checking entirely

4. SOCIAL PROOF:
   High share count -> implies credibility
   "If 50,000 people shared this, it must be true"
   This is a standard social heuristic applied incorrectly

5. SOURCE BLINDNESS:
   On mobile/social: source is less visible
   Who wrote this? Where is it from?
   Users share based on content, not source assessment
   Priming users to think about accuracy before sharing
   reduces misinformation spread (Fazio 2020)

6. ALGORITHMIC AMPLIFICATION:
   High-engagement content gets boosted by algorithm
   Misinformation that generates anger = high engagement
   Platform economics reward what spreads misinformation
```

---

## Prebunking vs. Debunking

The evidence base for intervention:

```
DEBUNKING (correction after belief)
=====================================

Standard intervention: fact-check the false claim
  State the false claim -> state it is false -> provide correction

Problems:
  BACKFIRE EFFECT (early research, since disputed):
    Nyhan & Reifler (2010): corrections can STRENGTHEN
    false beliefs among those who hold them
    Subsequent research: backfire is rare, not universal
    But: corrections rarely fully correct; partial updating
         is more common

  REPEATED EXPOSURE PROBLEM:
    Stating the false claim before correcting it
    increases recognition and fluency of the false claim
    "Don't think of a pink elephant"
    Solution: "truth sandwich" format (McIntyre 2018):
      Lead with the truth; mention the false claim briefly;
      return to the truth (don't give the false claim prominence)

  REPETITION EFFECT:
    If you need to repeat the false claim to correct it,
    the correction must be repeated even more times
    The correction rarely travels as far as the original claim

PREBUNKING (inoculation before belief)
========================================

INOCULATION THEORY (McGuire 1964 -> Lewandowsky 2020+):
  Expose people to a weakened form of manipulation
  -> They build "antibodies" against the manipulation technique
  -> Subsequent exposure to full-strength manipulation is resisted

Medical analogy:
  Vaccine: weakened pathogen -> immune response -> resistance
  Inoculation: weakened manipulation -> cognitive awareness -> resistance

TECHNIQUE-BASED INOCULATION:
  Not content-specific ("global warming is real")
  but technique-specific ("they use the manufacturing doubt technique")
  Works across topics where the technique is used

Lewandowsky & van der Linden work:
  "Prebunking" outperforms debunking in experimental settings
  Users inoculated against: emotional manipulation, false experts,
    ad hominem, slippery slope, impossible expectations

Cambridge case study:
  "Bad News" online game (Guskin & Vraga; Cambridge):
    Players practice creating misinformation
    Learn the techniques by doing them
    Shown to reduce susceptibility to those techniques
  "Go Viral!" (Google partnership): COVID-specific prebunking
    YouTube pre-roll ads using prebunking technique
    Randomized control: reduced susceptibility to vaccine disinfo
```

---

## Fact-Checking Organizations and IFCN

```
FACT-CHECKING LANDSCAPE
========================

IFCN (International Fact-Checking Network, Poynter 2015):
  Establishes code of principles for fact-checkers
  Verification process for member organizations
  Signatories: ~100+ organizations in 50+ countries
  Code principles:
    1. Nonpartisanship and fairness
    2. Standards and transparency of sources
    3. Transparency of funding and organization
    4. Transparency of methodology
    5. Open and honest corrections policy

MAJOR ORGANIZATIONS:
  Snopes: US; general claims; founded 1994 (oldest)
  PolitiFact: US; political statements; Tampa Bay Times
  FactCheck.org: US; political claims; Annenberg
  Washington Post Fact Checker: "Pinocchios" scale
  AFP Fact Check: French news agency; global
  Full Fact: UK; nonpartisan
  Boom: India; local language fact-checking
  Verificado: Latin America; collaborative

FACT-CHECKING METHODS:
  Identify specific claim + source
  Determine verifiability (some claims are opinions, not facts)
  Find primary sources (original data, statements)
  Contact relevant experts
  Consult official data (government, academic)
  Rate the claim (typically: True/Mostly True/Mixed/Mostly False/False/Pants on Fire)
  Publish reasoning transparently (show work)

LIMITATIONS:
  Bandwidth: ~100 fact-checks per week per major organization
    vs. millions of false claims circulating
  Selection: fact-checkers choose the newsworthy claims
    -> not representative of what average user encounters
  Political influence: fact-checkers themselves become
    targets of "bias" accusations; partisan trust gap
```

---

## Platform Intervention Options

```
PLATFORM MISINFORMATION INTERVENTIONS
=======================================

CONTENT LABELS:
  "This claim is disputed by fact-checkers"
  "Visit [official source] for information about COVID vaccines"
  Evidence: reduces sharing marginally; doesn't change beliefs much
  Problem: "implied truth effect" -- unlabeled content
    seen as implicitly true by users expecting labels

REDUCED DISTRIBUTION:
  Don't remove but demote in algorithm
  Fewer people see it; doesn't create "martyrdom" narrative
  Used by: Facebook for "borderline" content
  Opacity problem: users don't know their content was demoted

FRICTION INSERTION:
  Before sharing: "This article is from 2018. Are you sure?"
  Twitter: "Read the article before sharing"
  MIT research: reading prompts reduce false sharing
    by ~8-11% (small but measurable effect)

ACCOUNT ACTION:
  Warning, suspension, ban for repeat violators
  Deplatforming major spreaders: Parler, Trump account removal
  Effectiveness: reduces reach immediately; audience migrates
  Long-term: displaces to less-moderated platforms

REMOVAL:
  Reserved for:
    CSAM (mandatory)
    Imminent physical threat
    Content violating specific laws (varies by country)
  Volume problem: 500 hours of YouTube uploaded per minute
  Removal cannot scale without automation errors

ADVERTISING DEMONETIZATION:
  Remove advertising from misinformation content/channels
  Economic incentive removal
  Effective for: financially motivated misinformation
  Limited for: ideologically motivated; state-sponsored

NONE OF THESE WORK WELL AT SCALE:
  The fundamental problem: platform economics reward
  high-engagement content; misinformation is high-engagement
  Fixing this requires changing the economic model
  No major platform has done this
```

---

## Deepfake Detection: Current State

```
DEEPFAKE DETECTION (2025)
==========================

WHAT IS A DEEPFAKE:
  Synthetic media (video, audio, image) generated by AI
  Typically: someone's face/voice replaced or created
  Technology: GAN (Generative Adversarial Network) based;
    now also diffusion models + LLMs

DETECTION METHODS:
  ARTIFACT DETECTION (increasingly obsolete):
    GAN models leave specific artifacts (blinking patterns,
    skin texture anomalies, lighting inconsistencies)
    As generation improves, artifacts disappear
    Detection trained on old models fails on new ones

  BIOLOGICAL SIGNAL DETECTION:
    Real faces have micro-expressions, pulse visible in skin
    Deepfakes lack these biological rhythms
    PPG (photoplethysmography): pulse signal in face color
    Limited: effective for lower-quality fakes only

  PROVENANCE / CRYPTOGRAPHIC:
    C2PA standard (Coalition for Content Provenance & Authenticity)
    Cameras and publishing tools sign content at capture
    Signature chain: camera -> edit tool -> publishing platform
    Breaks if any link unsigned
    Apple, Adobe, Canon, NYT members
    Limitation: adoption; old content has no signature

CURRENT STATE:
  Detection lags generation
  Best systems: ~80-90% accuracy on known models
  Unknown new models: much lower accuracy
  "The game is fundamentally asymmetric: attackers
   only need one undetected fake; defenders need
   to catch all fakes" (analogy to cybersecurity)
```

---

## Media Literacy: Evidence on Effectiveness

```
MEDIA LITERACY CURRICULA EFFECTIVENESS
========================================

WHAT THE RESEARCH SHOWS:
  Meta-analyses (Jeong et al. 2012; Webb et al. 2013):
    Traditional media literacy education:
    Small to moderate effect on:
      Critical thinking about media claims
      Skepticism toward media messages
    Weaker effect on:
      Behavior change (still sharing even if skeptical)
      Long-term retention (effects decay)

  SHORT-TERM INTERVENTIONS:
    Single "accuracy prompt" (asking users "is this accurate?")
    reduces misinformation sharing by 8-11% (Pennycook et al. 2020)
    -> Very low-cost; nudge-based

  PREBUNKING > MEDIA LITERACY:
    Technique inoculation (prebunking) shows stronger
    and more durable effects than traditional media literacy
    (Lewandowsky & van der Linden 2021 meta-analysis)

  THE "DIGITAL LITERACY" GAP:
    Ability to find credible sources ≠ ability to evaluate them
    SIFT method (Mike Caulfield):
      Stop -> Investigate the source -> Find better coverage
      -> Trace claims, quotes, media to original context
    Lateral reading: don't evaluate the source at the source;
      go elsewhere to find what others say about that source
      Expert behavior; teachable; more effective than at-source eval
```

---

## Decision Cheat Sheet

| Intervention | Effectiveness | Best use case |
|-------------|--------------|--------------|
| Debunking | Limited; partial belief update | High-profile, specific claim correction |
| Prebunking | Stronger and more durable | Inoculate against manipulation techniques |
| Content labels | Small sharing reduction; implied truth risk | Newsworthy high-reach misinformation |
| Friction insertion | ~8-11% sharing reduction | Impulsive sharing of unread content |
| Demonetization | Effective for financial motivation | Coordinated misinformation networks |
| Removal | Only scalable with automation errors | CSAM, imminent threat |

---

## Common Confusion Points

**Debunking does not reverse beliefs.** Corrections produce partial updating at best. The correction rarely reaches the people who saw the original false claim (it travels less far). Prebunking before initial exposure is more effective than correcting after.

**Bots did not explain the MIT finding.** The MIT study controlled for suspected bots. The finding — that false news spreads faster — is driven by human behavior, not automated amplification. Humans spread misinformation faster than the truth.

**The backfire effect is disputed.** The original Nyhan & Reifler (2010) finding that corrections can strengthen false beliefs has not replicated consistently. More recent research suggests backfire is rare. Corrections don't usually backfire — but they also don't fully correct.

**Fact-checking is not a scalable solution.** IFCN-affiliated organizations publish ~100 fact-checks per week total. Millions of false claims circulate per day. Fact-checking is a credibility signaling service and a reference source, not a misinformation prevention mechanism.

**Misinformation is not just a content problem.** The platform economics that reward high-engagement content (which misinformation tends to produce) are the structural cause. Content moderation treats symptoms; restructuring the incentive model is the systemic fix that no major platform has implemented.
