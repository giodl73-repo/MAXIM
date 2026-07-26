---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "08-STRINGS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:algorithms:strings
kind: guide
module: algorithms
section: mathematics-physics
title: String Algorithms
status: source-custody
source_custody: partial
current_path: algorithms/08-STRINGS.md
canonical_path: algorithms/08-STRINGS.md
backsource_ids: [mdloom-backfill:algorithms:08-strings, git-history:algorithms:08-strings]
concepts: [string matching, KMP, Z-algorithm, Rabin-Karp, tries, suffix array, suffix tree, suffix automaton, aho-corasick]
root_concepts: [string algorithms]
index_roles: [guide]
remap_from: []
remap_to: []
updated: null
---
# String Algorithms

Strings are the one combinatorial domain rich enough to demand a dedicated toolkit.
The central problem — find a pattern of length `m` in a text of length `n` — is
solvable in O(n+m) by exploiting the structure the naive O(nm) scan throws away
(KMP, Z), or in expected O(n+m) by hashing (Rabin-Karp). Indexing *all* substrings of
a text needs heavier machinery — tries, suffix arrays, suffix trees, suffix automata —
each with exact construction and query bounds. Every bound below states its model
(comparison vs hashing) and whether it is worst-case or expected.

```
  STRING ALGORITHMS LANDSCAPE
  =====================================================================================

   SINGLE-PATTERN MATCH (pattern P in text T)        MULTI-PATTERN / INDEXING
   ----------------------------------------          ------------------------
   naive            O(nm) worst                       TRIE          O(sum |P|) build
   KMP              O(n+m) worst, prefix function      AHO-CORASICK  O(n + sum|P| + matches)
   Z-algorithm      O(n+m) worst, Z-array             SUFFIX ARRAY  O(n log n)/O(n) build
   Rabin-Karp       O(n+m) EXPECTED (hashing)                       O(m log n) query
                    O(nm) worst (hash collisions)     SUFFIX TREE   O(n) build (Ukkonen)
   Boyer-Moore      O(n/m) best, sublinear in practice SUFFIX AUTOM. O(n) build, DAWG
                                                       (smallest substring index)

   THE KEY IDEA (KMP/Z): on a mismatch, the naive scan restarts from scratch (O(nm)).
   These algorithms PRECOMPUTE the pattern's self-overlap so the text pointer NEVER
   backs up -> each text char examined O(1) amortized -> O(n+m).

   THE KEY IDEA (suffix structures): index EVERY suffix of T once, then any substring
   query is a prefix lookup in that index.
```

**Read by query type**: matching one known pattern → KMP/Z (worst-case linear) or
Rabin-Karp (expected linear, trivial multi-pattern via hashing); matching many
patterns at once → Aho-Corasick; answering arbitrary substring/repeat/LCP queries on
a fixed text → a suffix array/tree/automaton.

---

## Layer 1: Why Naive Matching Is O(nm), and the Fix

```
   NAIVE: try every alignment, compare up to m chars each -> O(nm) worst.
   WORST CASE: T = "aaaaaaaaab", P = "aaaab"
     at each of ~n alignments, compare ~m chars before the final mismatch.

   T: a a a a a a a a a b
   P: a a a a b              mismatch at pos 4 -> naive restarts P at T[1] (BACKS UP)
      . a a a a b            ...and again, and again -> O(nm)

   INSIGHT: when "aaaa" matched then 'b' mismatched, we ALREADY KNOW the next 3 chars
   of T are "aaa" -- so we should resume P at its longest proper prefix that is also a
   suffix of what matched, WITHOUT re-reading T. That's the KMP prefix function.
```

---

## Layer 2: KMP — the Prefix Function (failure function)

KMP precomputes, for each prefix of `P`, the length of the **longest proper prefix
that is also a suffix** (the "border"). On a mismatch, it shifts `P` by that amount
and the text pointer never moves backward.

```
   prefix function pi for P = "ababaca":
     P:   a b a b a c a
     idx: 0 1 2 3 4 5 6
     pi:  0 0 1 2 3 0 1
   pi[4]=3 means "ababa" has border "aba" (len 3): prefix "aba" == suffix "aba".

   MATCHING T against P using pi (text pointer i never decreases):
     on mismatch at P[j]: set j = pi[j-1] (fall back in P only), keep i fixed.
     each step either advances i (n times) or decreases j (<= n times total)
     => O(n + m) WORST CASE.

   T = "ababaca b...",  match "ababaca" then continue from pi without rescanning T.
```

