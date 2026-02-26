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

## 2b. Care Ethics

```
CARE ETHICS (Carol Gilligan, Nel Noddings, Virginia Held):
  Critique of dominant frameworks: Kant, Mill, and Rawls all theorize
    ethics in terms of abstract principles, impartial reason, universal
    rules. Care ethics says this misses a central dimension of moral life.

  CORE CLAIMS:
    (1) Particular relationships generate particular obligations that
        cannot be captured by universal principles.
        My obligation to my child is different from my obligation to a
        stranger — not because I value my child more "impartially" but
        because the relationship itself is morally significant.
    (2) Care — attention, responsiveness, taking the other's needs
        seriously — is a fundamental moral value, not derived from utility
        or duty.
    (3) Context matters: moral decisions are embedded in relationships,
        history, and concrete circumstances, not abstract "principles"
        applied universally.

  GILLIGAN'S CRITIQUE OF KOHLBERG:
    Kohlberg's moral development scale placed abstract rule-following
    (Stage 6: universal justice principles) at the top.
    Gilligan: women in his studies scored lower not because they were
    less developed but because they were using a different but equally
    valid moral framework — one oriented toward care, relationships,
    and context rather than universal rules.
    NOT: women care, men reason. Claim is: two moral orientations exist;
    the dominant framework undervalued one.

  RELATION TO OTHER THEORIES:
    Care ethics vs. Kantian deontology: Kant requires impartiality —
      treat everyone by the same universal law. Care ethics: special
      obligations to particular people are not a bias to be overcome;
      they are central to morality.
    Care ethics vs. utilitarianism: utilitarian calculation aggregates
      welfare impersonally. Care ethics: the relationship between the
      one caring and the one cared-for cannot be dissolved into utility.
    Care ethics vs. virtue ethics: closest relative; virtue ethics also
      emphasizes character and context. Care ethics specifies which virtue
      (care) is primary and emphasizes relational context more heavily.

  ENGINEERING RELEVANCE:
    Software teams as caring relationships: engineering management that
      takes care seriously (mentoring, attention to individual engineers'
      needs, not treating engineers as interchangeable resources) maps
      onto care ethics.
    Product design: attention to vulnerable users (elderly, low-literacy,
      users in crisis) — whose particular needs are not captured by
      aggregate preference data — is a care-ethics intervention in design.
    AI systems: an AI assistant that genuinely "cares" in the care-ethics
      sense would attend to the individual user's particular situation,
      not just apply universal policy rules (deontological) or maximize
      aggregate welfare (utilitarian). Current systems do the latter two.
```

## 2c. Applied Ethics — Bioethics, Climate, Business, Animal Ethics

```
BIOETHICS (Beauchamp and Childress, Principles of Biomedical Ethics, 1979):
  Four principles framework — the dominant practical framework in medicine:
    Autonomy: respect patient's right to make informed decisions.
    Beneficence: act in the patient's best interest.
    Non-maleficence: do no harm (first, do no harm — primum non nocere).
    Justice: fair distribution of benefits and burdens; equitable access.
  These principles can conflict: autonomy (patient refuses treatment) vs.
    beneficence (doctor believes treatment is necessary).
  Informed consent: the autonomy principle operationalized.
    Must be voluntary, informed, and competent.
  RELEVANCE TO AI SYSTEMS IN HEALTHCARE:
    Clinical AI (diagnosis, treatment recommendation): autonomy requires
      explainability and patient override. Beneficence requires accuracy.
    Research: data consent under changing models of privacy.
    Genetic data: special category — family implications extend beyond
      the individual consenting.

CLIMATE ETHICS:
  Intergenerational justice: we emit carbon; future generations bear
    the cost. Standard utilitarian calculation applies; discount rate
    matters enormously. Stern Review: ~1.4% discount rate → aggressive
    mitigation justified. Nordhaus: 5% discount rate → less urgent.
    Philosophical question: what discount rate is ethically defensible
    for welfare of future people?
  Rights-based approaches: future people have rights that present
    generations cannot permissibly violate. Rights don't diminish with
    distance in time (why should they?).
  Collective action problem: climate is a commons. Game-theoretically,
    defecting (emitting) dominates regardless of others' actions.
    Carbon markets, treaties, and carbon taxes are institutional
    responses to the commons problem — but presuppose a political
    authority capable of enforcement.
  RELEVANCE: AI training compute is energy-intensive. Data centers are
    a growing fraction of global electricity demand. Climate ethics
    applies to infrastructure decisions at scale.

BUSINESS ETHICS:
  Shareholder vs. stakeholder theory:
    Friedman (1970): the social responsibility of business is to increase
      its profits (within legal/ethical rules). Managers are agents of
      shareholders; pursuing other goals is misappropriation.
    Freeman (1984): stakeholder theory — corporations have obligations to
      employees, customers, suppliers, communities, as well as shareholders.
      Sustainable value creation requires balancing all stakeholders.
  Corruption and collective action: bribery in international markets —
    if everyone does it, not paying is a competitive disadvantage.
    FCPA (Foreign Corrupt Practices Act) and UK Bribery Act: legal
    responses that attempt to level the coordination equilibrium.
  Whistleblowing: when is employee loyalty overridden by obligations
    to broader publics? Deontological: duty to prevent wrongdoing.
    Consequentialist: weigh harms of silence vs. harms of disclosure.
  RELEVANCE: AI companies making decisions about disclosure of safety
    findings, use of training data, engagement with authoritarian
    governments — all structurally identical to classic business ethics problems.

ANIMAL ETHICS:
  Peter Singer (utilitarian): if an animal can suffer, it is morally
    considerable. Factory farming causes immense suffering to billions
    of animals; the ethical arithmetic is clear. "Animal liberation"
    does not require animals to have rights — just that their suffering
    counts in utilitarian calculation.
  Tom Regan (rights-based): animals that are "subjects-of-a-life"
    (have beliefs, desires, preferences, a welfare that matters to them)
    have inherent value that cannot be traded off for utility.
    Rights, not just interests, should protect them.
  Contractarian response: moral obligations arise from contract-like
    relationships; animals cannot be parties to contracts → no direct
    obligations to animals (only indirect obligations not to be cruel,
    for what it does to us). Most philosophers find this unsatisfying.
  RELEVANCE TO AI: What confers moral status? If it's sentience/suffering
    → animals qualify; some future AI might qualify.
    If it's rationality/contract capacity → neither does.
    The same framework structures both debates.
```

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

