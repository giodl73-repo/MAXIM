# Language: Rust

> Memory safety without garbage collection — ownership types and the borrow checker eliminate entire classes of bugs at compile time. Zero-cost abstractions from ML/Haskell applied to systems programming.

---

## Type System Snapshot

| Axis | Rust |
|------|------|
| Binding | Early (static) default; `dyn Trait` for late binding |
| Typing | Static |
| Strength | Strong — no implicit conversions, ever |
| Type system | Nominal + trait-based polymorphism |
| Type inference | Partial — local bidirectional, Hindley-Milner-inspired |
| Memory model | **Ownership** — compile-time, zero GC overhead |

---

## Syntax Reference Card

### Variables & Types
```rust
let x = 5;              // immutable binding (default!)
let mut x = 5;          // mutable binding
let x: i32 = 5;         // explicit type
const MAX: u32 = 100;   // compile-time constant, must annotate type
static COUNT: i32 = 0;  // static lifetime, lives forever
let _ = 5;              // discard value

// Shadowing (rebinding same name)
let x = 5;
let x = x * 2;          // x is now 10 — creates new binding, not mutation
let x = x.to_string();  // x is now String — different type!

// Integer types (all fixed-width, no surprise sizes)
i8   i16   i32   i64   i128   isize    // signed
u8   u16   u32   u64   u128   usize    // unsigned
f32  f64                                // float
bool                                    // true / false (not 0/1)
char                                    // Unicode scalar value (4 bytes! not a byte)

// Numeric literals
1_000_000   // underscores for readability
0xFF        // hex
0b1010      // binary
0o17        // octal
1.0f64      // float literal with type suffix

// Type conversion — explicit always, no implicit
let x: i32 = 5;
let y: f64 = x as f64;  // explicit cast
```

### Ownership & Borrowing (the core Rust concept)
```rust
// Ownership: every value has exactly one owner
let s1 = String::from("hello");
let s2 = s1;        // s1 is MOVED — s1 is no longer valid!
// println!("{s1}") // ERROR: value used after move

// Clone for explicit copy
let s2 = s1.clone();    // deep copy — s1 still valid

// Copy types (stack-only: integers, floats, bool, char, tuples of Copy)
let x = 5;
let y = x;          // COPIED — x is still valid
println!("{x}");    // ✅

// References (borrowing)
let s = String::from("hello");
let r1 = &s;        // immutable reference — s still owns
let r2 = &s;        // multiple immutable refs OK
// let rm = &mut s; // ERROR: can't have mutable ref while immutable refs active

let mut s = String::from("hello");
let rm = &mut s;    // mutable reference — only ONE at a time
rm.push_str(" world");

// Lifetimes (elided in simple cases, explicit when ambiguous)
fn longest<'a>(s1: &'a str, s2: &'a str) -> &'a str {
    if s1.len() > s2.len() { s1 } else { s2 }
}
```

### Equality & Comparison
```rust
// Requires deriving or implementing traits
#[derive(PartialEq, Eq)]
struct Point { x: i32, y: i32 }

Point { x: 1, y: 2 } == Point { x: 1, y: 2 }  // true

// All built-in types implement PartialEq
1 == 1          // true
"hello" == "hello"  // true (&str comparison is value)
vec![1,2] == vec![1,2]  // true

// PartialEq vs Eq
// PartialEq: == defined but may be partial (floats: NaN != NaN)
// Eq: == is total (everything equals itself)
// f64 implements PartialEq but NOT Eq (because NaN)

// Comparison requires PartialOrd/Ord
#[derive(PartialOrd, Ord)]
// then: a < b, a.cmp(&b) == Ordering::Less

// Pointer equality
std::ptr::eq(a, b)  // same address

// Pattern matching (structural destructuring)
if let Point { x, y } = p { }
```

### Logical Operators
```rust
&&    // short-circuit AND
||    // short-circuit OR
!     // NOT (also used for macro invocation: vec![])

// Bitwise
&   |   ^   !   <<   >>
// Note: ! is bitwise NOT (not ~ like C)

// Bitwise on booleans (non-short-circuit)
true & false    // false (evaluates both sides)
```

