# Language: Scala

> FP + OOP fusion on the JVM — algebraic types, higher-kinded types, implicits/givens, and a rich type system. The language where Haskell-style FP meets industrial Java interop.

---

## Type System Snapshot

| Axis | Scala |
|------|-------|
| Binding | Late (virtual default, JVM) |
| Typing | Static |
| Strength | Strong |
| Type system | Nominal + some structural (structural typing exists) |
| Type inference | Partial — strong local inference; complex types need annotation |
| Memory model | GC (JVM) |

---

## Type Hierarchy and Implicits/Givens

Two things about Scala that bite everyone without a diagram: the unified type hierarchy (Nothing is the bottom type — not an exception, not a special case) and the implicit/given resolution order (the compiler is doing a structured search at each call site).

```
┌─────────────────────────────────────────────────────────────────────────┐
│                         SCALA TYPE HIERARCHY                            │
│                                                                         │
│                              Any                                        │
│                             /    \                                      │
│                        AnyVal   AnyRef  (≈ java.lang.Object)            │
│                       /  | | \     |  \  \  \                           │
│                    Int Double  \  String List  custom classes           │
│                   Boolean Char  \                                       │
│                   Long Float  Unit  (≈ void — the one-value type)       │
│                                 |                                       │
│                               Null  (subtype of all AnyRef only)        │
│                                 |    null literal has this type         │
│                                 |                                       │
│                             Nothing  (BOTTOM — subtype of everything)   │
│                                                                         │
│  Nothing enables:                                                       │
│    throw new Exception("msg")  :: Nothing  — fits anywhere              │
│    ???                         :: Nothing  — unimplemented stub         │
│    def loop: Nothing = loop    — diverging computation                  │
│                                                                         │
│  Why this matters: List[Nothing] <: List[Int] (if List is covariant)    │
│  Nil (the empty list) has type List[Nothing] — it fits any List[T]      │
└─────────────────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────────────────┐
│                    IMPLICIT / GIVEN RESOLUTION ORDER                    │
│                                                                         │
│  Call site: def sort[T](list: List[T])(using ord: Ordering[T])          │
│  You write: sort(points)   — compiler must find Ordering[Point]         │
│                                                                         │
│  Search order (first match wins):                                       │
│                                                                         │
│  1. Local scope                                                         │
│     given myOrd: Ordering[Point] = ...  // in current block/method      │
│         ↓ not found                                                     │
│  2. Imported scope                                                      │
│     import MyOrderings.given            // explicit import              │
│         ↓ not found                                                     │
│  3. Companion object of the type argument (Point)                       │
│     object Point { given Ordering[Point] = ... }  // idiomatic home     │
│         ↓ not found                                                     │
│  4. Companion object of the typeclass (Ordering)                        │
│     object Ordering { given Ordering[Int] = ... } // stdlib instances   │
│         ↓ not found → COMPILE ERROR                                     │
│                                                                         │
│  Scala 2 syntax:  implicit val myOrd: Ordering[Point] = ...             │
│  Scala 3 syntax:  given Ordering[Point] with { def compare(...) }       │
│                                                                         │
│  Derived instances: compiler can synthesize Ordering[List[T]]           │
│  from Ordering[T] via implicit/given functions — this is how            │
│  scalaz/cats/magnolia generate instances for case classes.              │
└─────────────────────────────────────────────────────────────────────────┘
```

---

## Syntax Reference Card

### Variables & Types
```scala
val x = 5           // immutable (prefer this)
var x = 5           // mutable
val x: Int = 5      // explicit type

// Numeric types
Byte  Short  Int  Long
Float  Double
Boolean
Char        // UTF-16 code unit
String      // java.lang.String

// Unit — the void equivalent
def f(): Unit = println("hello")

// Any, AnyVal, AnyRef
Any         // root of type hierarchy (≈ object in C#)
AnyVal      // value types (Int, Boolean, etc.)
AnyRef      // reference types (≈ java.lang.Object)
Nothing     // bottom type — subtype of everything (unreachable code, throw)
Null        // type of null literal (subtype of AnyRef)

// Case classes (like C# records — immutable data classes)
case class Point(x: Int, y: Int)
val p = Point(1, 2)
val p2 = p.copy(x = 10)     // non-destructive update
p.x  p.y                     // field access (methods, not fields)

// Point(1,2) == Point(1,2)  // true (case class provides equals/hashCode)
```

