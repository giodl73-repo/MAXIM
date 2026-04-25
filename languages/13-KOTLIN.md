# Language: Kotlin

> Modern JVM language — null safety baked in, coroutines for async, extension functions, and data classes. The C# of the Java world; dominant on Android.

---

## Type System Snapshot

| Axis | Kotlin |
|------|--------|
| Binding | Late — virtual by default (like Java) |
| Typing | Static |
| Strength | Strong |
| Type system | Nominal |
| Type inference | Partial — strong local inference |
| Memory model | GC (JVM — G1, ZGC, etc.) |

---

## Kotlin Ecosystem Landscape

Kotlin is not a new runtime — it compiles to the same JVM bytecode as Java. The value is entirely in what the compiler adds *before* that bytecode lands on the JVM.

```
KOTLIN SOURCE → COMPILER MAGIC → JVM BYTECODE → SAME RUNTIME AS JAVA

  Kotlin source (.kt)
       │
       ▼
  ┌─────────────────────────────────────────────────────────┐
  │               Kotlin Compiler (kotlinc)                 │
  │                                                         │
  │  Null safety checks ──────────────────┐                 │
  │  (T vs T? enforced at compile time)   │                 │
  │                                       ▼                 │
  │  data class codegen ──────────► .class files            │
  │  (equals/hashCode/toString/copy)      │  (standard JVM  │
  │                                       │   bytecode)     │
  │  Coroutine transformation ────────────┘                 │
  │  (suspend fun → state machine)                          │
  └─────────────────────────────────────────────────────────┘
       │
       ▼
  .class files (identical format to javac output)
       │
       ▼
  ┌───────────────────────────────────┐
  │           JVM Runtime             │  ← same JVM as Java
  │  Class Loader → JIT → GC → Exec  │
  └───────────────────────────────────┘

  Kotlin also compiles to: Kotlin/JS (browser) · Kotlin/Native (LLVM, no JVM)
  Kotlin Multiplatform (KMP): share business logic across JVM / iOS / Web
```

**What the Kotlin compiler generates that Java doesn't:**

```
  Kotlin feature          Compiler output (JVM bytecode level)
  ──────────────────────────────────────────────────────────
  String? (nullable)   →  null checks inserted at call sites
                          @Nullable annotation on method sig
  data class           →  equals() + hashCode() + toString()
                          copy() + componentN() methods
  extension fun        →  static method, receiver as first param
                          (zero runtime cost — pure syntax)
  object (singleton)   →  class with static INSTANCE field
  sealed class         →  abstract class + exhaustiveness info
  suspend fun          →  state machine class (CPS transform)
                          each suspension point = a resume case
```

**Coroutine state machine — the key mental model:**

```
  suspend fun fetchAndProcess(): String {
      val data = fetchData()    // suspend point 1
      val result = process(data) // suspend point 2
      return result
  }

  Compiler transforms to:
  ┌──────────────────────────────────────────────────┐
  │  State machine with label (continuation)         │
  │                                                  │
  │  label=0 → call fetchData(), suspend, save state │
  │  label=1 → resume, call process(), suspend       │
  │  label=2 → resume, return result                 │
  │                                                  │
  │  No OS thread blocked — just a heap object       │
  │  Resumed by the coroutine dispatcher when ready  │
  └──────────────────────────────────────────────────┘

  C# async/await does the same CPS transform.
  Kotlin coroutines generalize it further — composable,
  structured, cancellable, with explicit dispatcher control.
```

---

## Syntax Reference Card

### Variables & Types
```kotlin
val x = 5           // immutable (like C# readonly local) — inferred Int
var x = 5           // mutable — inferred Int
val x: Int = 5      // explicit type

// Kotlin types (NOT Java primitives — Kotlin compiles to JVM primitives where possible)
Byte    Short    Int    Long
Float   Double
Boolean
Char            // UTF-16 code unit (2 bytes)
String

// Nullability is in the type!
val s: String = "hello"    // non-null (compiler enforces)
val s: String? = null      // nullable (? suffix)
val s: String? = "hello"   // nullable but has value

// Number literals
1_000_000       // underscores for readability
1L              // Long
1.0f            // Float
0xFF            // hex

// Destructuring declarations
val (a, b) = Pair(1, 2)
val (x, y, z) = Triple(1, 2, 3)
for ((key, value) in map) { }

// const (compile-time — must be at top level or companion object)
const val MAX = 100

// Data classes (like C# record) — free equals/hashCode/toString/copy
data class Point(val x: Int, val y: Int)
val p2 = p.copy(x = 10)   // non-destructive update
```

