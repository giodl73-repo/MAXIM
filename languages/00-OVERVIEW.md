# Programming Languages — Taxonomy & Theory Map

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

---

## Type System — 6 Axes

### Axis 1: When Are Types Checked?

```
STATIC (compile time)              GRADUAL                DYNAMIC (runtime)
────────────────────────────────────────────────────────────────────────────
C, C++, Java, C#, Rust,           TypeScript             Python, JavaScript,
Go, Haskell, F#, Kotlin,          (any = escape hatch)   Ruby
Swift, Scala

Implication: static = errors at compile time; dynamic = errors at runtime
```

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
C++ VIRTUAL DISPATCH          JAVA/C# INTERFACE DISPATCH
──────────────────────────    ──────────────────────────
object ptr                    object ref
    │                             │
    ▼                             ▼
┌─────────┐                  ┌─────────┐
│ vptr    │──► vtable[]      │ typeptr │──► method table
│ field1  │     [0] dtor          │
│ field2  │     [1] speak()  ┌────────────────┐
└─────────┘     [2] move()   │ interface slot │──► concrete method
                             └────────────────┘

Cost: 1 pointer load + 1 indirect call + possible branch misprediction
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
| C        | ✅ | ❌ weak | ✅ | ❌ none | manual | early |
| C++      | ✅ | ❌ weak | ✅ | partial (auto) | RAII/manual | early + vtable |
| Java     | ✅ | ✅ | ✅ | partial (var) | GC | late (virtual default) |
| C#       | ✅ | ✅ | ✅ | partial (var) | GC | early (non-virtual default) |
| Python   | ❌ | ✅ | duck | ❌ none | RC+GC | late (always) |
| JS       | ❌ | ❌ weak | duck | ❌ none | GC | late (always) |
| TS       | gradual | ❌ | structural | partial | GC | late (always) |
| Rust     | ✅ | ✅ | ✅ | partial/local | ownership | early (+ dyn for late) |
| Go       | ✅ | ✅ | structural (iface) | partial (:=) | GC | late (via interface) |
| Haskell  | ✅ | ✅ | ✅ | full HM | GC | early (+ class dispatch) |
| F#       | ✅ | ✅ | ✅ | full HM | GC | early |
| Kotlin   | ✅ | ✅ | ✅ | partial | GC | late (virtual default) |
| Swift    | ✅ | ✅ | ✅ | partial | ARC | early + protocol dispatch |
| Scala    | ✅ | ✅ | ✅ | partial | GC | late (virtual default) |
| Ruby     | ❌ | ✅ | duck | ❌ none | GC | late (always) |
| SQL      | varies | ✅ | N/A | N/A | server | N/A |

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
const foo: IFoo = dog;  // ✅ — compatible
const bar: IBar = dog;  // ✅ — compatible — TypeScript doesn't care about name
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

OOP (Java/C#):           ✅ (new class)          ❌ (modify interface/base)
FP (Haskell pattern):    ❌ (modify match)        ✅ (new function)
Typeclasses (Haskell):   ✅                       ✅ (but requires care)
Traits (Rust):           ✅ (orphan rules)        ✅ (impl Trait for Type)
Open classes (Ruby):     ✅ (monkey-patch)        ✅ (monkey-patch)
```

This is why Haskell typeclasses, Rust traits, and Scala's typeclass pattern matter:
they solve the expression problem that class hierarchies cannot.
