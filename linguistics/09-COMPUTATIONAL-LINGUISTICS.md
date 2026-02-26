# Computational Linguistics — Formal Grammars, Parsing, NLP

## The Big Picture

Computational linguistics sits at the intersection of linguistics and computer science — using formal tools to model language structure and building systems that process language automatically.

```
+------------------------------------------------------------------+
|              COMPUTATIONAL LINGUISTICS LANDSCAPE                  |
|                                                                  |
|  FORMAL GRAMMARS              PARSING ALGORITHMS                |
|  (CFG, PCFG, CCG, TAG,        (CYK, Earley, chart,             |
|   dependency grammar)          shift-reduce, neural)            |
|                                                                  |
|  CLASSIC NLP PIPELINE         STATISTICAL REVOLUTION            |
|  (tokenize → POS tag →        (IBM alignment models,           |
|   parse → NER → SRL)           n-gram LMs, HMMs, PCFGs)        |
|                                                                  |
|  DISTRIBUTIONAL               NEURAL NLP                        |
|  SEMANTICS                    (word2vec, GloVe, BERT,           |
|  (word2vec, GloVe,             Transformer, LLMs)               |
|   pointwise mutual info)                                        |
|                                                                  |
|  TCS BRIDGES:                                                    |
|  CFG parsing → CYK (O(n³)), Earley (O(n³)),                    |
|  weighted automata, inside-outside algorithm                    |
+------------------------------------------------------------------+
```

---

## Part I: Formal Grammars — The TCS Foundation

### Context-Free Grammar (CFG) — Review from TCS + Syntax

```
CFG = (N, Σ, R, S)
  N   — non-terminals (categories: NP, VP, S, ...)
  Σ   — terminals (words)
  R   — production rules: A → α, where A ∈ N, α ∈ (N ∪ Σ)*
  S   — start symbol

EXAMPLE:
  S  → NP VP
  NP → Det N | Det Adj N | N | NP PP
  VP → V | V NP | V NP PP | V PP
  PP → P NP
  Det → the | a
  N  → cat | dog | mouse | floor
  V  → chased | saw | put
  P  → on | under | near
  Adj → big | small

DERIVATION of "the cat chased a small dog":
  S → NP VP → Det N VP → "the" N VP → "the cat" VP
    → "the cat" V NP → "the cat chased" NP
    → "the cat chased" Det Adj N
    → "the cat chased a small dog"

AMBIGUITY: One string may have multiple parse trees.
  "I saw the man with the telescope"
    Reading 1: [I saw [the man with the telescope]] — man has telescope
    Reading 2: [[I saw the man] with the telescope] — I used telescope to see man
  Two distinct parse trees from same grammar.
```

### Probabilistic CFG (PCFG)

```
PCFG: each production rule has a probability.

  S  → NP VP    [1.0]
  NP → Det N    [0.6]
  NP → Det Adj N [0.2]
  NP → N        [0.2]
  VP → V NP     [0.5]
  VP → V        [0.3]
  VP → V PP     [0.2]

PROBABILITY OF PARSE TREE:
  P(tree) = ∏ P(rule) over all rules used

DISAMBIGUATION: Choose the most probable parse tree.
  P(reading 1) vs P(reading 2) → pick higher probability parse.

TRAINING: Estimate rule probabilities from treebank
  (annotated corpus of parsed sentences — e.g., Penn Treebank)
  MLE: P(A → α) = count(A → α) / count(A)
```

### Chomsky Normal Form (CNF)

Required for CYK algorithm:

```
CHOMSKY NORMAL FORM:
  Every production is either:
  A → B C    (exactly two non-terminals)
  A → a      (exactly one terminal)

  Any CFG can be converted to CNF:
  1. Eliminate ε-productions
  2. Eliminate unit productions (A → B)
  3. Binarize: A → B C D → A → B X, X → C D (introduce new non-terminals)
```

---

## Part II: Parsing Algorithms — The TCS Bridge

### CYK Algorithm — O(n³)

For a grammar in CNF:

