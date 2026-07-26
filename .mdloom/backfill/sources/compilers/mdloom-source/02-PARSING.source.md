---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "02-PARSING.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:parsing
kind: guide
module: compilers
section: compilers
title: Syntax Analysis - LL vs LR, LALR, Parser Generators, Error Recovery
status: source-custody
source_custody: partial
current_path: compilers/02-PARSING.md
canonical_path: compilers/02-PARSING.md
backsource_ids: [mdloom-backfill:compilers:02-parsing, git-history:compilers:02-parsing]
concepts: [parsing, recursive descent, LL, LR, SLR, LALR, parser generators, error recovery]
root_concepts: [syntax analysis]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Syntax Analysis — LL vs LR, LALR, and Error Recovery

## The Big Picture

The parser turns the token stream into a tree. You know the theory: context-free
grammars, pushdown automata, the Chomsky hierarchy. The engineering question is
*which subclass of CFGs* a given parsing technique can handle, because no practical
parser handles all of CFG efficiently. The whole field is organized around two
strategies — predict from the top (LL) or recognize from the bottom (LR) — and the
grammar classes each can and cannot accept.

```
+--------------------------------------------------------------------------+
|                       THE PARSING LANDSCAPE                              |
|                                                                          |
|                     all context-free grammars                            |
|   +------------------------------------------------------------------+   |
|   |  ambiguous grammars (no deterministic parser)                    |   |
|   |  +------------------------------------------------------------+  |   |
|   |  |          unambiguous CFG                                   |  |   |
|   |  |   +---------------------------------------------------+    |  |   |
|   |  |   |   LR(1)   (canonical -- most powerful 1-LA det.)  |    |  |   |
|   |  |   |  +---------------------------------------------+  |    |  |   |
|   |  |   |  |  LALR(1) (yacc/bison -- merged LR(1) states)|  |    |  |   |
|   |  |   |  |  +---------------------------------------+  |  |    |  |   |
|   |  |   |  |  |  SLR(1)                              |  |  |    |  |   |
|   |  |   |  |  |  +-------------------------------+   |  |  |    |  |   |
|   |  |   |  |  |  |  LR(0)                        |   |  |  |    |  |   |
|   |  |   |  |  |  +-------------------------------+   |  |  |    |  |   |
|   |  |   |  |  +---------------------------------------+  |  |    |  |   |
|   |  |   |  +---------------------------------------------+  |    |  |   |
|   |  |   +---------------------------------------------------+    |  |   |
|   |  |   |                                                   |    |  |   |
|   |  |   +---------------------------------------------------+    |  |   |
|   |  |   |   LL(k)   (top-down; LL(1) subset shown)          |    |  |   |
|   |  |   |   - cannot do LEFT RECURSION                      |    |  |   |
|   |  |   |   - LL(1) is a PROPER SUBSET of LR(1)             |    |  |   |
|   |  |   +---------------------------------------------------+    |  |   |
|   |  +------------------------------------------------------------+  |   |
|   +------------------------------------------------------------------+   |

|   GLR / Earley: handle ALL CFGs (incl. ambiguous), at higher cost        |
+--------------------------------------------------------------------------+
```

Read the nesting: `LR(0) ⊂ SLR(1) ⊂ LALR(1) ⊂ LR(1) ⊂ unambiguous CFG`. LL and LR
are different shapes that overlap but neither contains the other; LL(1) sits inside
LALR(1). The practical sweet spot — and the reason yacc/bison won the 1970s–2000s —
is **LALR(1)**: nearly the power of LR(1) at a fraction of the table size.

---

## Two Strategies: Predict (LL) vs Recognize (LR)

```
   TOP-DOWN (LL)                          BOTTOM-UP (LR)
   =============                          ==============
   Start at the start symbol.             Start at the leaves (tokens).
   At each step, look at the next         Shift tokens onto a stack; when
   token(s) and PREDICT which             the top of the stack matches a
   production to expand.                  rule's RHS, REDUCE it to the LHS.

       S                                       ... e + e
      / \   "I'll expand E next"               reduce E -> e + e
     E   ...                                       /|\
    /|\    grow the tree DOWNWARD              build the tree UPWARD
                                              toward the start symbol

   Leftmost derivation, read L-to-R.       Rightmost derivation in REVERSE.
   LL(k): k tokens of lookahead.           LR(k): k tokens, but tracks more
                                            left context in the stack/states.
   Natural as recursive functions.         Natural as a table-driven automaton.
```

