# Language: C#

> The home base — .NET CLR, modern type system evolution, LINQ, async/await origin, and records. Used as the reference language throughout this series.

---

## Type System Snapshot

| Axis | C# |
|------|-----|
| Binding | **Early** (non-virtual default) — unlike Java |
| Typing | Static |
| Strength | Strong |
| Type system | Nominal + structural for `dynamic` |
| Type inference | Partial — `var`, `new()`, anonymous types, `_` discard |
| Memory model | GC (.NET generational: Gen0/1/2 + LOH) |

---

## CLR Ecosystem Map

```
  SOURCE & TOOLCHAIN
  ┌─────────────────────────────────────────────────────────────────────┐
  │  .cs source files                                                   │
  │         │                                                           │
  │         ▼                                                           │
  │  ┌─────────────────────────────────────────────────────┐           │
  │  │  Roslyn Compiler (Microsoft.CodeAnalysis)           │           │
  │  │  ├── Syntax tree (parse)                            │           │
  │  │  ├── Semantic model (bind, type-check)              │           │
  │  │  ├── Analyzers + Source Generators (Roslyn API)     │           │
  │  │  └── Emit                                           │           │
  │  └─────────────────────────────────────────────────────┘           │
  │         │                                                           │
  │         ▼                                                           │
  │  IL / CIL  (.dll / .exe — platform-neutral bytecode)               │
  │  + Metadata (reflection info, assembly manifest)                    │
  └─────────────────────────────────────────────────────────────────────┘

  RUNTIME (CLR)
  ┌─────────────────────────────────────────────────────────────────────┐
  │  Class Loader  →  JIT Compiler (RyuJIT)  →  Native code (x64/ARM)  │
  │                       │                                             │
  │  ┌────────────────────┼────────────────────────────────────────┐   │
  │  │  Runtime Services  │                                        │   │
  │  │  ├── GC       Gen0 (short-lived) → Gen1 → Gen2 + LOH        │   │
  │  │  ├── Thread Pool   (I/O completion ports + worker threads)  │   │
  │  │  ├── Exception handling  (SEH-based, managed wrappers)      │   │
  │  │  ├── Reflection + Metadata API                              │   │
  │  │  └── P/Invoke + COM interop layer                           │   │
  │  └────────────────────────────────────────────────────────────┘   │
  └─────────────────────────────────────────────────────────────────────┘

  TYPE HIERARCHY (System namespace)
  ┌─────────────────────────────────────────────────────────────────────┐
  │  System.Object  (every managed type roots here)                     │
  │       │                                                             │
  │       ├── System.ValueType  (stack-allocated by default)            │
  │       │         ├── struct          (user-defined value types)      │
  │       │         ├── enum            (int-backed by default)         │
  │       │         ├── Nullable<T>     (T? — boxing on heap if needed) │
  │       │         └── record struct   (C# 10 — value type + =with=)   │
  │       │                                                             │
  │       └── Reference types  (heap-allocated, GC-tracked)            │
  │                 ├── class           (single inheritance)            │
  │                 ├── record class    (C# 9 — structural equality)    │
  │                 ├── interface       (multiple; default members C#8) │
  │                 ├── delegate        (type-safe function pointer)    │
  │                 └── array           (T[] — covariant, SZArray IL)   │
  │                                                                     │
  │  Managed pointers (not in hierarchy — compiler-only types)         │
  │       ├── ref T            (byref — alias to variable)              │
  │       ├── in T             (readonly ref — no copy, no write)       │
  │       ├── out T            (write-before-read byref)                │
  │       ├── Span<T>          (ref struct — stack-only slice)          │
  │       └── ref struct       (must live on stack, no boxing)          │
  └─────────────────────────────────────────────────────────────────────┘
```

---

## Syntax Reference Card

