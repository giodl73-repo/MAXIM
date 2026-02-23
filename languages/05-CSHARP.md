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
