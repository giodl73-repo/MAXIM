# Translation — Landscape and Taxonomy

## The Big Picture

```
TRANSLATION STUDIES — FIELD MAP
════════════════════════════════════════════════════════════════════

  TRANSLATION AS PRACTICE          TRANSLATION STUDIES AS DISCIPLINE
  (what translators do)            (what scholars study)
  ┌──────────────────────────┐     ┌──────────────────────────────┐
  │ • Literary translation   │     │ • Equivalence theory         │
  │ • Technical translation  │     │ • Polysystem theory          │
  │ • Legal translation      │     │ • Descriptive TS             │
  │ • Bible translation      │     │ • Cognitive approaches       │
  │ • Localization           │     │ • Postcolonial/feminist TS   │
  │ • Interpretation         │     │ • Machine translation        │
  │   (oral)                 │     │   evaluation                 │
  └──────────────────────────┘     └──────────────────────────────┘
             │                                  │
             └─────────────────┬────────────────┘
                               ▼
               THE CENTRAL TENSION:
               EQUIVALENCE PROBLEM
               ┌──────────────────────────────┐
               │ Can meaning transfer          │
               │ across languages?             │
               │                              │
               │ What is preserved?           │
               │ What is necessarily lost?    │
               │ Can loss be minimized?       │
               │ Is "equivalence" even        │
               │ a coherent goal?             │
               └──────────────────────────────┘
                               │
          ┌────────────────────┼────────────────────┐
          ▼                    ▼                    ▼
   FORMAL           DYNAMIC              CRITICAL
   EQUIVALENCE      EQUIVALENCE          APPROACHES
   (word-for-word)  (sense-for-sense)    (domestication vs.
   Nabokov          Nida                 foreignization;
                                         power and ideology)
```

---

## Why Translation Matters

Translation is not a marginal activity. It constitutes significant chunks of political, religious, scientific, and cultural history:

1. **Bible translations shaped nations**: Luther's German Bible (1522) standardized the German language and accelerated the Reformation. The King James Version (1611) defined English prose for 400 years. Every translation choice is a political and theological act.

2. **Mistranslations cause consequences**: The Japanese government's response to the Potsdam Declaration (1945) used the word *mokusatsu* — meaning either "withhold comment" or "treat with contempt." The Allies translated it as the latter. Whether this contributed to the decision to drop the atomic bombs is debated.

3. **Translation enables science**: The Toledo school of translators (12th century) translated Arabic versions of Aristotle, Euclid, and al-Khwarizmi into Latin — delivering Greek science and Islamic mathematics back to Western Europe. Without this, the Scientific Revolution would have been delayed.

4. **LLM quality is defined by translation**: The Transformer architecture (Vaswani et al. 2017) was developed for machine translation. Multilingual models (mBERT, mT5, NLLB) extend this. Translation quality benchmarks are central metrics in NLP evaluation. The learner already knows the Transformer architecture from AI work (01-LLM-CONCEPTS.md) — the translation connection is direct.

---

## Theoretical Traditions

```
TRANSLATION THEORY — TIMELINE AND SCHOOLS
════════════════════════════════════════════════════════════════

  ANTIQUITY-RENAISSANCE: Prescriptive Debates
  ─────────────────────────────────────────────────────
  Cicero (46 BCE): sense-for-sense preferred over word-for-word
  Jerome (382 CE): Vulgate — sense-for-sense (except scripture)
  Luther (1522): vernacular naturalization
  Core question: word-for-word or sense-for-sense?

  18TH-19TH CENTURY: Hermeneutic Tradition
  ─────────────────────────────────────────────────────
  Schleiermacher (1813): "bring the author to the reader"
  vs. "bring the reader to the author" — the binary
  Humboldt: languages are worldviews, not codes
  Dilthey: interpretation (Verstehen) not explanation
  Core question: can meaning transfer across linguistic worldviews?

  20TH CENTURY: Linguistic and Systemic Approaches
  ─────────────────────────────────────────────────────
  Nida (1964): formal vs. dynamic equivalence
  Jakobson (1959): interlingual / intralingual / intersemiotic
  Even-Zohar (1978-): Polysystem theory — translated literature
    occupies position in target culture's literary system
  Toury (1980s): Descriptive Translation Studies — norms, not rules
  Core question: how does translation function in culture?

  LATE 20TH CENTURY: Cultural and Critical Turn
  ─────────────────────────────────────────────────────
  Benjamin (1923): "Task of the Translator" — afterlife of original
  Derrida (1985): Tower of Babel — translation impossible and necessary
  Venuti (1995): Domestication vs. foreignization; visible translator
  Spivak (1992): Postcolonial translation — subaltern voices
  Core question: what power relations does translation enact?

  LATE 20TH-21ST CENTURY: Cognitive and Computational
  ─────────────────────────────────────────────────────
  Seleskovitch (1975): interpretive theory — deverbalization
  Gile (1995): effort model for interpretation
  Brown et al. (1990): statistical MT — noisy channel model
  Vaswani et al. (2017): Transformer architecture for MT
  Core question: what cognitive and computational processes
    underlie translation? How do we evaluate machine output?
```