## Bridge — Ethics and Engineering Practice

```
ETHICAL THEORY                   ENGINEERING ORGANIZATION PARALLEL
─────────────────────────────────────────────────────────────────
Deontology (follow the rule):    Process culture:
Some actions are prohibited      Code review is mandatory. Security
regardless of consequences.      sign-off is mandatory. Tests must
"Never ship without a test."      pass before merge. These are
"Never expose PII in logs."       deontological constraints —
Rules apply universally;          rule-following even when bypassing
no trade-off against utility.     them might produce better outcomes
                                  in a specific case.

Consequentialism (it works):     Ship-it culture:
Evaluate actions by outcomes.    "What matters is whether it works
Maximize aggregate value;         in production." Feature velocity
individual rule violations        trumps process compliance. A/B
justified by net positive         testing as empirical ethics:
outcomes.                         outcomes are the measure.
                                  The right decision is the one
                                  with better user metrics.

The engineering ethics tension:  Code review culture (deontological)
Every engineering leader         vs. sprint velocity (consequentialist)
navigates the trade-off daily.   is the same argument as Kant vs. Mill,
                                 applied to your team's norms.

Virtue ethics (character):       Engineering culture as character:
Not "what rule?" or "what        "What would a senior engineer do
outcome?" but "what would         here?" Hiring for values, not just
a person of good character do?"  skills. The "brilliant jerk" problem:
Character is stable; it guides   high consequentialist output, bad
novel situations where no rule   virtue character. Most engineering
pre-exists.                      orgs choose character over output.

Care ethics (relationships):     Engineering management:
Particular relationships         1:1s, mentoring, attention to
generate particular obligations.  individual engineers' growth.
Not "apply the rule to           "Treating engineers as replaceable
everyone equally" but            resources" is the care-ethics failure.
"what does this person need?"    Google's Project Aristotle: psychological
                                 safety (a care-ethics concept) was the
                                 top predictor of team performance.

Contractualism (Scanlon):        API design / platform governance:
An act is wrong if it violates   "Could any platform participant
principles no one could          reasonably reject this API contract?"
reasonably reject.               If you design an API that works for
                                 your use case but systematically
                                 disadvantages third-party developers,
                                 those developers could reasonably
                                 reject the principle underlying it.
                                 Platform ethics = contractualism
                                 applied to multi-sided systems.

Rawlsian veil of ignorance:      Inclusive design / accessibility:
Design principles not knowing    Design the system not knowing
your position in the system.     whether you are a power user or a
                                 low-vision user on a slow connection.
                                 WCAG and accessibility standards
                                 are Rawlsian: optimize for the least
                                 advantaged user, not the modal user.
```

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
