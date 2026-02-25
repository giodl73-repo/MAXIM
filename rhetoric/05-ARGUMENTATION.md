# Argumentation and Informal Logic

## The Big Picture

Argumentation theory is the study of how arguments work in natural language contexts — beyond formal logic, which deals with idealized arguments in symbolic form. The central framework is Stephen Toulmin's model (1958), which describes the actual structure of arguments in professional, legal, and everyday contexts.

```
+------------------------------------------------------------------+
|           ARGUMENTATION — LANDSCAPE                              |
+------------------------------------------------------------------+
|                                                                  |
|  FORMAL LOGIC                   INFORMAL LOGIC                   |
|  ------------                   ---------------                  |
|  Symbolic notation              Natural language                 |
|  Deductive validity             Plausibility, strength          |
|  Truth-preserving               Persuasion-focused              |
|  Context-free                   Context-dependent               |
|  All premises explicit          Some premises implicit          |
|                                                                  |
|  THE TOULMIN MODEL (1958) — THE KEY FRAMEWORK                   |
|  Claim + Data + Warrant + Backing + Qualifier + Rebuttal        |
|                                                                  |
|  INFORMAL FALLACIES                                              |
|  Ad hominem, straw man, false dilemma, slippery slope,          |
|  appeal to authority, hasty generalization, etc.                |
|                                                                  |
|  ARGUMENT MAPPING                                                |
|  Visual representation of argument structure                    |
|  Supports: design documents, decision memos, strategy docs     |
+------------------------------------------------------------------+
```

---

## Layer 1: The Toulmin Model — The Essential Framework

Stephen Toulmin's **The Uses of Argument** (1958) is the most practically useful book in argumentation theory for professional communicators. Toulmin was frustrated that formal logic could not describe how actual arguments work in law, science, and everyday life.

### The Six Components

```
TOULMIN'S SIX-COMPONENT MODEL
-------------------------------

         DATA ---------> CLAIM
          |                ^
          |                |
          +----> WARRANT --+
                    |
                    |
                  BACKING
                    |
              QUALIFIER (with)
                    |
              REBUTTAL (unless)

COMPONENT DEFINITIONS AND EXAMPLES

CLAIM: The conclusion; what you're trying to establish.
  "We should migrate to Platform X."

DATA (Grounds/Evidence): The facts you cite to support the claim.
  "Platform X has 99.99% uptime vs. our current 99.9%"
  "Our current platform has caused 12 incidents in Q4."
  "Industry analysts rank Platform X #1 for our use case."

WARRANT: The principle/rule that licenses the move from DATA to CLAIM.
  "A platform with higher reliability should be preferred."
  "Incident frequency is the key metric for our SLA commitments."
  The warrant is often IMPLICIT — the argument assumes the audience
  accepts it. Making the warrant explicit is the key move.

BACKING: Support for the warrant.
  "Higher reliability reduces customer churn — our data shows
  each outage costs us 0.3% monthly retention."
  The backing justifies the warrant when the warrant itself
  is contested.

QUALIFIER: The degree of certainty of the claim.
  "We should probably migrate to Platform X."
  "Assuming no unforeseen regulatory changes, we should migrate."
  Most real-world claims have qualifiers. Omitting them
  makes claims sound more certain than they are.

REBUTTAL: Conditions under which the claim does NOT hold.
  "Unless the migration cost exceeds $2M" or
  "Unless we need to maintain compatibility with Partner Y's system"
  Explicitly acknowledging rebuttals strengthens the argument
  (it demonstrates thoroughness) and allows the audience
  to provide the actual rebuttals.
```

### Worked Example: A Software Architecture Decision

```
TOULMIN APPLIED: A REAL TECHNICAL ARGUMENT
-------------------------------------------
SCENARIO: Arguing for adopting a microservices architecture

CLAIM:
  "We should decompose the monolith into microservices."

DATA:
  1. Our deployment frequency has dropped from weekly to monthly
     because the entire monolith must be tested/deployed.
  2. 3 of the 5 most recent incidents were caused by a change
     in Module A breaking Module B (tight coupling).
  3. Team size has grown from 20 to 80 engineers; coordination
     overhead has increased quadratically.

WARRANT (implicit — make it explicit):
  "When a monolithic architecture is causing deployment bottlenecks
  and tight-coupling incidents, and team size makes coordination
  expensive, decomposition to microservices addresses these specific issues."

BACKING:
  "The DORA metrics research (Forsgren et al., Accelerate) shows
  that high-performing teams deploy microservices-style architectures
  significantly more frequently with lower change failure rates."

QUALIFIER:
  "This will likely improve deployment frequency and reduce
  coupling-related incidents, assuming the team invests in
  the required platform work (service mesh, observability, etc.)."

REBUTTAL:
  "Unless the team does not yet have the operational maturity
  to run distributed systems (service mesh, distributed tracing,
  retries, backpressure) — in which case microservices will
  create more problems than they solve."
  "Unless the current performance characteristics of the
  monolith (e.g., low-latency shared memory) cannot be
  replicated in a distributed architecture."

COMPLETE ARGUMENT:
  "We should decompose the monolith [CLAIM], because deployment
  frequency has halved, coupling incidents are increasing, and
  team coordination costs are rising [DATA]. When coupling-related
  incidents and deployment bottlenecks are causing these specific
  problems, decomposition addresses them [WARRANT], as supported
  by the DORA research [BACKING]. This will likely improve our
  metrics [QUALIFIER], unless operational maturity is insufficient
  or performance requirements preclude distribution [REBUTTAL]."
```