The key asymmetry: an LR parser **defers its decision** until it has seen the whole
right-hand side plus lookahead, so it can use the entire left context encoded in its
state. An LL parser **must decide up front** which production to take from only `k`
lookahead tokens. That is why LR is strictly more powerful for the same `k`, and why
LR can handle left recursion that LL cannot.

---

## Top-Down: Recursive Descent and LL(k)

Recursive descent is the most-used parsing technique in production compilers
(clang, Roslyn, V8, rustc, tsc are all hand-written recursive descent). One function
per nonterminal; the call stack *is* the parse stack.

```
  Grammar (LL(1)):
    expr   -> term expr'
    expr'  -> + term expr' | epsilon
    term   -> factor term'
    term'  -> * factor term' | epsilon
    factor -> ( expr ) | NUM

  Parser (sketch):
    parse_expr():  parse_term(); parse_expr_rest()
    parse_expr_rest():
        if peek() == '+': eat('+'); parse_term(); parse_expr_rest()
        else: return                         # epsilon
```

### The two LL killers

```
  1. LEFT RECURSION  (infinite loop in top-down):
       expr -> expr + term      # parse_expr() calls parse_expr() forever
     FIX: rewrite to right recursion (the expr' form above), OR use a
          bottom-up parser (LR handles left recursion natively).

  2. INSUFFICIENT LOOKAHEAD (can't predict the production):
       stmt -> ID = expr
       stmt -> ID ( args )      # both start with ID -- LL(1) can't choose
     FIX: LEFT-FACTOR:
       stmt    -> ID stmt_tail
       stmt_tail -> = expr | ( args )
```

LL(1) decisions are driven by **FIRST** and **FOLLOW** sets: pick the production
whose FIRST set contains the lookahead token (or, for an epsilon-production, whose
FOLLOW set does). A grammar is LL(1) iff for every nonterminal the candidate
productions have disjoint FIRST sets (and the epsilon case does not collide with
FOLLOW).

| Class | Lookahead | Handles left recursion? | Typical form |
|-------|-----------|--------------------------|--------------|
| LL(1) | 1 token | No | hand recursive descent, FIRST/FOLLOW |
| LL(k) | k tokens | No | ANTLR3-style, larger predict tables |
| LL(*) / ALL(*) | unbounded (adaptive) | No (still needs elimination) | ANTLR4 |
| Pratt / precedence climbing | operator-driven | handled by precedence | expression parsing inside recursive descent |

**Pratt parsing** (precedence climbing) deserves a callout: it is how hand-written
recursive-descent compilers parse expressions with many precedence levels *without*
writing one function per level. Each operator gets a binding power; the parser loops,
consuming operators while their binding power exceeds the current minimum. This is in
clang, rustc, and most serious frontends.

---

## Bottom-Up: The LR Family

LR builds a DFA over **items** (a production with a dot marking progress), and runs
it over a stack. The four classes differ only in *how they compute the lookahead
that decides when to reduce*.

```
  Item: a production with a dot.   E -> E . + T   means
        "we've parsed E, expect to see + T next."

  The LR(0) automaton's states are sets of items (closures).
  Parsing = shift tokens / reduce by a rule, driven by ACTION + GOTO tables.

         stack of states          ACTION table        GOTO table
         +----+----+----+         (terminal x state    (nonterminal x
         | s0 | s4 | s7 |    +     -> shift/reduce/      state -> next state)
         +----+----+----+    |      accept/error)
              ^ top          |
                             +-> the parser's whole "decision"
```

### What separates LR(0) / SLR / LALR(1) / LR(1)

This is the precision core of the guide.

```
  LR(0):    Reduce whenever a state contains a completed item (dot at end),
            with NO lookahead. Conflicts the moment a state has both a
            completed item and a shiftable item, or two completed items.
            Almost no real grammar is LR(0).

  SLR(1):   Reduce by A->w only when the next token is in FOLLOW(A).
            Cheap lookahead (global FOLLOW set). Resolves many LR(0)
            conflicts, but FOLLOW is too coarse -- it ignores WHICH state
            you're in, so it still rejects grammars LALR accepts.

  LR(1):    Items carry an explicit lookahead token: [A -> w . , a].
            Reduce by A->w only when the next token is exactly `a`,
            computed per-state (context-sensitive). Most powerful 1-token
            class. COST: huge number of states (lookahead splits states).

  LALR(1):  Build the LR(1) automaton, then MERGE states that have the
            same core (same items ignoring lookahead), unioning their
            lookaheads. Same state count as LR(0)/SLR, almost the power of
            LR(1). This is what yacc and bison generate.
```

