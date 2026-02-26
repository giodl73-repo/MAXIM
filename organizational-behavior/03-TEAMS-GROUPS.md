# Teams and Groups — Dynamics, Groupthink, Psychological Safety, Effectiveness

## The Big Picture

Teams are the primary unit of knowledge work. The research on what makes teams effective is more solid than most leadership research — particularly the work on psychological safety, which has survived large-scale empirical testing. Understanding team failure modes (social loafing, groupthink, fault lines) is as important as understanding what enables performance.

```
TEAMS FRAMEWORK
================

INPUTS → PROCESSES/EMERGENT STATES → OUTPUTS
(Hackman IPO model)

INPUTS:
 Composition (skills, diversity, size, personalities)
 Resources (tools, budget, time, information)
 Context (org support, reward system, coaching availability)
 Task design (interdependence, complexity, whole task vs subtask)

PROCESSES:
 Taskwork (coordination, communication, decision-making)
 Teamwork (conflict management, backup behavior, monitoring)

EMERGENT STATES (developed over time):
 Trust; psychological safety; cohesion; collective efficacy;
 team mental models (shared understanding of task/team)

OUTPUTS:
 Performance (quantity, quality)
 Viability (team continues; members willing to work together again)
 Member wellbeing (growth, satisfaction)

KEY FINDING: Process quality depends heavily on emergent states.
 High psychological safety → learning behaviors → performance.
 The arrows go both directions: outputs reinforce or undermine states.
```

---

## Group vs Team and Task Interdependence

```
GROUP vs TEAM DISTINCTION
===========================

GROUP: people who share identity or affiliation; minimal task interdependence
 "All engineers at Microsoft" = group
 "This product review meeting" = group
 Primary interaction: information exchange; parallel work

TEAM: people with shared purpose + meaningful task interdependence
 + shared accountability for outcomes
 Teams require coordination; group failure doesn't cascade; team failure does
 "The Bing team" (if they actually coordinate) = team

TASK INTERDEPENDENCE (Thompson, 1967):
 POOLED: each member contributes independently; outputs summed
  Example: independent sales reps each with own territory
  Coordination: minimal; mostly standards and rules
  Failure mode: social loafing (can hide in the sum)

 SEQUENTIAL: A's output → B's input → C's input (assembly line logic)
  Example: content pipeline (writer → editor → publisher)
  Coordination: scheduling; sequencing; handoff quality
  Failure mode: bottleneck; upstream quality affects all downstream

 RECIPROCAL: mutual adjustment; back-and-forth between members
  Example: software development sprint; surgical team
  Coordination: mutual adjustment; frequent communication
  Failure mode: coordination overhead; conflict
  Team benefit: greatest where tasks are reciprocally interdependent

 INTENSIVE: simultaneous integration of all members' contributions
  Example: emergency room team managing a trauma case
  Coordination: real-time mutual adjustment; pooled expertise
  Team benefit: highest payoff; also highest coordination cost

TEAM SIZE:
 Optimal size varies by task type and interdependence
 Bezos "two-pizza rule" ≈ 5-8 people; some evidence for this range
 Dunbar numbers applied: ~5 (close coordination); ~15 (team); ~50 (tribe)
 Large teams: faster for additive tasks; slower for reciprocal tasks
  because coordination overhead grows superlinearly with size
 5-8 members: optimal for most reciprocally interdependent knowledge work
```

---

## Social Loafing

```
SOCIAL LOAFING — EFFORT REDUCTION IN GROUPS
=============================================

RINGELMANN EFFECT (Maximilien Ringelmann, 1913):
 Rope-pulling experiment: each person pulled less hard in groups than alone
 Individual effort decreased as group size increased
 1 person: 63 kg force; 3 people: 53 kg/person; 8 people: 31 kg/person

MECHANISM (Latané, Williams, Harkins, 1979):
 Social loafing occurs when:
  1. Outputs are pooled (individual contribution unidentifiable)
  2. Standards are absent (no clear individual expectations)
  3. Effort is easily diffused
 "Diffusion of responsibility": everyone assumes others will contribute

MODERATORS:
 IDENTIFIABILITY: when individual contributions are visible → loafing decreases
  This is why code reviews, named commits, individual metrics reduce loafing
  in software teams — each person's work is traceable
 COHESION AND COMMITMENT: high group cohesion → loafing decreases
  ("sucker effect": I don't want to be the one who lets the team down)
 TASK MEANINGFULNESS: intrinsically motivated tasks → less loafing
 EVALUATION POTENTIAL: belief that one's work will be evaluated → less loafing

WHEN GROUPS OUTPERFORM INDIVIDUALS:
 Additive tasks: parallel effort that aggregates (brainstorming, coding sprints)
  Group > individual on quantity; but quality may require independent judgment
 Disjunctive tasks (problem-solving; best answer wins): group can outperform
  best individual IF the group recognizes the best answer when presented
  "Process gain": best member's solution adopted by group
  BUT: groups often fail to use their best member (status effects; groupthink)
 Conjunctive tasks (chain; weakest link): group performance = weakest member
  → membership selection is crucial

NOMINAL GROUP TECHNIQUE:
 Structured process to harvest individual ideation + group combination
 1. Silent individual generation (written; no verbal influence)
 2. Round-robin sharing (each person, one idea at a time; no discussion)
 3. Group discussion (clarification, evaluation)
 4. Anonymous ranking/voting
 Research: outperforms interacting groups on quantity + quality of ideas
  (avoids production blocking; social pressure; anchoring to early ideas)
```