### Equality & Comparison
```kotlin
// == is structural equality (calls .equals(), null-safe)
"hello" == "hello"          // true (value equality)
val a = Point(1,2); val b = Point(1,2)
a == b                      // true (data class provides equals)

// === is reference equality
val a = "hello"; val b = StringBuilder("hello").toString()
a === b                     // false (different objects)
a == b                      // true (same content)

// != structural inequality
// !== reference inequality

// Null-safe comparison
null == null                // true
a == null                   // false

// Comparable
"a".compareTo("b")          // negative
// Comparison operators work with Comparable interface
```

### Logical Operators
```kotlin
&&      // short-circuit AND
||      // short-circuit OR
!       // NOT

// Bitwise — named functions (not operators)
a and b     // bitwise AND
a or b      // bitwise OR
a xor b     // bitwise XOR
a.inv()     // bitwise NOT
a shl 2     // left shift
a shr 2     // arithmetic right shift
a ushr 2    // unsigned right shift
```

### Collections
```kotlin
// Immutable (read-only view — NOT deeply immutable!)
val list = listOf(1, 2, 3)          // List<Int>
val map = mapOf("k" to 1)           // Map<String, Int>
val set = setOf(1, 2, 3)            // Set<Int>
val pair = 1 to "one"               // Pair<Int, String>

// Mutable
val list = mutableListOf(1, 2, 3)   // MutableList<Int>
val map = mutableMapOf("k" to 1)    // MutableMap<String, Int>
val set = mutableSetOf(1, 2, 3)     // MutableSet<Int>
list.add(4)
list[0] = 10
map["new"] = 5

// Array
val arr = arrayOf(1, 2, 3)          // Array<Int> (boxed)
val arr = intArrayOf(1, 2, 3)       // IntArray (primitive)
arr[0]  arr.size

// Ranges
1..10                // IntRange (inclusive)
1 until 10           // IntRange (exclusive end)
10 downTo 1          // downward
1..10 step 2         // [1,3,5,7,9]
'a'..'z'             // CharRange

// Collection operations (extension functions)
list.map { it * 2 }
list.filter { it > 2 }
list.reduce { acc, x -> acc + x }
list.fold(0) { acc, x -> acc + x }
list.any { it > 5 }
list.all { it > 0 }
list.none { it < 0 }
list.first { it > 2 }
list.firstOrNull { it > 100 }
list.groupBy { it % 2 }
list.sortedBy { it }
list.sortedByDescending { it }
list.flatMap { listOf(it, it * 2) }
list.zip(other)
```

### Control Flow
```kotlin
// If — expression in Kotlin
val max = if (a > b) a else b   // ternary replacement

if (cond) {
} else if (cond2) {
} else {
}

// When (replaces switch — exhaustive when used as expression)
val result = when (x) {
    0 -> "zero"
    1, 2 -> "one or two"
    in 3..10 -> "small"
    is String -> "it's a string: $x"
    else -> "other"
}

// When without argument (replaces if-else chain)
when {
    x < 0 -> "negative"
    x == 0 -> "zero"
    else -> "positive"
}

// Null checks
if (s != null) {
    s.length    // smart cast — compiler knows s: String here
}

// Loops
for (i in 1..10) { }
for (i in 0 until list.size) { }
for (item in list) { }
for ((index, value) in list.withIndex()) { }
for ((key, value) in map) { }
while (cond) { }
do { } while (cond)
list.forEach { println(it) }
repeat(5) { println(it) }
```

### Strings & Characters
```kotlin
// String — immutable (java.lang.String)
val s = "hello"
val s = "$name is ${age + 1} years old"     // string interpolation
val s = """
    multi
    line
""".trimIndent()                             // triple-quoted, stripped

// String operations (extension functions)
s.length
s.uppercase()  s.lowercase()
s.trim()  s.trimStart()  s.trimEnd()
s.contains("sub")
s.startsWith("prefix")
s.split(",")
s.replace("old", "new")
s.reversed()
s.take(3)  s.drop(3)
s.substringAfter(":")
s.toInt()  s.toIntOrNull()    // toIntOrNull returns null instead of throwing

// Char — UTF-16 code unit
val c = 'A'
c.code                         // 65 (Unicode code point)
c.isLetter()  c.isDigit()  c.isUpperCase()
```

