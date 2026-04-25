# Language: C++

> C with object-oriented and generic programming layered on top — the language that proves zero-cost abstraction is achievable at the cost of enormous complexity.

---

## Type System Snapshot

| Axis | C++ |
|------|-----|
| Binding | Early (non-virtual) + vtable (virtual) |
| Typing | Static |
| Strength | Weak-ish — many implicit conversions (narrowing, pointer coercions) |
| Type system | Nominal; templates add structural-ish behavior |
| Type inference | Partial — `auto`, `decltype`, template deduction |
| Memory model | RAII (destructors) + smart pointers + manual fallback |

---

## Conceptual Map

C++ is best understood as four orthogonal complexity axes that interact but can be learned independently. Most confusion comes from conflating axes that are actually independent mechanisms.

```
┌─────────────────────────────────────────────────────────────────────┐
│                    C++ COMPLEXITY AXES                              │
└─────────────────────────────────────────────────────────────────────┘

AXIS 1 — OOP LAYER (runtime polymorphism)
─────────────────────────────────────────
  Base class                   Derived class
  ┌──────────────────┐         ┌──────────────────────┐
  │ class Shape {    │◄────────│ class Circle : Shape {│
  │   virtual draw();│         │   void draw() override│
  │   virtual ~Shape │         │ };                    │
  │ }                │         └──────────────────────┘
  └────────┬─────────┘
           │ vtable pointer (one per object instance)
           ▼
  ┌──────────────────────────────┐
  │  vtable for Circle           │  ← one per concrete type, not per instance
  │  [0] → Circle::draw()        │    ~8 bytes added to every polymorphic object
  │  [1] → Circle::~Circle()     │    virtual call = pointer chase (cache miss risk)
  └──────────────────────────────┘

AXIS 2 — TEMPLATE LAYER (compile-time polymorphism)
────────────────────────────────────────────────────
  template<typename T>          Instantiation at compile time:
  T max(T a, T b) {             max<int>   → separate machine code
    return a > b ? a : b;       max<double> → separate machine code
  }                             Zero runtime overhead — no vtable, no boxing
                                Code bloat tradeoff: N types = N copies

  Pre-C++20: duck-typed (no constraint enforcement until instantiation error)
  C++20 Concepts: explicit constraints, checked at point of call

AXIS 3 — RAII LAYER (deterministic resource cleanup)
─────────────────────────────────────────────────────
  Constructor acquires          Destructor releases
  ┌─────────────────────┐       ┌─────────────────────┐
  │ MyFile(path) {      │       │ ~MyFile() {         │
  │   fd = open(path);  │  ←──→ │   close(fd);        │
  │ }                   │       │ }                   │
  └─────────────────────┘       └─────────────────────┘
         │                              ▲
         │  object lifetime             │
         └──────────────────────────────┘
  Works through exceptions — destructor called on stack unwind
  C# parallel: IDisposable + using() is RAII with manual trigger;
               C++ destructor fires automatically at scope exit

AXIS 4 — VALUE CATEGORIES (move semantics)
───────────────────────────────────────────

  Every expression has a value category:

  lvalue — has a persistent address; can appear on left of =
  ┌─────────────────────────────────────┐
  │  int x = 5;    x is an lvalue       │
  │  std::string s = "hello";           │
  │  s is an lvalue (has address &s)    │
  └─────────────────────────────────────┘

  rvalue — temporary; no persistent address; right side of =
  ┌─────────────────────────────────────┐
  │  5           — integer literal      │
  │  std::string("hello") — temporary   │
  │  getStr()    — return value         │
  └─────────────────────────────────────┘

  move — transfer ownership of rvalue resource (no copy)
  ┌──────────────────────────────────────────────────────┐
  │  std::vector<int> a = {1,2,3};                       │
  │  std::vector<int> b = std::move(a);  // a now empty  │
  │  // O(1) — no element copy; just pointer swap        │
  └──────────────────────────────────────────────────────┘

  T&    — lvalue reference (alias to existing object)
  T&&   — rvalue reference (binds to temporaries; enables move)
  const T& — binds to both lvalues and rvalues (universal const ref)
```

---

## Syntax Reference Card

### Variables & Types
```cpp
int x = 5;
auto x = 5;             // deduced int
auto x = 5.0;           // deduced double
const int MAX = 100;
constexpr int N = 10;   // compile-time constant (stronger than const)
int& ref = x;           // lvalue reference
int&& rref = 5;         // rvalue reference (move semantics)

// Integer types (same as C — prefer fixed-width)
#include <cstdint>
int32_t  int64_t  uint32_t  uint64_t

// Initialization forms
int a(5);               // direct
int a{5};               // uniform (C++11) — prevents narrowing
int a = 5;              // copy
auto a = int{5};        // explicitly typed uniform
```

