---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:lexing
kind: guide
module: compilers
section: compilers
title: Lexical Analysis - Regex to DFA, Tokenizing, Lexer Generators
status: source-custody
source_custody: partial
current_path: compilers/01-LEXING.md
canonical_path: compilers/01-LEXING.md
backsource_ids: [proof-backfill:compilers:01-lexing, git-history:compilers:01-lexing]
concepts: [lexing, tokenizing, regex, NFA, DFA, subset construction, maximal munch, lexer generators]
root_concepts: [lexical analysis]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Lexical Analysis — Regex → NFA → DFA → Tokens

## The Big Picture

The lexer turns a flat character stream into a flat token stream. It is the one
compiler stage that is *completely solved theory*: tokens are regular languages, so
a lexer is a finite automaton, and the whole construction — regex to NFA to DFA to
minimized DFA — is mechanical. You know this chain. The engineering question is not
"can we" but "how do real lexers handle longest-match, keywords, Unicode, and the
million-tokens-per-second throughput a language server needs."

```
+--------------------------------------------------------------------------+
|                      THE LEXER CONSTRUCTION CHAIN                        |
|                                                                          |
|   token specs (regexes)                                                  |
|        |                                                                 |
|        |  Thompson's construction (linear)                               |
|        v                                                                 |
|   +---------+        epsilon-moves, nondeterministic                     |
|   |   NFA   |        O(r) states for                                     |
|   +---------+        regex of size r                                     |
|        |                                                                 |
|        |  subset construction (powerset)                                 |
|        v                                                                 |
|   +---------+        deterministic, no epsilon, one move per char        |
|   |   DFA   |        worst case 2^n states                               |
|   +---------+        (rare in practice)                                  |
|        |                                                                 |
|        |  Hopcroft minimization  O(n log n)                              |
|        v                                                                 |
|   +-----------+      fewest states recognizing                           |
|   | min DFA   |      the same language                                   |
|   +-----------+                                                          |
|        |                                                                 |
|        |  drive with input + MAXIMAL MUNCH + token actions               |
|        v                                                                 |
|   +-----------------------------------------------------------+          |
|   |  TOKEN STREAM:  IDENT("foo") LPAREN INT(42) RPAREN SEMI   |          |
|   +-----------------------------------------------------------+          |
+--------------------------------------------------------------------------+
```

Read top-down: the spec compiles to an NFA, the NFA determinizes to a DFA, the DFA
minimizes, and the minimized DFA — plus the longest-match rule and per-token
actions — is the lexer. Everything above the bottom box is offline (lexer-generator
time); the bottom box is the hot loop at compile time.

---

## From Tokens to a Recognizer

A token class is a regular expression. The classic identifier and integer specs:

```
  IDENT   = [A-Za-z_][A-Za-z0-9_]*
  INT     = [0-9]+
  WS      = [ \t\r\n]+
  KEYWORD = if | else | while | return | ...
```

### Thompson's construction (regex → NFA)

Each regex operator becomes a small NFA fragment with epsilon transitions; fragments
compose. For `a(b|c)*`:

```
            eps         +--> b -->+
   ->(0)--a-->(1)--eps->(2)       (3)--eps-->((5))   accept
                         ^   +--> c -->+   |
                         |              v   |
                         +------- eps -----+
                    (the (b|c) loop: enter, choose b or c, loop back or exit)
```

Size is linear in the regex: an `r`-character regex yields O(r) states. The cost of
this convenience is nondeterminism — epsilon edges and multiple `a`-edges out of one
state mean you cannot run it by single-stepping.

### Subset construction (NFA → DFA)

Determinize by tracking the *set* of NFA states you could be in. Each DFA state is
an epsilon-closure of NFA states; on input `c`, move every member and take the
closure of the result.

```
  DFA state = subset of NFA states (after epsilon-closure)

  start  = eps-closure({0})
  move(S, c) = eps-closure( { t : s in S, s --c--> t } )

  Worked (for a(b|c)*):
    A = closure({0})              = {0}
    move(A,'a') = closure({1})    = {1,2,3,4? ...}  -> B    (entered the loop)
    move(B,'b') = closure(...)    -> B'  (accepting, can loop)
    move(B,'c') = closure(...)    -> B'' (accepting, can loop)
    B', B'' accept; b/c keep you in accepting states.
```

Worst case the DFA has 2^n states for n NFA states — but pathological blowup needs
contrived regexes (`(a|a)*...` style). Real token sets stay small. This is the same
powerset determinization you saw for NFAs in automata theory; nothing new, just
applied.

### Hopcroft minimization (DFA → minimal DFA)

Partition states into equivalence classes (accepting vs non-accepting), then refine:
two states are distinguishable if some input drives them to distinguishable states.
Refine until stable. O(n log n). The result is the unique (up to renaming) minimal
DFA for the language.