### Null / Nullable
```kotlin
// Null is in the type system — T vs T?
var name: String = "Alice"      // non-nullable — cannot be null
var name: String? = null        // nullable

// Safe call — returns null if receiver is null
name?.length                    // Int? (null if name is null)
name?.uppercase()?.length

// Elvis operator — default if null
val len = name?.length ?: 0     // 0 if name is null
val result = map["key"] ?: throw NoSuchElementException("missing key")

// Non-null assertion — throws NullPointerException if null (use sparingly)
val len = name!!.length         // crashes if null

// Smart cast — compiler tracks nullability
if (name != null) {
    println(name.length)        // name: String here (smart cast)
}

// let for null-safe execution
name?.let { n ->
    println("Name is $n")
    n.length
}

// Elvis with throw
val name = user.name ?: throw IllegalStateException("user has no name")
```

### Functions
```kotlin
// Function declaration
fun add(a: Int, b: Int): Int = a + b    // expression body
fun add(a: Int, b: Int): Int {          // block body
    return a + b
}

// Default arguments (no overload needed)
fun greet(name: String, greeting: String = "Hello") = "$greeting, $name!"

// Named arguments
greet(greeting = "Hi", name = "Alice")

// Vararg
fun sum(vararg nums: Int) = nums.sum()
sum(1, 2, 3)
sum(*intArrayOf(1, 2, 3))   // spread

// Extension functions — add methods to existing types
fun String.shout() = this.uppercase() + "!"
"hello".shout()             // "HELLO!"

// Infix functions
infix fun Int.times(str: String) = str.repeat(this)
3 times "ha"                // "hahaha"

// Lambda and higher-order functions
val double = { x: Int -> x * 2 }
val double: (Int) -> Int = { it * 2 }  // 'it' for single param

list.map { it * 2 }         // trailing lambda syntax (lambda outside parens)
list.filter { it > 2 }

// Function types
val f: (Int) -> Int = { x -> x * 2 }
val f: (Int, Int) -> Int = { a, b -> a + b }
val f: () -> String = { "hello" }

// Inline functions (inlines lambda at call site)
inline fun measure(block: () -> Unit): Long {
    val start = System.currentTimeMillis()
    block()
    return System.currentTimeMillis() - start
}

// Suspend functions (coroutines)
suspend fun fetchUser(id: Int): User {
    return withContext(Dispatchers.IO) {
        api.getUser(id)
    }
}
```

### Coroutines
```kotlin
import kotlinx.coroutines.*

// Launch (fire and forget)
GlobalScope.launch {
    val result = fetchData()
    updateUI(result)
}
// NOTE: GlobalScope.launch leaks coroutines — shown here for clarity.
// Production code: use coroutineScope { }, viewModelScope, or lifecycleScope instead.

// Async/await
val deferred = GlobalScope.async { fetchData() }
val result = deferred.await()

// Structured concurrency
coroutineScope {
    val a = async { fetchA() }
    val b = async { fetchB() }
    println(a.await() + b.await())
}

// Flow (reactive streams)
flow {
    emit(1)
    emit(2)
    emit(3)
}.collect { value ->
    println(value)
}
```

### Error Handling
```kotlin
try {
    val result = riskyOperation()
} catch (e: IOException) {
    log(e)
} catch (e: IllegalArgumentException) {
    throw RuntimeException("wrapped", e)
} finally {
    cleanup()
}

// runCatching — Result<T>
val result = runCatching { parseInput(s) }
result.getOrDefault(0)
result.getOrElse { e -> log(e); 0 }
result.map { it * 2 }
result.isSuccess  result.isFailure
```

---

## What Makes It Distinct

