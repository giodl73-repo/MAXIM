# Language: Java

> Write once, run anywhere — the JVM, garbage collection, and uniform object model that influenced C#, Kotlin, and Scala.

---

## Type System Snapshot

| Axis | Java |
|------|------|
| Binding | Late — all instance methods are virtual by default |
| Typing | Static |
| Strength | Strong — no implicit conversions between incompatible types |
| Type system | Nominal |
| Type inference | Partial — `var` (Java 10+), diamond `<>`, lambda type inference |
| Memory model | GC — G1GC default, ZGC/Shenandoah for low-latency |

---

## JVM Ecosystem Landscape

The JVM is the CLR's direct ancestor in concept — same idea, independent lineage. The pipeline maps cleanly.

```
SOURCE → COMPILER → BYTECODE → RUNTIME

  Java source (.java)
       │
       ▼
  ┌─────────┐
  │  javac  │
  └─────────┘
       │
       ▼
  .class files (JVM bytecode — stack-based instruction set, not native)
       │
       ▼
  ┌──────────────────────────────────────────────────────────┐
  │                      JVM Runtime                         │
  │                                                          │
  │  ┌──────────────┐    ┌──────────────┐    ┌───────────┐   │
  │  │ Class Loader │───▶│ JIT Compiler │───▶│  Native   │  │
  │  │              │    │  (HotSpot)   │    │   Code    │  │
  │  └──────────────┘    └──────────────┘    └───────────┘  │
  │         │                   │                            │
  │         ▼                   ▼                            │
  │  ┌──────────────┐    ┌──────────────┐                    │
  │  │  Bytecode    │    │  GC (G1GC /  │                    │
  │  │ Interpreter  │    │  ZGC / etc.) │                    │
  │  │  (warmup)    │    └──────────────┘                    │
  │  └──────────────┘                                        │
  └──────────────────────────────────────────────────────────┘

  JVM also hosts: Kotlin · Scala · Clojure · Groovy
  (all compile to the same .class bytecode format)
```

**CLR analogy — the parallel is direct:**

```
C#  pipeline:  .cs  →  csc   →  IL (MSIL)  →  CLR  →  native
Java pipeline: .java →  javac →  bytecode   →  JVM  →  native

  csc       ≈  javac          (ahead-of-time compiler to intermediate form)
  MSIL/IL   ≈  JVM bytecode   (portable stack-machine instructions)
  CLR       ≈  JVM            (runtime: class loader + JIT + GC + type system)
  RyuJIT    ≈  HotSpot JIT    (tiered JIT with profile-guided optimization)
  .NET GC   ≈  G1GC / ZGC     (generational garbage collectors)
  NuGet     ≈  Maven Central  (package repository)
  .csproj   ≈  pom.xml / build.gradle
```

Key JVM differences from CLR worth knowing:
- JVM JIT (HotSpot) uses **tiered compilation** — interpreted first, then C1 (fast compile), then C2 (optimizing). The JVM gets *faster as it runs* (warmup cost).
- **GC generations**: Young (Eden + Survivor) → Old Gen → (Metaspace for class metadata). G1GC uses region-based layout instead of contiguous generations.
- **No value types on the heap** until Project Valhalla (in progress). Every non-primitive is a heap-allocated object — contrast with C# structs.

---

## Syntax Reference Card

### Variables & Types
```java
int x = 5;                      // primitive (stack)
Integer x = 5;                  // boxed (heap) — autoboxing
final int MAX = 100;            // immutable
var x = 5;                      // type inferred (Java 10+)

// Primitives (no object overhead)
byte  short  int  long          // 1, 2, 4, 8 bytes
float  double                   // 4, 8 bytes
boolean  char                   // 1 bit (stored as int), 2 bytes (UTF-16)

// Boxed (nullable, work with generics)
Byte  Short  Integer  Long
Float  Double  Boolean  Character

// Records (Java 16+) — immutable data class
record Point(int x, int y) {}   // auto-generates equals, hashCode, toString, accessors
var p = new Point(1, 2);
p.x()   // accessor method (not field)
```

