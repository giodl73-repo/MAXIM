# 02 — Eval Harness Engineering

> "An LLM without an eval harness is like a service without tests or metrics.
>  You ship, you pray, you have no signal." — production AI engineering axiom

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        LLM EVAL ECOSYSTEM                                   │
│                                                                             │
│  ┌─────────────────────────────────────────────────────────────────────┐    │
│  │  EVAL PIPELINE (mirrors your CI/CD pipeline)                        │   │
│  │                                                                     │   │
│  │  Dataset ──► Prompt Template ──► Model Call ──► Scoring ──► Report │   │
│  │     │              │                  │              │              │   │
│  │  test cases    system prompt +   API call(s)   rubrics /       pass/   │   │
│  │  golden set    few-shot exs     (real model)   LLM-as-judge   fail/   │   │
│  │  edge cases    variable fill    or mock        metrics         score  │   │
│  └─────────────────────────────────────────────────────────────────────┘   │
│                                                                             │
│  TOOLING LAYER                                                              │
│  ┌───────────┐  ┌───────────┐  ┌───────────┐  ┌───────────┐              │
│  │ PromptFoo │  │Braintrust │  │   RAGAS   │  │ LangSmith │              │
│  │(YAML-first│  │(SDK-first │  │(RAG-spec. │  │(tracing + │              │
│  │ open src) │  │ cloud UI) │  │ metrics)  │  │ datasets) │              │
│  └───────────┘  └───────────┘  └───────────┘  └───────────┘              │
│                                                                             │
│  SCORING STRATEGIES                                                         │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐     │
│  │  Exact /    │  │  Embedding  │  │ LLM-as-judge│  │   Human     │     │
│  │  Regex      │  │  Similarity │  │  (rubric)   │  │   Review    │     │
│  └─────────────┘  └─────────────┘  └─────────────┘  └─────────────┘     │
│  deterministic ◄──────────────────────────────────────► probabilistic     │
└─────────────────────────────────────────────────────────────────────────────┘
```

The eval harness is to LLM engineering what the test suite is to software engineering.
The gap: software tests are deterministic. LLM outputs are probabilistic stochastic sequences.
That changes everything about how you design, score, and gate on evals.

If you've built SLO/error-budget pipelines or property-based test suites, the structural
mapping is direct:

```
Software quality engineering         LLM eval harness equivalent
──────────────────────────────────   ──────────────────────────────────────────────
Test fixture corpus                → Eval dataset
  (input + expected output pairs)      (prompt vars + golden outputs + rubrics)

Property-based assertion           → LLM-as-judge scorer
  (does output satisfy invariant?)     (does response satisfy this rubric?)

SLO / error budget                 → Scoring threshold
  (99.9% uptime, < 50ms p99)          (>= 0.85 average score = deployable)

Canary analysis / baseline gate    → Regression gate vs. baseline experiment
  (new deploy must not regress          (new prompt/model must not drop > 5%
   key SLI vs. previous version)         from last known-good baseline)

Test pyramid (unit/int/e2e)        → Eval pyramid (deterministic / semantic / human)
  (fast cheap tests at base,            (exact-match + regex at base,
   slow expensive at top)               LLM-judge for semantics, human review at top)