### Equality & Comparison
```cpp
x == y                  // value equality (overloadable)
x != y
x < y  x > y  x <= y  x >= y
x <=> y                 // spaceship (C++20) — returns std::strong_ordering

// Pointer equality
p == q                  // same address
*p == *q                // pointed-to values

// User-defined equality
struct Point {
    int x, y;
    bool operator==(const Point& o) const { return x==o.x && y==o.y; }
    auto operator<=>(const Point& o) const = default; // C++20: all comparisons
};

// Type traits (not runtime equality)
std::is_same_v<int, int32_t>   // true (on most platforms)
std::is_same_v<int, long>      // likely false
```

### Logical Operators
```cpp
&&  ||  !               // logical (short-circuit)
&   |   ^   ~           // bitwise
<<  >>                  // shift

// C++ also allows keyword aliases
and  or  not            // identical to &&, ||, !
and_eq  or_eq  xor_eq   // &=, |=, ^=
```

### Collections
```cpp
#include <vector>
#include <array>
#include <map>
#include <unordered_map>
#include <set>
#include <tuple>

// Vector (dynamic array)
std::vector<int> v = {1, 2, 3};
v.push_back(4);
v[0];  v.front();  v.back();
v.size();  v.empty();

// Array (fixed size, stack)
std::array<int, 3> a = {1, 2, 3};

// Map (sorted, O(log n))
std::map<std::string, int> m = {{"a", 1}, {"b", 2}};
m["key"] = val;
m.find("key") != m.end()  // check presence

// Unordered map (hash, O(1) avg)
std::unordered_map<std::string, int> um;

// Set
std::set<int> s = {3, 1, 4, 1};  // sorted, deduplicated

// Tuple
auto t = std::make_tuple(1, "two", 3.0);
auto [x, y, z] = t;    // structured binding (C++17)
std::get<0>(t);

// Span (non-owning view)
std::span<int> view = v;    // C++20
```

### Control Flow
```cpp
if (cond) { }
if (int n = getValue(); n > 0) { }   // init-if (C++17)

// Ternary
auto x = (a > b) ? a : b;

// Switch
switch (x) {
    case 1: break;
    [[fallthrough]];        // explicit fallthrough (C++17)
    default: break;
}

// Range-based for (C++11)
for (const auto& elem : container) { }
for (auto& [key, val] : map) { }     // structured bindings

// if constexpr (compile-time branch)
if constexpr (std::is_integral_v<T>) {
    // only compiled when T is integral
}
```

### Strings & Characters
```cpp
#include <string>
std::string s = "hello";
s += " world";              // mutable
s.size();  s.empty();
s.substr(1, 3);
s.find("lo");

// String view (non-owning reference)
std::string_view sv = s;    // no copy

// Formatting (C++20)
#include <format>
auto msg = std::format("Hello, {}! Age: {}", name, age);

// Raw string literal
auto raw = R"(no \n \t escapes here)";
auto delimited = R"---(contains ) brackets)---";

// Char types
char    c = 'A';            // typically 1 byte
wchar_t w = L'A';           // wide char (platform-dependent)
char8_t u8 = u8'A';        // UTF-8 code unit (C++20)
char16_t u16 = u'A';       // UTF-16 code unit
char32_t u32 = U'A';       // UTF-32 code point
```

### Null / Optional
```cpp
#include <optional>

// Optional<T> — the modern nullable
std::optional<int> maybeVal = std::nullopt;
maybeVal = 42;
if (maybeVal) { use(*maybeVal); }
maybeVal.value();           // throws std::bad_optional_access if empty
maybeVal.value_or(-1);      // safe with default

// Raw pointers — still the C approach
int *p = nullptr;           // null pointer
if (p != nullptr) { *p; }  // check before deref

// Smart pointers
std::unique_ptr<T> p = std::make_unique<T>(args);  // single owner
std::shared_ptr<T> p = std::make_shared<T>(args);  // ref-counted
std::weak_ptr<T> w = shared;                        // non-owning
```

### Functions
```cpp
// Regular function
int add(int a, int b) { return a + b; }

// Default arguments
void f(int x, int y = 0) { }

// Lambda (C++11)
auto f = [](int x) { return x * 2; };
auto capture = [y](int x) { return x + y; };     // capture by value
auto captureRef = [&y](int x) { return x + y; }; // capture by reference
auto moveCapture = [p = std::move(ptr)](int x) { }; // capture by move

// Generic lambda (C++14)
auto f = [](auto x) { return x; };

// Templates
template<typename T>
T identity(T x) { return x; }

// Concepts (C++20)
template<std::integral T>
T add(T a, T b) { return a + b; }
```