```
CYK ALGORITHM (Cocke-Younger-Kasami):
  Input: string w = w₁w₂...wₙ, grammar G in CNF
  Output: membership in L(G) (or parse forest if PCFG)

  TABLE: T[i][j] = set of non-terminals that generate wᵢ...wⱼ

  BASE CASE:
    T[i][i] = {A | A → wᵢ ∈ R}  (single words)

  RECURSIVE CASE:
    T[i][j] = {A | A → B C ∈ R, ∃k: B ∈ T[i][k] ∧ C ∈ T[k+1][j]}

  FINAL: w ∈ L(G) iff S ∈ T[1][n]

COMPLEXITY: O(n³ |G|) where |G| = number of rules
  Three nested loops: i (start), j (end), k (split point)

PCFG VARIANT:
  T[i][j][A] = max probability of A → wᵢ...wⱼ
  Use Viterbi-like dynamic programming
  Find max over all splits k and all rule A → B C
```

Example trace (abbreviated):

```
"the cat saw the dog"
  1     2   3    4   5

T[1][1] = {Det}  (the → Det)
T[2][2] = {N}    (cat → N)
T[3][3] = {V}    (saw → V)
T[4][4] = {Det}  (the → Det)
T[5][5] = {N}    (dog → N)

T[1][2] = {NP | NP → Det N} = {NP}
T[4][5] = {NP | NP → Det N} = {NP}
T[3][5] = {VP | VP → V NP ∧ V ∈ T[3][3] ∧ NP ∈ T[4][5]} = {VP}
T[1][5] = {S | S → NP VP ∧ NP ∈ T[1][2] ∧ VP ∈ T[3][5]} = {S} ✓
```

### Earley Algorithm — O(n³) general, O(n²) unambiguous

Earley parser processes left-to-right, handles any CFG (not just CNF):

```
EARLEY ALGORITHM:
  Earley items: [A → α • β, i]
    — production A → αβ
    — dot (•) shows how far parse has progressed
    — i = start position of this constituent

  OPERATIONS:
  SCANNER:    [A → α • aβ, i] + w_{j} = a → [A → αa • β, i]
  PREDICTOR:  [A → α • Bβ, i] → [B → • γ, j] for all B → γ
  COMPLETER:  [B → γ •, j] + [A → α • Bβ, i] → [A → αB • β, i]

COMPLEXITY:
  O(n³) general, O(n²) for unambiguous grammars, O(n) for some simple grammars.
  Handles arbitrary CFGs (not just CNF) directly.
  Earley parsers are general; CYK requires CNF but is simpler to implement.
```

### Chart Parsing (General Framework)

Both CYK and Earley are **chart parsers** — they share the bottom-up dynamic programming approach of storing partial analyses in a chart to avoid recomputation:

```
CHART = data structure recording all partial parses
  Avoids redundant computation (memoization / tabling)
  Agenda-driven: process edges when "triggered"

VARIANTS:
  Bottom-up chart: CYK-style
  Top-down chart: prediction-first (Earley-style)
  Left-corner: hybrid (prediction + bottom-up)

Neural parsers (2015+) train directly on treebank data.
Chart parsing is the classic algorithm but neural parsers now dominate NLP.
```

---

## Part III: Classic NLP Pipeline

Before deep learning, NLP used a modular pipeline:

```
RAW TEXT
    │
    ▼
TOKENIZATION — split into words, handle punctuation, contractions
    │           "it's" → ["it", "'s"] or ["it's"] depending on task
    ▼
SENTENCE SEGMENTATION — find sentence boundaries
    │                   "Mr. Smith bought shares. He paid $1.2M." → 2 sentences
    ▼
POS TAGGING — assign grammatical category to each token
    │          "The/DT cat/NN sat/VBD on/IN the/DT mat/NN"
    │          (Penn Treebank tagset: DT, NN, VBD, IN, etc.)
    │          Algorithm: HMM Viterbi (1990s), MaxEnt (2000s), neural (2015+)
    ▼
PARSING — syntactic analysis
    │      CFG/PCFG parsing (above), dependency parsing
    ▼
NER — Named Entity Recognition
    │   Identify PERSON/LOCATION/ORGANIZATION/DATE/MONEY tokens
    │   "Barack Obama/PERSON visited Paris/LOCATION in 2010/DATE"
    ▼
COREFERENCE RESOLUTION — find which mentions refer to same entity
    │   "Obama... He said... The president..."  → all Obama
    ▼
SEMANTIC ROLE LABELING (SRL)
    │   "John sold Mary a book yesterday."
    │   John = AGENT, Mary = RECIPIENT, book = THEME, yesterday = TEMPORAL
    ▼
DISCOURSE — RST relations, coherence, QA, summarization
```