---

## Groupthink

```
GROUPTHINK (IRVING JANIS, 1972)
=================================

Irving Janis, "Victims of Groupthink"; then "Groupthink: Psychological Studies
of Policy Decisions and Fiascoes" (1982)

DEFINITION:
 Deterioration of mental efficiency, reality testing, and moral judgment
 in a cohesive in-group, in the interest of maintaining group solidarity

ANTECEDENT CONDITIONS:
 High group cohesion (necessary but not sufficient)
 Insulation from outside opinions/expertise
 Directive, opinionated leader (leader signals preferred conclusion early)
 High stress/time pressure/moral dilemma
 Low self-esteem or recent failure

EIGHT SYMPTOMS:
 1. Illusion of invulnerability: excessive optimism; risk ignoring
 2. Collective rationalization: discount warnings; override doubts collectively
 3. Belief in group's moral superiority: ethical violations not examined
 4. Stereotyped view of outsiders: outgroup members seen as weak/evil/stupid
 5. Pressure on dissenters: members who express doubts get pressured to conform
 6. Self-censorship: members withhold concerns to maintain harmony
 7. Illusion of unanimity: silence = consent; member views exaggerated as agreed
 8. Self-appointed mindguards: some members actively shield group from counter-info

CLASSIC CASES:
 Bay of Pigs (1961): Kennedy's advisors; dissent suppressed; invasion failed
 NASA Challenger (1986): engineer objections overridden; launch decision
  ("launch fever"; Morton Thiokol engineers told to "put on your management hat")
 NASA Columbia (2003): similar dynamics; foam strike risk minimized
 Pearl Harbor (1941): military intelligence discounting warning signals
 Enron: culture of suppressing bad news; auditors not questioning

JANIS'S PREVENTION STRATEGIES:
 Assign devil's advocate role (explicit; rotated)
 Leader withholds opinion until others have spoken
 Use outside experts (periodic; not just when in trouble)
 Anonymous critique (use written, confidential objection channel)
 Hold second-chance meetings (revisit decision after initial agreement)
 Subgroup deliberation (split team; work independently; compare)
 Encourage expression of concerns ("premortem" — Klein's method)

KLEIN PREMORTEM:
 Before finalizing a decision: "Imagine it's one year from now.
  The project failed. What happened?"
 Generates: specific failure scenarios; tacit concerns surfaced
 Evidence: reduces overconfidence; surfaces hidden concerns
 More psychologically safe than asking "what could go wrong?"
  (hypothetical framing reduces threat)
```

---

## Psychological Safety

```
PSYCHOLOGICAL SAFETY (EDMONDSON)
===================================

Amy Edmondson, Harvard Business School (1999, 2018)

DEFINITION:
 A belief that one will not be punished or humiliated for
 speaking up with ideas, questions, concerns, or mistakes

NOT:
 - Comfort (comfortable teams can still avoid hard truths)
 - Trust in another person (interpersonal; safety is collective)
 - Permission to be unconditionally nice (accountability matters)
 - Absence of conflict (productive conflict increases with safety)

THE MEASUREMENT SCALE (7 items):
 1. If you make a mistake on this team, it is often held against you (R)
 2. Members of this team are able to bring up problems and tough issues
 3. People on this team sometimes reject others for being different (R)
 4. It is safe to take a risk on this team
 5. It is difficult to ask other members of this team for help (R)
 6. No one on this team would deliberately act in a way that undermines efforts
 7. Working with members of this team, my unique skills are valued and utilized

EVIDENCE BASE:
 Edmondson original (1999): nursing teams; safety predicted learning behavior
  (reporting errors); learning behavior predicted clinical outcomes
 Google Project Aristotle (2012-2015): studied 180+ teams at Google
  → psychologically safety was #1 predictor of team effectiveness
  (above team composition, seniority, size, etc.)
 Multiple meta-analyses: safety → learning; creativity; performance;
  member wellbeing; reduced turnover intention
 One of the most replicated findings in organizational research

WHAT CREATES PSYCHOLOGICAL SAFETY:
 Leader behavior (most powerful lever):
  - Framing work as learning, not execution of known processes
  - Modeling fallibility ("here's what I got wrong"; "what am I missing?")
  - Demonstrating curiosity (asking questions genuinely, not to test)
  - Responding constructively when bad news arrives
   (not punishing the messenger; not minimizing the concern)
 Team norms:
  - Explicit expectations about speaking up
  - Celebrating "near misses" as learning (aviation model)
  - Rotating who speaks first (avoid anchoring to high-status voices)

WHAT DESTROYS PSYCHOLOGICAL SAFETY:
 Leader anger at bad news (punishing the messenger)
 Blaming individuals publicly for system failures
 Competitive team structure (members compete rather than cooperate)
 Status hierarchies that prevent junior members from speaking
 Past retaliation against whistleblowers or objectors
 Leader who has "all the answers" (intellectual safety → others stop thinking)

SAFETY ≠ PERFORMANCE STANDARDS:
 High safety + high performance standards = "learning zone" (optimal)
 High safety + low standards = "comfort zone" (no progress)
 Low safety + high standards = "anxiety zone" (compliance, not learning)
 Low safety + low standards = "apathy zone" (disengaged)
```