### Error Handling
```cpp
#include <stdexcept>

// Exceptions
try {
    throw std::runtime_error("something went wrong");
} catch (const std::invalid_argument& e) {
    std::cerr << e.what();
} catch (const std::exception& e) {
    std::cerr << e.what();
} catch (...) {
    // catch all
}

// std::expected (C++23) — Result-like type
#include <expected>
std::expected<int, std::string> divide(int a, int b) {
    if (b == 0) return std::unexpected("division by zero");
    return a / b;
}
auto result = divide(10, 2);
if (result) { use(*result); }
else { log(result.error()); }
```

---

## What Makes It Distinct

1. **Zero-cost abstractions** — the design principle: features you don't use cost nothing; features you do use couldn't be written faster by hand. Templates and inlining make this possible.
2. **RAII** — Resource Acquisition Is Initialization: constructors acquire, destructors release. Deterministic cleanup even through exceptions. The design C# borrowed for `using`.
3. **Undefined behavior** — C++'s major footgun. Signed overflow, out-of-bounds access, null deref, use-after-move — the compiler assumes these don't happen and optimizes accordingly.
4. **Templates vs virtuals** — two orthogonal polymorphism mechanisms. Templates = compile-time (static dispatch, code bloat). Virtuals = runtime (vtable, flexible). Choosing wrong kills performance or flexibility.
5. **Move semantics** — `&&` rvalue references enable transfer of ownership without copying. Foundational for performance; confusing syntax.

---

## Bridge: C++ Templates → C# Generics

You know C# generics deeply. C++ templates look similar but operate on a fundamentally different model. The key distinction: **C# generics are constrained at definition time; C++ templates are duck-typed at instantiation time.**

### The Same Constraint, Three Ways

Suppose you want a function that adds two values of the same type, where that type must support `+`.

**C# — constraint enforced at definition, checked at call site:**
```csharp
// IAddable doesn't exist in BCL, but the pattern is familiar:
T Add<T>(T a, T b) where T : IComparable<T>
{
    return a.CompareTo(b) > 0 ? a : b;   // contrived but shows constraint
}

// Real BCL pattern with operator constraint (C# 11+):
T Sum<T>(T a, T b) where T : INumber<T>
{
    return a + b;   // only compiles because INumber<T> guarantees +
}
```

**C++ pre-C++20 — no constraint; error appears at instantiation, not definition:**
```cpp
template<typename T>
T add(T a, T b) {
    return a + b;   // compiles fine even if T has no operator+
}                   // error fires only when you call add<SomeType>()
                    // and the error message is a template instantiation wall

add(1, 2);          // fine — int has +
add(MyStruct{}, MyStruct{});  // error here, not at the template definition
```

**C++20 Concepts — the direct analog to C# `where` constraints:**
```cpp
// Define a concept (like a C# interface constraint)
template<typename T>
concept Addable = requires(T a, T b) {
    { a + b } -> std::convertible_to<T>;   // T must support +, result convertible to T
};

// Apply it — error fires at call site with a readable message
template<Addable T>
T add(T a, T b) {
    return a + b;
}

// Shorthand with standard library concepts
template<std::integral T>           // std::integral is a built-in concept
T addInts(T a, T b) { return a + b; }

// Or with requires clause inline
template<typename T>
    requires std::floating_point<T> || std::integral<T>
T addNumeric(T a, T b) { return a + b; }
```

### Mental Model Comparison

| Aspect | C# Generics | C++ Templates (pre-C++20) | C++20 Concepts |
|--------|-------------|--------------------------|----------------|
| Constraint enforcement | Definition time | Instantiation time | Definition time |
| Error location | Call site, readable | Instantiation site, cryptic | Call site, readable |
| Mechanism | Interface/delegate matching | Duck typing — any type that compiles | Named constraints (`concept`) |
| Reification | One IL method, boxing for value types | Separate machine code per type (monomorphization) | Same as templates — separate code per type |
| Analog to `where T : IComparable<T>` | Native syntax | Write SFINAE (arcane) | `requires std::totally_ordered<T>` |
| Runtime cost | Possible boxing overhead | Zero — fully inlined/specialized | Zero |

> **Key insight**: C++ templates are more powerful than C# generics (they can constrain on arbitrary syntactic properties, not just interface membership), but pre-C++20 the error messages are famously terrible. C++20 Concepts close most of that gap. If you're writing modern C++, use Concepts wherever you'd use `where` in C#.