### Equality & Comparison
```scala
// == calls .equals() — structural, null-safe
Point(1,2) == Point(1,2)    // true
"hello" == "hello"          // true (unlike Java!)
1 == 1.0                    // true (numeric widening)

// eq — reference equality (like Object.ReferenceEquals)
val a = new Object()
val b = a
a eq b                      // true
a eq new Object()           // false

// ne — reference inequality
// != — structural inequality (calls .equals())

// Null-safe == (null == null is true)
null == null                // true
"hello" == null             // false (no NPE)

// Ordering / Comparable
"abc" < "abd"               // true (uses Ordered)
implicitly[Ordering[Int]].compare(1, 2)  // -1
```

### Logical Operators
```scala
&&    // short-circuit AND
||    // short-circuit OR
!     // NOT

&     |     ^     // bitwise (also non-short-circuit boolean)
~                 // bitwise NOT
<<    >>    >>>   // shifts
```

### Collections
```scala
// Scala collections are immutable by default
import scala.collection.mutable  // for mutable

// List — immutable linked list
val lst = List(1, 2, 3)
val lst = 1 :: 2 :: 3 :: Nil   // cons cells
lst.head    // 1
lst.tail    // List(2,3)
lst.isEmpty
1 +: lst    // prepend (returns new List)
lst :+ 4    // append (returns new List, O(n))
List(1,2) ++ List(3,4)          // concat

// Vector — immutable indexed (preferred over List for large)
val v = Vector(1, 2, 3)         // O(log n) access
v(0)                            // index access (! uses parens not brackets)
v.updated(0, 99)                // new Vector with element changed

// Map — immutable
val m = Map("a" -> 1, "b" -> 2)
m("a")                          // 1 — throws if missing
m.get("a")                      // Some(1)
m + ("c" -> 3)                  // new Map
m - "a"                         // new Map without "a"
m.updated("a", 99)

// Set — immutable
val s = Set(1, 2, 3)
s + 4   s - 2   s & other   s | other

// Array — mutable (backed by JVM array)
val a = Array(1, 2, 3)
a(0) = 99                      // SUBSCRIPT USES () NOT []!!!
a(0)                           // access

// Range
1 to 10              // Range inclusive
1 until 10           // Range exclusive
1 to 10 by 2         // [1,3,5,7,9]

// Tuple
val t = (1, "hello", true)      // (Int, String, Boolean)
t._1  t._2  t._3               // access (1-indexed!)
val (a, b, c) = t               // destructure

// Collection operations
lst.map(_ * 2)
lst.filter(_ > 1)
lst.foldLeft(0)(_ + _)          // fold left
lst.foldRight(0)(_ + _)         // fold right
lst.reduce(_ + _)
lst.flatMap(x => List(x, x*2))
lst.zip(other)
lst.zipWithIndex
lst.groupBy(_ % 2)
lst.sortBy(-_)                  // descending
lst.take(3)  lst.drop(3)
lst.distinct                    // unique elements

// For comprehension (like C# LINQ / Haskell do)
val result = for {
    x <- 1 to 5
    if x % 2 == 0
    y = x * x
} yield y   // Vector(4, 16)

// Works on any monad!
val opt: Option[Int] = for {
    a <- Some(5)
    b <- Some(3)
} yield a + b   // Some(8)
```

### Bridge: C# LINQ / F# Computation Expressions → Scala `for`

You already own this mental model. The three syntaxes are isomorphic — they all desugar to `flatMap` / `map` / `filter` chains.