```
   Power (1 token):   LR(0)  <  SLR(1)  <  LALR(1)  <  LR(1)
   State count:       small      small     small       LARGE
                                            ^^^^^
                               the sweet spot: LR(1) power-ish,
                               LR(0) size
```

### The LALR conflict — what merging costs you

Merging LR(1) states can create a conflict that neither the LR(1) automaton nor
either pre-merge state had. This is the *only* power LALR loses versus LR(1), and it
is a **reduce-reduce** conflict.

```
  Two LR(1) states with the same CORE but different lookaheads:

    State P:  [A -> w . , {a}]      [B -> w . , {b}]    (no conflict: a != b)
    State Q:  [A -> w . , {b}]      [B -> w . , {a}]    (no conflict: b != a)

  LALR merges P and Q (same core), UNIONING lookaheads:

    Merged:   [A -> w . , {a,b}]    [B -> w . , {a,b}]
                                    ^^^^^^^^^^^^^^^^^^^
              On `a`: reduce by A? or by B?  REDUCE-REDUCE CONFLICT.
              Neither original state was ambiguous; the merge created it.
```

Practical consequence: bison's infamous "reduce/reduce conflict" on grammars that
are technically LR(1) but not LALR(1). The fix is to refactor the grammar to give the
two rules distinguishable contexts, or to use an LR(1) generator (like `lalr1` vs
`lr.type=canonical`, or menhir).

| Conflict | LR(0) | SLR | LALR | LR(1) | Caused by |
|----------|-------|-----|------|-------|-----------|
| shift/reduce | common | reduced | reduced | reduced | completed item + shiftable item in one state (e.g. dangling else) |
| reduce/reduce | possible | possible | possible (from merge) | rarest | two completed items reducible on the same lookahead |

The classic **shift/reduce** example is the *dangling else*: `if E then if E then S
else S` — does `else` bind to the inner or outer `if`? yacc/bison default to
**shift** (bind to nearest `if`), which happens to be the language-correct choice,
and emit a warning.

---

## Parser Generators

```
   LALR(1) generators                  LL / PEG / GLR generators
   ==================                  =========================
   +--------+  +--------+              +--------+  +-----------+
   | yacc   |  | bison  |              | ANTLR  |  | tree-     |
   | (1975) |  | (GNU)  |              | (LL*)  |  | sitter    |
   +--------+  +--------+              +--------+  | (GLR-ish, |
   +--------+                          +--------+  |  incrmntl)|
   | menhir |  (LR(1)/LALR, OCaml)     | PEG.js |  +-----------+
   +--------+                          | / pest |  +-----------+
   Used by: GCC (historically),        | (PEG)  |  | Earley    |
   many C compilers, SQL parsers.      +--------+  | (any CFG) |
                                                   +-----------+
```

| Generator | Class | Notes |
|-----------|-------|-------|
| yacc / bison | LALR(1) (bison adds GLR) | the workhorses; emit ACTION/GOTO tables |
| menhir | LR(1)/LALR(1) | OCaml; better conflict explanations |
| ANTLR4 | ALL(*) (adaptive LL) | hand-grammar-friendly, good error messages |
| tree-sitter | GLR, incremental, error-tolerant | editors/IDEs — reparses on keystroke |
| PEG (pest, PEG.js) | parsing expression grammars | ordered choice, no ambiguity, but `*` is greedy/committed |
| Earley | all CFGs incl. ambiguous | O(n³) worst, O(n²) unambiguous, O(n) deterministic; NLP, research |

**The industry reality**: despite generators, most *production language* compilers
hand-write a recursive-descent parser. Generated parsers dominate for SQL, config
languages, protocol grammars, and one-off DSLs where the grammar is stable and error
messages matter less.

---

## Error Recovery — The Hard Part of Real Parsers

A theory parser stops at the first error. A real parser must recover and keep going
so it can report *many* errors and feed an IDE a partial tree.