### Variables & Types
```csharp
var x = 5;                      // inferred: int
int x = 5;                      // explicit
const int MAX = 100;            // compile-time constant
readonly int size;              // runtime constant (set in ctor only)
int x = default;                // 0 (default value for type)

// Newer declaration forms (C# 9+)
using var stream = File.OpenRead("f");  // scoped using

// Deconstruction
var (a, b) = (1, 2);
var (x, y, _) = point;         // _ discards third

// Nullable value types
int? n = null;                  // Nullable<int>
n.HasValue  n.Value  n.GetValueOrDefault()

// Nullable reference types (C# 8+ — project-level opt-in)
string? nullable = null;
string nonNull = "value";       // compiler warns if you assign null
```

### Equality & Comparison
```csharp
// == is overloadable
// For string: == is VALUE equality (C# overrides ==)
string a = "hello";
string b = new string("hello".ToCharArray());
a == b              // true (string overloads ==)
object.ReferenceEquals(a, b)    // false (different objects)

// object.Equals / virtual
a.Equals(b)                     // true
object.Equals(a, b)             // null-safe

// Records get structural == automatically (C# 9+)
record Point(int X, int Y);
new Point(1, 2) == new Point(1, 2)  // true ✅

// Pattern matching
x is int n                          // type check + extract
x is > 0 and < 100                  // relational pattern
x is null                           // null check

// IComparable
string.Compare(a, b, StringComparison.OrdinalIgnoreCase)
```

### Logical Operators
```csharp
&&    // short-circuit AND
||    // short-circuit OR
!     // NOT
&     // non-short-circuit logical AND (also bitwise)
|     // non-short-circuit logical OR (also bitwise)
^     // bitwise XOR (not exponentiation!)
~     // bitwise complement
<<  >>  >>>   // shifts (>>> unsigned right shift, C# 11+)

// Null-conditional and null-coalescing
x?.Property         // null if x is null
x?.Method()         // null if x is null
x ?? "default"      // "default" if x is null
x ??= "default"     // assign default if x is null
```

### Collections
```csharp
// C# 12 collection expressions (preferred syntax)
int[] arr = [1, 2, 3];
List<int> list = [1, 2, 3];
int[] spread = [..arr, 4, 5];

// Pre-C# 12
int[] arr = new[] { 1, 2, 3 };
int[] arr = new int[5];                     // zero-initialized
var list = new List<int> { 1, 2, 3 };
var dict = new Dictionary<string, int>
{
    ["a"] = 1,                              // index init
    { "b", 2 }                              // add init
};
var set = new HashSet<int> { 1, 2, 3 };

// Tuples (C# 7+)
(int x, int y) point = (1, 2);
var (x, y) = point;                         // deconstruct
point.x  point.y                            // named members

// Records (immutable data classes, C# 9+)
record Point(int X, int Y);
var p2 = p with { X = 10 };               // non-destructive mutation

// LINQ
var result = list
    .Where(x => x > 0)
    .Select(x => x * 2)
    .OrderBy(x => x)
    .ToList();

// Query syntax
var result = from x in list
             where x > 0
             select x * 2;
```

### Control Flow
```csharp
if (cond) { } else if (cond2) { } else { }

// Ternary
var max = (a > b) ? a : b;

// Switch expression (C# 8+) — the main pattern matching mechanism
var result = shape switch
{
    Circle c => Math.PI * c.Radius * c.Radius,
    Rectangle r => r.Width * r.Height,
    _ => throw new ArgumentException()
};

// Tuple switch
var (role, country) = (user.Role, user.Country);
var access = (role, country) switch
{
    (Role.Admin, _) => Access.Full,
    (_, "US") => Access.US,
    _ => Access.Basic
};

// Pattern matching in if
if (obj is Customer { Name: var name, Age: > 18 })
    Console.WriteLine(name);

// Null checks
if (x is not null) { }
ArgumentNullException.ThrowIfNull(x);   // .NET 6+
```