KMP is the proof that single-pattern matching is **Θ(n+m) worst-case** in the
comparison model — no hashing, no probability. The prefix function is also a building
block for periodicity and border problems.

### Z-algorithm — the same power, different array

```
   The Z-array: Z[i] = length of the longest substring starting at i that MATCHES a
   prefix of the string.  Computed in O(n) via a "Z-box" sliding window.

   S = "aabxaabxcaabxaabxay"
   To match P in T: build Z on  P + '#' + T.  Any position with Z >= |P| is a match.
   => O(n+m) worst-case, often simpler to implement correctly than KMP.
```

KMP and Z are equivalent in power (both O(n+m) worst-case); Z is frequently easier to
get right, while KMP's failure function generalizes to Aho-Corasick.

---

## Layer 3: Rabin-Karp — Hashing (expected linear, multi-pattern friendly)

Rabin-Karp slides a **rolling hash** over the text: hash the pattern once, then update
the window hash in O(1) per shift, comparing full strings only on a hash match.

```
   ROLLING (polynomial) HASH, base b mod prime q:
     h(s) = (s[0]*b^{m-1} + s[1]*b^{m-2} + ... + s[m-1]) mod q
     slide by one: new = ( (old - s[i]*b^{m-1})*b + s[i+m] ) mod q     -- O(1) update

   match P="abc" in T="zabcx":
     hash("zab"), roll -> hash("abc") == hash(P)?  yes -> VERIFY chars (guard collision)
   EXPECTED O(n+m) with a good random prime.  WORST O(nm) if every window collides
     (an adversary who knows q can force this -> use a random q, see cryptography/).

   STRENGTH: hashing k patterns of equal length is O(n + k) expected -- store pattern
   hashes in a set and check membership per window. (Naive/KMP would be O(k(n+m)).)
```

Rabin-Karp is the bridge to `cryptography/`: the rolling hash is a (non-cryptographic)
polynomial hash, and its adversarial worst case is defeated exactly the way hash-table
flooding is — randomize the modulus/seed so collisions can't be precomputed (the same
theme as `06` and the randomized classes of `09`). It is the natural choice for
**multi-pattern** and **2D / substring-fingerprint** problems.

---

## Layer 4: Tries and Aho-Corasick (multi-pattern)

### Trie — prefix tree

```
   store {"cat","car","card","dog"}:        each edge = a character; a path = a string.
            (root)
           /      \
         c          d
         |          |
         a          o
        / \         |
       t   r        g*       * = end-of-word marker
      *   /|\
         '' d        ("car" is a word; "card" extends it)
            *
   lookup/insert "word": O(|word|).  space O(total chars).  prefix queries: free.
```

### Aho-Corasick — match a *set* of patterns in one pass

Aho-Corasick is "KMP over a trie": build a trie of all patterns, add **failure links**
(longest proper suffix that is a trie node), and scan the text once.

```
   trie of patterns + failure links (dashed) form an automaton:
     scan T left to right, following goto edges; on mismatch follow failure links.
     each text char -> O(1) amortized transitions.
   COMPLEXITY: build O(sum |P_i|);  match O(n + #matches).
   => find ALL occurrences of ALL patterns in O(n + total pattern length + #matches).
```

This is the engine behind multi-keyword scanners, intrusion-detection signatures, and
dictionary matchers — one linear pass for an entire pattern set.

---

## Layer 5: Suffix Structures (index every substring of one text)

To answer arbitrary substring/repeat/LCP queries on a *fixed* text, preprocess all its
suffixes. Three structures, same goal, different trade-offs.

```
   text T = "banana$"   ( $ = unique sentinel )
   all suffixes:        suffix array SA = sorted suffix START indices:
     0 banana$            $        -> 6
     1 anana$             a$       -> 5      SA = [6, 5, 3, 1, 0, 4, 2]
     2 nana$              ana$     -> 3      (suffixes in lexicographic order)
     3 ana$               anana$   -> 1
     4 na$                banana$  -> 0
     5 a$                 na$      -> 4
     6 $                  nana$    -> 2

   SUFFIX ARRAY: SA[] + LCP[] (longest-common-prefix of adjacent suffixes).
     build O(n log n) (or O(n) with SA-IS/DC3); substring query O(m log n) by binary
     search on SA (O(m + log n) with LCP). Compact: just integers.
   SUFFIX TREE: compressed trie of all suffixes; build O(n) (Ukkonen). Richer queries
     (longest repeated substring, LCA-based LCP) but ~larger constant/memory.
   SUFFIX AUTOMATON (DAWG): smallest automaton recognizing all substrings of T;
     build O(n); O(n) states; counts distinct substrings, online construction.
```