### Equality & Comparison
```java
// THE classic Java trap:
// == for primitives: value equality [OK]
// == for objects:    REFERENCE equality [NO] (almost never what you want)

String a = "hello";
String b = new String("hello");
a == b          // false (different objects) ← TRAP
a.equals(b)     // true (same content) [OK]

// Null-safe equality
Objects.equals(a, b)    // null-safe; returns false if either is null, true if both null

// Comparable
"a".compareTo("b")     // negative (a < b)
Integer.compare(1, 2)  // -1

// Records get equals() automatically
new Point(1,2).equals(new Point(1,2))   // true [OK]
```

### Logical Operators
```java
&&    // logical AND  (short-circuit)
||    // logical OR   (short-circuit)
!     // logical NOT
&     // bitwise AND  (also non-short-circuit boolean AND)
|     // bitwise OR   (also non-short-circuit boolean OR)
^     // bitwise XOR
~     // bitwise complement
<<    >>    >>>     // left shift, signed right shift, unsigned right shift
```

### Collections
```java
// Immutable (preferred for data passing)
List.of(1, 2, 3)
Map.of("k", 1, "k2", 2)    // up to 10 pairs
Set.of(1, 2, 3)
Map.copyOf(map)

// Mutable
new ArrayList<>(List.of(1, 2, 3))
new HashMap<>()
new HashSet<>()
new LinkedHashMap<>()       // insertion-ordered map
new TreeMap<>()             // sorted map

// Array (fixed size)
int[] a = {1, 2, 3};
int[] a = new int[5];       // zero-initialized
int[][] matrix = new int[3][3];

// No tuple — use records or Map.Entry<K,V> or custom
// Streams (Java 8+)
list.stream()
    .filter(x -> x > 0)
    .map(x -> x * 2)
    .collect(Collectors.toList())
```

### Control Flow
```java
if (cond) { } else if (cond2) { } else { }

// Ternary
int max = (a > b) ? a : b;

// Switch expression (Java 14+) — no fall-through, returns value
int result = switch (day) {
    case MONDAY, FRIDAY -> 8;
    case TUESDAY -> 9;
    default -> 5;
};

// Pattern matching in switch (Java 21+)
Object obj = ...;
switch (obj) {
    case Integer i -> System.out.println("int: " + i);
    case String s when s.length() > 5 -> System.out.println("long string");
    case null -> System.out.println("null");
    default -> System.out.println("other");
}

// Pattern matching instanceof (Java 16+)
if (obj instanceof String s && s.length() > 3) {
    s.toUpperCase()   // s is String in this scope
}

// Enhanced for
for (var item : list) { }
for (var entry : map.entrySet()) { entry.getKey(); entry.getValue(); }
```

### Strings & Characters
```java
// String — immutable, backed by char[] (UTF-16 internally)
String s = "hello";
String s2 = new String("hello");    // new object (avoid)
s.length()                          // number of chars (UTF-16 units, not code points!)
s.charAt(0)                         // char at index
s.substring(1, 3)                   // "el"
s.contains("ell")
s.replace("l", "L")
s.strip()                           // trim (Unicode-aware)
s.isBlank()                         // true if empty or whitespace
s.split(",")                        // String[]

// String.formatted (Java 15+)
"Hello, %s! Age: %d".formatted(name, age)

// Text blocks (Java 15+)
String json = """
    {
        "key": "value"
    }
    """;   // indentation stripped to minimum

// StringBuilder (mutable)
var sb = new StringBuilder();
sb.append("hello").append(" ").append("world");
sb.toString()

// char
char c = 'A';           // UTF-16 code unit
int code = (int) c;     // 65
```

### Null / Optional
```java
// null exists everywhere for reference types
String s = null;

// Optional<T> — explicit nullable return type (Java 8+)
Optional<String> opt = Optional.of("value");
Optional<String> empty = Optional.empty();
Optional<String> nullable = Optional.ofNullable(maybeNull);

opt.isPresent()             // true
opt.isEmpty()               // false
opt.get()                   // "value" — throws if empty!
opt.orElse("default")
opt.orElseGet(() -> compute())
opt.orElseThrow()
opt.map(String::toUpperCase)
opt.filter(s -> s.length() > 3)
opt.flatMap(s -> Optional.of(s + "!"))

// Note: Optional not recommended for fields — use nullable fields + annotation
// @Nullable @NonNull from libraries (JetBrains, Checker Framework)
```