**Penn Treebank POS Tags (most common):**

| Tag | Description | Example |
|-----|-------------|---------|
| CC | Coordinating conjunction | and, or |
| DT | Determiner | the, a |
| IN | Preposition or subordinating conjunction | in, of, that |
| JJ | Adjective | big, old |
| NN | Noun, singular or mass | cat, information |
| NNS | Noun, plural | cats |
| NNP | Proper noun, singular | London |
| RB | Adverb | quickly |
| VB | Verb, base form | run |
| VBD | Verb, past tense | ran |
| VBG | Verb, gerund | running |
| VBN | Verb, past participle | run |

---

## Part IV: The Statistical Revolution

Late 1980s–2000s: empiricism displaced rule-based NLP.

### N-gram Language Models

```
N-GRAM LM:
  Model: P(w₁w₂...wₙ) = ∏ᵢ P(wᵢ | wᵢ₋ₙ₊₁...wᵢ₋₁)

  BIGRAM: P(wᵢ | wᵢ₋₁) — probability of word given previous word
  TRIGRAM: P(wᵢ | wᵢ₋₂, wᵢ₋₁) — given two previous words

  MLE: P(w₂|w₁) = count(w₁,w₂) / count(w₁)

  SMOOTHING needed (zero counts):
    Laplace (add-1): P(w₂|w₁) = (count(w₁,w₂)+1) / (count(w₁)+|V|)
    Kneser-Ney: sophisticated backoff + interpolation — long standard baseline
    Perplexity = 2^H where H = entropy of model on test data
```

### HMMs for Sequence Labeling

```
HIDDEN MARKOV MODEL (HMM) for POS tagging:

  States: POS tags (hidden)
  Observations: words (observed)

  PARAMETERS:
    Transition P(tag_i | tag_{i-1}) — from training data
    Emission P(word | tag)          — from training data

  VITERBI: find most likely tag sequence given observed words
  (Dynamic programming — you know this from algorithms class)

  P(tag | word) is not directly modeled — instead:
  argmax_{tags} P(words | tags) × P(tags)   (HMM, generative)

  Maximum Entropy / Log-linear models (2000s):
  argmax_{tags} P(tags | words)  — discriminative, more features
```

### IBM Word Alignment Models

IBM Models 1–5 (1993) — for statistical machine translation:

```
P(f | e) = ∑ over alignments P(f, a | e)

  f = foreign sentence
  e = English sentence
  a = alignment (which foreign word corresponds to which English word)

  EM algorithm learns alignments without supervision from parallel corpora.
  Foundation of statistical MT (Google Translate ~2006–2016).
```

---

## Part V: Distributional Semantics — word2vec / GloVe

Distributional hypothesis (Harris 1954; Firth 1957):

```
"You shall know a word by the company it keeps."
  (Firth, 1957)

Words that appear in similar contexts have similar meanings.
  "dog" and "cat" appear in similar contexts (pets, vet, food, animals)
  → their distributional vectors should be similar.

CLASSICAL APPROACH:
  Co-occurrence matrix M[w][c] = count(w, c in window of size k)
  Dimensionality reduction: SVD (Latent Semantic Analysis)
  Similarity: cosine(M[w₁], M[w₂])
```

### word2vec (Mikolov et al., 2013)

```
word2vec: learn word vectors to predict context from word (or word from context)

SKIP-GRAM MODEL:
  Input: target word w
  Output: predict context words c₁...cₙ (in window around w)

  Maximize: ∑_{t} ∑_{-k≤j≤k, j≠0} log P(w_{t+j} | w_t)

  P(c | w) = exp(v_c · v_w) / ∑_{c'} exp(v_{c'} · v_w)  (softmax)

  NEGATIVE SAMPLING: approximate softmax — sample negative examples
    vs. full vocabulary normalization.

CBOW MODEL: predict target from context (reverse direction)

RESULT: dense vectors (typically 100–300 dimensions) where:
  vector("king") - vector("man") + vector("woman") ≈ vector("queen")
  Arithmetic on meaning! — semantic compositionality in vector space.
```

