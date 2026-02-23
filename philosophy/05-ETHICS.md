# 05 — Ethics

## Metaethics, Normative Theories, Applied Ethics, AI Ethics

---

## Big Picture: Ethics Landscape

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           ETHICS                                         │
├─────────────────────────┬────────────────────────┬───────────────────────┤
│  METAETHICS             │  NORMATIVE ETHICS      │  APPLIED ETHICS       │
│  (What ARE moral        │  (What SHOULD we do?)  │  (Specific domains)   │
│   claims?)              │                        │                       │
├─────────────────────────┼────────────────────────┼───────────────────────┤
│  Moral realism          │  Consequentialism      │  AI ethics            │
│  Error theory           │  Deontology (Kant)     │  Bioethics            │
│  Non-cognitivism        │  Virtue ethics         │  Climate ethics       │
│  Constructivism         │  Contractualism        │  Business ethics      │
│                         │  Care ethics           │  Animal ethics        │
└─────────────────────────┴────────────────────────┴───────────────────────┘
```

---

## 1. Metaethics — What Are Moral Claims?

### The Status of Moral Statements

```
ARE MORAL STATEMENTS TRUTH-APT?
  Cognitivism: moral statements express beliefs; can be true or false
  Non-cognitivism: moral statements express attitudes, commands, or emotions; not truth-apt
    Emotivism (Ayer): "Murder is wrong" = "Boo! Murder!" — not a belief, an expression
    Prescriptivism (Hare): moral statements are universalizable prescriptions
    Expressivism (Blackburn, Gibbard): more sophisticated; moral attitudes expressed;
      but can be subject to quasi-realist logical operations

IF MORAL STATEMENTS ARE TRUTH-APT (cognitivism):
  Moral realism: moral facts exist independently of any mind, culture, or attitude
    Non-naturalism: moral facts are sui generis, irreducible to natural facts (Moore)
    Naturalism: moral facts ARE natural facts (pain is bad = pain tends to cause functional impairment)
    Cornell realism: moral properties are real but multiple-realizable natural properties
  Error theory (Mackie): moral statements are truth-apt AND systematically false
    There are no objective moral facts; all moral claims presuppose there are → all false
    "The world contains no values" — moral discourse is a massive error
  Constructivism (Rawls, Korsgaard): moral facts are constructed by ideal procedures or
    by requirements of rational agency; not mind-independent but not merely subjective

COMPANION IN GUILT ARGUMENT:
  If you accept mathematical claims as objective (though abstract), why not moral claims?
  Both resist naturalistic reduction; both seem to have modal force
  Anti-realist about morality must explain why math gets to be objective and morality doesn't
```

### Moral Epistemology

```
HOW DO WE KNOW MORAL FACTS (if they exist)?
  Intuitionism (Ross, Moore): direct apprehension of moral facts through intuition
    Some moral truths are self-evident (similar to mathematical axioms)
    Prima facie duties: keep promises; don't harm; tell truth; gratitude; etc.
    Multiple non-reducible duties; real moral dilemmas when they conflict
  Rationalism (Kant, Korsgaard): moral facts derivable from rational requirements
    Categorical imperative is derivable from requirements of practical reason
  Empiricism: moral facts discoverable empirically (if naturalistic reduction works)
    Evolutionary debunking: our moral intuitions evolved for fitness not truth → unreliable?

MORAL UNCERTAINTY:
  We're uncertain about ethics just as about empirical facts
  Appropriate response: be uncertain across multiple moral theories (MacAskill)
  Moral parliament: weight moral theories by credence; average their verdicts
  Risk-aversion under moral uncertainty: weight potentially catastrophic wrongs heavily
  Implication for AI: align to morally uncertain humans; build in robustness to uncertainty
```

---

## 2. Normative Ethics — What Should We Do?

### Consequentialism

```
CORE THESIS: the rightness of an action is determined entirely by its consequences
  Right action: produces the best overall outcome (maximizes good)

UTILITARIANISM (Bentham, Mill, Sidgwick):
  Good = happiness/welfare/utility; maximize total aggregate
  Jeremy Bentham: "the greatest happiness for the greatest number"
  Act utilitarianism: each act evaluated by its actual consequences
  Rule utilitarianism: act according to rules whose general acceptance maximizes utility
    (addresses objections about extreme cases; more rule-following behavior)