---

## The Equivalence Problem

The central theoretical issue: what does it mean for a translation to be "equivalent" to its source?

**Formal equivalence**: Match each source element with a target element — word-for-word, structure-for-structure. Nabokov's interlinear Onegin is the extreme. Loses naturalness; gains fidelity to form.

**Dynamic equivalence** (Eugene Nida): Match the effect of the source on its original audience with the effect of the translation on the target audience. "Closest natural equivalent." Produces fluent texts; loses foreignness and form.

**Functional equivalence**: What the text *does* (performative, referential, aesthetic functions).

**The impossibility thesis**: Humboldt — each language "divides the world differently." The categories built into German grammar are not the categories built into Swahili grammar. Translation is always transformation.

Jakobson's famous example: "I hired a worker" — Russian has no grammatical way to leave the worker's gender unspecified. The translator must choose. The choice adds information not in the source.

---

## Machine Translation as Parallel Development

MT development mirrors and informed translation theory:

```
MT DEVELOPMENT TIMELINE
════════════════════════════════════════════════════════════════

  1954: Georgetown-IBM experiment — 60 sentences,
        rule-based; optimistic predictions
  1966: ALPAC report — MT not working, cut funding
        (first AI winter analogue in MT)
  1990: IBM statistical MT (Brown et al.) —
        noisy channel model; translation as decoding
  2006: Google Translate — phrase-based SMT at scale
  2014: Neural MT — sequence-to-sequence with attention
        (Bahdanau et al.) — quality leap
  2017: Transformer (Vaswani et al.) — self-attention
        replaces recurrence; current foundation
  2019+: Multilingual models — mBERT, mT5, NLLB-200
         (200 languages); zero-shot cross-lingual transfer

  KEY PARALLEL TO THEORY:
  ALPAC era ↔ equivalence theory (looking for rules)
  Statistical MT ↔ descriptive TS (corpus-based)
  Neural MT ↔ cognitive approaches (learned representations)
  Multilingual models ↔ universal language theory question
```

---

## Guide Map

```
TRANSLATION GUIDES
──────────────────────────────────────────────────────────────
00  Overview (this file)     Field map, why it matters
01  Equivalence Problem       Nida, Jakobson, Benjamin, Derrida,
                             Venuti, Schleiermacher
02  History of Translation    Cicero to Jerome to Luther to modern
03  Bible Translation         LXX, Vulgate, Luther, KJV, modern
04  Literary Translation      Fidelity/freedom, retranslation,
                             canonical translators
05  Nabokov                   Radical literalism, Onegin,
                             Wilson polemic, the paradox
06  Untranslatability         Cassin, Sapir-Whorf, color terms,
                             legal translation, humor
07  Interpretation            Simultaneous/consecutive, Nuremberg,
                             Gile's effort model
08  Machine Translation       Rule-based → statistical → neural;
                             Transformer architecture
09  BLEU and NMT Evaluation   BLEU mechanics and failures, BERTScore,
                             MQM, hallucination, bias
──────────────────────────────────────────────────────────────
```

---

## Decision Cheat Sheet

| Question | Go to |
|----------|-------|
| What is the central theoretical debate? | 01-EQUIVALENCE-PROBLEM |
| How did translation shape religion and politics historically? | 02-HISTORY-TRANSLATION, 03-BIBLE-TRANSLATION |
| How is literary translation different from other types? | 04-LITERARY-TRANSLATION |
| Why did Nabokov translate Onegin interlinearly? | 05-NABOKOV |
| What is untranslatable and why? | 06-UNTRANSLATABILITY |
| How does simultaneous interpretation work cognitively? | 07-INTERPRETATION |
| How did MT evolve from rules to neural? | 08-MACHINE-TRANSLATION |
| What is BLEU and why is it inadequate? | 09-BLEU-NMT |

---

## Common Confusion Points

**Translation vs. interpretation**: In common usage these terms are interchangeable. In professional and academic usage: *translation* is written; *interpretation* is oral (conference interpretation, court interpretation, medical interpretation). Different skill sets, different training, different cognitive demands.

**Translation Studies vs. Linguistics**: Translation studies is an interdisciplinary field that takes from linguistics, literary theory, cultural studies, cognitive science, and computer science. It is not a subfield of linguistics, though linguistic approaches (equivalence, corpus-based) are central.

**Machine translation vs. human translation**: Not a simple quality hierarchy. NMT produces fluent output that often fools non-experts. But MQM (multidimensional quality metrics) and human evaluators find systematic failures: hallucination (making up facts), pragmatic failure (missing register, irony), cultural inadequacy. For literary and legal translation, human translation remains standard. For bulk technical translation, NMT with human post-editing is the industry norm.

**"Lost in translation" is not the whole story**: Robert Frost's "poetry is what is lost in translation" is a popular but partial view. Gregory Rabassa, who translated García Márquez, argued some things are *gained* in translation — a skilled translator can make explicit what was culturally implicit, and some texts improve in translation. Jorge Luis Borges wrote that some texts have been improved by their translations.