### Functions
```java
// Methods (all instance methods are virtual by default)
int add(int a, int b) { return a + b; }
static int staticAdd(int a, int b) { return a + b; }
final int noOverride(int x) { return x; }    // sealed against override

// Lambdas (Java 8+)
Function<Integer, Integer> double_ = x -> x * 2;
BiFunction<Integer, Integer, Integer> add = (a, b) -> a + b;
Predicate<String> nonEmpty = s -> !s.isEmpty();
Consumer<String> print = System.out::println;
Supplier<String> supply = () -> "value";

// Method references
list.forEach(System.out::println)
list.stream().map(String::toUpperCase)

// Generics
<T> T identity(T x) { return x; }
<T extends Comparable<T>> T max(T a, T b) { return a.compareTo(b) > 0 ? a : b; }

// Functional interfaces (implement with lambdas)
@FunctionalInterface
interface Transformer<T, R> { R transform(T input); }
```

### Error Handling
```java
// Checked exceptions — MUST be declared or caught
void readFile(String path) throws IOException {
    // compiler forces caller to handle
}

// Unchecked (RuntimeException) — optional to catch
void risky() {
    throw new IllegalStateException("bad state");
}

// Multi-catch
try {
    // ...
} catch (IOException | SQLException e) {
    log(e.getMessage());
} finally {
    // always runs
}

// Try-with-resources (auto-close, like C# using)
try (var stream = new FileInputStream("file")) {
    // stream.close() called automatically
}
```

---

## What Makes It Distinct

