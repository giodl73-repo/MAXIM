# Machine Translation: Rule-Based to Neural

## The Big Picture

```
MACHINE TRANSLATION — EVOLUTION
════════════════════════════════════════════════════════════════════

  1949-1966          1966-1989        1990-2014       2014-present
  ┌─────────────┐   ┌─────────────┐  ┌─────────────┐  ┌───────────────┐
  │ RULE-BASED  │   │ ALPAC       │  │ STATISTICAL │  │ NEURAL MT     │
  │ MT (RBMT)   │   │ WINTER      │  │ MT (SMT)    │  │               │
  │             │ → │             │→ │             │→ │ Seq2seq (2014)│
  │ Bilingual   │   │ Funding     │  │ Noisy       │  │ Attention     │
  │ dictionaries│   │ cut; MT     │  │ channel     │  │ (2014)        │
  │ + grammar   │   │ declared    │  │ model;      │  │ Transformer   │
  │ rules       │   │ unprofitable│  │ phrase-     │  │ (2017)        │
  │             │   │             │  │ based;      │  │ Multilingual  │
  │ Georgetown- │   │ Limited     │  │ Google      │  │ models        │
  │ IBM 1954    │   │ commercial  │  │ Translate   │  │ (2019+)       │
  │ (60 Russian │   │ use         │  │ 2006        │  │               │
  │ sentences)  │   │             │  │             │  │               │
  └─────────────┘   └─────────────┘  └─────────────┘  └───────────────┘

  QUALITY INFLECTION:
  RBMT: ~30-40% adequate    SMT: ~50-60% adequate    NMT: ~70-80%+ adequate
  (rough estimates for general text; varies greatly by domain/language pair)
```

---

## Rule-Based Machine Translation (RBMT)

### The Georgetown-IBM Experiment (1954)

January 7, 1954: IBM and Georgetown University demonstrated the first public machine translation system. 60 Russian sentences, ~250-word vocabulary, 6 grammar rules. The system translated sentences like "Mi pyeryedayom mislyi posryedstvom ryechi" → "We transmit thoughts by means of speech."

```
RBMT ARCHITECTURE
════════════════════════════════════════════════════════════════

  SOURCE TEXT
       │
       ▼
  MORPHOLOGICAL ANALYSIS
  (identify word forms, stems, case, number, tense)
       │
       ▼
  SYNTACTIC PARSING
  (parse into phrase structure)
       │
       ▼
  SEMANTIC ANALYSIS
  (assign word sense; resolve ambiguity via rules)
       │
       ▼
  TRANSFER
  (map source-language structures to target-language
   structures via bilingual dictionary + structural rules)
       │
       ▼
  GENERATION
  (produce grammatical target-language text)
       │
       ▼
  OUTPUT

  KEY RESOURCE:
  Bilingual dictionary (source word → target word)
  + Grammar rules (source structure → target structure)
  These were hand-crafted by linguists.
```

### The ALPAC Report (1966) — First AI Winter Analogue

The Automatic Language Processing Advisory Committee (ALPAC) report (1966) evaluated 10 years of RBMT research and concluded:

> "There is no immediate or foreseeable prospect of useful machine translation."

The report recommended cutting MT research funding and focusing on computational linguistics instead.

**Why it was (partly) right**:
- Rule-based systems couldn't handle ambiguity at scale
- Exceptions outnumbered rules
- Quality was far below human translation

**Why it was (partly) wrong**:
- It declared MT unviable just before statistical methods showed promise
- It measured quality by Cold War-era standards (military/technical translation)
- The commercial market it dismissed (technical manuals, not scientific text) was actually huge

Result: 20+ years of reduced MT funding; commercial development continued on the margins.

---

## Statistical Machine Translation (SMT)

### The IBM Models (1990)

Peter Brown, Stephen Della Pietra, Vincent Della Pietra, and Robert Mercer at IBM Research published a series of papers (1990-1993) that founded statistical MT.

**Key insight**: Reframe translation as a probabilistic inference problem — the noisy channel model.

```
NOISY CHANNEL MODEL FOR MT
════════════════════════════════════════════════════════════════

  The source text (foreign) is a "noisy" version of
  what was originally a well-formed target text.
  The translator's job: recover the most likely
  target text given the noisy source.

  Formally:
  Given source sentence f, find target sentence e
  that maximizes P(e|f):

  argmax P(e|f) = argmax P(f|e) × P(e)
      e                  e
                         ↑            ↑
                Translation      Language
                model            model
                (P(f|e):         (P(e):
                how likely       how likely
                is the           is this English
                foreign text     sentence?)
                given this
                English?)

  Training: Learn P(f|e) from bilingual corpora
            (parallel texts: same text in both languages)
           Learn P(e) from monolingual English corpora

  The bilingual corpus does the work of the dictionary.
  The language model does the work of grammar rules.
  Both are learned from data, not hand-coded.
```

### Word Alignment

The central SMT problem: given a sentence and its translation, which source words correspond to which target words?