---

## Team Effectiveness Models

```
HACKMAN'S TEAM EFFECTIVENESS FRAMEWORK
=========================================

J. Richard Hackman (1987, "The Design of Work Teams"; 2002, "Leading Teams")

CONDITIONS FOR EFFECTIVENESS:
 (not leadership behaviors; structural/contextual conditions)

 1. REAL TEAM: clear boundaries; stable membership; clear interdependence
    Many "teams" in organizations are not teams in Hackman's sense
    (too fluid; too large; no interdependence; temporary without closure)
 2. COMPELLING DIRECTION: clear, challenging, consequential task
    Ambiguous goals = chronic underperformance; members pursue own goals
 3. ENABLING STRUCTURE:
    Task: whole, meaningful piece of work (not subtask of subtask)
    Composition: right skills + manageable size
    Norms: explicit standards for behavior and contribution quality
 4. SUPPORTIVE CONTEXT:
    Reward system: team-level recognition and reward (not just individual)
    Information: access to needed data
    Education: availability of coaching/training
 5. EXPERT COACHING: available when the team needs it (not just at start)
    Process coaching: help the team work well together
    Task coaching: help the team learn new skills

THE LAUNCH IS CRITICAL:
 Hackman finding: ~60% of team effectiveness determined at team launch
 The first meeting, first assignments, initial norms → persist
 Most leadership interventions come too late (mid-project interventions
  when problems are visible; Hackman: prevent, don't rescue)

GRPI MODEL (Rubin, Plovnick, Fry, 1977):
 Goals → Roles → Processes → Interpersonal relationships
 The hierarchy matters: goals before roles; roles before process
 Most teams fail by skipping to process without clear goals and roles

LENCIONI'S FIVE DYSFUNCTIONS:
 Patrick Lencioni, "The Five Dysfunctions of a Team" (2002)
 (Business book; not academic; but widely used framework)
  1. Absence of trust (invulnerability → can't be honest)
  2. Fear of conflict (artificial harmony; no productive debate)
  3. Lack of commitment (ambiguity from avoiding conflict → no buy-in)
  4. Avoidance of accountability (team members won't call out peers)
  5. Inattention to results (individual status > team outcomes)
 These build on each other: absence of trust → fear of conflict → ...
 OB evaluation: conceptually useful; not rigorously empirically tested;
  the dysfunctions are real and observable; the pyramid sequence is intuitive
```

---

## From Multi-Site Engineering Organizations to Team Research

Fault lines, diversity effects, and virtual team dynamics are the specific research domains that apply when a VP designs team structures across distributed sites.

**Fault lines explain why Redmond-Hyderabad or Seattle-Dublin teams split into factions.** When multiple diversity attributes align (seniority correlates with geographic location; domain expertise correlates with time zone; tenure correlates with nationality), the team has a structural fault line — a latent fracture that activates under conflict or pressure. The research finding: teams whose diversity attributes are uncorrelated (a junior in Seattle paired with a senior in Hyderabad across multiple such pairings) are more resilient than teams where all the seniors are in one location. The organizational implication: in structuring engineering teams across sites, actively break the correlation between site membership and other attributes (seniority, domain, tenure, role) rather than creating a team where "the Hyderabad team is the testing team" — which creates both a fault line and a status hierarchy.

**Information elaboration is the mechanism that determines whether diversity helps or hurts.** The net benefit of task-relevant diversity (different expertise, different institutional knowledge, different technical exposure) depends entirely on whether the team actually uses the diverse information. Teams with high psychological safety, rotating facilitation, and explicit "what do others think" processes elaborates diverse information and outperform homogeneous teams. Teams with status hierarchies that silence junior voices, dominant communicators who crowd out alternatives, and "efficiency over exploration" norms fail to elaborate and underperform. The diversity itself is not the variable — the process that enables or blocks elaboration is.

