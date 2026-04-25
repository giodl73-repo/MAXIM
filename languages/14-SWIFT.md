# Language: Swift

> Apple's replacement for Objective-C — value semantics, protocol-oriented programming, ARC memory management, and Swift Concurrency (actors + async/await).

---

## Type System Snapshot

| Axis | Swift |
|------|-------|
| Binding | Early + protocol witness tables (dispatch) |
| Typing | Static |
| Strength | Strong |
| Type system | Nominal + protocol-based structural-ish |
| Type inference | Partial (bidirectional, strong) |
| Memory model | **ARC** — Automatic Reference Counting (compiler-inserted retain/release) |

---

## Memory Models — Conceptual Landscape

```
SWIFT'S THREE MEMORY MODELS
┌─────────────────────────────────────────────────────────────────────┐
│  struct / enum / tuple — VALUE SEMANTICS                            │
│                                                                     │
│  let a = Point(x: 1, y: 2)                                          │
│  var b = a         ← COPY on assignment (independent value)         │
│  b.x = 99          ← a.x is still 1                                 │
│                                                                     │
│  Storage: stack or inline in containing type                        │
│  Lifetime: deterministic — freed when binding goes out of scope     │
│  Collections (Array, Dict, String): copy-on-write (COW)             │
│    var c = a  ← shares buffer until either mutates                  │
│    c.append(x) ← NOW a copy is made (O(n) at mutation, not assign)  │
│                                                                     │
│  C# comparison: like C# struct, but ALL collections are value types │
└─────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────┐
│  class — REFERENCE SEMANTICS + ARC                                  │
│                                                                     │
│  let a = Node(val: 1)   refcount=1                                  │
│  let b = a              refcount=2  ← b and a point to same object  │
│  b.val = 99             ← a.val is now 99!                          │
│                                                                     │
│  ARC lifecycle (compiler-inserted):                                 │
│  ┌──────────┐  assign   ┌──────────────────┐  last ref gone         │
│  │  object  │──────────►│  retain (rc++)   │                       │
│  │  on heap │  release  │  release (rc--)  │──────►  deinit()      │
│  └──────────┘◄──────────│  rc==0 → dealloc │         deallocate    │
│                          └──────────────────┘                       │
│                                                                     │
│  Retain cycles: A → B → A  neither rc ever reaches 0               │
│  Fix: break with weak var (Optional) or unowned (non-Optional)      │
│                                                                     │
│  C# comparison: like C# class (GC handles cycles; ARC does not)    │
└─────────────────────────────────────────────────────────────────────┘
┌─────────────────────────────────────────────────────────────────────┐
│  actor — ARC + SERIAL EXECUTOR ISOLATION                           │
│                                                                     │
│  actor Counter { var value = 0 }                                   │
│                                                                     │
│  External access must go through actor's serial queue:             │
│                                                                     │
│  Task 1 ──► await counter.increment() ─┐                           │
│  Task 2 ──► await counter.get()       ─┼─► serial executor        │
│  Task 3 ──► await counter.increment() ─┘   (one at a time)        │
│                                              ↓                      │
│                                         counter.value (safe)       │
│                                                                     │
│  ARC manages lifetime (same as class)                               │
│  Serial executor prevents data races (no locks needed!)            │
│                                                                     │
│  C# comparison: like a class protected by a SemaphoreSlim(1),      │
│  but enforced by the compiler via async/await protocol             │
└─────────────────────────────────────────────────────────────────────┘

DECISION FLOWCHART — which memory model?
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  Does it need to be shared across multiple owners?                  │
│         │                                                           │
│        YES ──────────────────────────────────────────────────────►  │
│         │                        Does it need thread-safe           │
│         │                        isolated mutable state?            │
│         │                              │                            │
│         │                             YES ──────────► actor         │
│         │                              │                            │
│         │                              NO ───────────► class        │
│         │                                                           │
│        NO                                                           │
│         │                                                           │
│         └──────────────────────────────────────────────► struct     │
│                                                          (default)  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Syntax Reference Card

### Variables & Types
```swift
let x = 5               // immutable constant (inferred: Int)
var x = 5               // mutable variable
let x: Int = 5          // explicit type annotation

// Types
Bool                    // true / false
Int                     // platform-width (64-bit on modern)
Int8  Int16  Int32  Int64
UInt  UInt8  UInt16  UInt32  UInt64
Float   Double
String
Character               // extended grapheme cluster (NOT a UTF-16 code unit!)