1. **All instance methods are virtual** — default in Java; you must use `final` to prevent override. C# is the opposite. This affects performance and design.
2. **Primitive vs boxed duality** — `int` (fast, can't be null, no generics) vs `Integer` (object, nullable, works with `List<Integer>`). Autoboxing bridges them but causes subtle bugs and boxing overhead.
3. **Checked exceptions** — Java forces you to declare or handle `IOException`, `SQLException`, etc. Controversial design; Kotlin, C#, and Scala all abandoned it.
4. **JVM ecosystem** — runs alongside Kotlin, Scala, Clojure on the same VM. Massive library ecosystem. JVM JIT is mature and excellent.
5. **Verbose generics** — `List<? extends Comparable<? super T>>` — wildcard type bounds are famously unreadable. TypeScript and Scala handle this better.

---

## Bridge from C#: Virtual-by-Default vs Non-Virtual-by-Default

This is the single highest-impact behavioral difference between Java and C#. Every Java instance method is virtual unless explicitly sealed. Every C# instance method is non-virtual unless explicitly opened.

```
METHOD DISPATCH — THE DEFAULT FLIP

  Java (virtual by default):          C# (non-virtual by default):
  ┌─────────────────────────┐         ┌─────────────────────────┐
  │ class Animal {          │         │ class Animal {          │
  │   void speak() { ... }  │         │   void Speak() { ... }  │
  │ }                       │         │ }                       │
  │                         │         │                         │
  │ class Dog extends Animal│         │ class Dog : Animal {    │
  │   void speak() { ... }  │         │   void Speak() { ... }  │
  │ }                       │         │ }                       │
  └─────────────────────────┘         └─────────────────────────┘

  Animal a = new Dog();               Animal a = new Dog();
  a.speak()  →  Dog.speak()  [OK]       a.Speak()  →  Animal.Speak() [!]
  (virtual dispatch works)            (non-virtual — Dog hides, not overrides)
```

**Keyword mapping:**

| Intent | Java | C# |
|--------|------|----|
| Override a method | `@Override void speak()` | `override void Speak()` |
| Prevent override | `final void speak()` | `sealed override void Speak()` (or just no `virtual`) |
| Allow override in C# | *(default)* | `virtual void Speak()` |
| Prevent subclassing | `final class Dog` | `sealed class Dog` |

**The `@Override` annotation in Java:**
- It is *optional* but strongly recommended — the compiler will catch if you're not actually overriding anything (typo, wrong signature).
- In C#, `override` is *mandatory* — the compiler enforces it.

**When this matters:**

```java
// Java — unexpected polymorphism
class Base {
    void process() { log("Base"); }       // virtual — always was
}
class Derived extends Base {
    void process() { log("Derived"); }    // overrides silently (no keyword needed)
}

Base b = new Derived();
b.process();   // prints "Derived" — virtual dispatch
```

```csharp
// C# — no polymorphism without explicit opt-in
class Base {
    void Process() { Log("Base"); }       // non-virtual
}
class Derived : Base {
    new void Process() { Log("Derived"); } // 'new' = hide, not override
}

Base b = new Derived();
b.Process();   // prints "Base" — no dispatch through reference type
```

**Practical consequence:** Writing Java-style subclasses in C# will silently fail to dispatch correctly unless you add `virtual`/`override`. Writing C#-style classes in Java will dispatch to the subclass even when you didn't intend to open the method for override — add `final` to lock it down.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| javac / OpenJDK | Compiler and runtime |
| Maven / Gradle | Build and dependency management |
| Spring Boot | Web framework (dominant) |
| Hibernate / JPA | ORM |
| JUnit 5 / Mockito | Testing |
| IntelliJ IDEA | Primary IDE |
| GraalVM | Native compilation (AOT) |

---

## Gotchas from C#

| C# behavior | Java behavior | Note |
|-------------|-------------|-------|
| `==` on strings is value equality | `==` on strings is reference equality | Use `.equals()` always |
| Properties: `obj.Name` | No properties: `obj.getName()` | Records have `obj.name()` though |
| Non-virtual by default | Virtual by default | Sealed classes / `final` |
| No checked exceptions | Checked exceptions (`throws`) | Verbose or work around with unchecked |
| `int?` = `Nullable<int>` | No nullable primitives — use `Integer` | Boxing overhead |
| `using` = scoped dispose | `try-with-resources` | Different syntax, same concept |
| `var` since C# 3 | `var` since Java 10 | Both are local type inference |

---

## When to Choose Java

- Enterprise applications (Spring ecosystem)
- Android development (though Kotlin is preferred)
- Large teams with Java expertise
- When you need the full JVM ecosystem and don't want to adopt Kotlin/Scala
- Interop with existing Java codebases

---

## Decision Cheat Sheet

| Decision | Use X when... |
|----------|---------------|
| **`ArrayList` vs `LinkedList`** | `ArrayList` almost always — O(1) random access, CPU-cache-friendly. `LinkedList` only when you need O(1) insert/delete at arbitrary positions with an iterator in hand (rare in practice). |
| **`ArrayList` vs `array`** | Array when size is fixed and you need raw performance or primitive storage (`int[]`). `ArrayList` when you need dynamic sizing or collection API. |
| **`HashMap` vs `LinkedHashMap`** | `LinkedHashMap` when insertion order matters (predictable iteration, LRU cache with `removeEldestEntry`). `HashMap` otherwise — faster. |
| **`HashMap` vs `TreeMap`** | `TreeMap` when you need keys in sorted order or range queries (`headMap`, `tailMap`, `subMap`). `HashMap` otherwise — O(1) vs O(log n). |
| **Checked vs unchecked exception** | Checked (`extends Exception`) when the caller can reasonably recover and you want the compiler to enforce handling — e.g., `IOException`, `SQLException`. Unchecked (`extends RuntimeException`) for programming errors or unrecoverable conditions. When in doubt: unchecked. Checked exceptions are controversial; Kotlin, C#, Scala all dropped them. |
| **`interface` vs `abstract class`** | `interface` for defining a contract a class can implement alongside others (multiple interface implementation allowed). `abstract class` when you need shared state (fields) or non-public members. Java 8+ `default` methods blurred the line — interfaces can now have implementations, so the gap is smaller. Still: a class can only extend one abstract class. |
| **`Stream` vs `Collection`** | `Stream` for lazy pipeline processing — chaining `filter/map/reduce` without materializing intermediates. `Collection` when you need to iterate multiple times, random access, or mutate. Streams are single-use and lazy; collections are reusable and eager. |
| **`Optional<T>` vs null** | `Optional<T>` for method return types where absence is a legitimate outcome and you want to force callers to handle it. Do NOT use `Optional` for fields, parameters, or collection elements — it adds boxing overhead and API noise without benefit. Null + `@Nullable` annotation is fine for internal fields. |
| **Java vs Kotlin (new JVM project)** | Kotlin for greenfield Android, new Spring Boot services, or when your team is comfortable — better null safety, less boilerplate, coroutines. Java when you need maximum library compatibility, Java-only tooling, or a larger hiring pool. |
| **`record` vs `class`** | `record` for pure immutable data carriers (DTOs, value objects, response types). `class` when you need mutability, inheritance, or non-trivial construction logic. |