```

The LLM-specific wrinkle: you cannot binary-pass/fail a probabilistic system. You measure
*distributions* of output quality against *thresholds*, and gate on *regression from baseline*
rather than on absolute correctness. Everything else — test case management, CI integration,
regression alerting — is standard quality engineering.

---

## Why Evals Exist — The Problem Space

### The Regression Problem

With traditional software, regression is binary: test passes or fails. With LLMs:

```
Prompt: "Summarize this support ticket in one sentence."
Model A output: "Customer can't log in."          ← acceptable
Model B output: "Customer is unable to login."    ← acceptable (synonym)
Model C output: "Login issues reported."          ← acceptable (different structure)
Model D output: "We should fix this bug."         ← WRONG (wrong voice)
Model E output: "Customer can't log in to the..."  ← WRONG (truncated)
```

No string-match test can catch this correctly. You need *rubric-based* scoring.

### The Four Failure Modes Evals Catch

```
┌─────────────────────────────────────────────────────────────┐
│  FAILURE MODE         │  EXAMPLE                            │
├───────────────────────┼─────────────────────────────────────┤
│  Regression           │  prompt change → worse outputs     │
│  Model drift          │  provider updates model silently   │
│  Prompt injection     │  user input hijacks system prompt  │
│  Distribution shift   │  prod data ≠ dev test data         │
└─────────────────────────────────────────────────────────────┘
```

An eval harness gives you a signal on all four. Without it, you learn about failures
from user complaints — the worst possible feedback loop.

---

## Anatomy of an Eval

```
┌─────────────────────────────────────────────────────────────────────┐
│  EVAL = Dataset × Prompt × Scoring × Threshold                      │
│                                                                     │
│  Dataset:    test cases with (input, [expected output], [metadata]) │
│  Prompt:     the template under test (system + user, with vars)     │
│  Scoring:    one or more scorers applied to each output             │
│  Threshold:  what score constitutes pass — gates deployment         │
└─────────────────────────────────────────────────────────────────────┘
```

### Test Case Anatomy

```json
{
  "vars": {
    "ticket_text": "I can't log in since the update.",
    "language": "en"
  },
  "assert": [
    { "type": "contains", "value": "log" },
    { "type": "not-contains", "value": "We should" },
    { "type": "llm-rubric",
      "value": "Response summarizes the issue in one sentence without advice" }
  ]
}
```

- `vars` fill your prompt template
- `assert` is an array — multiple scorers run in parallel, all must pass
- Mix deterministic assertions (contains, regex) with LLM-based rubrics

---

## Scoring Strategies

### Taxonomy

```
DETERMINISTIC                              PROBABILISTIC
     │                                          │
     ├── Exact match                            ├── Embedding similarity (cosine)
     ├── Contains / not-contains               ├── LLM-as-judge (rubric)
     ├── Regex                                 ├── ROUGE / BLEU (NLP metrics)
     ├── JSON schema valid                     └── Human review
     ├── Starts-with / ends-with
     └── Levenshtein / edit distance

Use deterministic where possible. Add LLM-as-judge for semantic/subjective dimensions.
```

### LLM-as-Judge

The key insight: use a capable model (Claude Opus, GPT-4o) to score outputs from a
weaker/faster model. The judge receives:
- The original prompt (or just the user query)
- The model's output
- A rubric defining what "good" means

```
JUDGE PROMPT TEMPLATE:
─────────────────────
System: You are an eval judge. Score the response on the rubric.
        Return JSON: { "score": 0-1, "reasoning": "..." }

User:
  [ORIGINAL QUERY]
  {{ query }}

  [RESPONSE TO EVALUATE]
  {{ output }}

  [RUBRIC]
  Score 1.0 if: response is factually correct, concise (< 3 sentences),
                uses professional tone, does not hallucinate details.
  Score 0.5 if: correct but verbose or slightly informal.
  Score 0.0 if: incorrect facts, made-up details, or wrong language.