// Numeric literals
1_000_000
0xFF        0b1010      0o17
1.0e6

// Type conversion — explicit always
let x = 5
let y = Double(x)       // explicit

// Tuples
let t = (1, "hello")
let (a, b) = t           // destructure
t.0  t.1                 // access by index
let t = (x: 1, y: 2)    // named
t.x  t.y

// typealias
typealias Celsius = Double
typealias Handler = (Result<Data, Error>) -> Void
```

### Equality & Comparison
```swift
// == requires Equatable protocol conformance
struct Point: Equatable {
    var x, y: Int
}
Point(x:1, y:2) == Point(x:1, y:2)     // true
Point(x:1, y:2) != Point(x:1, y:3)     // true

// === is reference equality for class instances (AnyObject)
class Node { }
let a = Node(); let b = a
a === b     // true (same object)
a !== b     // false

// Standard types all conform to Equatable
"hello" == "hello"   // true
[1,2,3] == [1,2,3]   // true (Array conforms to Equatable when element does)

// Comparable — < > <= >=
"abc" < "abd"        // true (lexicographic)
```

### Logical Operators
```swift
&&    // short-circuit AND
||    // short-circuit OR
!     // NOT

&     |     ^     ~     // bitwise
<<    >>                // shift
```

### Collections
```swift
// Array — value type (copies on write)
var arr = [1, 2, 3]         // [Int]
let arr: [Int] = [1, 2, 3]
let arr = [Int]()           // empty
arr.append(4)
arr.append(contentsOf: [5, 6])
arr[0]  arr.first  arr.last
arr.count  arr.isEmpty
arr.contains(2)
arr.filter { $0 > 1 }
arr.map { $0 * 2 }
arr.reduce(0, +)
arr.sorted()  arr.sorted(by: >)
arr[1...3]                  // ArraySlice (half-open: arr[1..<3])

// Dictionary — value type (copies on write)
var dict = ["key": 1, "k2": 2]     // [String: Int]
dict["key"]                          // Int? (Optional)
dict["key", default: 0]             // Int (no Optional)
dict["new"] = 5
dict.removeValue(forKey: "key")
for (k, v) in dict { }
dict.keys  dict.values

// Set — value type, unordered, unique
var s: Set = [1, 2, 3, 2]   // Set<Int> = {1,2,3}
s.insert(4)
s.contains(2)
s.union([4,5])               // new Set
s.intersection([2,3,4])      // new Set

// Range
1...10          // ClosedRange<Int> (includes 10)
1..<10          // Range<Int> (excludes 10)
...5            // PartialRangeThrough<Int>
5...            // PartialRangeFrom<Int>
```

### Control Flow
```swift
// If — no parens, braces required
if x > 0 {
} else if x < 0 {
} else {
}

// Ternary
let max = a > b ? a : b

// if let (optional binding — the primary null-safety pattern)
if let value = optionalValue {
    // value: T here (unwrapped, non-optional)
    use(value)
}

// Multiple optional bindings
if let x = opt1, let y = opt2, x > 0 {
    use(x, y)
}

// Guard — early exit pattern
guard let value = optionalValue else {
    return          // must exit scope
}
// value: T available for rest of function

// Switch — exhaustive, no fallthrough
switch x {
case 0:
    print("zero")
case 1, 2:
    print("one or two")
case 3...10:
    print("small")
case let n where n < 0:
    print("negative: \(n)")
default:
    print("other")
}

// Pattern matching in switch
switch shape {
case .circle(let r):
    area = .pi * r * r
case .rectangle(let w, let h):
    area = w * h
}

// Loops
for i in 1...10 { }
for item in array { }
for (index, item) in array.enumerated() { }
for (key, value) in dict { }
while cond { }
repeat { } while cond
```

### Strings & Characters
```swift
// String — value type, Unicode-correct, very different from other languages
let s = "hello"
let s = "Hello, \(name)!"       // string interpolation
let s = """
    multi
    line
    """                         // multi-line literal (leading whitespace stripped to alignment)
let s = #"raw \(no interp)"#    // raw string (# prefix)
let s = #"\(name)"#             // interpolation in raw: \#(name)

