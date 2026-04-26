# Behavioral Economics in Policy

## Government Behavioral Insight Teams

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    BEHAVIORAL INSIGHT TEAMS GLOBALLY                        │
│                                                                             │
│  BIT (UK Behavioural Insights Team, 2010):                                  │
│  First government behavioral unit. Started in Cabinet Office.               │
│  Now quasi-commercial, operating in 30+ countries.                          │
│  Flagship interventions: tax compliance, organ donation, employment services │
│                                                                             │
│  SBST (Social and Behavioral Sciences Team, US, 2014-2017):                 │
│  White House unit. Executive Order (Obama). >200 trials run.                │
│  Abolished under Trump; partially revived under Biden as Evidence Team.     │
│                                                                             │
│  IDEAS42 (US, 2008): Non-profit behavioral consulting.                      │
│  BETA (Australian Government Behavioral Economics Team, 2015)               │
│  EAST unit in Singapore, Netherlands, France, Canada, Denmark               │
│                                                                             │
│  COMMON METHODOLOGY:                                                        │
│  1. Diagnose the behavioral bottleneck (why don't people do X already?)     │
│  2. Design the intervention (EAST framework; exploit behavioral patterns)   │
│  3. Test with randomized controlled trial (A/B test)                        │
│  4. Scale if effective                                                      │
│                                                                             │
│  CONNECTION TO COMPUTING:                                                   │
│  This is A/B testing applied to policy. Same statistical framework as       │
│  product feature testing (see statistics-applied/). Same power calculations. │
│  The political challenge: policymakers less comfortable with randomized     │
│  control than product managers. Same technical problem, different context.  │
└─────────────────────────────────────────────────────────────────────────────┘
```

## Classical to Behavioral Welfare Economics

Standard welfare economics rests on two foundations that behavioral economics directly challenges:

```
CLASSICAL WELFARE ECONOMICS (THE BASELINE):

  Revealed Preference Principle (Samuelson 1938):
    Observed choices reveal true preferences.
    If agent chooses A over B, then A ≽ B.
    → Welfare = choice outcomes. Paternalism is unjustified (agent knows best).

  Pareto Criterion:
    Policy X is an improvement iff it makes at least one person better off
    and no one worse off.
    "Better off" = revealed-preferred outcome achieved.
    → No interpersonal utility comparisons needed. Efficiency without paternalism.

  IMPLICATION: In classical welfare economics, a government has no role in
  correcting individual choices (only in correcting market failures: externalities,
  public goods, information asymmetry). The agent's revealed choice IS their welfare.

BEHAVIORAL WELFARE ECONOMICS — THE PIVOT:

  Problem: if preferences are systematically distorted, revealed choice ≠ welfare.
    Present bias: I choose to smoke today, but if asked to commit to quit next month,
    I would. My immediate choice and my planned choice are inconsistent.
    My "true" preference is ambiguous — which one should welfare follow?

    Endowment effect: I'd sell my coffee mug for $1 if I didn't have it, but
    demand $4 to give it up. My WTP ≠ WTA by 4×. Which reflects my true value?

    Default effects: I'm in a retirement plan at 3% because it was the default.
    I've never considered whether I want 3% or 10%. Default ≠ considered choice.

  BEHAVIORAL WELFARE APPROACHES:

  1. DUAL PREFERENCE APPROACH (Thaler 1980, O'Donoghue & Rabin 1999):
     Distinguish "wanters" (System 1 immediate preferences) from
     "planners" (System 2 considered preferences).
     Welfare = planner's preferences. Policy should help planner overcome wanter.
     → Justifies commitment devices, nudges that support considered choice.

  2. WELFARE AS DECISION UTILITY vs EXPERIENCED UTILITY (Kahneman):
     Decision utility: utility revealed by choice (what we pick)
     Experienced utility: moment-by-moment hedonic quality (how it actually feels)
     These diverge (focusing illusion, adaptation, affective forecasting errors)
     → Welfare might be better measured by experienced utility than decision utility.

  3. PREFERENCE PURIFICATION / REVEALED PREFERENCE REPAIR:
     Estimate what agent would choose if bias were removed.
     If defaults drive choice → purify by assuming agent preferred what
     they'd choose with active deliberation.
     Technically difficult; requires assumptions about counterfactual preferences.

  4. LIBERTARIAN PATERNALISM (Thaler-Sunstein):
     Preserve choice (respect revealed preference for those who override defaults)
     but set defaults to maximize welfare of those who don't override.
     Sidesteps the question of "what is true preference" by preserving autonomy.
     If you really want something different: opt out. Welfare improved for the many;
     autonomy preserved for the minority with different preferences.

  POLICY CRITERION SHIFT:
  Classical: Pareto improvement (no one worse off by own preferences)
  Behavioral: "asymmetric paternalism" (Camerer et al. 2003) —
    Policies that benefit people with bounded rationality while imposing
    minimal cost on fully rational agents.
    Example: auto-enrollment default costs nothing to rational agents (they opt out
    to their preferred level); helps present-biased agents who would never enroll.
```

## Tax Compliance

```
STANDARD MODEL OF TAX COMPLIANCE (Allingham-Sandmo 1972):
  Compliance = f(audit probability, penalty severity, income)
  Rational agent: evade if expected gain from evasion > expected penalty.
  Policy implication: increase audits and penalties → more compliance.

  PROBLEM: Empirical compliance rates far exceed what audit probabilities justify.
  In US: audit rate ~0.5% of returns; penalty ~75% of underpayment.
  Expected cost of evasion: 0.005 × 0.75 = 0.375% of underpaid tax.
  Yet compliance rates are ~85%. Rational model predicts much lower compliance.
  Additional drivers: social norms, moral commitment, perceived legitimacy.

BEHAVIORAL INTERVENTIONS — EVIDENCE:
  BIT UK TRIAL (HMRC, 2012-2014):
  200,000+ late-paying self-assessment taxpayers randomized to letters:
    Control: standard reminder letter
    Treatment 1: "9 out of 10 people in your area pay their taxes on time."
                 → +15% compliance vs. control
    Treatment 2: "Most people in your profession pay their taxes on time."
                 → +25% compliance (profession > generic descriptor)
    Treatment 3: "You are one of the few people who has not paid their taxes."
                 → combination of norm + loss frame → +32% compliance
    Treatment 4: Simplify letter + norm + loss frame → +38% compliance

  MECHANISMS WORKING:
  1. Social norm (descriptive): "most people comply" → conformity
  2. Loss frame: "you are unlike most" → loss aversion (falling below norm = loss)
  3. Simplification: friction reduction → EASY principle
  4. Personal specificity: profession-specific norm > generic norm (more relevant)

  COST: letter redesign. Effect: ~£30M additional revenue in pilot.
  Cost-effectiveness: extraordinary.

IRS USA CONTEXT:
  IRS voluntary compliance rate: ~85% (of estimated owed taxes)
  Tax gap: ~$600-700B/year (tax owed but not paid)
  Behavioral interventions largely untested at scale in US (political resistance).
  SBST (2014-2017): some IRS trials completed; results promising.
  Real opportunity: behavioral interventions substantially cheaper than enforcement.
```

## Organ Donation

```
ORGAN DONATION DEFAULT EFFECTS — DOCUMENTED:

  CLASSIC DATA (Johnson & Goldstein 2003):
  Opt-IN countries (must actively register as donor):
    Denmark: 4.25%    Netherlands (1994): 27.5%
    United Kingdom: 17.2%   Germany: 12%
  Opt-OUT countries (must actively opt out; default = donor):
    Sweden: 85.9%    Hungary: 99.97%
    Austria: 99.98%  Belgium: 98.0%  France: 99.9%

  The difference: ONLY THE DEFAULT. Not law, culture, wealth, religion
  (Austria vs. Germany: same religion, language, culture, GDP — different defaults).

  UK CHANGE (2020):
  England moved from opt-in to "deemed consent" (opt-out) for adults.
  Wales: moved to opt-out in 2015 → donation rates increased ~25% over 5 years.
  Scotland: opt-out from 2021.

  MANDATED CHOICE (alternative):
  Must indicate preference (yes/no) when getting a driver's license.
  US: most states use this for driver's license — not true mandated choice but
  a prompted enrollment.
  Effect: higher registration rates than pure opt-in; lower than opt-out.
  About 42% (Netherlands historical mandated choice) vs. 12% (opt-in) vs. 99% (opt-out).

KIDNEY MARKETS:
  Unrelated: UNOS waitlist in US: ~100,000 on kidney waitlist. ~20 die per day.
  Behavioral insight: even with unlimited supply, default mechanism matters for
  allocation equity and utilization.
```

## Energy Conservation

```
OPOWER (Now Oracle Utilities) — NEIGHBOR COMPARISON:
  Home Energy Reports (HER): monthly/bi-monthly mailing showing:
  - Your energy use
  - Your "efficient neighbors'" average use
  - "All neighbors'" average use
  With smiley faces (green = below average, frowny = above average, neutral).

  SCALE: 60M+ households in US and UK.
  EFFECT: ~2% average reduction in energy consumption.
  Persistent: effect sustained over years (not novelty; becomes part of norm).
  Heterogeneous: above-average users reduce; below-average users might INCREASE
  (Schultz 2007: without injunctive norm to reinforce, descriptive norm alone
  can "permit" below-average users to increase → add normative message "✓ good").

  COST-EFFECTIVENESS:
  Compared to:
    Time-of-use pricing: ~5% reduction, much more complex
    Cash rebates for efficiency upgrades: higher %, much higher cost
    Opower: 2% at ~$0.02-0.05/kWh saved (very cheap)
  At grid scale: millions of kWh reduction → utility-scale impact.

  MECHANISM: Social proof (descriptive norm) + loss framing (being above average = loss).

HOME ENERGY AUDITS + IMPLEMENTATION INTENTION:
  Allcott & Mullainathan: scheduling the audit at point of interest → higher uptake.
  "When do you want to schedule this?" at point of call → implementation intention.
```

## Retirement Savings

```
AUTO-ENROLLMENT IN 401(k) — BENCHMARK INTERVENTION:
  Madrian & Shea (2001): company switched from opt-in to opt-out 401(k) enrollment.
  6-month enrollment: 37% → 86% (+49pp).
  One year: 45% → 86%.
  Most new employees: stay at default contribution rate (3% of salary) regardless of optimal.
  Problem: default contribution rate (typically 3%) is below optimal (~10-15%).

  AUTO-ESCALATION (SMarT — Save More Tomorrow):
  Thaler & Benartzi (1999, 2004):
  Problem: people don't save enough even with enrollment.
  Solution: commit workers in advance to increase savings rate with each raise.
  Key design:
  1. Commitment is future (present bias doesn't resist future commitment)
  2. Increase is from upcoming raise (doesn't feel like a pay cut)
  3. Default is to stay enrolled (inertia works for you)
  4. Can opt out at any time
  Results: average savings rate grew from 3.5% to 11.6% over 4 years.
  Now widely adopted; default escalation built into many 401(k) plans.

PENSION POLICY EVIDENCE:
  UK NEST (National Employment Savings Trust, 2012):
  Auto-enrollment into pension: opt-out rate ~9% (91% remain enrolled).
  Previous voluntary enrollment rate: ~50%.
  Behavioral change without any change in incentives — only default changed.

  US SECURE ACT (2019) AND SECURE 2.0 (2022):
  Require auto-enrollment for new 401(k) plans from 2025.
  Congressional action institutionalizing the behavioral finding.
  Estimated impact: millions of additional Americans saving for retirement.
```

## Health Behaviors

```
VACCINATION — ANNOUNCEMENT VS. PARTICIPATORY:
  Milkman et al. (2011): flu vaccination rates in health system.
  Presumptive announcement framing ("I'm going to give you your flu shot now")
  vs. participatory ("Would you like a flu shot?"):
  Presumptive → significantly higher acceptance.
  Mechanism: presumptive sets default to vaccinate; participatory requires active opt-in.

  SCHEDULED APPOINTMENT (vs. "come when you can"):
  Randomly assigned specific appointment time → higher attendance.
  Implementation intention created by appointment letter.

MEDICATION ADHERENCE:
  Major problem: ~50% of chronic disease patients don't take medications as prescribed.
  Behavioral interventions:
  - Reminder SMS: modest but consistent effect (~5-10% improvement)
  - Pill organizers: reduce complexity friction
  - Automatic refill: removes decision to refill (reduces forgetting to renew)
  - Financial incentives: effective but costly; often don't outlast the payment
  - Social accountability (buddy system): peer support → sustained adherence

CAFETERIA CHOICE ARCHITECTURE:
  Thaler & Sunstein suggestion: put healthy food at eye level and front.
  Wansink et al.: food placement and presentation matters for consumption.
  Salad bar at front → more salad selected.
  School cafeteria studies: fruit at eye level → 70% increase in fruit selection
  without changing availability or price.
  Note: some Wansink studies retracted; core findings (placement effects) more robust.
```

## Employment Services

```
SBST INTERVENTIONS IN EMPLOYMENT:
  US SBST (2016): letters to Veterans Affairs enrollees re: vocational benefits.
  Simplified + social norm + loss framing → higher benefits enrollment.
  Effect size: ~15-20% increase.

  UNEMPLOYMENT INSURANCE AND ACTIVE JOB SEARCH:
  Denmark experiment (Bhargava & Manoli 2015):
  Complex UI application → simplified format → +40% uptake among eligible.
  Many eligible workers not receiving benefits due to application complexity (friction).

  REDUCING APPLICATION FRICTION:
  Benefits enrollment across programs (SNAP, Medicaid, EITC):
  Significant fractions of eligible people don't claim benefits.
  Primary reason: complexity and friction, not lack of awareness.
  EAST approach: reduce friction → large enrollment increases.
  "Passive enrollment" models (pre-enrollment using administrative data) → near-100% uptake.

INTERVIEW PREPARATION:
  Interviewing techniques that reduce discrimination:
  Structured interviews (standardized questions, scoring rubric):
    Reduces anchor/affect heuristic → more valid assessment.
  Blind review (remove identifying information):
    Reduces in-group bias and availability heuristic effects.
  Both improve selection quality — behavioral insight applied to hiring.
```

## Decision Cheat Sheet

| Policy application | Intervention | Effect size |
|---|---|---|
| Tax compliance | Social norm letter ("most in your area paid") | +15-38% compliance in delinquent pool |
| Organ donation | Opt-out default | 70-90pp higher donation registration |
| Energy conservation | Neighbor comparison + normative message | 2% persistent reduction at scale |
| Retirement savings enrollment | Auto-enrollment default | +49pp enrollment rate |
| Retirement savings adequacy | Auto-escalation (SMarT) | 3.5% → 11.6% savings rate over 4 years |
| Vaccination uptake | Presumptive announcement | 15-30% higher acceptance vs. participatory |
| Benefits enrollment | Simplify application + reduce friction | 20-40% increase in eligible uptake |

## Common Confusion Points

**SBST/BIT interventions are RCTs, not pilots**: Behavioral insight teams specifically test with randomized controlled trials before recommending scale-up. This is methodologically more rigorous than most policy evaluation. The same standards as clinical trials for drug approval are being applied to policy interventions.

**Social norm effects can backfire**: The Schultz 2007 finding (boomerang effect) is important: if you tell below-average consumers they're below average, you give them permission to increase. Always include both descriptive AND injunctive norm (approval/disapproval cue) to prevent rebound. Opower uses the smiley/frowny faces as the injunctive element.

**Behavioral policies are not a substitute for structural change**: Nudges work in the "last mile" — when people have the resources and capacity to act but behavioral friction prevents it. They don't address structural causes: people without retirement accounts need access to retirement savings vehicles, not just better defaults. Behavioral economics complements, doesn't replace, policy addressing structural barriers.

**Spillover effects matter**: Interventions in one domain can affect behavior in other domains. If a tax nudge makes people feel like compliant citizens, they may behave more pro-socially in other domains (positive spillover). If an energy nudge makes people feel virtuous, they may "offset" elsewhere (negative spillover / moral licensing). Evidence on spillovers is mixed and context-dependent.