### GloVe (Pennington et al., 2014)

```
GloVe (Global Vectors):
  Explicitly models log of co-occurrence counts
  Loss function:
    ∑_{i,j} f(X_{ij}) (v_i · ṽ_j + b_i + b̃_j - log X_{ij})²

  X_{ij} = count(word i, context j)
  f(X) = weighting function (down-weights very frequent pairs)

  Advantage over word2vec: explicitly uses global corpus statistics
  rather than local window predictions.
  Both produce similar quality vectors in practice.
```

---

## Part VI: Transformers as Linguistic Models

The Transformer (Vaswani et al., 2017) changed NLP entirely. From a linguistic perspective:

```
TRANSFORMER ARCHITECTURE (simplified):
  Input: sequence of tokens w₁...wₙ
  Tokenization: subword (BPE, WordPiece, SentencePiece)
    "tokenization" → ["token", "##ization"] (BERT WordPiece)
    "unbelievable" → ["un", "##believe", "##able"]

  SELF-ATTENTION (the key mechanism):
    For each token, compute attention over all other tokens.
    h_i = ∑_j α_{ij} v_j   where α_{ij} = softmax(q_i · k_j / √d)

    q (query), k (key), v (value) are learned projections.
    Attention = weighted sum of values, weighted by query-key similarity.

  MULTI-HEAD ATTENTION:
    H parallel attention heads → different "aspects" of meaning
    (some heads capture syntax, some semantics, some coreference — empirically)

  POSITIONAL ENCODING:
    No recurrence — position encoded as sinusoidal or learned embeddings.

BERT (Bidirectional Encoder Representations from Transformers):
  Pre-trained on masked language modeling (predict masked tokens)
  and next sentence prediction.
  Produces CONTEXTUAL word embeddings — same word gets different vectors
  in different contexts ("bank" in "river bank" ≠ "bank account").
  Fine-tuned on downstream tasks (classification, NER, QA).

GPT family:
  Decoder-only transformer, autoregressive language modeling.
  Predict next token given all previous tokens.
  Scaled to LLM sizes → emergent few-shot learning.
```

<!-- @editor[content/P2]: Transformer section could note that subword tokenization (BPE) is a morphological compromise — it recapitulates some morpheme boundaries without linguistic design, which connects to 02-MORPHOLOGY's segmentation discussion -->
**What transformers learn linguistically:**

```
PROBING STUDIES (2019–present):
  Train classifiers on frozen BERT representations to decode:
  - POS tags → highly decodable from early layers
  - Parse tree depth → decodable from middle layers
  - Semantic roles → decodable from upper layers
  - Coreference → partially decodable, but hard
  - Anaphora → still difficult

  ATTENTION HEADS and syntax:
  Specific heads in BERT reliably track:
  - Direct object of verb
  - Determiners
  - Coreferent mentions
  Attention ≈ dependency tree relations in some heads (Michel et al.)

  Transformers implicitly learn syntactic/semantic structure from raw text.
  They are not parsing explicitly, but the representations encode structure.
```

---

## Part VII: Universal Dependencies

**Universal Dependencies (UD)** is a cross-linguistic framework for consistent dependency treebanks.

```
DEPENDENCY GRAMMAR:
  Instead of phrase structure trees, represent syntax as labeled arcs
  from head to dependent.

  "The cat chased the dog."

  cat ←det— The
  cat ←nsubj— chased (root)
  chased ←obj— dog
  dog ←det— the

  Graph: directed arcs, each word has one head (except ROOT)
  Root: "chased" is root of the sentence.

UD RELATION TYPES (selected):
  nsubj   — nominal subject
  obj     — direct object
  iobj    — indirect object
  det     — determiner
  amod    — adjectival modifier
  nmod    — nominal modifier
  advmod  — adverbial modifier
  case    — case marker (preposition as dependent of NP)
  aux     — auxiliary
  mark    — subordinator

UD TREEBANKS:
  ~250 treebanks in ~100 languages (UD v2.12)
  Consistent annotation scheme enables cross-linguistic comparison
  Training data for neural dependency parsers (transition-based, graph-based)
```