```
  PANIC-MODE recovery (most common):
    On error, SKIP tokens until you hit a "synchronizing" token
    (`;`, `}`, `end`), then resume. Crude but robust.

       int x = = 5 ;  void f() ...
              ^ error here; skip to `;`, resume at `void`.

  PHRASE-LEVEL: insert/delete/replace a single token to repair locally
    ("inserted missing ';'"). Good messages, can cascade if wrong.

  ERROR PRODUCTIONS: add grammar rules for COMMON mistakes
    stmt -> error ;          # bison's `error` token
    Lets the grammar "expect" malformed input and recover gracefully.

  GLR / tree-sitter: keep MULTIPLE parse possibilities alive; on error,
    the surviving parse is often the intended one. This is why IDEs use
    tree-sitter -- a single typo doesn't blank the whole syntax tree.
```

The modern IDE bar is **error-tolerant, incremental** parsing: tree-sitter and the
Roslyn parser both produce a *complete* tree even for broken code, with error nodes
in place, and reparse only the edited region. Roslyn's parser inserts "missing"
tokens (zero-width synthetic nodes) so the tree shape is always valid for downstream
tooling.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Hand-written recursive descent (you've read C compiler source) | Still the dominant production technique — clang/Roslyn/rustc/V8/tsc all do it |
| yacc/bison `.y` grammar files | LALR(1) generators — the ACTION/GOTO tables are the LR automaton compiled to data |
| `System.Linq.Expressions` / expression trees | A parsed AST is the same idea: a tree you walk; the parser is what builds it |
| Roslyn `SyntaxTree`, red-green nodes | The output of an error-tolerant, incremental recursive-descent parser |
| Operator precedence in a calculator | Pratt parsing / precedence climbing — binding powers replace one-function-per-level |
| Regex (regular) vs grammar (context-free) | Lexer = regular = no nesting; parser = context-free = matched brackets, recursion |

The headline: **the theory ranks LR above LL in power, but industry ships LL
(recursive descent)** because hand-written parsers give better error messages,
trivially support incremental/error-tolerant reparsing, and are easier to maintain
than a generated state table. Power loses to engineering ergonomics here.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Parse a real programming language frontend | Hand-written recursive descent + Pratt for expressions |
| Parse expressions with many precedence levels | Pratt parsing / precedence climbing |
| Generate a parser for a stable DSL / SQL / config | bison (LALR), ANTLR4, or a PEG tool |
| Handle a grammar with left recursion | LR family (LALR/LR(1)) — it's native; LL needs rewriting |
| Get maximum 1-lookahead power with small tables | LALR(1) (yacc/bison) |
| Need true LR(1) power (LALR rejects your grammar) | menhir / canonical LR(1), or refactor the grammar |
| Parse ambiguous or natural-language-ish grammar | GLR or Earley |
| Reparse on every keystroke in an editor | tree-sitter (incremental, error-tolerant, GLR) |
| Resolve dangling-else | Shift (bind to nearest), the standard default |
| Report many errors, not just the first | Panic-mode sync tokens + error productions, or tree-sitter |

---

## Common Confusion Points

**LL and LR are not a strict hierarchy — but LL(1) ⊂ LR(1).** Neither LL nor LR
contains the other in general (different `k`, different grammar shapes), but the
common case LL(1) is a *proper subset* of LR(1) (and of LALR(1) for non-degenerate
grammars). Anything you can parse LL(1) you can parse LR(1); the reverse fails (left recursion).

**LALR conflicts come from state *merging*, not from the grammar being ambiguous.** A
grammar can be unambiguous and LR(1) yet still throw a LALR reduce/reduce conflict
because merging same-core states unions their lookaheads. The grammar is fine; LALR's
approximation is what breaks.

**SLR's weakness is using global FOLLOW.** SLR reduces on FOLLOW(A) regardless of
state. LALR computes lookahead *per state*, so it distinguishes contexts SLR
conflates. That is the entire SLR < LALR gap.

**Dangling-else is a shift/reduce conflict, and shifting is correct.** It is not an
ambiguity in the language if the spec says "else binds to nearest if" — it is an
ambiguity in the *grammar* that the parser resolves by preferring shift. yacc warns
but does the right thing.

**Recursive descent ≠ weak.** Production compilers ship recursive descent not because
LR is unavailable but because hand-written parsers win on diagnostics, incremental
reparse, and maintainability. Power and practicality diverge here.

**PEG is not CFG.** Parsing expression grammars use *ordered* choice (`/` commits to
the first match) and are unambiguous by construction, but that committed choice means
a PEG can silently parse a different language than the "same-looking" CFG. Greedy `*`
in PEG never backtracks across a committed choice.