// String is a Collection<Character>
s.count                         // character count (grapheme clusters!)
for char in s { }
s.startIndex  s.endIndex        // String.Index (not Int!)
s[s.startIndex]                 // first character
s.prefix(3)                     // "hel"

// String.Index (NOT integer indexing!)
let i = s.index(s.startIndex, offsetBy: 2)
s[i]                            // 'l'
// This complexity exists because String.Index accounts for variable-width chars

// String operations
s.uppercased()  s.lowercased()
s.trimmingCharacters(in: .whitespaces)
s.contains("sub")
s.hasPrefix("hel")
s.hasSuffix("llo")
s.split(separator: ",")
s.replacingOccurrences(of: "old", with: "new")
s + " world"                    // concatenation
s.isEmpty

// Character — extended grapheme cluster (NOT a UTF-16 code unit)
let c: Character = "A"
let c: Character = "é"          // ONE character (e + combining acute = 1 grapheme)
let c: Character = "😊"         // ONE character

// Unicode scalars
for scalar in s.unicodeScalars { scalar.value }
```

### Null / Optional
```swift
// Optional<T> = T? — baked into the language
var x: Int? = nil
var x: Int? = 42

// Force unwrap — crashes if nil (use sparingly)
let val = x!

// Optional binding (safe)
if let val = x {
    use(val)
}

// Guard (early exit)
guard let val = x else { return }
use(val)  // val available here

// Optional chaining — propagates nil
let street = person?.address?.street    // String?

// Nil coalescing
let val = x ?? 0                        // 0 if nil
let val = x ?? y ?? z                   // chain

// map and flatMap on Optional
x.map { $0 * 2 }          // Int?
x.flatMap { findUser($0) } // User? (flatMap unwraps nested Optional)

// Optional in switch
switch x {
case let v?:                // .some(v)
    use(v)
case nil:                   // .none
    handleNil()
}
```

### Functions
```swift
func add(_ a: Int, _ b: Int) -> Int {    // _ = no external label
    return a + b
}
add(1, 2)               // called without label

func greet(name: String) -> String {     // with external label
    return "Hello, \(name)!"
}
greet(name: "Alice")    // must use label!

func greet(to name: String) -> String {  // external/internal label
    return "Hello, \(name)!"
}
greet(to: "Alice")

// Default parameters
func connect(host: String = "localhost", port: Int = 8080) { }

// Variadic
func sum(_ nums: Double...) -> Double { nums.reduce(0, +) }

// inout (pass by reference)
func swap(_ a: inout Int, _ b: inout Int) {
    (a, b) = (b, a)
}
swap(&x, &y)

// Closures
let double = { (x: Int) -> Int in x * 2 }
let double: (Int) -> Int = { $0 * 2 }    // shorthand argument $0
[1,2,3].map { $0 * 2 }                  // trailing closure

// Generics
func identity<T>(_ x: T) -> T { x }
func max<T: Comparable>(_ a: T, _ b: T) -> T { a > b ? a : b }

// Protocols (structural-ish polymorphism)
protocol Describable {
    func describe() -> String
}
extension Int: Describable {
    func describe() -> String { "the number \(self)" }
}
```

### Memory: ARC
```swift
// Strong reference (default) — increments ref count
let a = MyClass()           // ref count = 1

// Weak reference — doesn't increment ref count (must be Optional)
weak var delegate: MyDelegate?

// Unowned — doesn't increment, assumes non-nil (crash if nil)
unowned let owner: Owner

// Common ARC pattern to avoid retain cycles
class ViewController {
    var completion: (() -> Void)?

    func setup() {
        completion = { [weak self] in    // capture list
            self?.updateUI()             // self is Optional here
        }
    }
}
```

### Error Handling
```swift
// throws / try / catch
enum FileError: Error {
    case notFound(path: String)
    case permissionDenied
}

func readFile(_ path: String) throws -> String {
    guard fileExists(at: path) else {
        throw FileError.notFound(path: path)
    }
    return try String(contentsOfFile: path)
}

do {
    let content = try readFile("/etc/hosts")
    print(content)
} catch FileError.notFound(let path) {
    print("not found: \(path)")
} catch {
    print("error: \(error)")
}

// try? — converts to Optional (nil on error)
let content: String? = try? readFile("/etc/hosts")

// try! — force (crashes on error)
let content = try! readFile("/etc/hosts")