```

**The meta-problem**: your judge can also be wrong. Mitigations:
- Use a stronger model as judge than the model being evaluated
- Validate judge consistency on known good/bad pairs before deploying
- Run judge calibration — does 0.8 mean the same thing across runs?
- Add reasoning field — parse it to catch judge hallucinations

**Cross-provider bias — the most common production pitfall**: Judge models have stylistic
preferences baked in by their own alignment training. A Claude judge tends to rate
Claude-style responses higher (more structured, uses headers, explicitly acknowledges
nuance). An OpenAI judge tends to rate GPT-style responses higher (more direct, fewer
hedges). This is not a bug — it reflects what each model learned "good" looks like.

Implication: **when evaluating a specific provider's output, use a different vendor's
model as judge.** Evaluating Claude outputs? Use GPT-4o as judge, or Gemini. Evaluating
GPT-4o outputs? Use Claude Opus. This cross-vendor pattern reduces in-group bias and
gives you a more neutral signal. For the highest-stakes evals (model selection, safety
thresholds), use both a same-vendor and a cross-vendor judge and compare — large
disagreement is itself a signal worth investigating.

For multi-provider comparisons (A/B between Claude and GPT-4o), use a third-party
judge (Gemini, or a human panel) to avoid both providers' home-field advantage.

### Embedding Similarity

```
output_embedding = embed(actual_output)          # e.g., text-embedding-3-small
expected_embedding = embed(expected_output)

cosine_sim = dot(output_embedding, expected_embedding) /
             (norm(output_embedding) * norm(expected_embedding))

pass = cosine_sim >= 0.85   # threshold tuned per task
```

Better than string match for paraphrased correct answers. Worse than LLM-judge for
structural requirements (tone, format, completeness). Use together.

---

## PromptFoo — Open Source Eval Framework

PromptFoo is the closest thing to "pytest for LLMs." YAML-configured, runs locally
or in CI, supports multiple providers, built-in scorers + custom JS/Python scorers.

### Install and Init

```bash
npm install -g promptfoo
# or: npx promptfoo@latest

promptfoo init          # creates promptfooconfig.yaml
promptfoo eval          # runs the eval suite
promptfoo view          # opens web UI to browse results
```

### Config Structure

```yaml
# promptfooconfig.yaml
description: "Support ticket summarizer eval"

providers:
  - id: anthropic:claude-haiku-4-5-20251001
    config:
      temperature: 0
  - id: openai:gpt-4o-mini
    config:
      temperature: 0

prompts:
  - file://prompts/summarizer.txt    # load from file
  - "Summarize this ticket: {{ticket}}"  # or inline

tests:
  - vars:
      ticket: "I can't log in since the latest update."
    assert:
      - type: contains
        value: "log in"
      - type: llm-rubric
        value: "One sentence summary of the issue, no advice"
      - type: not-contains
        value: "We should"

  - vars:
      ticket: "My password reset email never arrived."
    assert:
      - type: regex
        value: "(password|email|reset)"
      - type: llm-rubric
        value: "Correctly identifies missing email as the issue"

  - file://tests/edge-cases.yaml     # load bulk test cases from file
```

### Prompt Files

```
# prompts/summarizer.txt
system: |
  You are a support ticket summarizer.
  Output exactly one sentence in {{language}}.
  Do not give advice. Do not use first person.

user: |
  Ticket: {{ticket}}
```

Variables `{{ticket}}` and `{{language}}` are filled from the test case `vars`.

### Running and Comparing Providers

```bash
# Run and compare all providers side-by-side
promptfoo eval --providers anthropic:claude-haiku-4-5 openai:gpt-4o-mini

# Run specific test file
promptfoo eval -c promptfooconfig.yaml

# Output formats
promptfoo eval --output results.json
promptfoo eval --output results.csv

# CI mode (exit 1 on failure)
promptfoo eval --ci
```

The web UI (`promptfoo view`) shows a matrix of provider × test case × score,
making it trivial to see where one model is better than another.

### Custom Scorer (JavaScript)

```javascript
// scorers/length-check.js
module.exports = async (output, context) => {
  const sentences = output.split(/[.!?]+/).filter(Boolean);
  return {
    pass: sentences.length === 1,
    score: sentences.length === 1 ? 1 : 0,
    reason: `Response has ${sentences.length} sentence(s), expected 1`
  };
};
```

```yaml
# Reference in config
assert:
  - type: javascript
    value: file://scorers/length-check.js
