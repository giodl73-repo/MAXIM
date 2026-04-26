# Programming Languages — Taxonomy & Theory Map

---

## Reading Order for C# Developers

The guides in this section are written with C# as the anchor. Every language is explained relative to what you already know — the .NET runtime model, nominal type system, GC, async/await, LINQ, and OOP patterns. Use this table to sequence your reading based on what you want to get out of it.

| If you want to... | Read next | Why |
|---|---|---|
| Understand the JVM ecosystem | Java → Kotlin | Java is the C# parallel (same era, same intent, different tradeoffs); Kotlin modernizes it the way C# modernized itself |
| Write systems code / escape the GC | C → Rust | C is the foundation everything else builds on; Rust is the safe modern version with ownership instead of GC |
| Learn functional programming on familiar ground | F# → Haskell | F# is .NET FP with HM inference — close enough to C# to start; Haskell is the deep end, pure and uncompromising |
| Build web frontends | JavaScript → TypeScript | JS is unavoidable ecosystem knowledge; TS adds structural types that feel C#-adjacent |
| Understand Go's concurrency model | Go | Radical simplicity as a design philosophy; goroutines + channels are a distinct concurrency model from async/await |
| Apple platform development | Swift | Closest to C# in day-to-day feel; ARC vs GC is the key difference to internalize |
| Explore the ML/data ecosystem | Python | Not because of the language — because of the ecosystem; scripting complement to everything else |
| Understand JVM-side functional programming | Scala | After Kotlin or Haskell; more complex type system, but powerful; typeclasses via implicits/givens |
| Scripting, Rails DSL patterns, metaprogramming | Ruby | After Python; different philosophy (Smalltalk lineage, open classes, everything is an object) |
| Data querying / relational thinking | SQL | Foundational; LINQ is .NET's answer to SQL — reading SQL makes LINQ's design obvious |