---

## Decision Cheat Sheet

| Decision | Use When | Avoid When / Watch Out For |
|----------|----------|---------------------------|
| **`std::unique_ptr<T>`** | Single, clear owner; ownership transfers via move; no sharing needed | Sharing across threads or callbacks that outlive the owner; use `shared_ptr` then |
| **`std::shared_ptr<T>`** | Shared ownership; lifetime uncertain; multiple holders | Default choice "because it's safe" — ref-counting has cost; prefer `unique_ptr` when ownership is clear |
| **Raw pointer `T*`** | Non-owning observer (you know owner outlives you); C interop; performance-critical inner loops | Owning a heap allocation — use smart pointers; uninitialized raw pointers = UB |
| **`std::vector<T>`** | Dynamic-size contiguous storage; most collections | When size is truly fixed at compile time (`std::array` is better); when you need non-contiguous storage |
| **`std::array<T, N>`** | Fixed-size stack-allocated array; know size at compile time | When size varies; prefer over raw arrays — has `.size()`, range-for, no decay |
| **`std::span<T>`** | Non-owning view over contiguous data (vector, array, raw array); function parameter that shouldn't copy | Storing — span does not own; dangling span if underlying container is destroyed |
| **Virtual dispatch** | Runtime polymorphism; set of types not known at compile time; plugin/extension points | Performance-critical hot paths (vtable = indirect call + cache miss); when all types are known at compile time |
| **Templates** | Compile-time polymorphism; all types known at compile time; zero-overhead abstractions | When binary size matters (each instantiation = separate code); deeply recursive templates (compile time cost) |
| **`std::variant<A,B,C>` + `std::visit`** | Closed set of types known at compile time; want exhaustive pattern matching; value semantics preferred | Open-ended extension (use virtual then); when types share no common behavior |
| **RAII via destructor** | The default — any resource with clear ownership (file, lock, connection, memory) | When cleanup order across objects is complex (carefully consider destruction order) |
| **`unique_ptr` custom deleter** | Non-memory resources (file descriptors, C library handles) needing RAII wrapping | When you need the deleter to be stateful and shared — `shared_ptr` custom deleter instead |
| **`std::string`** | Owning, mutable string data; building/modifying strings | Passing read-only string to a function — use `std::string_view` to avoid copies |
| **`std::string_view`** | Non-owning read-only view of string data; function parameters; parsing | Storing — does not own memory; dangling view if source string is destroyed or reallocated |
| **C++17** | Conservative target; widely supported (GCC 7+, Clang 5+, MSVC 2017+); `if constexpr`, `std::optional`, structured bindings | Cutting-edge features — use C++20/23 only if your toolchain guarantees it |
| **C++20** | Modern baseline for new projects; Concepts, `std::span`, `std::format`, coroutines | Embedded or constrained toolchains still on C++14/17 |
| **C++23** | `std::expected`, `std::print`, `std::flat_map`; opt in feature by feature | Broad deployment — compiler support still catching up as of 2025 |

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| gcc / clang / MSVC | Compilers |
| CMake | Build system (the default) |
| Conan / vcpkg | Package managers |
| AddressSanitizer / UBSan | Sanitizers (build with -fsanitize=address) |
| clang-tidy / cppcheck | Static analysis |
| Catch2 / GoogleTest | Testing |
| Abseil / Boost | Extended standard library |

---

## Gotchas from C#

| C# behavior | C++ behavior | Consequence |
|-------------|-------------|-------------|
| `new` returns managed object | `new` returns raw pointer (memory leak if not deleted) | Use `make_unique`/`make_shared` |
| `foreach` is safe | `for (auto x : v)` — modifying `v` during iteration = UB | Never modify while iterating |
| `string` is immutable | `std::string` is mutable | Thread safety differs |
| Virtual by default | Virtual must be opted in with `virtual` | Forgetting `virtual` = wrong method called |
| Interfaces are clean | Multiple inheritance creates diamond problem | Understand virtual inheritance |
| Integer overflow is defined | Signed overflow is **undefined behavior** | Use unsigned or check first |
| `null` is safe to assign | Uninitialized pointer is UB to read | Always initialize: `T* p = nullptr;` |

---

## When to Choose C++

- Game engines and real-time graphics (Unreal, LLVM, etc.)
- High-frequency trading and latency-critical systems
- Embedded systems with more complexity than C can handle
- Interop with existing C++ libraries (Qt, OpenCV, TensorFlow C++ API)
- Systems where you need both C compatibility AND OOP/templates

**Not for**: web services, business applications, rapid prototyping. Use Rust if you want C++-level performance with memory safety.
