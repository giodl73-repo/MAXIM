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