### Strings & Characters
```csharp
// string — immutable, System.String, UTF-16
string s = "hello";
string s = $"Hello, {name}! Score: {score:F2}";    // interpolation
string s = $"Debug: {obj:D}";                       // with format
string s = @"C:\Users\no\escape\needed";            // verbatim
string s = """
    Raw "string" with "quotes"
    no escaping needed
    """;                                             // raw (C# 11)

// Operations
s.Length                    // char count (UTF-16 units)
s.ToUpper()  s.ToLower()
s.Trim()  s.TrimStart()  s.TrimEnd()
s.Contains("sub")
s.StartsWith("prefix")
s.Replace("old", "new")
s.Split(',')
string.Join(", ", list)
s[0]                        // char at index
s[1..3]                     // "el" (Range indexing, C# 8+)
s[^1]                       // last char (Index from end)

// StringBuilder
var sb = new StringBuilder();
sb.Append("hello").Append(' ').Append("world");
sb.ToString()

// char — UTF-16 code unit (2 bytes)
char c = 'A';
char.IsLetter(c)
char.ToUpper(c)
(int)c                      // 65

// Rune — full Unicode code point (C# 8+)
Rune r = new Rune(0x1F600);  // emoji as single code point
```

### Null / Nullable
```csharp
// Reference types: always nullable pre-C#8; nullable analysis in C# 8+
string? s = null;               // explicitly nullable
string nonNull = "value";       // compiler ensures non-null

// Value types: Nullable<T> = T?
int? n = null;
n.HasValue
n.Value                         // throws InvalidOperationException if null
n.GetValueOrDefault(0)

// Null operators
x?.Property                     // null propagation
x?.Method()?.Property           // chained
x ?? defaultValue               // null coalescing
x ??= defaultValue              // null coalescing assignment

// Null patterns
if (x is null) { }
if (x is not null) { }
x ?? throw new ArgumentNullException(nameof(x));
```

### Functions
```csharp
// Method
int Add(int a, int b) => a + b;     // expression-bodied
int Add(int a, int b) { return a + b; }

// Static local function (C# 8+)
static int Local(int x) => x * 2;

// Generic method
T Identity<T>(T x) => x;
T Max<T>(T a, T b) where T : IComparable<T> => a.CompareTo(b) > 0 ? a : b;

// Lambda / delegate
Func<int, int> double_ = x => x * 2;
Func<int, int, int> add = (a, b) => a + b;
Action<string> print = s => Console.WriteLine(s);
Predicate<string> nonEmpty = s => !string.IsNullOrEmpty(s);

// Method group
Action<string> print = Console.WriteLine;

// Async/await
async Task<string> FetchAsync(string url)
{
    var response = await httpClient.GetStringAsync(url);
    return response;
}

// Extension methods
static class StringExtensions
{
    public static string Shout(this string s) => s.ToUpper() + "!";
}
"hello".Shout()   // "HELLO!"
```

### Error Handling
```csharp
try
{
    var result = DoSomething();
}
catch (ArgumentNullException e) when (e.ParamName == "x")  // exception filter
{
    Console.Error.WriteLine(e.Message);
}
catch (InvalidOperationException e)
{
    throw new ApplicationException("wrapped", e);    // rethrow with context
}
catch (Exception e)
{
    throw;      // rethrow preserving stack trace (not: throw e;)
}
finally
{
    // always runs
}

// using — deterministic cleanup (IDisposable)
using var connection = new SqlConnection(connectionString);
// connection.Dispose() called at end of scope

// Modern: Result pattern (common in functional C#)
// No built-in Result<T,E> — use libraries like LanguageExt, FluentResults
```

---

## What Makes It Distinct