1. **Null safety is in the type system** — unlike Java where NPE is always possible, Kotlin's `String` vs `String?` makes nullability a compile-time property. The `?.` and `?:` operators make null handling ergonomic.
2. **Extension functions** — add methods to any type without inheritance. The entire Kotlin standard library is built as extensions on Java types. This is C#'s extension methods, elevated.
3. **Coroutines** — lightweight structured concurrency. Not OS threads. Suspend functions are composable. Kotlin coroutines influenced many languages' async designs.
4. **Data classes** — `data class Point(val x: Int, val y: Int)` generates `equals()`, `hashCode()`, `toString()`, `copy()`. One line vs. a class full of boilerplate in Java.
5. **`when` expression** — richer than Java `switch`. Works on types, ranges, conditions. Must be exhaustive when used as expression. Sealed classes + when = discriminated unions.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| Gradle | Build system |
| Maven | Alternative build |
| Spring Boot + Kotlin | Web framework |
| Ktor | Kotlin-native web framework |
| Exposed / Room | Database |
| Android SDK | Mobile development |
| kotlinx.serialization | Serialization |
| Arrow | Functional programming library |

---

## Gotchas from C#

| C# behavior | Kotlin behavior | Consequence |
|-------------|----------------|-------------|
| Non-virtual by default | Virtual by default (like Java) | Seal classes to prevent override |
| `==` is value equality (for string) | `==` is always structural (null-safe) | Consistent — no trap |
| `T?` is nullable (C# 8+) | `T?` is nullable (always) | Similar concept, different syntax |
| `var` is immutable context-dependent | `val` = immutable, `var` = mutable | Explicit split |
| `using (x)` for dispose | `use {}` on Closeable | Different syntax |
| `IEnumerable<T>` everywhere | `Iterable<T>` / `Sequence<T>` | Same concept, different API |
| async/await | suspend/coroutines | Coroutines are more composable |

---

## Decision Cheat Sheet

| Decision | Use X when... |
|----------|---------------|
| **`data class` vs regular `class`** | `data class` for pure value/data carriers — DTOs, responses, domain value objects. You get `equals`/`hashCode`/`toString`/`copy` free. Regular `class` when you need mutable state, inheritance hierarchy, or non-trivial lifecycle. |
| **`data class` vs `sealed class`** | `sealed class` when you have a fixed set of subtypes and need exhaustive `when` — discriminated unions. Think `Result`, `NetworkState`, `UiEvent`. `data class` for a single concrete type. Combine them: `sealed class` parent with `data class` children. |
| **`val` vs `var`** | Default to `val`. Use `var` only when mutation is genuinely necessary. `val` in Kotlin is a read-only reference, not deeply immutable — the object it points to can still be mutable. Equivalent to C# `readonly` local. |
| **`GlobalScope` vs `CoroutineScope` vs `coroutineScope {}`** | Never `GlobalScope` in production — coroutines escape structured concurrency, can't be cancelled, and leak on teardown. `coroutineScope {}` (lowercase) for suspend functions that launch parallel work and wait — cancellation propagates. `viewModelScope` / `lifecycleScope` in Android — tied to component lifecycle. `CoroutineScope(dispatcher)` when you own the lifecycle explicitly. |
| **`Flow` vs `Channel`** | `Flow` for cold streams — nothing happens until `collect` is called; each collector gets its own execution. `Channel` for hot streams — producer and consumer are decoupled, values exist independently of observers. Use `Flow` for most reactive pipelines; `Channel` for event buses or producer/consumer queues. `StateFlow` / `SharedFlow` are hot `Flow` variants that bridge the gap. |
| **Extension function vs utility object** | Extension function when the operation logically "belongs" on the type and you want call-site readability (`str.toSlug()`). Utility object (`object StringUtils`) when you're grouping unrelated helpers, need Java interop with static methods, or the operation is clearly external to the type. |
| **`runBlocking` vs `runCatching`** | These are unrelated — name similarity is a trap. `runBlocking { }` bridges blocking and coroutine worlds — blocks the calling thread until the coroutine completes; use in `main()` or tests, never in production coroutine code. `runCatching { }` wraps a block in a `Result<T>` to capture success or exception without a try/catch; pure error handling, no coroutine semantics. |
| **`Sequence` vs `List` operations** | `Sequence` (lazy, like Java `Stream`) for long chains of `filter/map` on large collections — avoids intermediate list allocations. `List` operations (eager) for short chains or small collections where the overhead of lazy evaluation exceeds the benefit. |