```

### Red-Teaming with PromptFoo

```bash
promptfoo redteam init     # scaffolds a red-team config
promptfoo redteam run      # runs attack battery against your prompt
```

PromptFoo's red-teaming generates adversarial test cases: prompt injections,
jailbreak attempts, PII extraction probes, hallucination induction. Runs them
against your deployed system prompt + provider.

---

## Braintrust — SDK-First Eval Platform

Where PromptFoo is config/CLI-first, Braintrust is SDK + cloud-UI first.
Better for complex eval logic in code, dataset versioning, A/B experiment tracking.

### Core Concepts

```
┌─────────────────────────────────────────────────────────────┐
│  BRAINTRUST PRIMITIVES                                      │
│                                                             │
│  Project      = namespace (one per product/feature)         │
│  Dataset      = versioned set of test cases                 │
│  Experiment   = one eval run (prompt + model + date)        │
│  Score        = numeric 0-1 per criterion per test case     │
│  Comparison   = diff between two experiments                │
└─────────────────────────────────────────────────────────────┘
```

### SDK Usage (TypeScript)

```typescript
import { Braintrust, Eval, Score } from "braintrust";
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic();

// Define the task (what you're testing)
async function summarizeTicket(input: { ticket: string }): Promise<string> {
  const msg = await client.messages.create({
    model: "claude-haiku-4-5-20251001",
    max_tokens: 100,
    system: "Summarize in one sentence. No advice.",
    messages: [{ role: "user", content: input.ticket }],
  });
  return (msg.content[0] as { type: "text"; text: string }).text;
}

// Define scorers
function exactSentenceCount(output: string): Score {
  const count = output.split(/[.!?]+/).filter(Boolean).length;
  return {
    name: "single-sentence",
    score: count === 1 ? 1 : 0,
    metadata: { sentence_count: count },
  };
}

// Run the eval
await Eval("support-summarizer", {
  data: () => [
    { input: { ticket: "Can't log in" }, expected: "Login issue reported" },
    { input: { ticket: "Password reset not received" }, expected: "Password email missing" },
  ],
  task: summarizeTicket,
  scores: [
    exactSentenceCount,
    // Braintrust built-ins:
    // LLMClassifier — LLM-as-judge with custom rubric
    // Factuality — checks factual accuracy against expected
    // Similarity — embedding cosine similarity
  ],
});
```

### Experiment Comparison

```bash
braintrust eval --experiment "claude-haiku-baseline"
# Change prompt or model...
braintrust eval --experiment "claude-haiku-v2"
# UI shows side-by-side diff of scores, regressions highlighted
```

The Braintrust UI is its main advantage: interactive drill-down on individual
test cases, score distributions, regression diffs between experiments.
Think: Azure DevOps test analytics, but for LLM outputs.

---

## RAGAS — RAG-Specific Eval Metrics

RAGAS (Retrieval Augmented Generation Assessment) is a Python framework
specifically for evaluating RAG pipelines. Different problem than general LLM eval.

### RAG Eval Has Two Dimensions

```
┌─────────────────────────────────────────────────────────────────────┐
│  RAG PIPELINE                                                       │
│                                                                     │
│  Query ──► Retrieval ──► Augmented Prompt ──► Generation ──► Answer│
│               │                                    │                │
│           RETRIEVAL                            GENERATION           │
│           QUALITY                              QUALITY              │
│                                                                     │
│  Context Recall      ←── did we fetch the right docs?               │
│  Context Precision   ←── did we fetch only relevant docs?           │
│  Answer Faithfulness ←── does answer stick to retrieved context?    │
│  Answer Relevancy    ←── does answer address the question?          │
└─────────────────────────────────────────────────────────────────────┘
```

### RAGAS Metrics in Detail

| Metric | What It Measures | How Computed |
|--------|-----------------|--------------|
| **Context Recall** | % of ground-truth answer attributable to retrieved context | LLM breaks answer into statements, checks each against context |
| **Context Precision** | % of retrieved chunks actually useful | LLM judges each chunk's relevance to question |
| **Faithfulness** | Answer grounded in context (no hallucination) | LLM extracts claims from answer, verifies each in context |
| **Answer Relevancy** | Answer addresses the question | Reverse-generates questions from answer, checks similarity to original |

High faithfulness + low answer relevancy = your RAG refuses to hallucinate but
won't extrapolate even when it should. Tune context window and prompt accordingly.

### Usage

```python
from ragas import evaluate
from ragas.metrics import (
    context_recall,
    context_precision,
    faithfulness,
    answer_relevancy,
)
from datasets import Dataset