### Using the Toulmin Model to Find Weaknesses

```
USING TOULMIN DIAGNOSTICALLY
------------------------------
When an argument fails to convince, use Toulmin to find where:

WEAK DATA: The evidence doesn't support the claim.
  "You're claiming a platform switch will reduce incidents,
  but we haven't shown our incidents are platform-caused."
  Fix: find better evidence; adjust the claim to fit the evidence.

CHALLENGED WARRANT: The audience doesn't accept the rule.
  "Higher uptime doesn't necessarily mean we should switch —
  migration risk might outweigh the reliability gain."
  Fix: make the warrant explicit and back it; or revise it.
  The hidden warrant is the most common reason arguments fail
  to persuade: the speaker assumes a principle the audience
  doesn't share.

WEAK BACKING: The warrant is challenged and the backing is thin.
  "The DORA research applies to companies with different
  scale and architecture than ours."
  Fix: find more specific backing; or acknowledge the limitation.

MISSING QUALIFIER: The claim is overstated.
  "This WILL fix our deployment problems" vs.
  "This will likely significantly improve our deployment frequency."
  Overstated claims invite skepticism; qualified claims
  are more credible.

IGNORED REBUTTAL: The audience can think of a counterexample
  that the argument hasn't addressed.
  Address it explicitly in the argument.
  "Some might say X — here's why that doesn't apply in our case."
```

---

## Layer 2: Informal Fallacies — The Recognition Toolkit

An informal fallacy is an argument that appears valid but has a flaw in its reasoning. Knowing the catalog lets you: (a) avoid making these errors and (b) identify them when others make them.

### Ad Hominem Fallacies

```
AD HOMINEM (against the person)
--------------------------------
DIRECT AD HOMINEM:
  Attack the person making the argument rather than
  the argument itself.
  "You can't trust his proposal — he failed his
  previous project."
  (The proposal might still be good regardless of his track record.)

  IMPORTANT: not always fallacious.
  In Aristotle's sense, ethos matters — if someone
  consistently makes poor judgments, their current
  judgment is legitimately less credible.
  The fallacy is dismissing the argument entirely
  based on the person rather than evaluating the argument.

TU QUOQUE (appeal to hypocrisy):
  "You tell me to exercise, but you don't exercise."
  The advice might still be correct regardless of the advisor's behavior.

CIRCUMSTANTIAL AD HOMINEM:
  "Of course you'd say that — you have a financial interest."
  The bias might exist AND the argument might still be correct.
  Identify the bias; evaluate the argument on its merits.
```

### Relevance Fallacies

```
STRAW MAN:
  Misrepresent the opponent's position (usually a weaker version)
  and attack the misrepresentation.
  "They're saying we should never upgrade anything."
  (What was actually said: "We should be more careful about
  major upgrades without thorough testing.")
  The straw man is one of the most common rhetorical tactics.
  Recognition: "That's not what I said" is the symptom.

FALSE DILEMMA (false dichotomy):
  Present only two options when more exist.
  "Either we complete this by year-end or the project fails."
  (Third option: extend the timeline; fourth: reduce scope.)
  False dilemmas are rhetorically powerful because binary
  choices are easier to decide than n-way choices.
  Recognition: ask "what other options exist?"

SLIPPERY SLOPE:
  Claim that A inevitably leads to B, B to C, C to D,
  without showing the mechanisms of each step.
  "If we allow remote work, productivity will decline,
  morale will improve but accountability will disappear,
  and eventually the team will dissolve."
  Some slippery slopes are real (addiction: one drink leads
  to patterns of use for some people). The question is
  whether the mechanisms are shown.

APPEAL TO AUTHORITY (argumentum ad verecundiam):
  Citing an authority in an unrelated domain, or
  citing an authority as if their authority ends the debate.
  "Elon Musk says we should adopt X technology."
  (In fields outside his expertise; or: even in his
  field, his authority doesn't end the argument.)
  Legitimate authority appeals cite relevant experts
  whose domain matches the claim.

APPEAL TO POPULARITY (argumentum ad populum):
  "Everyone is moving to cloud-native architectures."
  (The majority doing something doesn't make it correct.)
  But: in matters of convention and adoption, popularity
  is legitimately relevant (network effects, ecosystem support).

RED HERRING:
  Introduce an irrelevant point to distract from the actual issue.
  "Why are we debating this technology choice when the real
  problem is our hiring pipeline?"
  (May be true that hiring is important; doesn't address
  the technology choice.)
```