| Stage | Algorithm | Cost | Determinism |
|-------|-----------|------|-------------|
| regex → NFA | Thompson | O(r) states | nondeterministic, ε-moves |
| NFA → DFA | subset/powerset | up to 2^n states | deterministic |
| DFA → min DFA | Hopcroft | O(n log n) | deterministic, minimal |

---

## Maximal Munch — The Rule That Makes Lexing Work

A DFA recognizes *a* lexeme. A lexer must repeatedly carve the **longest** valid
lexeme from the remaining input. That is the **maximal-munch** (longest-match) rule,
and it is the central engineering decision of every lexer.

```
  Input:  "if x>=10"

  Naive (shortest match) would stop at the first accepting state:
     "i" -> IDENT? but DFA can keep going...

  Maximal munch: keep consuming while a transition exists; remember the
  LAST accepting state seen; when stuck, emit the token for that state and
  rewind input to just after it.

  position ->  i  f     x     >  =     1  0
               ^^                ^^^^         ^^^^
               "if" is a keyword (longest match beats IDENT "i","if")
                                 ">="  beats ">" then "="
                                              "10" is one INT, not "1","0"
```

The "remember last accepting state, then rewind" loop is the canonical lexer driver:

```
  start_of_lexeme = pos
  last_accept = NONE
  state = DFA.start
  while transition(state, input[pos]) exists:
      state = transition(state, input[pos]); pos++
      if state is accepting: last_accept = (state, pos)
  if last_accept == NONE: ERROR (no valid token)
  emit token for last_accept.state
  pos = last_accept.pos          # rewind past the longest match
```

### Where maximal munch bites

```
  C++ before C++11:   vector<vector<int>>
                      ">>" lexed as the shift operator, not two closers!
                      Required a special-case in the parser/lexer.

  a---b   in C:       "a" "--" "-" "b"  (longest-match grabs "--" first),
                      not "a" "-" "--" "b". Bug magnet.

  Rust ranges:        1..10   "1" ".." "10"  -- but  1.0  is a float.
                      The lexer needs lookahead to disambiguate `.`.
```

These are not theory gaps — they are the price of a greedy longest-match rule, and
every language spec pins down the resolution.

---

## Keywords vs Identifiers — The Standard Trick

You almost never put every keyword in the DFA as its own regex. Keywords *are* valid
identifiers, so you lex an identifier and then look it up.

```
  +----------------+      lex with IDENT regex      +------------------+
  | char stream    | -----------------------------> | lexeme "return"  |
  +----------------+                                 +--------+--------+
                                                              |
                                              hash-table lookup in keyword set
                                                              |
                                         +--------------------+-------------+
                                         |                                  |
                                   in keyword set?                    not found
                                         |                                  |
                                         v                                  v
                                 emit KW_RETURN                       emit IDENT("foo")
```

This keeps the DFA small (one identifier pattern, not 50 keyword patterns whose
states would dominate the table) and makes adding a keyword a one-line table change.
Perfect-hash generators (gperf) make the lookup branchless. C# (Roslyn) and most
production lexers do exactly this.

---

## Lexer Generators — and Why Many Modern Lexers Are Hand-Written

```
   GENERATED                                 HAND-WRITTEN
   =========                                 ============
   You write token regexes;                  You write the state machine
   a tool emits the DFA table + driver.      (or just a switch loop) directly.

   +----------+   +--------+   +---------+    +---------------------------+
   | lex/flex |   | re2c   |   | Logos   |    | clang, Roslyn, V8, rustc  |
   | (C)      |   | (C/C++)|   | (Rust   |    | hand-written lexers       |
   |          |   | inline |   |  proc-  |    |                           |
   |          |   |  DFA)  |   |  macro) |    | Why: error messages,      |
   +----------+   +--------+   +---------+    | speed, incremental relex, |
                                              | weird context-sensitive   |
   Pros: declarative, correct by             | rules, trivia (comments/  |
     construction, fast to change.           | whitespace) attachment.   |
   Cons: generic error messages, awkward                                  |
     for context-sensitive tokens.          +---------------------------+
```

| Tool | Lang | Form | Notable user |
|------|------|------|--------------|
| lex / flex | C | generated DFA table | classic Unix toolchain |
| re2c | C/C++ | inline DFA, no runtime | git, PHP, ninja |
| ragel | many | state machine compiler | Mongrel, Sphinx |
| ANTLR (lexer) | Java/many | generated, integrated with parser | many DSLs |
| Logos | Rust | derive macro → DFA | many Rust frontends |
| tree-sitter | C | incremental, error-tolerant | editors / IDEs |

Production language compilers usually **hand-write** the lexer. The reasons are all
engineering, not theory: precise error recovery and positions, raw throughput for a
language server relexing on every keystroke, attaching "trivia" (comments and
whitespace) to tokens for formatters, and context-sensitive lexing (string
interpolation, here-docs, Python indentation) that a pure regex DFA cannot express.

---

## Beyond Pure Regular: Where Lexers Cheat