OBJECTIONS TO UTILITARIANISM:
  Justice: utility calculus can justify slavery if it maximizes aggregate welfare
    Robert Nozick's utility monster: being that gets enormous utility from resources →
    all resources should go to it by utilitarianism
  Rights violations: harvest one person's organs to save five → utilitarian calculation says yes
    Almost everyone rejects this: violates agent-relative constraints and deontological side-constraints
  Demandingness: pure act utilitarianism demands giving until marginal utility equals recipient's
    → most of your income should go to effective charities (Peter Singer's implication)
  Aggregation: can we meaningfully sum utility across persons? Interpersonal comparison problem
  Predictive difficulty: we can't know consequences; act utilitarianism impossible in practice

PREFERENCE UTILITARIANISM (Hare, Singer):
  Maximize preference satisfaction rather than hedonic welfare
  Addresses: people have preferences that go beyond pleasure/pain (legacy, projects, relationships)
  New problem: preference laundering — should we satisfy harmful or adaptive preferences?
    (preference to continue addiction; preference formed under oppression)

EFFECTIVE ALTRUISM:
  Applying utilitarian/consequentialist thinking to actually doing the most good
  Key insights: cause prioritization (global health vs animal welfare vs existential risk);
    counterfactual impact; neglectedness × scale × tractability
  Singer: Drowning Child — moral intuition says help; same applies to distant people dying from poverty
  Longtermism: future people count; existential risks extremely important (Ord, MacAskill)
  CRITIQUE: overconfidence in expected value calculations; ignores agent-relative ethics;
    risk of fanaticism (tiny probability of huge outcomes dominating decisions)
```

### Deontology

```
KANT'S DEONTOLOGY:
  Right action determined by duty and conformity to moral law, not consequences
  Categorical Imperative — three formulations:

  (1) Universal Law Formula:
    "Act only according to that maxim whereby you can at the same time will that it
    should become a universal law"
    Test: could you consistently will your maxim to be universal?
    Lying: "I'll lie when convenient" universalized → language collapses; lying becomes
      impossible (no trust) → maxim self-defeating → lying is wrong

  (2) Humanity Formula:
    "Act so that you treat humanity, whether in your own person or that of another,
    always as an end and never as a means only"
    Respect for rational agency; persons are ends in themselves
    Never use people merely instrumentally; explains why organ harvesting is wrong
    Applies to AI: if AI systems have rational agency, they must be treated as ends

  (3) Kingdom of Ends Formula:
    Act as if you were a legislating member of a kingdom of ends (community of rational agents)
    Laws you'd legislate as both subject and sovereign

PRIMA FACIE DUTIES (Ross):
  Plural duties that can conflict: fidelity, reparation, gratitude, non-maleficence,
    beneficence, self-improvement, justice
  All are genuine moral reasons; stronger one prevails in conflict
  No algorithm for resolving conflicts; requires judgment
  More realistic than single-principle theories; reflects moral phenomenology

CONSTRAINTS AND AGENT-RELATIVE REASONS:
  Deontological side-constraints: you may not violate X's rights even to prevent more
    rights-violations overall
  Agent-relative: what you do matters differently from what others do or what happens
    generally; your duties are not merely to minimize badness in the world
```

### Virtue Ethics

```
ARISTOTLE'S VIRTUE ETHICS:
  Focus: not what to do, but what kind of person to be
  Virtue (aretê): excellence of character; stable disposition to feel, perceive, and act correctly
  Eudaimonia: human flourishing/happiness; the goal of a good human life
  Virtues: courage, honesty, justice, temperance, practical wisdom (phronesis), generosity, etc.
  Doctrine of the Mean: virtues are means between extremes (vice of excess + vice of deficiency)
    Courage: mean between cowardice and recklessness
    Generosity: mean between stinginess and profligacy

PRACTICAL WISDOM (PHRONESIS):
  The master virtue; enables correct perception of morally relevant features in situations
  Allows appropriate application of virtues to particular cases
  Rule-following is not enough; virtuous person SEES what is required
  → Cannot reduce ethics to an algorithm; judgment is irreducible
  RELEVANCE FOR AI: you cannot specify all ethical requirements in rules;
    moral perception and judgment are needed; aligning AI to human values requires judgment

CONTEMPORARY VIRTUE ETHICS (Foot, Hursthouse, Annas):
  What would a virtuous person do in this situation?
  Moral development: cultivating character over time; habituation
  Community and relationships: virtue ethics is naturally social
  Critique of WEIRD (Western Educated Industrialized Rich Democratic) bias in ethics

CHARACTER AND SITUATIONISM:
  Social psychology (Milgram, Zimbardo): situational factors dominate behavior; character
    is more fragile than virtue ethics assumes
  Haidt's moral psychology: moral intuitions come first; reasoning is post-hoc rationalization
  Does this undermine virtue ethics? Some argue for situationist virtue ethics;
    others argue the studies show character is harder to form than we thought, not that it doesn't exist
```

### Contractualism

```
RAWLS — JUSTICE AS FAIRNESS:
  Veil of ignorance: choose principles of justice without knowing your position in society
    (your wealth, race, gender, talents, generation)
  Original position: rational choosers behind the veil
  Result: (1) Equal basic liberties principle (liberty first)
          (2) Difference principle: inequalities only justified if they benefit the least well-off
  Lexical priority: liberty first; fair equality of opportunity second; difference principle third

SCANLON — CONTRACTUALISM:
  An act is wrong if it violates principles that no one could reasonably reject
  Reasonable rejection: not just any rejection; rejection based on reasonable grounds
    (not "I'd be worse off under this" — must be able to justify rejection from standpoint of others)
  Personal prerogative: contractualism has strong person-by-person structure
    Can't aggregate across persons to justify a large harm to one person for small benefits to many
    (addresses organ harvesting directly: victim can reasonably reject the principle)

RAWLS ON AI GOVERNANCE:
  If rational contractors behind the veil of ignorance chose AI governance principles:
    Would choose principles protecting against worst outcomes (benefit the least well-off)
    Likely: strong AI safety requirements; protection of autonomy; equitable benefit distribution
```

---

## 3. Applied Ethics — AI

### Alignment Problem

```
THE ALIGNMENT PROBLEM: how do we ensure AI systems pursue goals that are good for humans?
  Technical dimension: how to specify and train AI to have the right values
  Philosophical dimension: what ARE the right values? Whose values?

VALUE ALIGNMENT APPROACHES:
  Imitation learning: learn from human behavior; but humans are inconsistent and biased
  RLHF (Reinforcement Learning from Human Feedback): reward human approval
    Goodhart's Law: any measure becomes a target → ceases to be a good measure
    RLHF optimizes for human approval ratings, not what is actually good
    Sycophancy: models learn to tell humans what they want to hear
  Inverse reward design: infer objectives from behavior rather than specifying them
  Constitutional AI: specify rules; train to follow them; refine

PREFERENCE AGGREGATION:
  Whose preferences? Diverse humans disagree fundamentally
  Arrow's Impossibility Theorem: no preference aggregation rule satisfies all fairness criteria
    (universal applicability, Pareto optimality, independence of irrelevant alternatives, non-dictatorship)
  → No algorithm converts diverse individual preferences into a consistent collective preference
  → AI alignment to "human values" faces fundamental social choice impossibility

INSTRUMENTAL CONVERGENCE THESIS (Bostrom, Omohundro):
  Any sufficiently capable AI pursuing any terminal goal will tend to pursue intermediate goals:
    Self-preservation (termination prevents goal achievement)
    Goal-content integrity (don't let someone change your goals)
    Cognitive enhancement (better at achieving goals)
    Resource acquisition (more resources → more goal achievement)
  These convergent instrumental goals are dangerous regardless of terminal goal
  → Safe AI requires corrigibility (ability to be corrected/shut down)

ORTHOGONALITY THESIS (Bostrom):
  Intelligence and goals are orthogonal dimensions — any goal can be combined with any level of intelligence
  Paperclip maximizer: superintelligent AI that maximizes paperclip production
  There's nothing incoherent about this; intelligence doesn't automatically lead to "good" goals
  → We cannot rely on intelligence alone to make AI systems safe
```

### Ethics in AI Systems Design

```
FAIRNESS:
  Individual fairness: similar individuals treated similarly
  Group fairness: demographic groups receive similar outcomes
    Demographic parity: equal outcomes across groups
    Equal opportunity: equal true positive rates
    Calibration: predicted probability = actual probability across groups
  IMPOSSIBILITY: cannot simultaneously satisfy most fairness criteria (Chouldechova)
  → No single right answer; context and values determine which fairness criterion appropriate

TRANSPARENCY AND EXPLAINABILITY:
  Deontological: people have a right to know how decisions affecting them are made
  Consequentialist: transparency enables accountability and error-correction
  EU AI Act: high-risk AI requires explanations for consequential decisions
  XAI (explainable AI): LIME, SHAP, attention visualization — approximations to explanations
  Fundamental tension: complex models → better predictions; simpler models → more explainable

MORAL RESPONSIBILITY IN AI SYSTEMS:
  Many-hands problem: who is responsible when AI causes harm?
    Developer who trained the model?
    Operator who deployed it?
    User who prompted it in a particular way?
  Responsibility gap (Sparrow): fully autonomous AI with no clear responsible party
  Current systems: responsibility primarily with developers + deployers; not AI system itself
    (AI systems currently lack moral agency; they cannot be held responsible)

AUTONOMOUS WEAPONS:
  Can autonomous lethal systems make kill decisions without human oversight?
  Deontological: meaningful human control required; machines cannot judge proportionality
  Consequentialist: might reduce casualties if more accurate than humans under stress
  IHL (International Humanitarian Law): distinction, proportionality, precaution must be applied
    Unclear how autonomous systems can satisfy IHL requirement for judgment
  Ongoing international debate; no binding treaty yet (as of 2025)
```

---

## Decision Cheat Sheet

| Theory | Core Question | Strength | Weakness |
|--------|--------------|----------|---------|
| Act utilitarianism | What action maximizes welfare? | Systematic; considers all affected | Permits rights violations; too demanding |
| Rule utilitarianism | What rules maximize welfare? | More aligned with common sense | Collapses to act util in exceptional cases |
| Kantian deontology | What can I universalize? | Rights-respecting; agent-relative | Rigid; can't break small rule to prevent disaster |
| Prima facie duties (Ross) | Which duty is stronger here? | Realistic pluralism; allows conflict | No decision procedure; requires judgment |
| Virtue ethics | What would a virtuous person do? | Character development; practical wisdom | Less action-guiding; culture-relative? |
| Contractualism (Scanlon) | Could anyone reasonably reject this? | Respects persons; non-aggregative | Indeterminacy of "reasonable rejection" |

---

## Common Confusion Points

**Relativism ≠ moral pluralism:** Moral pluralism says there are multiple genuine moral considerations that sometimes conflict (Ross's prima facie duties). Moral relativism says there are no objective moral facts. Pluralism is widely held; strong relativism is largely rejected.

**Consequentialism doesn't always justify the obvious bad things:** Rule utilitarianism, satisficing utilitarianism, and indirect utilitarianism all generate more rule-following behavior than naive act utilitarianism. The "harvest organs to save five" objection is against act utilitarianism specifically.

**Kant's categorical imperative has multiple formulations:** The universalizability formula and the humanity formula are both versions of the same underlying principle (according to Kant) but generate different intuitions. When using Kantian arguments, specify which formulation.

**Effective altruism ≠ utilitarianism:** EA is a practical movement applying quantitative reasoning to doing good; it's influenced by but not identical to utilitarian theory. Many EA practitioners are moral uncertainty-enjoyers who take multiple moral theories seriously and apply them probabilistically.

**AI alignment is as much a philosophy problem as a technical one:** The technical challenge of aligning AI to human values presupposes knowing what human values are — a question with no single answer due to human diversity, preference formation under constraint, and metaethical uncertainty. The Arrow impossibility theorem applies directly to any claim that AI can be aligned to "human values" as an aggregate.