### Collections
```rust
// Array — fixed size, stack-allocated
let a: [i32; 3] = [1, 2, 3];
let zeros = [0; 5];         // [0, 0, 0, 0, 0]
a[0]  a.len()

// Slice — reference to contiguous sequence
let slice: &[i32] = &a;
let slice = &a[1..3];       // [2, 3]

// Vec — dynamic array (heap)
let v: Vec<i32> = vec![1, 2, 3];
let mut v = Vec::new();
v.push(4);
v.pop()                     // Option<i32>
v[0]                        // panics if out of bounds
v.get(0)                    // Option<&i32> — safe
v.iter()                    // iterator (immutable)
v.iter_mut()                // iterator (mutable)
v.into_iter()               // consuming iterator

// HashMap
use std::collections::HashMap;
let mut m: HashMap<String, i32> = HashMap::new();
m.insert("key".to_string(), 1);
m.get("key")                // Option<&i32>
m.entry("key").or_insert(0) // get or insert
m.contains_key("key")
for (k, v) in &m { }

// HashSet
use std::collections::HashSet;
let mut s: HashSet<i32> = HashSet::new();
s.insert(1);
s.contains(&1)

// Tuple
let t = (1, "hello", 3.14);
t.0  t.1  t.2               // access by index
let (x, y, z) = t;          // destructure

// Struct
struct Point { x: i32, y: i32 }
let p = Point { x: 1, y: 2 };
let p2 = Point { x: 5, ..p };  // struct update syntax

// Enum (ADTs — algebraic data types)
enum Shape {
    Circle(f64),                        // tuple variant
    Rectangle { width: f64, height: f64 },  // struct variant
    Point,                              // unit variant
}
```

### Control Flow
```rust
// If — no parens, braces required
if x > 0 {
    println!("positive");
} else if x < 0 {
    println!("negative");
} else {
    println!("zero");
}

// If is an expression
let msg = if x > 0 { "positive" } else { "non-positive" };

// Match — exhaustive, every arm must be covered
match shape {
    Shape::Circle(r) => std::f64::consts::PI * r * r,
    Shape::Rectangle { width, height } => width * height,
    Shape::Point => 0.0,
}

// Match guards
match x {
    n if n < 0 => "negative",
    0 => "zero",
    n if n < 10 => "small",
    _ => "large",
}

// Multiple patterns
match x {
    1 | 2 | 3 => "small",
    4..=9 => "medium",
    _ => "large",
}

// if let (pattern match on one variant)
if let Some(v) = option_val {
    use(v)
}

// while let
while let Some(v) = iter.next() {
    process(v)
}

// Loop (infinite, exit with break + value)
let result = loop {
    if condition { break value; }
};

// For — iterators only (no C-style for)
for i in 0..10 { }          // 0..10 is Range
for i in 0..=10 { }         // inclusive
for item in &vec { }         // borrow
for item in vec { }          // consume
for (i, item) in vec.iter().enumerate() { }
```

### Strings & Characters
```rust
// Two string types — a fundamental Rust distinction
&str    // string slice — borrowed reference to UTF-8 data
        // "literal" is &'static str
        // immutable, may be on stack/static/heap

String  // owned string — heap-allocated, growable
        // String::from("hello") or "hello".to_string()

// Common operations on both
s.len()             // byte count (not char count for non-ASCII!)
s.chars().count()   // Unicode char count
s.is_empty()
s.contains("sub")
s.starts_with("prefix")
s.to_uppercase()
s.trim()

// String (owned) specific
let mut s = String::new();
s.push_str(" world");
s.push('!');        // single char
s + " suffix"       // consumes s!
format!("{s} {s2}") // create new String without consuming

// Interpolation via format!
let msg = format!("Hello, {name}! Score: {score:.2}");
println!("{msg}");
eprintln!("Error: {err}");  // stderr

// Raw strings
let raw = r"no \n \t escaping";
let raw = r#"can contain "quotes""#;
let raw = r##"can contain #"# inside"##;

// char (not u8! — Unicode scalar value, 4 bytes)
let c: char = 'A';
let emoji: char = '😊';    // single emoji = one char
c as u32                    // Unicode code point
char::from(65u8)            // ASCII only

// String slicing (bytes, not chars — careful with UTF-8!)
let hello = "Hello";
&hello[0..5]                // OK — valid UTF-8 boundary
// &hello[0..1]             // panic if splits a multi-byte char!
```

### Null / Option
```rust
// No null in Rust. Period.
// Use Option<T>
enum Option<T> {
    Some(T),
    None,
}

let x: Option<i32> = Some(42);
let y: Option<i32> = None;

// Unwrap — panics if None
x.unwrap()
x.expect("should have a value")

// Safe access
x.unwrap_or(0)              // default value
x.unwrap_or_else(|| compute_default())
x.unwrap_or_default()       // T::default()
x.is_some()  x.is_none()

// Transforming
x.map(|v| v * 2)            // Some(84) or None
x.filter(|v| *v > 0)
x.and_then(|v| if v > 0 { Some(v) } else { None })  // flatMap

// Pattern matching
match x {
    Some(v) => println!("{v}"),
    None => println!("nothing"),
}

if let Some(v) = x {
    println!("{v}");
}

// ? operator — propagates None (or Err) to caller
fn find_user(id: u32) -> Option<User> {
    let db = get_db()?;     // returns None if get_db() returns None
    db.find(id)
}
```