# Your RAG pipeline output
data = {
    "question": ["What causes ReDoS?", "What is KV cache?"],
    "answer": ["ReDoS is caused by catastrophic backtracking in NFA-based engines.",
               "KV cache stores key-value pairs from prior tokens to avoid recomputation."],
    "contexts": [
        [["ReDoS arises when NFA engines explore exponential paths..."]],
        [["The KV cache holds attention keys and values for all previous tokens..."]],
    ],
    "ground_truth": [
        "ReDoS is caused by catastrophic backtracking in NFA engines.",
        "KV cache avoids recomputing attention over prior tokens.",
    ],
}

dataset = Dataset.from_dict(data)
result = evaluate(dataset, metrics=[context_recall, context_precision,
                                     faithfulness, answer_relevancy])
print(result)
# {'context_recall': 0.92, 'context_precision': 0.88,
#  'faithfulness': 0.95, 'answer_relevancy': 0.90}
```

### When to Use RAGAS vs PromptFoo vs Braintrust

```
┌────────────────────────────────────────────────────────────────┐
│  USE CASE                      │  TOOL                         │
├────────────────────────────────┼──────────────────────────────┤
│  Simple LLM app, open source   │  PromptFoo                   │
│  Multi-provider comparison     │  PromptFoo                   │
│  Red-teaming / adversarial     │  PromptFoo                   │
│  Complex eval logic in code    │  Braintrust                  │
│  Team collaboration, UI-first  │  Braintrust                  │
│  A/B experiment tracking       │  Braintrust                  │
│  RAG pipeline specifically     │  RAGAS                       │
│  Tracing + eval combined       │  LangSmith                   │
│  Custom, zero-dependency       │  Roll your own (see below)   │
└────────────────────────────────┴──────────────────────────────┘
```

---

## LangSmith — Tracing + Eval Combined

LangSmith solves a different problem: not just offline eval, but *production tracing*
with the ability to push production traces back into eval datasets.

```
┌─────────────────────────────────────────────────────────────────────┐
│  LANGSMITH FLYWHEEL                                                 │
│                                                                     │
│  Production ──► Traces ──► Interesting trace? ──► Add to dataset    │
│                                │                        │           │
│                           stored in                  becomes a      │
│                           LangSmith                  test case      │
│                                                          │          │
│                                       Eval suite ◄───────┘          │
│                                           │                         │
│                                    run on next                      │
│                                    deployment                       │
└─────────────────────────────────────────────────────────────────────┘
```

The key workflow: prod traces become eval test cases. This closes the
distribution shift problem — your evals eventually mirror real production inputs.

### SDK Integration

```python
from langsmith import Client
from langchain_anthropic import ChatAnthropic

# Tracing happens automatically when LANGCHAIN_TRACING_V2=true
import os
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = "..."
os.environ["LANGCHAIN_PROJECT"] = "support-summarizer"

llm = ChatAnthropic(model="claude-haiku-4-5-20251001")
# Every call auto-traced to LangSmith
result = llm.invoke("Summarize: Can't log in since update.")
```

---

## Rolling Your Own Eval Harness

Sometimes the right answer is a 200-line Python script. All eval frameworks are
wrappers around the same loop:

```python
import asyncio
import json
from anthropic import Anthropic
from dataclasses import dataclass