```
WORD ALIGNMENT EXAMPLE
════════════════════════════════════════════════════════════════

  German: Das Buch ist rot
  English: The book is red

  Das    → The
  Buch   → book
  ist    → is
  rot    → red

  But:
  German: Ich habe das Buch gelesen
  English: I have read the book

  Ich  → I
  habe → have
  das  → the
  Buch → book
  gelesen → read (but "read" appears before "book" in English!)

  IBM Models 1-5 (from simple word alignment to fully
  parametric models) learned to handle:
  • Reordering (verb-final German → English SOV)
  • Fertility (one source word → multiple target words or vice versa)
  • NULL alignment (some words have no counterpart)
```

### Phrase-Based SMT (PBSMT)

By the late 1990s, "phrase-based" SMT improved quality by translating phrases rather than individual words:

- Build a phrase table: all pairs of source-target phrases seen in training data, with probabilities
- At translation time: find the best coverage of the source sentence by phrase pairs
- A language model reorders and selects among options

Google Translate (2006) used phrase-based SMT at massive scale, with enormous training corpora (the entire Web as bilingual corpus). Quality was surprisingly good for European language pairs; poor for morphologically complex or typologically distant languages.

---

## Neural Machine Translation (NMT)

### Sequence-to-Sequence (2014)

Sutskever, Vinyals, and Le (Google) introduced the sequence-to-sequence architecture (2014):

```
SEQUENCE-TO-SEQUENCE ARCHITECTURE (2014)
════════════════════════════════════════════════════════════════

  SOURCE SENTENCE: "The cat sat on the mat"
                              ↓
  ENCODER (LSTM):
  Reads input word by word; builds hidden state
  Each word updates the hidden state
  Final hidden state = fixed-length "thought vector"
  representing the entire source sentence
                              ↓
  THOUGHT VECTOR (bottleneck)
  A single fixed-length vector (256 or 512 dim)
  must encode the entire source sentence meaning
                              ↓
  DECODER (LSTM):
  Generates output word by word, conditioned on
  thought vector and previously generated words
  "Le chat était assis sur le tapis"
                              ↓
  OUTPUT SENTENCE

  PROBLEM: Fixed-length bottleneck
  Long sentences → thought vector can't encode all information
  → quality degrades with sentence length
```

### Attention Mechanism (Bahdanau et al. 2014)

Dzmitry Bahdanau, Kyunghyun Cho, Yoshua Bengio: "Neural Machine Translation by Jointly Learning to Align and Translate" (2014) — the attention paper that changed everything.

```
ATTENTION MECHANISM
════════════════════════════════════════════════════════════════

  PROBLEM SOLVED: Fixed bottleneck loses long-range information.
  SOLUTION: Allow decoder to "attend to" different parts of
  the encoder's output at each decoding step.

  ENCODER: Instead of one thought vector, produces a
  sequence of hidden states (one per input word).

  DECODER: At each output step, computes:
  1. Attention weights: how relevant is each source
     hidden state for generating the current output word?
  2. Context vector: weighted sum of source hidden states
  3. Generates output word using context vector

  "Das Buch" → generating "The book":
  Decoder attends heavily to positions of "Das" and "Buch"
  while generating "The" and "book" respectively.

  Generates "Die rote Katze":
  Decoder for "red" → attends to "rote"
  Decoder for "cat" → attends to "Katze"

  QUALITY IMPROVEMENT:
  Attention allows the model to handle long sentences,
  reordering, and rare constructions much better than
  the fixed bottleneck.

  This is the same attention mechanism in the Transformer —
  the learner already knows this from 01-LLM-CONCEPTS.md.
```

### The Transformer (Vaswani et al. 2017)

"Attention Is All You Need" (Vaswani, Shazeer, Parmar, et al., 2017) replaced the recurrent architecture (LSTM) with entirely attention-based processing:

```
TRANSFORMER ARCHITECTURE FOR MT
════════════════════════════════════════════════════════════════

  (The learner knows this from 01-LLM-CONCEPTS.md)

  KEY DIFFERENCES FROM RECURRENT:
  1. No sequential processing — all positions processed
     in parallel → faster training
  2. Multi-head self-attention: each word attends to
     all other words in the sequence simultaneously
  3. Positional encoding: since no recurrence, must
     explicitly encode word order
  4. Encoder-decoder architecture with cross-attention:
     decoder attends to encoder states

  MT-SPECIFIC QUALITY LEAP:
  • Better handling of long-range dependencies
  • Better reordering
  • Faster training (parallelizable)
  • Scales with model size and data in ways RNNs didn't

  TRAINING: Sequence-to-sequence objective:
  Teacher forcing — at each step, use the ground truth
  previous word (not the model's previous output)
  Evaluated by BLEU score on held-out test set

  STANDARD BENCHMARK:
  WMT (Workshop on Machine Translation) annual competition
  Tests EN-DE, EN-FR, EN-CS, EN-ZH and other pairs
  BLEU scores on newstest sets track year-over-year progress
```

---