```
C# LINQ query syntax:
  from x in list
  where x > 0
  select x * 2
  ≡  list.Where(x => x > 0).Select(x => x * 2)

F# computation expression (option builder):
  option {
      let! x = Some 5
      let! y = Some 3
      return x + y
  }
  ≡  Some 5 |> Option.bind (fun x ->
     Some 3 |> Option.map  (fun y -> x + y))

Scala for comprehension:
  for {
      x <- Some(5)
      y <- Some(3)
      if x > 0
  } yield x + y
  ≡  Some(5).flatMap(x =>
     Some(3).withFilter(_ => x > 0).map(y =>
     x + y))
```

The desugar rules (Scala):

| `for` syntax | Desugars to |
|---|---|
| `x <- expr` | `expr.flatMap(x => ...)` (last generator uses `map`) |
| `if guard` | `expr.withFilter(x => guard)` |
| `y = expr` | val binding — no method call, just a `let` |
| `yield result` | the final `map`'s body |

**The key insight**: Scala's `for` is not a loop construct — it is the syntactic surface of any monad. Swap `Option` for `Either`, `List`, `Future`, or a custom type and the same syntax works as long as that type has `flatMap` and `map`. This is exactly the Haskell `do`-notation generalization, and it is exactly what F# computation expressions do with a custom builder.

```scala
// All three of these use the same for-comprehension syntax:

// Option — short-circuit on None
for { user <- findUser(id); addr <- user.address } yield addr.city

// Either — short-circuit on Left, carry typed error
for { x <- parseAge(s); y <- validate(x) } yield y * 2

// List — cartesian product (non-determinism)
for { x <- List(1,2); y <- List("a","b") } yield (x, y)
// → List((1,"a"), (1,"b"), (2,"a"), (2,"b"))

// Future — async sequencing (runs sequentially, not in parallel!)
for { user <- fetchUser(id); order <- fetchOrder(user) } yield order
```

---

### Control Flow
```scala
// If — expression in Scala
val result = if (x > 0) "positive" else "non-positive"

if (cond) {
} else if (cond2) {
} else {
}

// Match (exhaustive pattern matching — the star feature)
x match {
    case 0 => "zero"
    case 1 | 2 => "one or two"
    case n if n < 0 => s"negative: $n"
    case _ => "other"
}

// Algebraic data type matching
shape match {
    case Circle(r) => math.Pi * r * r
    case Rectangle(w, h) => w * h
}

// Type matching
x match {
    case s: String => s.length
    case n: Int => n
    case _ => 0
}

// For loops (imperative — use for comprehension for functional)
for (i <- 1 to 10) println(i)
for (item <- list) println(item)
for ((k, v) <- map) println(s"$k -> $v")

while (cond) { }
```

### Algebraic Data Types (Scala 3 / Scala 2 enum)
```scala
// Scala 2 — sealed trait hierarchy (the ADT pattern)
sealed trait Shape
case class Circle(radius: Double) extends Shape
case class Rectangle(w: Double, h: Double) extends Shape
case object Point extends Shape

// Scala 3 — enum (cleaner)
enum Shape:
    case Circle(radius: Double)
    case Rectangle(w: Double, h: Double)
    case Point

// Pattern matching is exhaustive on sealed types
def area(s: Shape): Double = s match
    case Shape.Circle(r) => math.Pi * r * r
    case Shape.Rectangle(w, h) => w * h
    case Shape.Point => 0.0
```

### Strings & Characters
```scala
// String — java.lang.String (immutable)
val s = "hello"
val s = s"Hello, $name! ${age + 1} years old"   // string interpolation (s prefix)
val s = f"Pi is $pi%.2f"                          // formatted (f prefix)
val s = raw"no \n escape"                          // raw (raw prefix)
val s = """multi
line"""
val s = """multi
          line""".stripMargin    // strips leading whitespace to | marker

// String operations (Java methods available)
s.length  s.size
s.toUpperCase  s.toLowerCase
s.trim
s.contains("sub")
s.startsWith("prefix")
s.split(",")                    // Array[String]
s.replace("old", "new")

// Char — UTF-16 code unit
val c = 'A'                     // Char literal
c.toInt                         // 65
c.isLetter  c.isDigit  c.isUpper
```