---

## Part VIII: Open Problems

Computational linguistics has solved much — but several deep problems remain:

```
UNSOLVED / HARD PROBLEMS:

1. COREFERENCE RESOLUTION AT SCALE:
   Current systems handle explicit pronouns reasonably well.
   Cross-document coreference, implicit coreference (who is "the president"
   in complex discourse?) still difficult.
   Winograd schema: "The city council refused the demonstrators a permit
   because they feared violence." — who feared? Humans solve trivially; models struggle.

2. COMMON-SENSE REASONING:
   "The man who was hit by the car was rushed to the hospital."
   → the car didn't go to the hospital (infer)
   → the man might not survive (infer)
   Requires world knowledge, not just linguistic patterns.
   LLMs have improved this but not solved it — failures are systematic and surprising.

3. COMPOSITIONALITY AT SCALE:
   "The tall, bald professor whose students always submit late assignments
    during finals week agreed that the proposal was problematic."
   Formal semantics can compose this. Neural models may handle it well.
   But rare constructions, nested negations, complex quantifier interactions
   still fail in current models.

4. GROUNDED MEANING:
   Words in LLMs are defined by contexts of other words — no connection
   to the physical world. "Red" has distributional relations with "apple,"
   "blood," "fire" — but no visual grounding (for text-only LLMs).
   Multimodal models attempt to bridge this.

5. DISCOURSE AND DIALOGUE:
   Tracking topic, given/new information, implicature across turns,
   common ground update — deep discourse-level processing is where
   current models degrade fastest in long documents.
```

---

## Decision Cheat Sheet

| Task | Classical approach | Modern approach |
|------|-------------------|----------------|
| POS tagging | HMM Viterbi | BiLSTM/BERT fine-tune |
| Phrase-structure parsing | PCFG + CYK/Earley | Neural chart parser |
| Dependency parsing | Arc-eager transition system | Biaffine graph-based neural |
| NER | CRF over features | BERT fine-tune |
| Coreference | Feature-based ranking models | Coref-BERT, end-to-end models |
| Machine translation | IBM Models + phrase-based | Encoder-decoder Transformer |
| Semantic similarity | TF-IDF, LSA | Sentence-BERT embeddings |
| Language modeling | n-gram + KN smoothing | Transformer LLM |
| Word sense disambiguation | Lesk algorithm, WordNet | BERT contextual embeddings |
| SRL (semantic role labeling) | PropBank + SVM | BERT + biaffine attention |

---

## Common Confusion Points

**CYK requires CNF; Earley doesn't:**
CNF is only needed for CYK's simplicity. Any CFG can be parsed with Earley directly. In practice, NLP systems often binarize anyway for efficiency.

**PCFG is not the same as a weighted CFG:**
PCFG requires probabilities per non-terminal to sum to 1 (a proper probability distribution over rule expansions). Weighted CFG is more general. For parsing, PCFGs are used; for lattice/transducer operations, weighted CFGs/FSTs are used.

**word2vec and GloVe give static embeddings:**
The same word always gets the same vector regardless of context. "Bank" = one vector. This is their key limitation. BERT gives contextual embeddings — different vectors for "bank" in different contexts.

**"Transformer" is an architecture, not a model:**
BERT, GPT-4, T5, LLaMA are all Transformer-based models. The Transformer is the underlying architecture. This parallels: "relational database" (architecture) vs. SQL Server, PostgreSQL (specific systems).

**Attention is not syntax:**
Despite some attention heads learning syntactic relations, Transformers are not parsing — they're learning statistical regularities that happen to correlate with syntactic structure. The representation is emergent, not explicitly structured. This is a feature (powerful generalization) and a bug (brittle on adversarial inputs).

**UD is annotation, not theory:**
Universal Dependencies is an annotation scheme for treebanks — not a syntactic theory. You can agree with dependency grammar as a formalism and still debate UD's specific choices. UD prioritizes cross-linguistic consistency over theoretical purity.