// Result<T, E>
func parse(_ s: String) -> Result<Int, ParseError> {
    guard let n = Int(s) else { return .failure(.invalid) }
    return .success(n)
}

switch parse("42") {
case .success(let n): print(n)
case .failure(let e): print(e)
}
```

### Concurrency (Swift 5.5+)
```swift
// async/await
func fetchUser(id: Int) async throws -> User {
    let data = try await URLSession.shared.data(from: url).0
    return try JSONDecoder().decode(User.self, from: data)
}

// Task
Task {
    let user = try? await fetchUser(id: 42)
}

// async let (parallel)
async let a = fetchA()
async let b = fetchB()
let (ra, rb) = try await (a, b)

// Actor (data race safety)
actor Counter {
    private var value = 0
    func increment() { value += 1 }
    func get() -> Int { value }
}
let counter = Counter()
await counter.increment()
```

---

## What Makes It Distinct

1. **Value semantics everywhere** — `Array`, `Dictionary`, `String`, `struct`, and `enum` are all value types. Passing them copies them (copy-on-write for collections). No accidental sharing. Very different from C# and Java reference semantics.
2. **ARC vs GC** — no stop-the-world garbage collector. Reference counts are updated at compile-inserted retain/release calls. Deterministic deallocation, but requires care with retain cycles.
3. **Protocol-Oriented Programming** — "prefer protocols over classes." Protocols + extensions + generics with constraints replaces deep class hierarchies. Similar to Rust traits.
4. **Swift Concurrency** — actors prevent data races at the type system level. `@MainActor` ensures UI updates on main thread. Structured concurrency via `TaskGroup`.
5. **Enums are powerful** — unlike C/Java/C# enums, Swift enums are full algebraic data types with associated values. `case .circle(radius: 5.0)` carries data. Used everywhere in Swift idioms.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| Xcode | Primary IDE (macOS/iOS development) |
| Swift Package Manager | Package management |
| SwiftUI | Declarative UI framework |
| UIKit / AppKit | Traditional UI (iOS/macOS) |
| Combine | Reactive programming |
| Foundation | Standard library extensions |
| XCTest | Testing |
| Vapor | Server-side Swift |

---

## Gotchas from C#

| C# behavior | Swift behavior | Consequence |
|-------------|---------------|-------------|
| Classes are reference types | Structs (value types) are the default | Copies instead of shared refs |
| `null` with `?:` coalesce | `nil` with `??` coalesce | Same concept, different syntax |
| `string` length = char count | `string.count` = grapheme count (can differ!) | "é" = 1 Character but 2 Unicode scalars |
| `using` for IDisposable | `defer` for cleanup | `defer` is statement-based, not scope-based |
| `interface` declared separately | Protocol conformance in `extension` | Retroactive conformance is normal |
| Generics at runtime | Generics at compile time (monomorphized) | Can't use `T` at runtime for type checks |

---

## Decision Cheat Sheet

| Decision | Use X | When Y |
|----------|-------|--------|
| **`struct` vs `class` vs `actor`** | `struct` | Value semantics; no shared mutable state; default choice for data models |
| | `class` | Shared identity across multiple owners; inheritance needed; Objective-C interop |
| | `actor` | Shared mutable state accessed from concurrent contexts; replaces class + lock |
| **`weak` vs `unowned`** | `weak var` | Reference may become nil during its lifetime; delegate patterns; Optional required |
| | `unowned let/var` | Reference outlives current object and will never be nil; parent-child ownership where child can't outlive parent; crash if assumption violated |
| **`throws` vs `Result<T,E>`** | `throws` / `try` / `catch` | Synchronous error propagation; integrates with `async throws`; most Swift APIs |
| | `Result<T,E>` | Storing errors as values; callbacks/completion handlers; explicit error type needed at call site without do/catch |
| **`async let` vs `TaskGroup`** | `async let` | Fixed number of parallel tasks known at compile time; bind results directly |
| | `TaskGroup` | Dynamic number of tasks (loop-generated); collecting results from variable-count work items |
| **protocol with `associatedtype` vs generic constraint** | generic constraint `<T: Protocol>` | Caller chooses the concrete type; static dispatch; preferred when type is known at call site |
| | `associatedtype` protocol | Protocol defines a family of related types; type is determined by the conforming type, not the caller; use with `some Protocol` or `any Protocol` (Swift 5.7+) |