### Null / Option
```scala
// Option[T] — the right way (avoid null)
val x: Option[Int] = Some(42)
val y: Option[Int] = None

// Pattern matching
x match {
    case Some(v) => use(v)
    case None => handleMissing()
}

// map / flatMap / filter
x.map(_ * 2)                    // Some(84) or None
x.filter(_ > 0)
x.flatMap(findUser)             // avoid Option[Option[T]]
x.getOrElse(0)
x.orElse(Some(99))
x.isDefined  x.isEmpty
x.toList                        // List(42) or Nil
x.foreach(println)              // side effect if Some

// For comprehension on Option
val result: Option[Int] = for {
    a <- Some(5)
    b <- Some(3)
    if a > 0
} yield a + b   // Some(8)

// null exists but avoid it
// In interop with Java: Option.apply(javaMethod()) converts null to None
Option(javaMethod())            // Some(v) or None
```

### Functions & Implicits
```scala
// Function definition
def add(a: Int, b: Int): Int = a + b
def add(a: Int, b: Int): Int = {
    a + b
}

// Curried function (manual)
def add(a: Int)(b: Int): Int = a + b
val add3 = add(3) _   // partial application — requires trailing _

// Function literals
val double = (x: Int) => x * 2
val add = (a: Int, b: Int) => a + b

// Higher-order functions
def applyTwice(f: Int => Int, x: Int): Int = f(f(x))
applyTwice(_ + 1, 5)    // 7 (using placeholder syntax)

// Composition
val double: Int => Int = _ * 2
val addOne: Int => Int = _ + 1
val doubleThenAdd = double andThen addOne   // left-to-right
val addThenDouble = double compose addOne   // right-to-left

// Generics
def identity[T](x: T): T = x
def max[T: Ordering](a: T, b: T): T =
    if (implicitly[Ordering[T]].gt(a, b)) a else b

// Implicits (Scala 2) / Givens (Scala 3)
// This is Scala's typeclass mechanism
given Ordering[Point] with
    def compare(a: Point, b: Point): Int = a.x.compare(b.x)

// Extension methods (Scala 3)
extension (s: String)
    def shout: String = s.toUpperCase + "!"

"hello".shout   // "HELLO!"

// Context functions (Scala 3)
def withDB[T](f: Database ?=> T): T = f(using openDB())
```

### Error Handling
```scala
// Try[T] — Success or Failure
import scala.util.{Try, Success, Failure}
val result = Try(riskyOperation())
result match {
    case Success(v) => use(v)
    case Failure(e) => log(e)
}
result.getOrElse(defaultValue)
result.map(v => v * 2)
result.recover { case _: IOException => 0 }

// Either[E, A] — Left = error, Right = success
def divide(a: Int, b: Int): Either[String, Int] =
    if (b == 0) Left("division by zero")
    else Right(a / b)

divide(10, 2) match {
    case Right(v) => println(v)
    case Left(e) => println(s"Error: $e")
}

// For comprehension on Either
val result: Either[String, Int] = for {
    x <- divide(10, 2)
    y <- divide(x, 3)
} yield x + y

// Exceptions (Java-compatible)
try {
    riskyOperation()
} catch {
    case e: IOException => handle(e)
    case e: Exception => throw new RuntimeException("wrapped", e)
} finally {
    cleanup()
}
```

---

## What Makes It Distinct

