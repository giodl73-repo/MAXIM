# Session 3 — Programming Languages

## Purpose

A **cross-language reference series** across 16 major languages.
Same template for every language so you can slot any language against C# (home base) immediately.
Not tutorials. Reference cards for someone who already knows PL theory and needs syntax + ecosystem facts.

---

## Series Structure

```
languages/
├── 00-OVERVIEW.md     — genealogy, paradigm map, type-system axes, early/late binding
├── 01-CHEATSHEET.md   — comparison tables: operators, delimiters, collections, 16 languages × 10 topics
│
├── 02-C.md            — C: the substrate everything compiles toward
├── 03-CPP.md          — C++: objects, templates, RAII, undefined behavior
├── 04-JAVA.md         — Java: JVM, nominal typing, checked exceptions
├── 05-CSHARP.md       — C#: home base reference card
├── 06-PYTHON.md       — Python: dynamic, duck typing, GIL, asyncio
├── 07-JAVASCRIPT.md   — JS: dynamic, prototypal, event loop
├── 08-TYPESCRIPT.md   — TypeScript: structural types, type narrowing, template literal types
├── 09-RUST.md         — Rust: ownership, borrow checker, zero-cost abstractions
├── 10-GO.md           — Go: structural interfaces, goroutines, explicit error returns
├── 11-HASKELL.md      — Haskell: pure FP, HM inference, lazy evaluation, monads
├── 12-FSHARP.md       — F#: functional .NET, algebraic types, computation expressions
├── 13-KOTLIN.md       — Kotlin: modern JVM, null safety, coroutines
├── 14-SWIFT.md        — Swift: value semantics, protocols, ARC, Swift concurrency
├── 15-SCALA.md        — Scala: FP + OOP on JVM, implicits, cats/zio
├── 16-RUBY.md         — Ruby: metaprogramming, duck typing, convention over configuration
└── 17-SQL.md          — SQL: relational algebra, set semantics, declarative
```

---

## Per-Language Template

Every language file covers the same sections in the same order:

| Section | Content |
|---------|---------|
| **Type system snapshot** | 6-axis table: binding, typing, strength, nominal/structural, inference, memory |
| **Syntax reference card** | Variables, equality, logical ops, collections, if/match, strings, null, functions, errors |
| **What makes it distinct** | 3–5 differentiators that don't compress into a table cell |
| **Ecosystem** | Toolchain, package manager, dominant libraries, where this language wins |
| **Gotchas from C#** | Traps specific to someone coming from C# |
| **When to choose it** | Decision guide |

---

## Cross-Reference Index

| What you want | Where to look |
|---------------|---------------|
| Type theory → real toolchains | `00-OVERVIEW.md` |
| "What's Python's null syntax?" | `01-CHEATSHEET.md` — comparison tables |
| "What makes Rust different?" | `09-RUST.md` — What Makes It Distinct |
| Haskell monads / type classes | `11-HASKELL.md`, also `computing/23-PL-THEORY.md` |
| Rust borrow checker theory | `09-RUST.md`, also `computing/22-COMPILERS.md` |
| F# vs C# — same CLR, different worldview | `12-FSHARP.md` |

---

## Learner Context

MIT Math + TCS — these are **not being taught**:
- HM type inference, parametric/ad-hoc polymorphism
- Lambda calculus, Curry-Howard
- Operational/denotational semantics
- Formal language theory, automata, decidability

What this series delivers instead:
- Where each theoretical concept surfaces in real compilers and runtimes
- The specific syntax each language chose and the tradeoffs behind it
- Ecosystem vocabulary — what's idiomatic vs anti-pattern
- Migration model: C# as home base, every other language bridged to it

---

## Artifact Index

| File | Language | Status |
|------|----------|--------|
| `languages/00-OVERVIEW.md` | Taxonomy — all languages | ✅ Complete |
| `languages/01-CHEATSHEET.md` | Universal comparison tables | ✅ Complete |
| `languages/02-C.md` | C | ✅ Complete |
| `languages/03-CPP.md` | C++ | ✅ Complete |
| `languages/04-JAVA.md` | Java | ✅ Complete |
| `languages/05-CSHARP.md` | C# | ✅ Complete |
| `languages/06-PYTHON.md` | Python | ✅ Complete |
| `languages/07-JAVASCRIPT.md` | JavaScript | ✅ Complete |
| `languages/08-TYPESCRIPT.md` | TypeScript | ✅ Complete |
| `languages/09-RUST.md` | Rust | ✅ Complete |
| `languages/10-GO.md` | Go | ✅ Complete |
| `languages/11-HASKELL.md` | Haskell | ✅ Complete |
| `languages/12-FSHARP.md` | F# | ✅ Complete |
| `languages/13-KOTLIN.md` | Kotlin | ✅ Complete |
| `languages/14-SWIFT.md` | Swift | ✅ Complete |
| `languages/15-SCALA.md` | Scala | ✅ Complete |
| `languages/16-RUBY.md` | Ruby | ✅ Complete |
| `languages/17-SQL.md` | SQL | ✅ Complete |

---

## Session Log

| Date | What Was Done |
|------|---------------|
| 2026-02-22 | Session 3 initialized. 19 files: overview + cheatsheet + 16 language reference cards + SQL. |