A few common token-level needs are *not* regular and require the lexer to carry a
little state — a deliberate, bounded departure from the DFA model.

```
  Python indentation (off-side rule):
     The lexer keeps an INDENT STACK and emits synthetic INDENT/DEDENT
     tokens. A pure DFA has no stack -> this is the lexer doing a tiny
     bit of the parser's job.

  String interpolation  "$"+expr+"":
     Lexer modes / a mode stack. Entering ${ switches to "expression mode";
     the matching } pops back to "string mode".

  Nested comments  /* ... /* ... */ ... */ :
     Requires a counter -> not regular (matched nesting is context-free).
     Lexers special-case it with a depth counter.
```

The clean theory says lexing is regular. The clean theory is a guideline; real
lexers add a stack or a mode register exactly where the language forces them to, and
keep the DFA for everything else.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| .NET `Regex` (backtracking NFA engine) | A *lexer* uses a DFA — no backtracking, linear time, but no captures/backrefs. Different trade-off: throughput over expressiveness. |
| `System.Text.RegularExpressions` catastrophic backtracking | Cannot happen in a DFA lexer — DFA is O(n) in input length, guaranteed. RE2 / re2c chose DFA precisely to kill ReDoS. |
| Roslyn `SyntaxToken` with leading/trailing trivia | The hand-written lexer attaches whitespace/comments as trivia so the parser sees clean tokens but the formatter keeps everything. |
| A `switch` statement over characters | That *is* a hand-coded DFA — each `case` is a state transition. Most hand-written lexers are exactly this. |
| Tokenizing in a `StringTokenizer` | Same job, no token classes/positions — a lexer additionally classifies and tracks source spans for diagnostics. |

The headline bridge: **a regex *library* (.NET, PCRE) and a lexer's regex are not the
same machine.** Libraries use backtracking NFAs for captures and backreferences;
lexers use DFAs for guaranteed linear time and high throughput. RE2 and re2c exist
because Google needed the DFA guarantee at scale.

---

## The Token Stream — What Sema and the Parser Receive

```
  source:  return x + 1;

  +---------------------------------------------------------------+
  | KW_RETURN  span=[0,6)                                         |
  | IDENT "x"  span=[7,8)                                         |
  | PLUS       span=[9,10)                                        |
  | INT 1      span=[11,12)   value=1                             |
  | SEMI       span=[12,13)                                       |
  | EOF                                                           |
  +---------------------------------------------------------------+
       ^                ^                       ^
       kind             lexeme/value            source span (for errors)
```

Every token carries (1) a **kind** (the token class), (2) a **value/lexeme** where
relevant (the literal `1`, the identifier text `x`), and (3) a **source span** so
later phases can point error messages at the right characters. Drop the span and you
lose the ability to produce a usable diagnostic — the single most important
non-theory property of a real lexer.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Recognize a token class | A regex → DFA (one DFA per language, all classes merged) |
| Carve the next token from input | Maximal munch (longest match, remember last accept, rewind) |
| Recognize keywords | Lex as IDENT, then hash-lookup against the keyword set |
| Guarantee linear-time lexing (no ReDoS) | A DFA lexer (re2c / RE2-style), never a backtracking engine |
| Generate a lexer declaratively | flex / re2c / Logos / ANTLR lexer |
| Build a compiler-grade lexer | Hand-write it — error positions, speed, trivia, incremental relex |
| Handle Python indentation | Indent stack emitting synthetic INDENT/DEDENT tokens |
| Handle string interpolation | Lexer modes / a mode stack |
| Relex on every keystroke (IDE) | Incremental, error-tolerant lexer (tree-sitter) |

---

## Common Confusion Points

**A lexer DFA does not backtrack — but maximal munch *rewinds*.** The DFA itself is
deterministic and linear. The longest-match loop may consume past the last accepting
state and then rewind the input pointer to it. That rewind is bounded by the lexeme
length, not exponential backtracking. Different mechanism, easy to conflate.

**Regex in a lexer ≠ regex in `.NET`/PCRE.** Lexer regexes compile to DFAs (no
captures, no backreferences, linear time). Library regexes are backtracking NFAs
(captures, backreferences, possible catastrophic blowup). Same syntax, different
machine, different guarantees.

**Keywords are usually not in the DFA.** Putting every keyword in as its own pattern
bloats the DFA. The standard design lexes an identifier and looks it up — keywords
are a *property of the symbol table lookup*, not a separate automaton.

**Maximal munch is a choice with consequences.** `a---b`, `>>` in templates, and
`1..10` vs `1.0` are all artifacts of greedy longest-match. The language *spec* must
state the rule; the lexer cannot guess.

**Some "lexing" is not regular.** Python indentation, nested comments, and string
interpolation force the lexer to keep a stack or a counter. The "lexing is regular"
slogan is the 90% case; production lexers carry the minimum extra state the language
demands. The full power hierarchy (regular → context-free → ...) is assumed here;
this is just where the boundary is crossed in practice.
