---
tags: [backfill]
ops: [backfill]
content_tags: [markdown]
proof_original: "03-SEMANTIC-ANALYSIS.md"
---
---
maxim_schema: maxim.frontmatter.v1
id: maxim:compilers:semantic-analysis
kind: guide
module: compilers
section: compilers
title: Semantic Analysis - Symbol Tables, Scopes, Type Checking and Inference
status: source-custody
source_custody: partial
current_path: compilers/03-SEMANTIC-ANALYSIS.md
canonical_path: compilers/03-SEMANTIC-ANALYSIS.md
backsource_ids: [proof-backfill:compilers:03-semantic-analysis, git-history:compilers:03-semantic-analysis]
concepts: [semantic analysis, symbol table, scope, type checking, type inference, unification, AST]
root_concepts: [semantic analysis]
index_roles: [guide, root-concept]
remap_from: []
remap_to: []
updated: null
---
# Semantic Analysis — Symbol Tables, Scopes, and Types

## The Big Picture

Parsing answers "is this well-formed syntax?" Semantic analysis answers "does it
*mean* something, and is it consistent?" — name resolution (what does `x` refer
to?), scope (where is `x` visible?), and type checking/inference (does `x + y`
make sense, and what type is it?). You know the typing judgments from type theory;
this guide is about the data structures and algorithms a frontend uses to *decide*
them at scale, and how Hindley-Milner inference actually runs.

```
                       SEMANTIC ANALYSIS PIPELINE

   parse tree (concrete)
        |  build/lower
        v
   +----------+        AST: desugared, names not yet resolved
   |   AST    |
   +----------+

        |
        |  PASS 1: build symbol tables (declarations -> scopes)
        v

   +-------------------+   scope tree:  global -> module -> fn -> block
   |  SYMBOL TABLES    |   each entry: name, kind, type-slot, source span
   +-------------------+

        |
        |  PASS 2: NAME RESOLUTION (every use -> its declaration)
        v

   +-------------------+   each IDENT node now points at a Symbol
   |  RESOLVED AST     |
   +-------------------+

        |
        |  PASS 3: TYPE CHECKING / INFERENCE (annotate every node)
        v

   +-------------------+   each expr node now carries a Type;
   |  TYPED AST        |   type errors emitted with spans
   +-------------------+

        |
        v  hand to IR generation (guide 04)
```

Read top-down: the tree is built, names are bound to declarations, and types are
checked or inferred — each pass annotating the same tree. The output is a **typed,
resolved AST**, the contract the IR generator consumes.

---

## Parse Tree vs AST

The parser can produce a *concrete syntax tree* (every token, every grammar
nonterminal) or directly an *abstract syntax tree* (only the semantically
meaningful structure). Frontends almost always want the AST.

```
  source:  -(1 + 2)

  CONCRETE (parse) tree              ABSTRACT (AST)
  =====================              ==============
        unary                            Neg
       /  |  \                            |
      -  expr ...                        Add
         /|\                            /   \
        ( expr )                     Int(1) Int(2)
          /|\
       1  +  2
   (records parens, the              (parens gone -- they only
    expr->term->factor chain)         affected structure, not meaning;
                                       no intermediate nonterminals)
```

```
  AST drops:  parentheses, redundant nonterminals (expr->term->factor),
              punctuation that only guided parsing.
  AST keeps:  operators, operands, declarations, control structure --
              everything with semantic content.
  AST may add: desugaring (for-loop -> while; a += b -> a = a + b;
              string interpolation -> concat calls).
```

Tools that must reproduce source exactly (formatters, refactoring engines, IDEs)
keep a *lossless* concrete tree instead — Roslyn's red-green trees and tree-sitter
both retain every character so the original text round-trips.

---

## Symbol Tables and Scope

A symbol table maps names to declarations. Because of nested scopes, it is really a
*tree of scopes*, and lookup walks outward from the current scope to the root.

```
   SCOPE CHAIN (lexical scoping)

   global scope:
   +----------------------------------+
   |  printf, main, MAX               |
   +----------------------------------+
              ^
              | parent
   function main():
   +----------------------------------+
   |  argc, argv, i                   |
   +----------------------------------+
              ^
              | parent
   block { ... }:
   +----------------------------------+
   |  i  (SHADOWS outer i), tmp       |
   +----------------------------------+

   Lookup("i") from the innermost block:
     found in block scope -> the shadowing `i`. Stop.
   Lookup("argc"):
     not in block, not... found in function scope. Stop.
   Lookup("printf"):
     walk all the way to global. Found.
   Lookup("nope"):
     reach root, not found -> UNRESOLVED NAME error.
```

| Implementation | Lookup | Scope entry/exit | Used by |
|----------------|--------|------------------|---------|
| stack of hash maps | O(1) avg per level, O(depth) chain | push/pop a map | many classic compilers |
| single hash map + scope marks | O(1), undo on exit | push markers, pop entries | fast, cache-friendly |
| persistent/immutable map | O(log n) | structural sharing, no undo | functional compilers, IDEs (snapshot per edit) |

Two subtleties that matter in real languages:

```
  SHADOWING:   an inner `i` hides an outer `i`. Legal in most languages;
               the inner scope's entry wins on lookup.

  FORWARD REFERENCE / HOISTING:
     - C: a function may be CALLED before its definition if DECLARED
          (the prototype goes in the table first).
     - JS: `var` and function declarations are HOISTED to the top of the
          scope (the binder inserts them before processing the body).
     - This is why semantic analysis often needs TWO passes: collect all
          declarations in a scope first, THEN resolve uses -- so mutual
          recursion and forward references work.
```

---

## Name Resolution

With scopes built, every identifier *use* is linked to its *declaration*. After
this pass, the AST's `IDENT` nodes no longer carry just a string — they carry a
pointer to a `Symbol`.

```
  Before resolution:        After resolution:
  Call                      Call
   |--callee: "f"            |--callee: -> Symbol#42 (fn f, defined at L3)
   |--arg:    "x"            |--arg:    -> Symbol#17 (param x, defined at L1)

  Resolution also catches:
    - use of undeclared name
    - duplicate declaration in one scope
    - use-before-declaration (where the language forbids it)
    - ambiguous overload / import collision
```

This is exactly Roslyn's *binder* phase and tsc's *binder*: build the symbol table,
then bind each syntax node to its symbol. The `SemanticModel` you query in Roslyn is
the result — "what does this identifier mean here?"

---

## Type Checking vs Type Inference

Two regimes. **Checking**: the program is fully annotated; verify the annotations
are consistent. **Inference**: annotations are absent; *reconstruct* the most
general types that make the program well-typed.

```
   TYPE CHECKING (e.g. Java, C, C#)        TYPE INFERENCE (e.g. ML, Haskell,
   ==============================            Rust locals, C# var, TS)
   int x = f(y);                           let x = f y           -- no annotations
   - look up type of f: int -> int          - assign fresh type vars
   - check y : int                          - generate equality CONSTRAINTS
   - check result int assignable to int     - SOLVE by UNIFICATION
   Local, syntax-directed, one walk.        - generalize remaining vars (forall)
                                            Global-ish; the famous algorithm
                                            is Hindley-Milner / Algorithm W.
```

You know the typing judgment `Γ ⊢ e : τ`. Checking *applies* the rules top-down;
inference *solves* for the metavariables that make the rules hold. The full
metatheory (soundness, principal types, parametricity) lives in
`programming-language-theory/02-TYPE-THEORY.md` and `formal-methods/04-TYPE-THEORY.md`
— here we run the algorithm.

### Bidirectional checking — the modern default

Most real type checkers are **bidirectional**: they alternate between *checking* a
term against a known expected type and *synthesizing* a type from a term. This is how
TypeScript, Rust, Swift, and modern functional languages localize inference and
produce good error messages.

```
  check(e, T):  "does e have type T?"      (type flows IN -- e.g. a lambda
                                            argument whose type is known)
  synth(e) -> T: "what type does e have?"  (type flows OUT -- e.g. a literal,
                                            a variable, a function call result)

  Rule of thumb:
    annotations + function results -> synthesize
    lambda bodies + container literals against expected -> check
```

---

## Hindley-Milner Inference, Worked

The HM core: assign fresh type variables, collect constraints from the typing
rules, solve by **unification**, then **generalize**. Here is `let id = \x -> x in
id id` reconstructed.

```
  Step 1 -- fresh vars and constraints for \x -> x :
     x : a            (fresh)
     body x : a
     so  \x -> x : a -> a

  Step 2 -- generalize at the `let`:
     id : forall a. a -> a       (a is not free in the environment -> bind it)

  Step 3 -- use `id id`. INSTANTIATE id twice with fresh vars:
     left  id : b -> b
     right id : c -> c
     application (left right): require (b -> b) = (c -> c)'s argument type
        unify  b   with  (c -> c)        =>  b := (c -> c)
        result type:  b  = (c -> c)
     so  id id : c -> c            (a function, the identity again)

  Generalize:  id id : forall c. c -> c
```

### Unification — the engine

Unification finds the most general substitution making two type terms equal. It is
the same algorithm behind Prolog and behind every HM type checker.

```
  unify(t1, t2):
    if t1, t2 are the same type var          -> ok, no-op
    if t1 is a var a                          -> bind a := t2  (OCCURS CHECK first!)
    if t2 is a var a                          -> bind a := t1  (OCCURS CHECK first!)
    if t1 = f(s1..sn), t2 = f(u1..un)         -> unify si with ui pairwise
    if constructors differ (Int vs Bool, ->)  -> TYPE ERROR

  OCCURS CHECK:  refusing to bind  a := (a -> a)  would create an infinite
                 type. The occurs check rejects it -> "cannot construct
                 infinite type" -- the error you see for  \x -> x x.
```

```
  Example unify( (a -> Int),  (Bool -> b) ):
     match the -> constructor, recurse:
       unify(a, Bool)  -> a := Bool
       unify(Int, b)   -> b := Int
     result substitution: { a := Bool, b := Int }
     both sides become  Bool -> Int.   Consistent.
```