1. **Non-virtual by default** — unlike Java. Methods only become virtual with `virtual` keyword. `override` is required, `sealed` locks it back. Cleaner object model.
2. **LINQ** — Language-Integrated Query: `from x in list where x > 0 select x` works on IEnumerable, IQueryable (SQL), XML, and anything that implements the pattern. Transformative for data handling.
3. **async/await** — C# invented it (2012). `async`/`await` as a first-class language feature, not a library bolted on. Node.js, Python, Rust all followed.
4. **Records + pattern matching** — C# 9–12 added records, pattern switches, list patterns, property patterns. Functional programming features added to an OOP language.
5. **Nullable reference types (C# 8+)** — opt-in static null analysis. The type system now distinguishes `string` (non-null) from `string?` (nullable). Gradual adoption via project settings.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| dotnet CLI | Build, run, publish |
| NuGet | Package manager |
| ASP.NET Core | Web framework |
| Entity Framework Core | ORM |
| xUnit / NUnit / MSTest | Testing |
| Blazor | WebAssembly / server-side UI |
| MAUI | Cross-platform desktop/mobile |
| Roslyn | Compiler API (source generators, analyzers) |

---

## The C# Evolution Milestones

| Version | Year | Key Addition |
|---------|------|-------------|
| 2.0 | 2005 | Generics, nullable types, iterators |
| 3.0 | 2007 | LINQ, lambda, `var`, extension methods |
| 4.0 | 2010 | `dynamic`, named/optional params |
| 5.0 | 2012 | **async/await** |
| 6.0 | 2015 | String interpolation, `?.`, `nameof` |
| 7.0 | 2017 | Tuples, pattern matching, `out var` |
| 8.0 | 2019 | Nullable references, `switch` expressions, ranges |
| 9.0 | 2020 | Records, init-only, top-level statements |
| 10.0 | 2021 | Record structs, global using, file-scoped namespace |
| 11.0 | 2022 | Raw strings, generic math, `required` |
| 12.0 | 2023 | Collection expressions, primary constructors |
| 13.0 | 2024 | `params` collections, `lock` object, `field` keyword |

---

## Decision Cheat Sheet

### Type declaration: which form?

| Use | When | Avoid when |
|-----|------|------------|
| `record class` | Immutable data bags; structural equality needed; DTOs, value objects | Mutable state; identity matters (two instances with same data are distinct) |
| `record struct` | Same as record class but value semantics + stack allocation matters; small immutable structs | Large structs (copy cost); need inheritance |
| `class` | Mutable state; identity matters; OOP inheritance hierarchies | Pure data containers with no behavior |
| `struct` | High-frequency small values; avoid GC pressure; `Span<T>`, `Vector<T>` patterns | Size > ~16 bytes; need inheritance; virtual dispatch |
| `readonly struct` | Struct that is never mutated after construction; enables `in` param optimization | Any mutation needed |
| `ref struct` | Must not escape the stack; wraps managed pointers (`Span<T>`) | Stored in fields, captured in lambdas, boxed |

### Async return type: Task vs ValueTask?

| Use | When |
|-----|------|
| `Task<T>` | General case; method sometimes async; consumed by multiple awaiters |
| `ValueTask<T>` | Hot path that frequently completes synchronously (avoids heap alloc); cache-hit patterns |
| `Task` (no result) | Fire-and-forget infrastructure; never `async void` except event handlers |
| `async void` | **Only** event handlers (`Button.Click += async (s,e) => ...`); exceptions are unobservable everywhere else |
| `IAsyncEnumerable<T>` | Streaming results; infinite sequences; `await foreach` consumers; server-sent events |

### Memory / buffer: which abstraction?

| Use | When | Constraint |
|-----|------|------------|
| `T[]` | General heap arrays; interop; long-lived | Heap allocation; GC pressure at high frequency |
| `Span<T>` | Stack-allocated slices; parsing; zero-copy subranges | Cannot escape stack; no async; no fields in classes |
| `Memory<T>` | Same as Span but heap-capable; can cross async boundaries | Slight overhead vs Span |
| `ArraySegment<T>` | Legacy interop with older APIs expecting segments | Less expressive than Span/Memory |
| `IMemoryOwner<T>` | Pooled memory (ArrayPool); explicit lifetime | Manual Dispose required |

### Collection interface: how narrow?

| Use | When |
|-----|------|
| `IEnumerable<T>` | Lazily-evaluated sequences; LINQ source; widest compatibility; caller only iterates |
| `IReadOnlyCollection<T>` | Count needed; caller does not mutate; slightly narrower than List |
| `IReadOnlyList<T>` | Index access needed; immutable view of ordered data |
| `ICollection<T>` | Caller may Add/Remove; Count guaranteed |
| `IList<T>` | Full random-access + mutation; prefer concrete type in private APIs |
| Concrete (`List<T>`, `T[]`) | Private/internal APIs; performance-critical code where interface dispatch matters |

### LINQ provider: IEnumerable vs IQueryable?

| Use | When |
|-----|------|
| `IEnumerable<T>` | In-memory data; F# seq equivalent; evaluated in the process |
| `IQueryable<T>` | Database queries via EF Core; expression tree translated to SQL; never call `.ToList()` until you mean it |

### Span<T> vs Memory<T> vs array — async boundary decision

```
Need zero-copy slice?
    └── Yes → Span<T>
            └── Crosses async boundary / stored in field?
                    ├── No  → Span<T> (stack only)
                    └── Yes → Memory<T>

Long-lived heap buffer with explicit lifetime?
    └── Yes → ArrayPool<T>.Shared.Rent() + IMemoryOwner<T>
```

---

## Common Confusion Points

**`record struct` equality is struct equality, not reference equality**
```csharp
record struct Point(int X, int Y);
Point a = new(1, 2);
Point b = new(1, 2);
a == b   // true — value equality (field-by-field)
// But: record struct is a VALUE TYPE — copied on assignment
// Mutation after copy does not affect the original
```
Contrast: `record class` is a reference type with structural `==`. Two variables can hold the same object. `record struct` cannot — you always have a copy.

**`async void` swallows exceptions**
```csharp
// BAD — exception escapes to SynchronizationContext and crashes the process
async void DoWork() { await Task.Delay(1); throw new Exception("lost"); }

// GOOD — exception is captured in the Task; caller can observe it
async Task DoWork() { await Task.Delay(1); throw new Exception("observable"); }

// async void is ONLY acceptable for event handlers where the framework
// provides the SynchronizationContext exception handler:
button.Click += async (s, e) => { await DoWorkAsync(); };
```

**`throw` vs `throw e` — stack trace destruction**
```csharp
catch (Exception e)
{
    throw;        // CORRECT — preserves original stack trace
    throw e;      // WRONG  — resets stack trace to this line; loses origin
    // If you must re-wrap:
    throw new ApplicationException("context", e);   // inner exception preserves trace
    // Or .NET 6+:
    ExceptionDispatchInfo.Capture(e).Throw();        // rethrows with original trace
}
```

**`in` parameter is NOT the iterator keyword**
```csharp
// `in` = readonly ref — caller's variable is passed by reference, not copied,
// but the callee cannot write to it. Optimization for large readonly structs.
void Process(in Matrix4x4 m) { /* m is a ref, no copy, but readonly */ }

// NOT the same as `in` in foreach:
foreach (var item in collection) { }   // different keyword, different meaning
```

**`IDisposable` + async: ConfigureAwait and disposal order**
```csharp
// `await using` for IAsyncDisposable (streams, EF DbContext, etc.)
await using var ctx = new AppDbContext(options);

// ConfigureAwait(false) — suppress SynchronizationContext capture
// Use in library code (not UI or ASP.NET controller code):
var data = await repository.GetAsync().ConfigureAwait(false);

// Disposal happens AFTER the await completes — using var is safe:
using var stream = File.OpenRead("f");
var content = await ReadAllAsync(stream);   // stream still open during await
// stream.Dispose() called here, after await
```

**Value tuple field names exist only at compile time**
```csharp
(int X, int Y) point = (1, 2);
point.X   // works at compile time via compiler magic
// At IL level: System.ValueTuple<int,int> with fields Item1, Item2
// Names are encoded in [TupleElementNames] attribute on the return type
// Reflection sees Item1/Item2; cross-assembly names depend on attribute presence
```

**Pattern matching exhaustiveness: when does the compiler warn?**
```csharp
// Compiler checks exhaustiveness for switch EXPRESSIONS (C# 8+)
// Switch STATEMENTS do not warn — another reason to prefer switch expressions

Shape s = ...;
var area = s switch                 // compiler WILL warn if a DU case is missing
{
    Circle c => ...,
    // Rectangle missing → CS8509 warning
};

// For class hierarchies (not sealed): compiler cannot know all subtypes
// — you must include _ => ... fallthrough
```

**`init` vs `readonly` — the subtle difference**
```csharp
class Config
{
    public string Name { get; init; }   // settable in object initializer + ctor
    public readonly string Id;          // settable ONLY in ctor (not initializer)
}

// init allows: new Config { Name = "x" }
// readonly does NOT allow object initializer syntax — ctor only
```