```
   WHICH SUFFIX STRUCTURE?
   suffix array     -> memory-tight, simplest, O(n log n)/O(n) build; the practical default
   suffix tree      -> need O(n) build + rich tree queries (longest repeat, matching stats)
   suffix automaton -> count/enumerate distinct substrings, online, smallest substring index
   all three: substring search, # occurrences, longest common substring of two texts.
```

Suffix arrays back bioinformatics (genome alignment, `genomics/`), full-text search,
and compression (the BWT in `bzip2` is a suffix-array sort) — cross-ref
`information-theory/` and `cryptography/`.

---

## Old World → New World Bridges

| You already know | The string-algorithm concept |
|---|---|
| `String.IndexOf` / `str.find` | Naive O(nm) or a Boyer-Moore-style sublinear scan under the hood |
| `grep` / `ripgrep` literal search | KMP/Boyer-Moore (single) or a DFA/automaton for multi-pattern |
| A multi-keyword content filter / IDS | Aho-Corasick — all patterns in one linear pass |
| Regex matching | NFA/DFA simulation — DP over (position × state), `computing/21-AUTOMATA.md` |
| "This regex hangs on weird input" | Catastrophic backtracking vs linear automaton matching — model choice matters |
| Genome alignment / full-text index | Suffix array/tree (`genomics/`) |
| `bzip2` compression | BWT = a suffix-array sort (`information-theory/`) |
| Content-defined chunking / dedup | Rolling (Rabin) hash — same primitive as Rabin-Karp |

The regex-backtracking bridge is the practically sharpest one: an engineer who has
been paged for a "ReDoS" outage has met the difference between a backtracking matcher
(exponential worst case) and a linear automaton (`computing/21-AUTOMATA.md`) — the
string toolkit is what stays linear.

---

## Decision Cheat Sheet

| I need to... | Use | Bound |
|---|---|---|
| Find one known pattern, worst-case linear | KMP or Z-algorithm | O(n+m) worst |
| Find one pattern, expected linear, simple | Rabin-Karp | O(n+m) expected |
| Find *many* patterns in one pass | Aho-Corasick | O(n + Σ\|P\| + matches) |
| Sublinear average matching | Boyer-Moore | O(n/m) best, fast in practice |
| Prefix lookups / autocomplete | trie | O(\|word\|) per op |
| Substring search on a fixed text, repeatedly | suffix array | O(m log n) query |
| Longest repeated / common substring | suffix tree / automaton | O(n) build |
| Count distinct substrings | suffix automaton | O(n) |
| Fingerprint windows / dedup | rolling hash | O(1) per slide |
| Match a regex without backtracking blowup | DFA/NFA automaton | O(n) — `computing/21-AUTOMATA.md` |

---

## Common Confusion Points

### "Rabin-Karp is O(n+m), same as KMP"

Rabin-Karp is O(n+m) **expected** (hashing); its **worst case is O(nm)** when every
window hash collides — and an adversary who knows the modulus can force it. KMP and Z
are O(n+m) **worst-case** in the comparison model, no probability. Use a randomized
prime for Rabin-Karp's robustness, and prefer KMP/Z when you need a hard guarantee.

### "KMP backs up to recompare the text"

The whole point of KMP is that the **text pointer never moves backward** — only the
pattern pointer falls back via the prefix function. That is exactly why it is linear:
each text character is examined O(1) amortized. The naive algorithm backs the text up,
which is the source of its O(nm).

### "A suffix tree and a suffix array are interchangeable"

They answer the same queries but differ in build (suffix tree O(n) via Ukkonen vs
suffix array O(n) via SA-IS or O(n log n) simpler), memory (array is far more compact),
and query ergonomics (tree gives O(n) longest-repeat directly; array needs the LCP
array). The suffix array is the practical default for memory; the tree for rich
tree-shaped queries.

### "Tries are just hash maps for strings"

A trie shares structure among common prefixes, so it gives O(|key|) lookup *independent
of the number of keys*, plus free prefix/range queries (autocomplete) and ordered
traversal — none of which a hash map offers. The trade-off is memory overhead per node
and worse cache behavior.

### "Regex is a string algorithm with one complexity"

Regex matching's complexity depends on the **engine model**: a Thompson NFA / DFA
matches in O(n) (linear, `computing/21-AUTOMATA.md`), but a backtracking engine (PCRE,
many language built-ins) can be *exponential* on adversarial patterns (ReDoS). Same
notation, radically different worst case — the model is the whole story.