## Training Data: The Parallel Corpus Problem

All SMT and NMT systems require parallel corpora — the same text in both languages, aligned at the sentence level.

```
PARALLEL CORPUS SOURCES
════════════════════════════════════════════════════════════════

  INSTITUTIONAL:
  • Europarl: European Parliament proceedings in 24 languages
    (10 million sentences per language pair)
  • UN Corpus: UN documents in 6 languages
  • Canadian Hansard: Parliamentary debates (EN-FR)
  • Opus: open source parallel corpus collection

  WEB-CRAWLED:
  • Google's training data: proprietary; enormous
  • CommonCrawl: web crawl; contains parallel data
    detected by language identification
  • ParaCrawl: focused web crawl for EU language pairs

  THE BIBLE:
  The Bible is available in 2,000+ languages,
  all verse-aligned. It is the only large parallel
  corpus for many low-resource languages.
  → Used for low-resource MT experiments
  → Limitation: religious text; domain mismatch
    for general-purpose MT

  QUALITY PROBLEMS:
  Web-crawled parallel data contains noise:
  • Mis-aligned sentences
  • Machine-translated references (creating circular training)
  • Inconsistent domains
  • Duplicate content

  LOW-RESOURCE LANGUAGES:
  Languages with small corpora (many African languages,
  indigenous languages, minority dialects) have
  dramatically worse MT quality.
  NLLB-200 (No Language Left Behind, Meta 2022):
  trained on 200 languages; dedicated data collection
  for low-resource pairs.
```

---

## Multilingual Neural MT

```
MULTILINGUAL MT ARCHITECTURE
════════════════════════════════════════════════════════════════

  CHALLENGE: Build one model that translates many pairs,
  not N×(N-1) separate models.

  APPROACH:
  mBERT (Devlin et al. 2018): multilingual BERT;
  trained on 104 languages; shared vocabulary
  (WordPiece); models share cross-lingual representations.

  mT5 (Xue et al. 2021): multilingual T5 encoder-decoder.

  NLLB-200 (Meta 2022): specifically for MT across 200 langs.

  ZERO-SHOT CROSS-LINGUAL TRANSFER:
  Train on EN-FR and EN-DE pairs.
  Ask to translate FR → DE (never seen directly in training).
  Because the model shares representations across languages,
  it can do reasonable FR→DE translation through English
  as an implicit pivot.

  Quality: generally lower than direct pair;
  varies by language similarity to training pairs.

  BENEFITS OF MULTILINGUAL MODELS:
  • Positive transfer: high-resource languages help
    low-resource ones
  • Single model deployment vs. hundreds of models
  • Zero-shot capabilities for new language pairs
  • Cross-lingual representations useful for downstream tasks

  COSTS:
  • "Curse of multilinguality": capacity diluted across
    languages; each language pair gets less model capacity
  • Requires careful data balancing (temperature sampling)
    to prevent high-resource languages from dominating
```

---

## Decision Cheat Sheet

| Era | Approach | Key mechanism | Quality | Failure modes |
|-----|---------|--------------|---------|--------------|
| RBMT 1954-1990s | Rules + dictionaries | Hand-coded grammar + bilingual dictionary | Low; brittle | Ambiguity; exception handling; vocabulary coverage |
| SMT 1990-2014 | Statistical models | Noisy channel; word alignment; language model | Medium; improving | Reordering; morphology; fluency |
| Seq2seq NMT 2014-2017 | Encoder-decoder LSTM | Fixed thought vector + attention | Higher; fluent | Long sentences; hallucination begins appearing |
| Transformer NMT 2017+ | Self-attention | Multi-head attention; parallel processing | High; near-human for some pairs | Hallucination; low-resource; pragmatics; cultural |
| Multilingual 2019+ | Shared multilingual model | Cross-lingual transfer | Variable by language | Capacity dilution; low-resource still poor |

---

## Common Confusion Points

**ALPAC was premature but useful**: The 1966 ALPAC report was too pessimistic about the timeline for useful MT, but it correctly identified that RBMT as practiced couldn't scale. The report redirected effort toward computational linguistics, which laid the groundwork for statistical MT 25 years later.

**Attention ≠ alignment**: In SMT, word alignment is a hard assignment (this source word → this target word). Attention is soft (learned probability distribution over source states at each decoding step). Attention can spread weight across multiple source positions; hard alignment assigns each target word to one source word (or NULL).

**Google Translate 2006 was phrase-based SMT, not NMT**: The NMT switch happened in 2016. Pre-2016 Google Translate used PBSMT at massive scale. The quality jump when NMT was introduced was large and immediately noticed by users.

**Parallel corpus quality matters more than size**: More data helps, but noisy data (mis-aligned sentences, MT-translated references) can hurt. The field has learned that data quality filtering is as important as data collection.

**The Bible is everyone's training data**: Because the Bible is the only large parallel corpus for hundreds of languages, MT into and out of those languages systematically reflects biblical register and vocabulary. This is a subtle bias that rarely gets discussed but affects any low-resource MT system.