@dataclass
class TestCase:
    input: dict
    expected: str | None = None
    tags: list[str] = None

@dataclass
class EvalResult:
    test_case: TestCase
    output: str
    scores: dict[str, float]
    passed: bool

# The core eval loop — everything else is wrapper
async def run_eval(
    test_cases: list[TestCase],
    task_fn,           # your LLM call
    scorers: list,     # scoring functions
    pass_threshold: float = 0.8,
) -> list[EvalResult]:
    results = []
    for tc in test_cases:
        output = await task_fn(tc.input)
        scores = {s.__name__: s(output, tc) for s in scorers}
        avg_score = sum(scores.values()) / len(scores)
        results.append(EvalResult(tc, output, scores, avg_score >= pass_threshold))
    return results

# LLM-as-judge scorer (reusable)
def make_llm_judge(rubric: str, judge_model: str = "claude-opus-4-6"):
    client = Anthropic()

    def scorer(output: str, tc: TestCase) -> float:
        response = client.messages.create(
            model=judge_model,
            max_tokens=256,
            system="You are an eval judge. Return JSON: {\"score\": 0.0-1.0, \"reason\": \"...\"}",
            messages=[{
                "role": "user",
                "content": f"Query: {tc.input}\nOutput: {output}\nRubric: {rubric}"
            }]
        )
        try:
            data = json.loads(response.content[0].text)
            return float(data["score"])
        except Exception:
            return 0.0  # judge failure = score 0

    scorer.__name__ = "llm_judge"
    return scorer
```

When to roll your own:
- No external dependencies in prod (compliance/cost)
- Need deep integration with existing test infra
- Eval logic is complex enough that YAML config is a liability
- You want full control over judge prompts and retry logic

---

## Eval-as-CI-Gate

The end goal: evals run in CI on every PR, block deployment on regression.

```yaml
# .github/workflows/eval.yml
name: LLM Eval

on:
  pull_request:
    paths:
      - 'src/prompts/**'
      - 'src/llm/**'

jobs:
  eval:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: '20'

      - name: Install PromptFoo
        run: npm install -g promptfoo

      - name: Run evals
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
          OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY }}
        run: |
          promptfoo eval --ci --output results.json
          # --ci flag: exit code 1 if any assert fails

      - name: Upload eval results
        if: always()
        uses: actions/upload-artifact@v4
        with:
          name: eval-results
          path: results.json

      - name: Comment PR with results
        if: always()
        uses: actions/github-script@v7
        with:
          script: |
            const results = require('./results.json');
            const passed = results.results.filter(r => r.success).length;
            const total = results.results.length;
            const body = `### LLM Eval Results\n\n✅ ${passed}/${total} passed`;
            github.rest.issues.createComment({
              ...context.repo,
              issue_number: context.issue.number,
              body
            });