### Functions
```rust
fn add(a: i32, b: i32) -> i32 {
    a + b           // last expression is return value (no semicolon)
}

fn add(a: i32, b: i32) -> i32 {
    return a + b;   // explicit return also works
}

// Unit return (implicit if no return type)
fn print_hello() {
    println!("Hello");
}

// Closures
let double = |x: i32| x * 2;
let double = |x| x * 2;     // types inferred from context
let add = |x, y| x + y;

// Capturing
let factor = 3;
let triple = |x| x * factor;   // captures factor by reference
let triple = move |x| x * factor;  // captures by value (moved into closure)

// Trait bounds
fn print<T: Display>(x: T) { println!("{x}"); }
fn print<T: Display + Debug>(x: T) { }
fn print(x: &impl Display) { }   // impl Trait shorthand
fn print(x: &dyn Display) { }    // dynamic dispatch (fat pointer)

// Generic functions
fn first<T>(slice: &[T]) -> Option<&T> {
    slice.first()
}

// Async
async fn fetch(url: &str) -> Result<String, reqwest::Error> {
    reqwest::get(url).await?.text().await
}
```

### Error Handling
```rust
// Result<T, E> — the primary error mechanism
enum Result<T, E> {
    Ok(T),
    Err(E),
}

// Pattern match
match std::fs::read_to_string("file.txt") {
    Ok(content) => println!("{content}"),
    Err(e) => eprintln!("Error: {e}"),
}

// ? operator — propagates Err to caller (like throw but explicit)
fn read_file() -> Result<String, std::io::Error> {
    let content = std::fs::read_to_string("file.txt")?;  // returns Err if fails
    Ok(content.trim().to_string())
}

// Chaining
let result = std::fs::read_to_string("file.txt")
    .map(|s| s.to_uppercase())
    .map_err(|e| format!("failed: {e}"));

// Common error types
use std::error::Error;
fn run() -> Result<(), Box<dyn Error>> {  // any error type
    let v: i32 = "42".parse()?;
    Ok(())
}

// anyhow crate (application code)
use anyhow::{Result, Context};
fn run() -> Result<()> {
    let s = std::fs::read_to_string("file")?;
    s.parse::<i32>().context("failed to parse as int")?;
    Ok(())
}
```

---

## What Makes It Distinct

1. **Ownership = memory safety without GC** — the borrow checker proves at compile time that no use-after-free, double-free, or data race can occur. No runtime cost. This is why Rust is used in kernels, browsers, and safety-critical systems.
2. **Traits (not inheritance)** — Rust has no class hierarchy. Behavior is composed via traits. `impl Display for MyType` adds formatting. `impl Iterator for MyType` integrates with the entire ecosystem. This solves the expression problem.
3. **Affine types** — each value can be used at most once. `move` semantics enforce this. The type system enforces linearity that C++ offers only as convention (RAII).
4. **Zero-cost abstractions** — `Iterator` chains compile to the same code as hand-written loops. Generics are monomorphized (no vtable). Closures inline. "You don't pay for what you don't use."
5. **`Result` and `Option` are first-class** — the `?` operator makes error propagation ergonomic without exceptions. No unchecked exceptions, no null pointer surprises.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| cargo | Build system + package manager (excellent) |
| rustfmt | Formatter |
| clippy | Linter |
| rust-analyzer | LSP (IDE integration) |
| tokio / async-std | Async runtimes |
| serde | Serialization/deserialization |
| reqwest / axum | HTTP |
| rayon | Data parallelism |
| anyhow / thiserror | Error handling |

---

## Gotchas from C#

| C# behavior | Rust behavior | Consequence |
|-------------|---------------|-------------|
| Variables are mutable by default | Variables are **immutable** by default | Add `mut` or compiler error |
| `string` is managed, always safe | `&str` vs `String` are different types | Learn the difference early |
| `null` is nullable | No null — use `Option<T>` | Forces explicit handling |
| `foreach` borrows the collection | `for x in v` **moves** v by default | Use `for x in &v` to borrow |
| Generic `List<T>` works at runtime | Generics monomorphize — larger binary | Trade-off: performance vs size |
| `async Task<T>` runs on ThreadPool | `async fn` returns a Future — must be driven by a runtime | Choose tokio/async-std |
| `try/catch` exceptions | `Result<T,E>` + `?` operator | Different mental model but explicit |