HM gives **principal types** (a most-general type that every other valid type is an
instance of) and runs in near-linear time with union-find for the substitution —
though it is theoretically DEXPTIME in pathological let-nesting (rarely hit).

---

## Attribute Grammars — The Formal Frame

Semantic analysis is classically described as decorating the parse tree with
*attributes* that flow up (synthesized) or down (inherited). It is the formal model
behind "annotate every node with a type."

```
  SYNTHESIZED attribute: computed from children, flows UP.
     E.type  is synthesized from E1.type and E2.type in  E -> E1 + E2.

  INHERITED attribute: passed from parent/siblings, flows DOWN.
     declared type of a variable flows down into the scope where it's used.

           E.type  (up)
            / \
       E1.type E2.type
         ^       ^         both synthesized, combined at the parent

  Type-checking is mostly an S-attributed (synthesized-only) or
  L-attributed (one left-to-right pass) computation -- which is exactly
  why a single AST walk usually suffices.
```

Production compilers rarely *write* a formal attribute grammar, but the mental model
— "what flows up, what flows down, can I do it in one pass" — is precisely how you
reason about whether type checking needs one walk or a fixpoint.

---

## Old World → New World Bridges

| You know | Maps to |
|----------|---------|
| Roslyn `SemanticModel` / `ISymbol` | The output of name resolution: every syntax node bound to a symbol |
| Roslyn *binder* phase | The name-resolution pass building/walking symbol tables |
| C# `var` and `out var` | Local type inference — a constrained HM (no let-generalization across statements) |
| C# overload resolution | A constraint-solving search over candidate signatures, ranked by conversions |
| `dynamic` in C# | Deferring type checking to runtime — opting out of static semantic analysis |
| Generic constraints (`where T : IComparable`) | Bounded quantification — the checker verifies the bound at instantiation |
| TypeScript structural typing | Subtyping by shape; the checker compares members, not names (vs C#'s nominal) |

The headline bridge: **C#'s `var` is HM with the generalization step removed.** Full
HM (ML/Haskell) infers polymorphic `forall` types at `let`; `var` infers only the
single monomorphic type of one initializer. Same unification machinery, deliberately
weaker generalization so error messages stay local and predictable.

---

## Where the Errors Come From

```
  Lexical error:    bad character          (guide 01)
  Syntax error:     ill-formed structure   (guide 02)
  ----------------------------------------------------------------
  SEMANTIC errors (this guide):
     undeclared name             -> name resolution
     duplicate declaration       -> symbol table insert
     type mismatch               -> checking / failed unification
     "cannot infer type"         -> ambiguous, under-constrained inference
     "cannot construct infinite type" -> occurs check failure
     wrong arity / bad overload  -> checking call sites
     use before initialization   -> a dataflow check (borders on guide 05)
```

Good error messages are *the* differentiator of a production frontend, and they are
hardest here: a single mismatch can be reported at many nodes, and inference must
pick the most likely culprit. This is why hand-written checkers (Roslyn, tsc, rustc)
invest enormously in diagnostic quality.

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Bind every name to its declaration | Symbol tables + scope-chain name resolution |
| Handle shadowing | Innermost scope wins on lookup |
| Handle forward references / mutual recursion | Two passes: collect declarations, then resolve uses |
| Verify fully-annotated code | Type checking — syntax-directed, one walk |
| Reconstruct missing types | Type inference — Hindley-Milner / Algorithm W |
| Solve type equalities | Unification (with the occurs check) |
| Localize inference + good errors | Bidirectional checking (check vs synthesize) |
| Get C#-style `var` | HM without let-generalization |
| Reason about one-pass vs fixpoint | Attribute-grammar view (synthesized vs inherited) |
| Compare TS-style shapes | Structural subtyping (members, not names) |

---

## Common Confusion Points

**Parse tree ≠ AST.** The parse tree records the grammar derivation (every
nonterminal, every paren); the AST keeps only semantic structure. Formatters and
IDEs keep a lossless concrete tree; backends want the AST.

**Name resolution and type checking are different passes.** Resolution links a use to
a declaration (a graph problem over scopes). Type checking asks whether the resulting
program is well-typed (a constraint problem over types). Forward references break the
first; type errors break the second.

**Inference is not "no types," it is *reconstructed* types.** An HM program is just as
statically typed as an annotated one — the types are computed, not absent. "Untyped"
(dynamic) is a different thing entirely.

**The occurs check is why `\x -> x x` fails.** Without it, unification would build the
infinite type `a = a -> a`. The "cannot construct infinite type" diagnostic is the
occurs check firing — a correctness feature, not a limitation.

**`var` is not `dynamic`.** `var` is fully static inference resolved at compile time;
`dynamic` defers checking to runtime. They look similar at the keyword level and are
opposites in the type system.

**HM gives principal types; bidirectional/overload-heavy systems often don't.** Pure
HM has a unique most-general type. The moment you add subtyping, overloading, or rank-
n polymorphism, principality can be lost — which is why C#/TS/Swift use bidirectional
checking with explicit annotations at the boundaries.