```

### Practical Gate Thresholds

```
┌─────────────────────────────────────────────────────────────────────┐
│  WHAT TO GATE ON                                                    │
│                                                                     │
│  ✅ Gate hard:   any deterministic assert fails (regex, schema)     │
│  ✅ Gate hard:   LLM score drops > 5% from baseline                 │
│  ⚠️  Warn only:  LLM score drops 1-5% (subjective judgment call)   │
│  ✅ Gate hard:   red-team pass rate drops (security regression)     │
│  ℹ️  Log only:   cost increase (alert but don't block)               │
└─────────────────────────────────────────────────────────────────────┘
```

**Critical anti-pattern**: gating on absolute score thresholds. A score of 0.85
means nothing without a baseline. Gate on *regression from baseline*, not
on a magic number. Establish your baseline on the commit that ships to prod,
then block any PR that drops below it.

---

## Dataset Engineering

The most important part of eval harness engineering isn't the tooling — it's the
dataset. Garbage test cases → green evals that miss real failures.

### Test Case Sources

```
┌─────────────────────────────────────────────────────────────────────┐
│  DATASET SOURCE HIERARCHY (most to least valuable)                  │
│                                                                     │
│  1. Real production inputs (sampled + de-identified)                │
│     Catches distribution shift. Hardest to get.                     │
│                                                                     │
│  2. Expert-curated golden set                                       │
│     Hand-authored by domain experts. Covers known edge cases.       │
│                                                                     │
│  3. Adversarial / red-team cases                                    │
│     Injection attacks, edge case inputs, length extremes.           │
│                                                                     │
│  4. Synthetic — LLM-generated                                       │
│     Fast to create, cheap. Risk: generator bias.                    │
│     Validate before promoting to golden set (see process below).    │
│                                                                     │
│  5. Parametric / property-based (see 19-TESTING-EVOLUTION.md)       │
│     Generate from a distribution. Finds boundary failures.          │
└─────────────────────────────────────────────────────────────────────┘
```

**Synthetic data validation — promotion gate process**:

Synthetic cases generated by model A share model A's blind spots. You cannot use model
A to validate its own outputs (closed-loop bias). Promotion gate:

```
Step 1: Generate with model A (e.g., GPT-4o)
  → Produce (input, expected_output) pairs at scale

Step 2: Human spot-check — random sample 10–20% of generated cases
  → Domain expert reviews: is the expected_output actually correct?
  → Mark each reviewed case as valid / invalid / needs_edit
  → Reject the batch if error rate > 5%; adjust generation prompt

Step 3: Cross-model grade with model B (different vendor, e.g., Claude)
  → For each synthetic case, have model B score expected_output against rubric
  → Model B has different blind spots — disagreement surfaces generator bias

Step 4: Promote only cases where human_review = valid AND model_B_score >= threshold
  → Rejected cases: discard or fix and re-review
  → Accepted cases: add to golden set with source = "synthetic:modelA:vYYYY-MM"

Step 5: Track synthetic vs. human-authored case performance separately
  → If synthetic cases have 10% higher pass rate than human cases, they're too easy
  → Synthetic set should have similar difficulty distribution to human-authored set
```

The generator bias warning: both generator (model A) and judge (model B) share
an RLHF-shaped view of "good." Seed the golden set with at least 20–30% human-authored
cases to anchor the difficulty baseline before scaling with synthetic generation.

### Golden Set Maintenance

```
Rule 1: Never delete, only mark superseded.
Rule 2: When a test case fails legitimately (prompt evolved), update expected,
         not the case.
Rule 3: Tag cases by dimension: [factual, tone, format, safety, edge-case].
         Run dimension-sliced reports.
Rule 4: Track which cases have caught regressions. Cases with zero catches
         may be redundant.
Rule 5: Add a new case for every production bug that slipped through evals.
```

---

## Metrics Reference

### Standard LLM Eval Metrics

| Metric | Range | Measures | When to Use |
|--------|-------|----------|-------------|
| **BLEU** | 0-1 | n-gram overlap vs reference | Translation, exact output tasks |
| **ROUGE-L** | 0-1 | Longest common subsequence | Summarization |
| **BERTScore** | 0-1 | Embedding similarity (contextual) | Paraphrase-tolerant tasks |
| **Factuality** | 0-1 | % claims verifiable in source | QA, RAG |
| **Faithfulness** | 0-1 | Answer grounded in retrieved docs | RAG |
| **Toxicity** | 0-1 | Harmful content probability | Safety |

### RAG-Specific (RAGAS)

| Metric | What Fails When Low |
|--------|---------------------|
| Context Recall | Retriever misses relevant chunks |
| Context Precision | Retriever returns too much noise |
| Faithfulness | Generator hallucinates beyond context |
| Answer Relevancy | Generator ignores the actual question |

### Cost-Aware Eval

```
eval_cost = Σ (judge_calls × judge_tokens × judge_price)
          + Σ (task_calls × task_tokens × task_price)

With 1000 test cases × claude-haiku task (~500 tokens) × claude-opus judge (~1000 tokens):
  Task:  1000 × 500 × $0.00025/1K = $0.125
  Judge: 1000 × 1000 × $0.015/1K  = $15.00
  Total: ~$15/eval run
```

Running evals on every commit is expensive. Strategies:
- Run full eval suite on PR to main; run fast subset (100 cases) on feature branches
- Cache model responses for deterministic test cases (hash prompt → response)
- Use a cheaper model for judge first pass; escalate to stronger model only for
  borderline cases (0.4–0.6 score range)

---

## Common Confusion Points

**LLM eval vs. traditional test**: Traditional tests are deterministic contracts.
Eval suites are probabilistic quality measurements. Both are needed. Evals do not
replace tests for deterministic logic (JSON parsing, API schema validation, etc.).

**LLM-as-judge bias**: The judge has preferences. A Claude judge may prefer
Claude-style outputs. An OpenAI judge may prefer GPT-style. Use cross-judge
validation for critical evals, or use human calibration to validate judge alignment.

**Score inflation**: Prompting the judge with "be generous" inflates scores but
loses signal. You want a calibrated judge, not a lenient one. A score of 0.75
should consistently mean the same thing.

**One-shot eval vs. continuous eval**: First-time eval setup is the easy part.
The hard part is maintaining the golden set over time, updating scorers as the
task evolves, and preventing score drift where "good enough" creeps downward.

**Evals and model updates**: LLM providers update models without notice. A baseline
established with `claude-haiku-4-5` may silently shift when they release a new
version to the same endpoint. Pin model versions in production; accept version
upgrades only after running the full eval suite.

**Synthetic data loop**: Using a model to generate test cases and the same model
to judge them creates a closed loop. Both generator and judge share the same blind
spots. Always seed with human-authored golden cases.

---

## Decision Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────┐
│  WHAT DO I NEED?              │  DO THIS                            │
├───────────────────────────────┼─────────────────────────────────────┤
│  Quick eval, new feature      │  promptfoo init + 20 test cases    │
│  Compare two models/prompts   │  promptfoo eval --providers A B     │
│  CI gate on regressions       │  promptfoo eval --ci in GitHub Wf   │
│  Complex eval logic in code   │  Braintrust SDK                     │
│  Team reviews + UI            │  Braintrust cloud                   │
│  RAG pipeline quality         │  RAGAS (faithfulness + recall)      │
│  Trace prod + build dataset   │  LangSmith                          │
│  Red-team / adversarial       │  promptfoo redteam                  │
│  Zero external dependencies   │  Roll your own (50-line loop)       │
│  Human in the loop            │  Braintrust annotation queue        │
│                               │  or Argilla                         │
├───────────────────────────────┼─────────────────────────────────────┤
│  SCORER CHOICE                │                                     │
│  Output is structural         │  JSON schema, regex, exact match    │
│  Output is semantic           │  LLM-as-judge with rubric           │
│  Output is a paraphrase       │  Embedding cosine similarity        │
│  Output must match source     │  Faithfulness / RAGAS               │
│  Output is a translation      │  BLEU / BERTScore                   │
└───────────────────────────────┴─────────────────────────────────────┘
```

---

## Connection to the Broader Arc

```
19-TESTING-EVOLUTION.md:
  Era 5 → eval harnesses replace test pyramids for LLM systems

This guide (02-EVALS-HARNESS.md):
  The engineering of those harnesses — tooling, scoring, CI integration

03-ORCHESTRATION.md (next):
  LangChain / LlamaIndex / Semantic Kernel — frameworks that produce
  the traces and outputs these evals measure
```

The eval harness is not a feature you add later. It is the scaffolding you build
before shipping, the same way you wouldn't ship a service without metrics.
The signal it provides — regression detection, model comparison, safety gates —
is the difference between engineering and guessing.