### Inductive Fallacies

```
HASTY GENERALIZATION:
  Drawing a general conclusion from too few or unrepresentative cases.
  "Two customers complained about the feature; customers don't want it."
  (Two complaints from thousands of users is not representative.)
  Requires: adequate sample size; representative sampling.

POST HOC ERGO PROPTER HOC (after this, therefore because of this):
  A followed B in time; therefore A caused B.
  "We deployed the update; the incident occurred; the update
  caused the incident."
  (Correlation is not causation; other factors may explain the incident.)

DIVISION / COMPOSITION:
  COMPOSITION: what is true of the parts must be true of the whole.
    "Each component is simple; therefore the system is simple."
    (Emergent complexity from simple components is normal in CS.)
  DIVISION: what is true of the whole must be true of the parts.
    "This is a great team; therefore everyone on it is great."
    (The team may have interdependencies that make the whole
    better than each part individually.)
```

---

## Layer 3: Argument Mapping

Argument mapping is the visual representation of argument structure. It makes complex nested arguments visible and analyzable.

```
BASIC ARGUMENT MAP NOTATION
-----------------------------
  [CLAIM]
     |
  [REASON 1]    [REASON 2]    [REASON 3]
     |
  [EVIDENCE 1a] [EVIDENCE 1b]
                    |
                [OBJECTION]
                    |
                [REBUTTAL]

TOOLS:
  Rationale (software): interactive argument maps
  Argdown: markdown-based argument representation
  Pen + whiteboard: fastest for group use

WHY MAP ARGUMENTS:
  1. Find where the argument is weak (missing support).
  2. Show how reasons relate (convergent = independent
     reasons; linked = each depends on the other).
  3. Identify where the audience is likely to object.
  4. Structure a document from the map (each node = a section).

ENGINEERING APPLICATIONS:
  Design documents are argument maps in prose form.
  An RFC (Request for Comments) has:
    Claim: the proposed approach
    Data/Reasons: the requirements, constraints, evidence
    Warrant: the principles guiding the choice
    Rebuttal: the alternatives considered and why rejected
  Writing the Toulmin model explicitly improves document quality.
```

---

## Decision Cheat Sheet

| I want to... | Tool |
|-------------|------|
| Structure a persuasive argument completely | Toulmin: Claim + Data + Warrant + Backing + Qualifier + Rebuttal |
| Find where my argument is weak | Toulmin diagnostic: which component is contested? |
| Identify an argument's flaw | Informal fallacy taxonomy |
| Make my assumptions explicit | State the Warrant explicitly (most arguments hide their warrant) |
| Visualize a complex nested argument | Argument mapping |
| Anticipate and preempt objections | State the Rebuttal component explicitly |

---

## Common Confusion Points

**Formal validity is not rhetorical persuasiveness**
A formally valid argument (if P then Q; P; therefore Q) can fail to persuade if the audience doesn't accept P. The warrant in a Toulmin argument plays the role of P in the syllogism; the difference is that in everyday argumentation, P (the warrant) is usually implicit and contested. Making it explicit lets both parties examine whether they agree.

**Not all fallacies are always fallacious**
Ad hominem: if someone consistently demonstrates bad judgment in a domain, their credibility in that domain is legitimately lower — this is not a fallacy, it is Aristotle's ethos. Slippery slope: some actual causal chains do progress step-by-step. Appeal to authority: citing a domain expert on a domain question is legitimate. The fallacy versions are when these moves are made improperly — when the person's character is used to dismiss a valid argument, when the mechanism isn't shown, when the authority is outside their domain.

**The missing warrant is the most common problem**
Most failed arguments fail because the speaker and audience don't share the underlying principle (warrant). "Our incident rate is too high, so we should switch platforms" assumes that switching platforms addresses incident causes — this warrant may not be shared ("aren't our incidents due to process problems, not platform?"). State the warrant explicitly and it becomes available for examination.

**Qualification is strength, not weakness**
Qualified claims ("likely," "in most cases," "assuming X") are more credible than absolute claims because they are more accurate. An unqualified claim invites the objection "but what about when..." A qualified claim handles this in advance. Claiming certainty where you don't have it reduces your ethos when the audience knows the domain.