**Virtual team trust dynamics require intentional structural intervention.** Swift trust at the start of a virtual team (task-based, not relationship-based) is fragile: it depends on initial reliability signals (do people do what they say? do they respond promptly?). Without face-to-face trust-building mechanisms, early reliability failures can permanently set a low-trust equilibrium. The intervention: front-load synchronous time at team formation (the equivalent of a co-location kickoff week), make reliability standards explicit and symmetric across locations, and treat documentation and async update quality as a leadership indicator, not an administrative obligation. Proximity bias — the systematic advantage of co-located team members in performance review outcomes — requires explicit mitigation in the calibration process, not just awareness.

## Diversity and Virtual Teams

```
DIVERSITY IN TEAMS
====================

INFORMATION ELABORATION HYPOTHESIS (van Knippenberg et al.):
 Diversity benefit is realized when diverse knowledge is actually USED
 Task-relevant diversity: different expertise, perspectives, information
  → potentially better decisions (more information surface area)
 But: requires process for elaboration; doesn't happen automatically
 Social categorization: diversity also triggers in-group/out-group thinking
  → reduced trust; communication barriers; less information sharing
 NET EFFECT: diversity benefits are conditional; teams that elaborate
  diverse information outperform homogeneous teams on complex tasks;
  teams that fail to elaborate may underperform (process losses)

SURFACE vs DEEP-LEVEL DIVERSITY:
 Surface: visible differences (demographics, gender, race, age)
 Deep-level: attitudes, values, personality, cognitive styles
 Research: surface diversity → early conflict → often resolved over time
  Deep-level diversity → persistence of conflict through group life
  Deep-level similarity (shared values) → cohesion and trust

FAULT LINES (Lau & Murnighan, 1998):
 When multiple diversity attributes align (e.g., women tend to be junior;
  men tend to be senior in the same team) → structural fault line
 Fault lines → subgroup formation → team splits into factions
 Strong fault lines → polarization; reduced cooperation; performance loss
 Organizational implication: deliberately compose diverse teams so that
  diversity attributes don't correlate with each other

VIRTUAL TEAMS:
 Trust development: Swift trust at start (task-based, not interpersonal);
  must be maintained through reliable behavior (not relationship history)
 Communication richness: media synchronicity theory (Dennis & Valacich)
  Synchronous (video, voice): better for complex, equivocal communication
  Asynchronous (email, Slack): better for conveyance of established info
  Mismatch → misunderstanding; conflict escalation
 Time zone management: async-first design; single timezone overlap window
 Documentation: written work products substitute for observation;
  more equitable across time zones + protects against proximity bias
 Management: remote workers often under-promoted vs co-located peers
  (proximity bias; visibility bias; attribution of engagement to presence)
```

---

## Common Confusion Points

**Cohesion is not always good for teams**:
Highly cohesive teams can experience groupthink. The desire to maintain harmony and consensus can override critical thinking. Cohesion improves performance only when combined with productive norms — and productive norms require the ability to disagree.

**Psychological safety ≠ absence of accountability**:
The highest-performing teams have both high psychological safety AND high performance standards. Safety enables honest conversation about performance gaps. Accountability without safety = people hide problems. Safety without accountability = mediocrity without honest correction.

**Nominal groups outperform interacting groups on brainstorming**:
This is a consistent finding that surprises most people. Groups where members simultaneously interact inhibit individual idea generation (anchoring to early ideas, evaluation apprehension, production blocking). Nominal group technique (independent, then shared) produces more and better ideas.

**Hackman: most teams fail at launch, not mid-execution**:
Leaders typically intervene when problems become visible (mid-project or late). Hackman's research shows the structural conditions at team launch (direction, structure, membership) determine most of the outcome. Fixing a badly structured team mid-flight is much harder than structuring it well from the start.

---

## Decision Cheat Sheet

| Team Question | Answer |
|---------------|--------|
| #1 predictor of team effectiveness (Google) | Psychological safety |
| How to reduce social loafing | Make contributions identifiable; clear individual accountabilities |
| Groupthink antecedents | High cohesion + insulation + directive leader + stress |
| Best brainstorming structure | Nominal group technique (independent first; then share) |
| When diversity helps team performance | When task-relevant diverse information is elaborated |
| Optimal team size for knowledge work | 5-8 members (reciprocal interdependence) |
| What creates psychological safety | Leader fallibility + curiosity + constructive response to bad news |
| Hackman: when does team effectiveness get determined | ~60% at launch (structure, direction, composition) |
| Fault lines cause | Correlation of multiple diversity attributes within same team |