The guides are designed to be read in any order but reward sequential reading within a tier: the mainstream tier (C, C++, Java, C#, Python, JS, TS) builds shared vocabulary, and the specialist tier (Rust, Go, Swift, Kotlin, Haskell, F#, Scala, Ruby, SQL) assumes you have that vocabulary.

---

## Language Genealogy

```
ALGOL (1958) — block structure, lexical scope
│
├── LISP (1958) — homoiconicity, garbage collection, dynamic typing
│   ├── Scheme → Racket
│   ├── Common Lisp
│   └── ──influenced──► ML (1973, Robin Milner)
│                        ├── Standard ML
│                        ├── OCaml (1996) ─── Reason/ReScript
│                        └── Haskell (1990) ─── lazy, pure, typeclasses
│                            └── ──influenced──► Rust traits, F# DUs, Scala implicits/givens
│
├── CPL → BCPL → B → C (1972, Ritchie)
│   │
│   ├── C++ (1983, Stroustrup) — classes on top of C
│   │   └── ──influenced──► D, early Rust design
│   │
│   ├── Objective-C (1984) → Swift (2014, Apple)
│   │   └── Swift influenced by: Rust ownership + Haskell types + C++ value semantics
│   │
│   ├── Java (1995, Gosling) — "write once run anywhere"
│   │   ├── Kotlin (2011, JetBrains) — modern JVM
│   │   ├── Scala (2004, Odersky) — FP + OOP fusion
│   │   └── Clojure (2007, Hickey) — Lisp on JVM
│   │
│   └── C# (2000, Hejlsberg) — Java done right (Microsoft)
│       └── F# (2005, Syme) — ML/Haskell spirit on .NET
│
├── SIMULA (1967) — invented OOP (classes, virtual methods)
│   └── Smalltalk (1972, Kay) — "everything is a message send"
│       └── Ruby (1995, Matz) — Smalltalk purity + Perl pragmatism
│
└── FORTRAN (1957) → COBOL (1959) → Pascal (1970) → Delphi
    └── (less relevant lineage)

INDEPENDENT ORIGINS:
  JavaScript (1995, Eich) — 10 days: Scheme semantics + Self prototype OOP + Java syntax
      └── TypeScript (2012, Hejlsberg) — structural types on top of JS
  Python (1991, van Rossum) — ABC + Modula-3 influences; readability as core value
  Go (2009, Google) — C + CSP + simplicity; reaction against C++ complexity
  SQL (1974, IBM/Codd) — relational algebra → SEQUEL → SQL standard
  Rust (2010, Mozilla) — linear/affine types + Cyclone regions + C++ performance
```

---

## Paradigm Spectrum

> **C# sits here**: Multi-paradigm — primarily OOP (classes, interfaces, inheritance) with functional features layered in starting with C# 3 (LINQ, lambdas, expression trees) and accelerating through C# 9+ (records, pattern matching, immutability idioms). On the imperative/declarative axis, C# spans from imperative loops to declarative LINQ queries. Not purely anything.

```
IMPERATIVE ◄──────────────────────────────────────────────────────────► DECLARATIVE
   │                                                                           │
   C, Go     C++, Java,    Python,    Scala,      Haskell,     SQL, CSS,
             C#, Kotlin    Ruby,      F#,          Erlang        Prolog
                           JS, TS     Clojure
   │                                                                           │
 "how"                    "how + what"                               "what"
 sequence                   mixed                                set/logic/relation

PROCEDURAL → OBJECT-ORIENTED → FUNCTIONAL → DECLARATIVE/LOGIC
     C         Java, C#, C++     Haskell, F#       SQL, Prolog
               Python, Ruby      Scala (hybrid)
               JavaScript        Rust (hybrid)
```

C# occupies the same band as Java and C++ on the OOP axis, but has moved further toward functional than either — more so than Java (records, pattern matching, discriminated union emulation via sealed classes), less so than F# (which is functional-first with OOP as the secondary mode).

---

## Type System — 6 Axes

> **C# anchor summary**: Static · Strong · Nominal (with some structural via interfaces, and duck typing available via `dynamic`) · Partial inference (`var`, LINQ type inference) · Nominal subtyping + interface dispatch · GC (generational, .NET runtime). The axes below show where every other language sits relative to this baseline.

### Axis 1: When Are Types Checked?

```
STATIC (compile time)              GRADUAL                DYNAMIC (runtime)
────────────────────────────────────────────────────────────────────────────
C, C++, Java, C#, Rust,           TypeScript             Python, JavaScript,
Go, Haskell, F#, Kotlin,          (any = escape hatch)   Ruby
Swift, Scala

Implication: static = errors at compile time; dynamic = errors at runtime
```

**C# = Static.** `var` is still static — the type is inferred at compile time and fixed. `dynamic` is the escape hatch that opts into runtime dispatch, similar to TypeScript's `any`.

### Axis 2: Typing Strength (implicit coercions?)

```
STRONG (no surprise coercions)     WEAK (implicit coercions)
──────────────────────────────────────────────────────────────
Python, Haskell, Rust,             C (int/pointer freely mix)
Java, C#, F#, Kotlin,              C++ (extensive implicit conversions)
Swift, Scala, Go, Ruby             JavaScript ("1" + 1 = "11"; "1" - 1 = 0)

"Strong" means: if you want to add an int to a float, you must say so.
JavaScript is both dynamically typed AND weakly typed — worst of both worlds.
```

**C# = Strong.** You cannot add an `int` to a `double` without an explicit cast or promotion. The compiler enforces this. C++ is weaker than C# — implicit conversions are extensive and often surprising.

### Axis 3: Nominal vs Structural vs Duck

```
NOMINAL                         STRUCTURAL                    DUCK
(name determines type)          (shape determines type)       (runtime shape check)
────────────────────────────────────────────────────────────────────────────
C, C++, Java, C#,               TypeScript (primary),         Python,
Haskell, Rust, Kotlin,          Go (interfaces only),         Ruby,
Swift, Scala, F#                OCaml (objects)               JavaScript

Nominal: Dog and Cat are different types even if both have .name: string.
Structural: if they both have .name: string they're compatible (TS does this).
Duck: if it quacks it's a duck — discovered at runtime only.
```

**C# = Nominal.** Two interfaces with identical shape are not interchangeable unless there's an explicit relationship. The contrast with TypeScript is sharp: in TS, structural compatibility is all that matters. Go interfaces are structural — a type satisfies an interface by having the right methods, no `implements` keyword needed.

### Axis 4: Type Inference

```
FULL HM INFERENCE               PARTIAL                        NONE
(type flows both ways)          (local, one direction)         (always annotate)
────────────────────────────────────────────────────────────────────────────
Haskell, OCaml, F#,             C++ (auto), Java (var),       C (pre-C++11)
Rust (local+complex),           C# (var), TypeScript,
Scala (local)                   Go (:=), Kotlin, Swift

HM = Hindley-Milner: bidirectional, whole-program inference
C#/Java var: unidirectional, right-hand-side only
```

**C# = Partial (local, unidirectional).** `var x = someExpression` infers `x`'s type from the right-hand side. F# and Haskell have full HM inference — the type of a function argument can be inferred from how it's used later in the body, with no annotation needed anywhere. C# cannot do this.

### Axis 5: Subtyping / Polymorphism Model

```
NOMINAL SUBTYPING          STRUCTURAL SUBTYPING    TRAIT/TYPECLASS      PARAMETRIC
(class hierarchy)          (shape matching)        (ad-hoc polymorphism) (generics)
────────────────────────────────────────────────────────────────────────────────────
Java extends/implements    TypeScript types,        Rust traits,         All typed
C# class/interface,        Go interfaces,           Haskell typeclasses, languages
Kotlin, Scala, Swift       OCaml object types       F# interfaces,       (some better
                                                     Scala givens/implicits than others)
```

**C# = Nominal subtyping + generics.** The class/interface hierarchy is the primary polymorphism mechanism. C# generics are reified at runtime (unlike Java type erasure), which is closer to C++ templates in one sense but without monomorphization.

### Axis 6: Memory Model

```
MANUAL              RAII/OWNERSHIP          REFERENCE COUNTING      GC (TRACING)
(you manage)        (compiler manages)       (reference counted)     (runtime manages)
────────────────────────────────────────────────────────────────────────────────
C (malloc/free)    Rust (owned values,      Python (primary + cyclic Go (tricolor mark-sweep)
                   zero-cost drop)           collector for cycles)   Java (G1, ZGC, Shenandoah)
                   C++ (RAII, shared_ptr     Swift (ARC — compiler   C# (.NET GC, gen 0/1/2)
                   is ref-counted)           inserts retain/release) Haskell (GHC generational)
                                             C++ shared_ptr (manual  Kotlin/Scala/F# (JVM GC)
                                             use of RC)              Ruby/JavaScript (V8/etc)
```

**C# = GC (generational tracing).** The .NET GC is a generational, concurrent, stop-the-world-minimized collector — gen 0/1/2 with background GC threads from .NET 4.5+, and server GC tuned for throughput. Rust eliminates the GC entirely via ownership; Swift uses ARC (deterministic, no pauses, but requires careful cycle management).

---

## Early Binding vs Late Binding

This is one of the most important axes for performance reasoning.

### Early Binding (Static Dispatch)

The callee is resolved at **compile time**. The call site gets a direct jump instruction.

```
SOURCE                    COMPILE TIME              MACHINE CODE
─────────────────────────────────────────────────────────────────
foo(x);               ──► resolve foo to addr ──► CALL 0x7ff8_a3b2
                                                   (direct jump)

int add(int a, int b);   ──►  resolved immediately
add(1, 2);
```

**Where you get early binding:**
- C: all function calls (function pointers are late, regular calls are early)
- C++ non-virtual methods: `Foo::method()` — direct call
- Rust generics: `fn sum<T: Add>(a: T, b: T)` — **monomorphized** per concrete type, all static dispatch
- Java/C# static methods and final/sealed classes
- Haskell with optimization: typeclass dictionary often inlined away

### Late Binding (Dynamic Dispatch)

The callee is resolved at **runtime**. Requires an indirection.

```
C++ VIRTUAL DISPATCH:

  object ptr
      │
      ▼
  ┌──────────────────────────────────────┐
  │ vptr ──► vtable: [0]dtor [1]speak()  │
  │ field1                               │
  │ field2                               │
  └──────────────────────────────────────┘
  1 pointer load + 1 indirect call

JAVA/C# INTERFACE DISPATCH:

  object ref
      │
      ▼
  ┌──────────────────────────────────────┐
  │ typeptr ──► method table             │
  │ field1                               │
  └──────────────────────────────────────┘
      │
      ▼
  ┌──────────────────────────────────────┐
  │ interface slot ──► concrete method   │
  └──────────────────────────────────────┘
```

**Where you get late binding:**
- C++ `virtual` methods: vtable lookup per call
- Java: ALL instance methods are virtual by default (JIT can devirtualize common cases)
- C#: must opt in with `virtual`; non-virtual methods are statically dispatched
- Python: `__dict__` attribute lookup chain on every call (LOAD_ATTR bytecode)
- JavaScript: prototype chain walk, property lookup (V8 uses "hidden classes" to speed this up)
- Go interfaces: (type, value) fat pointer — indirect call through function pointer table
- Rust `dyn Trait`: fat pointer (data ptr + vtable ptr) — late binding

### The Rust Duality (Key Pattern)

```rust
// EARLY BINDING — monomorphized, zero cost
fn print_all<T: Display>(items: &[T]) { ... }
// Compiler generates: print_all_i32, print_all_String, etc.
// Binary is larger; no runtime cost

// LATE BINDING — dynamic dispatch, runtime cost
fn print_all(items: &[&dyn Display]) { ... }
// Single function; vtable lookup per call
// Binary is smaller; runtime indirection cost
```

---

## Language Quick Taxonomy Table

| Language | Static? | Strong? | Nominal? | Inference | Memory | Binding default |
|----------|---------|---------|----------|-----------|--------|-----------------|
| C        | [OK] | [NO] weak | [OK] | [NO] none | manual | early |
| C++      | [OK] | [NO] weak | [OK] | partial (auto) | RAII/manual | early + vtable |
| Java     | [OK] | [OK] | [OK] | partial (var) | GC | late (virtual default) |
| **C#**   | **[OK]** | **[OK]** | **[OK]** | **partial (var)** | **GC** | **early (non-virtual default)** |
| Python   | [NO] | [OK] | duck | [NO] none | RC+GC | late (always) |
| JS       | [NO] | [NO] weak | duck | [NO] none | GC | late (always) |
| TS       | gradual | [NO] | structural | partial | GC | late (always) |
| Rust     | [OK] | [OK] | [OK] | partial/local | ownership | early (+ dyn for late) |
| Go       | [OK] | [OK] | structural (iface) | partial (:=) | GC | late (via interface) |
| Haskell  | [OK] | [OK] | [OK] | full HM | GC | early (+ class dispatch) |
| F#       | [OK] | [OK] | [OK] | full HM | GC | early |
| Kotlin   | [OK] | [OK] | [OK] | partial | GC | late (virtual default) |
| Swift    | [OK] | [OK] | [OK] | partial | ARC | early + protocol dispatch |
| Scala    | [OK] | [OK] | [OK] | partial | GC | late (virtual default) |
| Ruby     | [NO] | [OK] | duck | [NO] none | GC | late (always) |
| SQL      | varies | [OK] | N/A | N/A | server | N/A |

C# row is bolded as the reference baseline. Read every other row as a delta from that row.

---

## Common Confusion: Nominal vs Structural in Practice

```csharp
// C# — NOMINAL: two types with identical shape are NOT the same
interface IFoo { string Name { get; } }
interface IBar { string Name { get; } }

class Dog : IFoo { public string Name => "Rex"; }
// Dog implements IFoo, does NOT implement IBar, even though shape is identical
```

```typescript
// TypeScript — STRUCTURAL: compatible shape = compatible type
interface IFoo { name: string; }
interface IBar { name: string; }

const dog = { name: "Rex" };
const foo: IFoo = dog;  // [OK] — compatible
const bar: IBar = dog;  // [OK] — compatible — TypeScript doesn't care about name
```

```go
// Go — STRUCTURAL interfaces: implement by shape, no declaration needed
type Stringer interface { String() string }

type Dog struct { Name string }
func (d Dog) String() string { return d.Name }
// Dog implicitly satisfies Stringer — no "implements" keyword
```

---

## The Expression Problem

A language design tension: can you add both new **types** and new **operations** to an existing system without modifying existing code?

```
                     ADD NEW TYPES          ADD NEW OPERATIONS
                     without touching       without touching
                     existing code?         existing code?

OOP (Java/C#):           [OK] (new class)          [NO] (modify interface/base)
FP (Haskell pattern):    [NO] (modify match)        [OK] (new function)
Typeclasses (Haskell):   [OK]                       [OK] (but requires care)
Traits (Rust):           [OK] (orphan rules)        [OK] (impl Trait for Type)
Open classes (Ruby):     [OK] (monkey-patch)        [OK] (monkey-patch)
```

This is why Haskell typeclasses, Rust traits, and Scala's typeclass pattern matter:
they solve the expression problem that class hierarchies cannot.