1. **The JVM's most expressive type system** — higher-kinded types (`F[_]`), type bounds, structural types, singleton types, dependent types (path-dependent). Enables libraries like Cats and ZIO.
2. **Implicits / Givens** — Scala's typeclass mechanism. Define instances of type classes as given values; compiler finds them automatically. Powers serialization (circe), validation, error handling (ZIO).
3. **For comprehension** — works on ANY monad. `for { x <- m; y <- n } yield f(x,y)` is desugared to `m.flatMap(x => n.map(y => f(x,y)))`. Works on `Option`, `Either`, `Try`, `Future`, `List`, custom types.
4. **`object` keyword** — companion objects (like C# static classes attached to a type), singleton modules, and case object for ADT variants without data.
5. **`()` for subscript** — `array(0)` not `array[0]`. `[T]` is for type parameters only. Deeply confusing for C# developers.

---

## Scala 2 vs Scala 3 Key Differences

| Feature | Scala 2 | Scala 3 |
|---------|---------|---------|
| Typeclass instance | `implicit val` | `given` |
| Use typeclass | `implicit` parameter | `using` parameter |
| Extension methods | `implicit class` | `extension (x: T)` |
| ADT | `sealed trait` + case classes | `enum` |
| Indentation | Braces required | Significant indentation (optional) |

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| sbt / Mill / Gradle | Build systems |
| scalafmt | Formatter |
| Cats / Scalaz | Functional programming |
| ZIO | Effect system (like Haskell IO + concurrency) |
| Akka / Pekko | Actor model |
| Spark | Big data (Scala is dominant) |
| http4s / Play | HTTP servers |
| circe | JSON |

---

## Gotchas from C#

| C# behavior | Scala behavior | Consequence |
|-------------|---------------|-------------|
| `array[0]` | `array(0)` — parens! | Very easy to confuse |
| `==` on strings is value | Same — `==` is value | Fine |
| `null` exists (C# 8+ optional) | `null` exists but Option is idiomatic | Need discipline |
| `interface` + `class` | `trait` + `class` (multiple trait mixin) | More flexible but complex |
| `delegate` / `Func<T,R>` | `Int => Int` (function type literal) | Cleaner syntax |
| `List<T>` is mutable | `List(...)` is immutable | Import mutable explicitly |
| `T._` accessed via `.field` | `case class` fields via `.field` | Same, but fields are methods |

---

## Decision Cheat Sheet

| Decision | Use X | When Y |
|----------|-------|--------|
| `List` vs `Vector` | `List` | Prepend-heavy workloads; pattern matching with `head :: tail`; short lists |
| `List` vs `Vector` | `Vector` | Random access; large collections; append or update operations (O(log n) vs O(n)) |
| `Option` vs `Try` vs `Either` | `Option` | Value might be absent and the reason is irrelevant — `Map.get`, optional config |
| `Option` vs `Try` vs `Either` | `Try` | Wrapping a Java API that throws exceptions; you want Success/Failure as values |
| `Option` vs `Try` vs `Either` | `Either[E, A]` | Typed, domain-specific errors that callers must handle — validation, parsing, business rules |
| Scala 2 `implicit` vs Scala 3 `given`/`using` | `implicit` | You're on Scala 2 or maintaining a Scala 2 codebase; no choice |
| Scala 2 `implicit` vs Scala 3 `given`/`using` | `given`/`using` | Scala 3 — cleaner, explicit, better tooling support; use for all new code |
| `sealed trait` + case classes vs Scala 3 `enum` | `sealed trait` | Scala 2 compatibility required; variants carry complex logic or multiple type parameters |
| `sealed trait` + case classes vs Scala 3 `enum` | Scala 3 `enum` | Scala 3 only; cleaner syntax; variants are simple data; compiler enforces exhaustiveness equally |
| `Future` vs ZIO `Task` | `Future` | Simple async in a small service; existing Akka/Play codebase; no need for resource management |
| `Future` vs ZIO `Task` | ZIO `Task` | Complex effectful programs; dependency injection via ZEnvironment; structured concurrency; retry/timeout as first-class concerns |
| `for` comprehension vs `flatMap` chains | `for` comprehension | Three or more monadic steps; intermediate values need names; readability matters |
| `for` comprehension vs `flatMap` chains | `flatMap`/`map` chains | One or two steps; composing in a pipeline; point-free style preferred |
