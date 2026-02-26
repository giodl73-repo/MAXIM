# Universal Language Cheat Sheet

> **Navigation** — This file is ~51KB / ~1,400 lines. Use your editor's symbol search or Ctrl+F on the section headers below to jump directly to a language or topic.
>
> **Part 1 — Mainstream & Enterprise** (C, C++, Java, C#, Python, JavaScript, TypeScript):
> [C](#c-1) · [C++](#c-2) · [Java](#java-1) · [C# (Home Base)](#c-home-base) · [Python](#python-1) · [JavaScript](#javascript-1) · [TypeScript](#typescript-1)
>
> **Part 2 — Systems, Functional & Specialist** (Rust, Go, Swift, Kotlin, Haskell, F#, Scala, Ruby, SQL):
> [Rust](#rust-1) · [Go](#go-1) · [Haskell](#haskell-1) · [F#](#f-1) · [Kotlin](#kotlin-1) · [Swift](#swift-1) · [Scala](#scala-1) · [Ruby](#ruby-1) · [SQL](#sql-1)
>
> **Comparison tables** (feature-first, all 16 languages): Variable Declaration · Equality · Logical/Bitwise · Delimiters · Collections · Conditionals · Strings · Null/Option · Functions · Error Handling

16 languages × 10 topics. Comparison tables first (feature-first lookup),
language quick cards second (language-first lookup).

---

## Part 1: Mainstream & Enterprise Languages

## Part A — Comparison Tables

### 1. Variable Declaration

| Language | Mutable | Immutable | Type annotation | Notes |
|----------|---------|-----------|-----------------|-------|
| C | `int x = 5;` | `const int x = 5;` | mandatory | no type inference |
| C++ | `int x = 5;` | `const int x = 5;` | `auto x = 5;` | `constexpr` = compile-time const |
| Java | `int x = 5;` | `final int x = 5;` | `var x = 5;` (Java 10+) | primitives vs boxed |
| C# | `var x = 5;` | `const int x=5;` / `readonly` | `int x = 5;` | `readonly` = runtime const |
| Python | `x = 5` | (convention: UPPER) | `x: int = 5` (hint only) | no enforcement |
| JavaScript | `let x = 5` | `const x = 5` | (no annotations) | avoid `var` |
| TypeScript | `let x: number = 5` | `const x = 5` | explicit or inferred | `as const` for literal types |
| Rust | `let mut x = 5;` | `let x = 5;` | `let x: i32 = 5;` | **immutable by default** |
| Go | `x := 5` | `const x = 5` | `var x int = 5` | `:=` short form in functions only |
| Haskell | (no mutation) | `let x = 5` | `x :: Int` | everything is a binding |
| F# | `let mutable x = 5` | `let x = 5` | `let x: int = 5` | immutable by default |
| Kotlin | `var x = 5` | `val x = 5` | `val x: Int = 5` | immutable by default idiom |
| Swift | `var x = 5` | `let x = 5` | `let x: Int = 5` | immutable by default |
| Scala | `var x = 5` | `val x = 5` | `val x: Int = 5` | prefer `val` |
| Ruby | `x = 5` | (convention: UPPER for constants) | (none; dynamic) | `$x` global, `@x` instance |
| SQL | varies by dialect | — | `DECLARE @x INT` (T-SQL) | procedural extensions only |

---

### 2. Equality & Comparison

| Language | Value equality | Reference/identity | Notes |
|----------|---------------|---------------------|-------|
| C | `==` | `==` (pointer address) | same op; pointers ARE addresses |
| C++ | `==` (overloadable) | `==` on raw pointers | `std::is_same<T,U>` for type equality |
| Java | `.equals()` | `==` | **classic trap**: `==` is ALWAYS reference for objects |
| C# | `==` / `.Equals()` | `Object.ReferenceEquals()` | `==` is overloadable; `string ==` is value |
| Python | `==` (calls `__eq__`) | `is` | `is None` not `== None` (PEP 8) |
| JavaScript | `===` | `===` | `==` coerces types — almost never use it |
| TypeScript | `===` | `===` | compiler nudges toward `===` |
| Rust | `==` (requires `PartialEq`) | `std::ptr::eq()` | no coercion ever; must derive/impl PartialEq |
| Go | `==` | `==` | works on comparable types; slices/maps cannot be `==` |
| Haskell | `==` (Eq typeclass) | (no concept — pure) | reference equality is meaningless in pure FP |
| F# | `=` | `LanguagePrimitives.PhysicalEquality` | structural by default (unlike C#) |
| Kotlin | `==` (calls `.equals()`) | `===` | `==` is null-safe structural |
| Swift | `==` (Equatable protocol) | `===` | `===` only for `AnyObject` (class references) |
| Scala | `==` (calls `.equals()`) | `eq` | `==` is null-safe; avoid `eq` |
| Ruby | `==` | `equal?` | also: `eql?` (type+value), `===` (case equality) |
| SQL | `=` | IS IDENTICAL TO (rare) | `NULL = NULL` is **false**; use `IS NULL` |

---

### 3. Logical & Bitwise Operators

| Language | AND | OR | NOT | Bitwise AND/OR | Notes |
|----------|-----|----|-----|----------------|-------|
| C | `&&` | `\|\|` | `!` | `&` / `\|` | `&`/`\|` don't short-circuit |
| C++ | `&&` | `\|\|` | `!` | `&` / `\|` | `and`/`or`/`not` keywords also valid |
| Java | `&&` | `\|\|` | `!` | `&` / `\|` | `&`/`\|` = non-short-circuit logical |
| C# | `&&` | `\|\|` | `!` | `&` / `\|` | `^` = XOR (not exponent) |
| Python | `and` | `or` | `not` | `&` / `\|` | `and`/`or` return operands, not bool |
| JavaScript | `&&` | `\|\|` | `!` | `&` / `\|` | `??` nullish coalescing; `&&` returns value |
| TypeScript | `&&` | `\|\|` | `!` | `&` / `\|` | `&` and `\|` also type operators |
| Rust | `&&` | `\|\|` | `!` | `&` / `\|` | `!` also macro invocation |
| Go | `&&` | `\|\|` | `!` | `&` / `\|` | `&^` = bit clear (AND NOT) |
| Haskell | `&&` | `\|\|` | `not` | `.&.` / `.\|.` | operators from `Data.Bits` |
| F# | `&&` | `\|\|` | `not` | `&&&` / `\|\|\|` | triple-char bitwise |
| Kotlin | `&&` | `\|\|` | `!` | `.and()` / `.or()` | bitwise = named infix functions |
| Swift | `&&` | `\|\|` | `!` | `&` / `\|` | standard |
| Scala | `&&` | `\|\|` | `!` | `&` / `\|` | standard |
| Ruby | `&&` / `and` | `\|\|` / `or` | `!` / `not` | `&` / `\|` | `and`/`or` have **lower precedence** than `&&`/`\|\|` |
| SQL | `AND` | `OR` | `NOT` | bitwise varies | keywords only; three-valued logic (NULL) |

---

### 4. Delimiter Semantics

| Language | `{ }` | `[ ]` | `( )` | `\|` |
|----------|-------|-------|-------|------|
| C | block; struct/array initializer | array subscript | grouping; call; cast | bitwise OR |
| C++ | block; aggregate init; lambda `[cap](){}` | array subscript; **lambda capture** | grouping; call; cast | bitwise OR; `std::variant` pattern |
| Java | block; array initializer | array type suffix; subscript | grouping; call; cast | bitwise OR |
| C# | block; object/collection initializer `{k,v}` | array; indexer; attribute `[Attr]` | grouping; call; cast | bitwise OR; switch arm `\| pat` |
| Python | **dict** `{"k":v}`; **set** `{v}` (not block!) | list literal; subscript; slice | grouping; call; **tuple** `(a,b)` | bitwise OR; union type `int \| str` (3.10+) |
| JavaScript | block; **object literal** `{k:v}` | array literal; subscript | grouping; call | bitwise OR |
| TypeScript | block; object literal; type `{x: T}` | array; tuple type `[T,U]`; type index `T["k"]` | grouping; call | union type `T \| U`; bitwise OR |
| Rust | block (expression!); struct literal; match arm | array literal `[1,2,3]`; slice type `&[T]`; subscript | grouping; call; **tuple** `(a,b)` | pattern OR `\| pat`; bitwise OR; closure `\|x\| x` |
| Go | block; struct/map/array/slice literal | array/slice type prefix `[]T`; subscript | grouping; call | bitwise OR |
| Haskell | explicit layout (rare); record `{field=val}` | list literal `[1,2,3]`; index `list !! i` | grouping; **tuple** `(a,b)`; call | pattern match arm `\| guard`; type `Either a b` |
| F# | record `{f=v}`; computation `{ }` | list `[1;2;3]`; array `[\|1;2;3\|]` | grouping; tuple | discriminated union case `\| Foo \| Bar` |
| Kotlin | block; lambda `{ x -> x }` | subscript | grouping; call | bitwise OR; when-arm `\| val` |
| Swift | block; closure `{ x in x }` | array literal; subscript; array type `[T]`; dict type `[K:V]` | grouping; call | bitwise OR |
| Scala | block; case body; function literal | subscript `a(i)` not `a[i]`!; type param `Array[T]` | **array subscript** `a(0)`; grouping; call; tuple | pattern match `\| pat`; bitwise OR |
| Ruby | hash `{"k"=>v}`; block `do\|x\| \|x\|` | array literal; subscript | grouping; call | block parameter `\|x\|`; bitwise OR |
| SQL | — | `ARRAY[1,2]` (PostgreSQL) | grouping; subquery | UNION (not same as `\|`) |

> **Scala trap**: `a(0)` is subscript, not `a[0]`. Square brackets are ONLY for type parameters.
> **Python trap**: `{}` is an empty dict, NOT an empty set. Empty set = `set()`.
> **C++ trap**: `[cap]` in lambdas is a capture list, not an array.

---

### 5. Collection Literals

| Language | Array / List | Map / Dict | Set | Tuple |
|----------|-------------|------------|-----|-------|
| C | `int a[]={1,2,3};` | (none built-in) | (none) | struct |
| C++ | `std::vector<int>{1,2,3}` | `std::map<K,V>{{k,v}}` | `std::set<T>{v}` | `std::make_tuple(a,b)` |
| Java | `new int[]{1,2,3}` | `Map.of(k,v)` | `Set.of(v)` | (none native) |
| C# | `new[]{1,2,3}` / `[1,2,3]` (C#12) | `new Dictionary<K,V>{{k,v}}` | `new HashSet<T>{v}` | `(a,b)` (C#7+) |
| Python | `[1, 2, 3]` | `{"k": v}` | `{1, 2, 3}` | `(1, 2, 3)` |
| JavaScript | `[1, 2, 3]` | `{"key": v}` | `new Set([v])` | (none) |
| TypeScript | `[1, 2, 3]` | `{"key": v}` | `new Set<T>([v])` | type: `[T, U]` |
| Rust | `[1,2,3]` (arr) / `vec![1,2,3]` (Vec) | `HashMap::from([(k,v)])` | `HashSet::from([v])` | `(1, 2, 3)` |
| Go | `[]int{1,2,3}` (slice) | `map[string]int{"k":1}` | (none) | (none) |
| Haskell | `[1, 2, 3]` | `Map.fromList [("k",1)]` | `Set.fromList [1,2,3]` | `(1, 2, 3)` |
| F# | `[1; 2; 3]` (list) / `[|1;2;3|]` (array) | `Map.ofList [("k",1)]` | `Set.ofList [1,2,3]` | `(1, 2, 3)` |
| Kotlin | `listOf(1,2,3)` | `mapOf("k" to 1)` | `setOf(1,2,3)` | `Pair(a,b)` |
| Swift | `[1, 2, 3]` | `["k": 1]` | `Set([1,2,3])` | `(1, 2, 3)` |
| Scala | `List(1,2,3)` / `Vector(1,2,3)` | `Map("k" -> 1)` | `Set(1,2,3)` | `(1, 2, 3)` |
| Ruby | `[1, 2, 3]` | `{"k" => v}` / `{k: v}` (sym key) | `Set.new([v])` | (none) |
| SQL | `ARRAY[1,2,3]` (PG) | (none) | (none) | `ROW(a,b)` |

---

### 6. If / Conditional / Pattern Match

| Language | If | Ternary | Pattern match / switch |
|----------|----|---------|------------------------|
| C | `if (cond) { }` | `cond ? t : f` | `switch(x) { case v: ... }` |
| C++ | `if (cond) { }` | `cond ? t : f` | `if constexpr (cond)` |
| Java | `if (cond) { }` | `cond ? t : f` | `switch(x) { case v -> ...}` (Java 14+) |
| C# | `if (cond) { }` | `cond ? t : f` | `x switch { pat => val }` |
| Python | `if cond:` | `t if cond else f` | `match x: case pat:` (3.10+) |
| JavaScript | `if (cond) { }` | `cond ? t : f` | `switch(x) { case v: }` |
| TypeScript | `if (cond) { }` | `cond ? t : f` | `switch(x)` + type narrowing |
| Rust | `if cond { }` | (if is expr: `let x = if c { a } else { b }`) | `match x { pat => expr }` |
| Go | `if cond { }` | (none — no ternary) | `switch x { case v: }` |
| Haskell | `if c then a else b` | (if is expr) | `case x of { pat -> expr }` |
| F# | `if cond then a [else b]` | (if is expr) | `match x with \| pat -> expr` |
| Kotlin | `if (cond) { }` (also expr) | `if (c) a else b` | `when(x) { v -> ... }` |
| Swift | `if cond { }` | `cond ? t : f` | `switch x { case pat: }` |
| Scala | `if (cond) a [else b]` (expr) | (if is expr) | `x match { case pat => expr }` |
| Ruby | `if cond; end` | `cond ? t : f` | `case x when pat then...end` |
| SQL | `WHERE cond` | `CASE WHEN c THEN v END` | `CASE` expression |

> **Go gotcha**: Go has no ternary operator. Write the if/else.
> **Rust**: if without else returns `()`. Both branches must be same type.
> **Haskell**: else is mandatory. Both branches must be same type (denotational consistency).

---

### 7. String & Character Rules

| Language | String type | Mutable? | Char type | Interpolation | Multiline |
|----------|-------------|----------|-----------|---------------|-----------|
| C | `char*` (null-term) | yes (array) | `char` (1 byte) | `printf("%s", s)` | `\n` escape |
| C++ | `std::string` | yes | `char` / `char32_t` | `std::format("{}", s)` | raw `R"(...)"` |
| Java | `String` | no | `char` (UTF-16 code unit) | `.formatted()` | `"""` text block (Java 15+) |
| C# | `string` | no | `char` (UTF-16 code unit) | `$"{var}"` | `@"verbatim"` / `"""` (C# 11) |
| Python | `str` | no | (no char — use 1-char string) | `f"{var}"` | `"""triple"""` |
| JavaScript | `string` | no | (no char) | `` `${var}` `` | template literal |
| TypeScript | `string` | no | (no char) | `` `${var}` `` | template literal |
| Rust | `String` (owned) / `&str` (slice) | `String` yes | `char` (4 bytes, Unicode scalar) | `format!("{var}")` | raw `r#"..."#` |
| Go | `string` (bytes, UTF-8) | no | `rune` = `int32` (code point) | `fmt.Sprintf("%s", s)` | backtick `` `raw` `` |
| Haskell | `String` = `[Char]` (use `Text`) | no | `Char` (Unicode code point) | `"Hello " ++ name` | string literal spans lines |
| F# | `string` (.NET String) | no | `char` (UTF-16 code unit) | `$"{var}"` | `@"verbatim"` |
| Kotlin | `String` | no | `Char` (UTF-16 code unit) | `"$var"` / `"${expr}"` | `"""triple"""` |
| Swift | `String` (value type!) | yes (var) | `Character` (grapheme cluster!) | `"\(var)"` | `"""multi"""` |
| Scala | `String` (Java String) | no | `Char` (UTF-16 code unit) | `s"$var"` | `"""triple"""` |
| Ruby | `String` | **yes (mutable)** | (no char type) | `"#{var}"` (double quotes only) | heredoc `<<~EOS` |
| SQL | `VARCHAR` / `TEXT` | (column) | `CHAR(n)` | concat or dialect format | multi-line literal |

> **Swift gotcha**: `Character` is an extended grapheme cluster — `"é"` is ONE Character even though it's two Unicode scalars (e + combining accent). Surprising string lengths.
> **Rust**: `&str` is the type of string literals. `String` is heap-allocated. They're different types.
> **Ruby**: Strings are mutable by default — `s << " world"` mutates in place.
> **Go**: iterating `for i, r := range s` gives runes; `s[i]` gives bytes.

---

### 8. Null / None / Option

| Language | Null literal | Nullable type | Safe access | Coalesce / default |
|----------|-------------|---------------|-------------|---------------------|
| C | `NULL` (0 cast) | `T*` (any pointer) | (manual null check) | `x ? x : default` |
| C++ | `nullptr` | `std::optional<T>` | `.value_or(default)` | `.value_or(default)` |
| Java | `null` | `Optional<T>` (not enforced) | `optional.map()` | `Optional.orElse()` |
| C# | `null` | `T?` (nullable ref, C# 8+) | `?.` | `??` |
| Python | `None` | `Optional[T]` (hint only) | (check `is None`) | `x or default` |
| JavaScript | `null` / `undefined` | `T \| null` / `T \| undefined` | `?.` | `??` |
| TypeScript | `null` / `undefined` | `T \| null` / `T?` | `?.` | `??` |
| Rust | (none — no null) | `Option<T>` = `Some(v)` / `None` | `?` operator / `.map()` | `.unwrap_or(default)` |
| Go | `nil` | pointer, interface, slice, map | (manual `if v != nil`) | (manual `if v == nil { v = def }`) |
| Haskell | (none — no null) | `Maybe a` = `Just a` / `Nothing` | `>>=` / `do` notation | `fromMaybe default` |
| F# | `None` | `'a option` = `Some v` / `None` | `Option.bind` | `Option.defaultValue default` |
| Kotlin | `null` | `T?` | `?.` | `?:` (Elvis) |
| Swift | `nil` | `Optional<T>` / `T?` | `?.` / `if let` | `??` |
| Scala | `null` (discouraged) | `Option[T]` = `Some(v)` / `None` | `.map()` / `flatMap()` | `.getOrElse(default)` |
| Ruby | `nil` | (no type system) | `&.` safe navigation | `\|\| default` |
| SQL | `NULL` | nullable column | `COALESCE(x, default)` | `COALESCE(x, default)` |

> **Rust/Haskell/F#**: null doesn't exist. The type system forces you to handle `None`/`Nothing`.
> **JavaScript**: has BOTH `null` AND `undefined`. `null` = "intentionally absent"; `undefined` = "not set".
> **C# 8+**: nullable reference types opt-in per project — `T?` is a nullable annotation, compiler warns.

---

### 9. Function Definition

| Language | Named function | Arrow / Lambda | Multi-arg curried |
|----------|---------------|----------------|-------------------|
| C | `int f(int x) { return x; }` | (function pointers only) | manual |
| C++ | `int f(int x) { return x; }` | `[=](int x) { return x; }` | `std::bind` / lambda |
| Java | `int f(int x) { return x; }` | `x -> x` (as `Function<T,R>`) | `f.andThen(g)` |
| C# | `int F(int x) => x;` | `x => x` (as `Func<T,R>`) | `Func<int,Func<int,int>>` |
| Python | `def f(x): return x` | `lambda x: x` | manual / `functools.partial` |
| JavaScript | `function f(x) { return x }` | `x => x` / `(x) => x` | manual / lodash |
| TypeScript | `function f(x: T): R { }` | `(x: T): R => expr` | manual |
| Rust | `fn f(x: i32) -> i32 { x }` | `\|x\| x` / `move \|x\| x` | manual / combinators |
| Go | `func f(x int) int { return x }` | `func(x int) int { return x }` | manual |
| Haskell | `f x = x` | `\x -> x` | **auto-curried** (all functions) |
| F# | `let f x = x` | `fun x -> x` | **auto-curried** (all functions) |
| Kotlin | `fun f(x: Int): Int = x` | `{ x: Int -> x }` | manual / Arrow-kt |
| Swift | `func f(x: Int) -> Int { x }` | `{ (x: Int) -> Int in x }` / `{ $0 }` | manual |
| Scala | `def f(x: Int): Int = x` | `(x: Int) => x` / `x => x` | manual or curried `def f(x)(y)` |
| Ruby | `def f(x); x; end` | `lambda {\|x\| x}` / `->(x){ x }` | manual / curry |
| SQL | `CREATE FUNCTION f(x T) RETURNS T` | (none) | (none) |

> **Haskell/F#**: ALL functions are curried. `f a b` is really `(f a) b`. Partial application is free.
> **Rust closures**: `\|x\| x` captures by reference; `move \|x\| x` captures by value.
> **Swift**: external parameter labels — `func f(label param: T)` — called as `f(label: value)`.

---

### 10. Error Handling

| Language | Primary mechanism | Catch / handle | Notes |
|----------|------------------|----------------|-------|
| C | Return code + `errno` | `if (ret < 0) { }` | no exceptions; UB on some errors |
| C++ | Exceptions | `try { } catch (T& e) { }` | zero-cost model (no throw = no cost) |
| Java | Checked exceptions | `try { } catch (E e) { }` | checked must be declared in `throws` |
| C# | Exceptions (unchecked) | `try { } catch (E e) { }` | no checked exceptions (unlike Java) |
| Python | Exceptions (EAFP style) | `try: except E as e:` | exceptions are objects |
| JavaScript | Exceptions | `try { } catch (e) { }` | `e` is `unknown` shape |
| TypeScript | Exceptions | `try { } catch (e) { }` | `e` is `unknown` type — narrow before using |
| Rust | `Result<T, E>` + `?` | `match result { Ok(v) => \| Err(e) => }` | no exceptions; `?` propagates |
| Go | Multiple return values | `if err != nil { }` | explicit; no exceptions |
| Haskell | `Either e a` / `Maybe a` / `IO` exceptions | `case result of Left e -> \| Right v ->` | pure code can't throw |
| F# | Exceptions + `Result` type | `try with \| :? ExnType as e ->` | both styles coexist |
| Kotlin | Exceptions (unchecked) | `try { } catch (e: E) { }` | no checked exceptions (unlike Java) |
| Swift | `throws` / `Result` | `do { try f() } catch E { }` | checked at call site |
| Scala | `Try[T]` / `Either` / exceptions | `Try(expr)` / `match { case Failure(e) =>}` | multiple styles; prefer `Either` in FP |
| Ruby | Exceptions | `begin; rescue E => e; end` | `raise`/`rescue` not throw/catch |
| SQL | (n/a in standard) | `BEGIN...EXCEPTION` (PL/pgSQL) | varies by dialect |

---

## Part B — Language Quick Cards

Format: all 10 topics in one compact block per language.

---

### C

```
BINDING  early (always)     TYPING  static, weak
MEMORY   manual (malloc/free)        NULL    NULL (0 cast to void*)

DECLARE  int x = 5;         CONST   const int x = 5;
EQUAL    == (value/ptr)     ID-EQ   == (same addr for ptrs)
NOT-EQ   !=                 COMPARE < > <= >=
LOGICAL  && || !            BITWISE & | ^ ~ << >>

ARRAY    int a[]={1,2,3};   STRUCT  struct Point {int x,y;};
PTR      int *p = &x;       CAST    (int) x

IF       if (cond) { }      TERNARY cond ? t : f
SWITCH   switch(x){case v: break;}

STRING   char* / char[]     CHAR    char (1 byte)
INTERP   printf("%s", s)    MULTI   escape \n

NULL     NULL               CHECK   if (p != NULL) {}

FUNC     int f(int x) { return x; }
LAMBDA   (none — use fn pointers)
ERROR    return code; errno
```

---

### C++

```
BINDING  early + vtable (virtual)   TYPING  static, weak-ish
MEMORY   RAII + manual              NULL    nullptr

DECLARE  int x = 5;  auto x = 5;   CONST   const int x = 5; constexpr
EQUAL    == (overloadable)          ID-EQ   == on raw pointers
NOT-EQ   !=                         COMPARE < > <= >= <=>  (spaceship C++20)
LOGICAL  && || !     (also: and or not)    BITWISE & | ^ ~ << >>

ARRAY    std::array<int,3>{1,2,3}   VECTOR  std::vector<int>{1,2,3}
MAP      std::map<K,V>{{k,v}}       SET     std::set<T>{v}
TUPLE    std::make_tuple(a,b)       PAIR    std::make_pair(a,b)

IF       if (cond) { }              TERNARY cond ? t : f
IF-INIT  if (auto p = f(); p) { }  CONSTIF if constexpr (cond) { }

STRING   std::string                CHAR    char / char32_t
INTERP   std::format("{}", x)  (C++20)     RAW    R"(raw string)"
LITERAL  "hello"s  (std::string literal)

NULL     nullptr                    OPTIONAL std::optional<T>

FUNC     int f(int x) { return x; }
LAMBDA   [=](int x) { return x; }  CLOSURE [&](int x){ }
GENERIC  template<typename T> T f(T x) { return x; }
ERROR    exceptions  try{} catch(std::exception& e){}
         or: std::expected<T,E>  (C++23)
```

---

### Java

```
BINDING  late (virtual default)     TYPING  static, strong, nominal
MEMORY   GC (G1GC default)          NULL    null  (reference types only)

DECLARE  int x = 5;  var x = 5;     FINAL   final int x = 5;
EQUAL    .equals()  (objects)        ID-EQ   ==  ← classic Java trap
NULL-EQ  Objects.equals(a, b)        COMPARE Comparable.compareTo()
LOGICAL  && || !                     BITWISE & | ^ ~ << >> >>>

ARRAY    new int[]{1,2,3}            LIST    List.of(1,2,3)
MAP      Map.of(k,v)                 SET     Set.of(v)
MUTABLE  new ArrayList<>()           MAP-MUT new HashMap<>()
TUPLE    (none built-in)             RECORD  record Point(int x, int y) {}

IF       if (cond) { }               TERNARY cond ? t : f
SWITCH   switch(x) { case v -> val } (Java 14+)
PATTERN  if (x instanceof Foo f) {}  (Java 16+)

STRING   String  (immutable, interned)   CHAR  char (UTF-16 code unit)
INTERP   String.format("%s", v) / "%s".formatted(v)
BLOCK    """text block"""  (Java 15+)    MULTI  """..."""

NULL     null                        OPTIONAL  Optional<T>
OPT      Optional.of(v) / .empty()   MAP-NULL  optional.map(f).orElse(def)

FUNC     int f(int x) { return x; }
LAMBDA   x -> x  (Function<T,R>)    BI-FUNC  (a,b) -> a+b
GENERIC  <T> T f(T x) { return x; }
ERROR    try { } catch (IOException e) { }  // checked = must declare in throws
         RuntimeException = unchecked
```

---

### C# (Home Base)

```
BINDING  early (non-virtual default)  TYPING  static, strong, nominal
MEMORY   GC (.NET generational)       NULL    null / null literal

DECLARE  var x = 5;  int x = 5;      CONST   const int x = 5;
IMMUT-F  readonly int x = 5;         RECORD  record Point(int X, int Y);
EQUAL    ==  (overloadable; string == is value)
ID-EQ    Object.ReferenceEquals(a, b)
NOT-EQ   !=                           COMPARE IComparable.CompareTo()
LOGICAL  && || !                      BITWISE & | ^ ~ << >>

ARRAY    new[] {1,2,3}  or  [1,2,3]  (C# 12)
LIST     new List<int>{1,2,3}  or  [1,2,3]
DICT     new Dictionary<K,V> { {k,v} }  or  new() { [k]=v }
SET      new HashSet<T> { v }
TUPLE    (a, b)  (ValueTuple)  or  Tuple.Create(a,b)

IF       if (cond) { }                TERNARY cond ? t : f
SWITCH   x switch { pat => val, _ => def }
PATTERN  x is int n && n > 0
NULL-COA ??                           NULL-PROP ?.

STRING   string  (immutable, System.String)  CHAR  char (UTF-16)
INTERP   $"{var}"  $"{expr:format}"   VERBATIM @"no\escape"
RAW      """raw string"""  (C# 11)   BUILDER  StringBuilder

NULL     null                         NULLABLE T?  (C# 8+ nullable refs)
OPTION   T?  on value types = Nullable<T>

FUNC     int F(int x) => x;           LAMBDA  x => x  (Func<T,R>)
LOCAL-FN static int Local(int x) => x; GENERIC T F<T>(T x) => x;
ASYNC    async Task<T> F() { return await ... ; }
ERROR    try { } catch (Exception e) { }
         no checked exceptions
```

---

### Python

```
BINDING  late (always — __dict__ lookup)  TYPING  dynamic, strong
MEMORY   reference counted + cycle GC     NULL    None

DECLARE  x = 5                        HINT    x: int = 5  (mypy only)
CONST    X = 5  (UPPER convention)    UNPACK  a, b = 1, 2

EQUAL    ==  (calls __eq__)           ID-EQ   is  (is None — always use is for None)
NOT-EQ   !=                           NOT-ID  is not
COMPARE  < > <= >=  (chaining: 1<x<10 works!)
LOGICAL  and  or  not                 BITWISE & | ^ ~ << >>

LIST     [1, 2, 3]                    DICT    {"k": v}
TUPLE    (1, 2, 3)  or  1,2,3        SET     {1, 2, 3}   (not {}: that's dict!)
EMPTY    []  {}  ()  set()            COMP    [x*2 for x in lst if x>0]

IF       if cond:  (no parens, colon)  TERNARY  t if cond else f
ELIF     elif cond:                    MATCH   match x:  case pat:  (3.10+)

STRING   str  (immutable, Unicode)    CHAR    (no char — 1-char str)
INTERP   f"{var}"  f"{expr!r}"        MULTI   """triple"""
BYTES    b"bytes"  (different type)   RAW     r"\no\escape"

NULL     None                         CHECK   if x is None:
OPTIONAL Optional[T]  (type hint)     DEFAULT x if x is not None else default

FUNC     def f(x): return x           LAMBDA  lambda x: x
ARGS     def f(*args, **kwargs)        DECO    @decorator
ASYNC    async def f(): return await g()
ERROR    try:  except ValueError as e:  else:  finally:
         raise ValueError("msg")
```

---

### JavaScript

```
BINDING  late (prototype chain)       TYPING  dynamic, weak
MEMORY   GC (V8 mark-sweep)           NULL    null / undefined

DECLARE  let x = 5                    CONST   const x = 5
AVOID    var x = 5  (function-scoped, hoisted — don't use)

EQUAL    ===  (strict: value + type)  COERCE  ==  (type coercion — avoid)
ID-EQ    ===  (for objects: reference)   NAN  Number.isNaN(x)  (NaN !== NaN!)
Object.is(a,b)  (handles NaN and -0 correctly)
NOT-EQ   !==  (strict)
LOGICAL  && || !                      NULL-CO ?? (nullish coalescing)
OPTIONAL ?.  (optional chaining)      BITWISE & | ^ ~ << >> >>>

ARRAY    [1, 2, 3]                    OBJECT  { key: val, "k2": val }
MAP      new Map([[k,v]])             SET     new Set([v])
SPREAD   [...arr]  {...obj}           DESTRUCT const {a,b} = obj; const [x,y] = arr;

IF       if (cond) { }                TERNARY cond ? t : f
SWITCH   switch(x) { case v: break; }  (fall-through by default!)
NULLISH  x ?? default                 SHORT-C cond && expr

STRING   string  (immutable)          CHAR    (no char — indexing gives string)
TEMPLATE `Hello ${name}!`             MULTI   `multi
line`
ESCAPE   \n \t \\ \`

NULL     null  (intentional absence)  UNDEF   undefined  (not set / missing)
CHECK    x == null  (catches both null and undefined)
SAFE     x?.prop  x?.method()

FUNC     function f(x) { return x }  ARROW  const f = x => x
ANON     x => x  or  (x, y) => x+y   IIFE   (() => { ... })()
ASYNC    async function f() { return await g() }
DESTRUCT function f({a, b}) { }
ERROR    try { } catch (e) { }  // e is untyped
         throw new Error("msg")
```

---

### TypeScript

```
BINDING  late (same as JS)            TYPING  static (structural), gradual
MEMORY   GC (same as JS)              NULL    null / undefined

DECLARE  let x: number = 5           CONST   const x = 5  (inferred)
AS-CONST const x = [1,2] as const    ASSERT  x as Type  (type assertion)

EQUAL    ===                          same as JS — TypeScript adds type narrowing
NOT-EQ   !==
LOGICAL  && || !  ??  ?.             BITWISE & | ^ ~ (also type operators: T & U, T | U)

ARRAY    number[]  or  Array<number>  TUPLE   [T, U]  type annotation
OBJECT   { key: string; val: number } RECORD  Record<K, V>
MAP      Map<K,V>  /  {[k:K]: V}     SET     Set<T>

IF       if (cond) { }                NARROW  if (typeof x === "string") { /* x: string */ }
GUARD    function isString(x): x is string { }
SWITCH   switch(x) { case v: }
SATISFY  x satisfies T  (C# "is" analogue, doesn't widen)

TYPE     type Alias = T | U          INTERFACE interface I { prop: T }
UNION    string | number             INTERSECT A & B
LITERAL  "foo" | "bar"               TEMPLATE `${string}Id`
CONDITIONAL T extends U ? A : B     MAPPED   { [K in keyof T]: F<T[K]> }
GENERIC  function f<T>(x: T): T { return x; }

STRING / CHAR: same as JavaScript
NULL     null / undefined            NULLABLE T | null   T | undefined   T?
COALESCE ??                          CHAIN   ?.

FUNC     function f(x: T): R { }    ARROW   (x: T): R => expr
OVERLOAD function f(x: string): string;  function f(x: number): number;
ERROR    try { } catch (e: unknown) { if (e instanceof Error) ... }
```

---

## Part 2: Systems, Functional & Specialist Languages

---

### Rust

```
BINDING  early (static) + dyn (late)   TYPING  static, strong, nominal
MEMORY   ownership (no GC)             NULL    (none — use Option<T>)

DECLARE  let x = 5;  (immutable)       MUT     let mut x = 5;
TYPE     let x: i32 = 5;               CONST   const X: i32 = 5;
STATIC   static X: i32 = 5;           SHADOW  let x = 5; let x = x + 1; (rebind)

EQUAL    ==  (requires PartialEq trait) ID-EQ  std::ptr::eq(a, b)
NOT-EQ   !=                             COMPARE PartialOrd: < > <= >=
LOGICAL  && || !                        BITWISE & | ^ ! << >>

ARRAY    [1, 2, 3]  (fixed-size)        VEC     vec![1, 2, 3]
SLICE    &[1, 2, 3]  (reference)        HASH    HashMap::from([("k", 1)])
TUPLE    (1, 2, 3)   access: t.0 t.1   STRUCT  struct Point { x: i32, y: i32 }
ENUM     enum Dir { North, South, East(i32) }

IF       if cond { }  (no parens — compiler warns)   IF-EXPR let x = if c { a } else { b };
IF-LET   if let Some(v) = opt { }      WHILE-L while let Some(v) = iter.next() { }
MATCH    match x { pat => expr, _ => default }
GUARD    match x { n if n > 0 => ..., }

STRING   &str  (borrowed slice, stack/static)   STRING  String  (owned, heap)
LITERAL  "hello"  is &str               OWN    String::from("hello")  or  "hello".to_string()
INTERP   format!("{x}")  format!("{x:.2}")    RAW    r#"no \escape"#
CHAR     char  (4 bytes — Unicode scalar value, NOT byte)
BYTE     b'A'  = u8 = 65

NULL     (no null)                      OPTION  Option<T> = Some(v) | None
UNWRAP   opt.unwrap()  (panic if None)  SAFE    opt.unwrap_or(default)
CHAIN    opt.map(|v| v+1).unwrap_or(0)  PROP   result?  (propagate Err/None)

FUNC     fn f(x: i32) -> i32 { x }    SHORT  fn f(x: i32) -> i32 { return x; }
CLOSURE  |x| x                          MOVE   move |x| x  (captures by value)
TRAIT    trait Foo { fn bar(&self); }   IMPL   impl Foo for MyType { }
GENERIC  fn f<T: Display>(x: T) { println!("{x}"); }
ASYNC    async fn f() -> i32 { ... }   AWAIT  let v = future.await;
ERROR    Result<T, E> = Ok(v) | Err(e)
         fn f() -> Result<T, Box<dyn Error>> { let v = might_fail()?; Ok(v) }
```

---

### Go

```
BINDING  early + interface dispatch     TYPING  static, strong, structural (interfaces)
MEMORY   GC (tricolor concurrent)       NULL    nil

DECLARE  x := 5  (short, inside func)  VAR    var x int = 5
CONST    const x = 5                   ZERO   var x int  (zero value = 0)
MULTI    x, y := 1, 2                  BLANK  _ , err := f()

EQUAL    ==  (comparable types)         NO-SLICE  slices cannot use ==  (use reflect.DeepEqual)
NOT-EQ   !=                             COMPARE  < > <= >=
LOGICAL  && || !                        BITWISE & | ^ &^ << >>  (&^ = AND-NOT)

SLICE    []int{1, 2, 3}                MAKE    make([]int, len, cap)
MAP      map[string]int{"k": 1}        MAKE-M  make(map[string]int)
STRUCT   type Point struct { X, Y int }  INIT  Point{X:1, Y:2}
CHANNEL  make(chan int, 10)             GOROUT  go f()  (launch goroutine)

IF       if cond { }  (no parens, braces required)
IF-INIT  if err := f(); err != nil { return err }
SWITCH   switch x { case v: }  (no fallthrough by default!)
TYPE-SW  switch v := x.(type) { case int: ... case string: ... }
FOR      for i := 0; i < n; i++ { }    RANGE  for i, v := range slice { }
FOREVER  for { }  (no while — use for)

STRING   string  (immutable, UTF-8 bytes)   RUNE  rune = int32 = Unicode code point
BYTE     byte = uint8                        RAW   `raw string literal`
INTERP   fmt.Sprintf("%s %d", s, n)         CONV  string([]byte{...})  []byte(s)

NULL     nil                            PTR-NULL  var p *int = nil
CHECK    if v == nil { }

FUNC     func f(x int) int { return x }  MULTI  func f() (int, error) { return 1, nil }
CLOSURE  func(x int) int { return x }   METHOD func (r Recv) Method(x int) int { }
INTERFACE type Stringer interface { String() string }  // implicit satisfaction
GOROUTINE go func() { ch <- compute() }()
ERROR    if err != nil { return fmt.Errorf("wrap: %w", err) }
         errors.Is(err, target)  errors.As(err, &target)
```

---

### Haskell

```
BINDING  early (+ typeclass dictionary dispatch)   TYPING  static, strong, nominal, HM
MEMORY   GC (generational, GHC)                   NULL    (none — use Maybe)

BINDING  let x = 5  (top-level: x = 5)            TYPE    x :: Int; x = 5
IMMUTABLE everything — no mutation (in pure code)
SHADOW   let x = 5; let x = x + 1  (new binding, not mutation)

EQUAL    ==  (Eq typeclass)           NEQ     /=
NOT-EQ   /=                           COMPARE Ord: compare, < > <= >=
LOGICAL  &&  ||  not                  BITWISE Data.Bits: .&. .|. xor complement

LIST     [1, 2, 3]  (linked list — O(n) access)
ARRAY    Data.Array  or  Data.Vector  (not built-in literal)
TUPLE    (1, 2, 3)   fst/snd for pairs
MAP      Data.Map.fromList [("k",1)]  (immutable balanced tree)
SET      Data.Set.fromList [1,2,3]

IF       if cond then a else b  (expression — else mandatory)
CASE     case x of { Just v -> v; Nothing -> 0 }
GUARD    f x | x > 0 = "pos" | otherwise = "non-pos"
PATTERN  f [] = 0; f (x:xs) = 1 + f xs  (pattern matching on definition)

STRING   String = [Char]  (linked list of Char — use Data.Text for real work)
TEXT     Data.Text  (packed UTF-16)   BYTESTR Data.ByteString
CHAR     Char  (Unicode code point)   LITERAL 'a' for Char, "s" for String
CONCAT   "hello" ++ " " ++ name       SHOW    show 42  = "42"

NULL     (no null)                    MAYBE   Maybe a = Just a | Nothing
FUNCTOR  fmap f (Just v) = Just (f v)  BIND  mx >>= \v -> f v
DO       do { v <- mx; f v }          FROM-M  fromMaybe 0 (Just 5)

FUNC     f x = x                      ANON    \x -> x
CURRY    f x y = x + y   (all functions auto-curry)
PARTIAL  add3 = f 3      (partial application)
COMPOSE  g . f  (right-to-left)        APP    f $ x  (right-assoc application)
TYPECLASS class Eq a where { (==) :: a -> a -> Bool }
INSTANCE  instance Eq MyType where { (==) = ... }
MONAD    do { x <- getLine; putStrLn x }
ERROR    error "msg"  (impure)  Maybe / Either for pure error handling
         catch in IO; throwIO for async exceptions
```

---

### F#

```
BINDING  early (+ method dispatch for .NET)   TYPING  static, strong, HM inference
MEMORY   GC (.NET)                            NULL    None (option) / null for .NET interop

LET      let x = 5                 MUTABLE   let mutable x = 5
TYPE     let x: int = 5            UNIT      ()  (the single value of type unit)

EQUAL    =  (structural by default)   REF-EQ  LanguagePrimitives.PhysicalEquality
NOT-EQ   <>  (not !=!)                COMPARE < > <= >=
LOGICAL  &&  ||  not                  BITWISE &&&  |||  ^^^  ~~~  <<<  >>>

LIST     [1; 2; 3]  (immutable linked list)   ARRAY  [|1; 2; 3|]
SEQ      seq { 1..10 }  (lazy IEnumerable)    MAP    Map.ofList [("k",1)]
TUPLE    (1, 2, 3)                            RECORD type Point = { X: int; Y: int }
DU       type Shape = Circle of float | Rect of float * float

IF       if cond then a [else b]  (expression)
MATCH    match x with | pattern -> expr | _ -> default
GUARD    match x with | n when n > 0 -> "pos" | _ -> "other"
PIPE     x |> f |> g |> h  (left-to-right composition — F#'s signature style)

STRING   string (.NET String)             CHAR   char
INTERP   $"{var}"                         VERB   @"verbatim\no\escape"
CONCAT   "a" + "b"  or  sprintf "%s" v    MULTI  @"multi
line" or verbatim

OPTION   option<'T> = Some v | None         NONE  None
BIND     opt |> Option.map (fun v -> v+1)   DEFAULT  Option.defaultValue 0 opt
RAILWAY  Result<'T,'E> for error chaining

FUNC     let f x = x                       ANON  fun x -> x
CURRY    let add x y = x + y  (auto-curried)  PARTIAL  let add3 = add 3
COMPOSE  f >> g  (left-to-right)               APP   f <| x  (right-assoc)
COMP-EXP computation { let! x = async; return x }
ASYNC    async { let! x = asyncF(); return x }
ERROR    try f() with | :? IOException as e -> ...
         Result type: Ok v / Error e
```

---

### Kotlin

```
BINDING  late (virtual default, like Java)    TYPING  static, strong, nominal
MEMORY   GC (JVM)                             NULL    null  (T? for nullable)

VAL      val x = 5  (immutable)               VAR    var x = 5
TYPE     val x: Int = 5                        CONST  const val X = 5  (compile-time)
DATA     data class Point(val x: Int, val y: Int)

EQUAL    ==  (structural, null-safe, calls .equals())
REF-EQ   ===  (reference equality)
NOT-EQ   !=                                   COMPARE Comparable; < > <= >=
LOGICAL  && || !                               BITWISE .and() .or() .xor() .inv()  (named)

LIST     listOf(1,2,3)  (immutable)           MUT-L  mutableListOf(1,2,3)
ARRAY    arrayOf(1,2,3)  or  IntArray(3){i->i}
MAP      mapOf("k" to 1)                      MUT-M  mutableMapOf("k" to 1)
SET      setOf(1,2,3)                         PAIR   1 to "one"  (infix to)
RANGE    1..10  (inclusive)  1 until 10  (exclusive)

IF       if (cond) { }  (also expression)     TERNARY  val x = if (c) a else b
WHEN     when(x) { v -> expr; else -> default }  (replaces switch)
NULL-CHK x?.prop  x?.method()                 ELVIS  x ?: default
SMART-C  if (x != null) { x.method() }  (smart cast)
NOT-NULL x!!  (throws NullPointerException if null)

STRING   String  (immutable)                  CHAR   Char  (UTF-16 code unit)
INTERP   "$var"  "${expr}"                    MULTI  """triple quoted"""
TRIM     """  ...  """.trimIndent()

NULL     null                                 NULLABLE  T?
SAFE     x?.let { ... }  x?.run { ... }
CAST     x as T  (throws); x as? T  (returns T?)

FUNC     fun f(x: Int): Int = x              LAMBDA  { x: Int -> x }
EXTFUN   fun String.shout() = this.uppercase()
INLINE   inline fun f(block: () -> Unit) { block() }
SUSPEND  suspend fun f(): T { ... }  (coroutine)
COROUT   launch { val v = withContext(IO) { fetch() } }
ERROR    try { } catch (e: IOException) { }  (unchecked, unlike Java)
         sealed class Result<T>  or  runCatching { }
```

---

### Swift

```
BINDING  early + protocol witness tables (dispatch)   TYPING  static, strong, nominal
MEMORY   ARC (reference counting, compiler-inserted)  NULL    nil

LET      let x = 5  (immutable)               VAR    var x = 5
TYPE     let x: Int = 5                        CONST  (let at module scope)

EQUAL    ==  (requires Equatable protocol)     REF-EQ  ===  (AnyObject only — classes)
NOT-EQ   !=                                    COMPARE Comparable: < > <= >=
LOGICAL  && || !                                BITWISE & | ^ ~ << >>

ARRAY    [1, 2, 3]  (value type!)              DICT   ["k": v]
SET      Set([1,2,3])  or  Set<Int>()          TUPLE  (1, 2, 3)
RANGE    1...10  (closed)  1..<10  (half-open)
OPTARR   [T?]  (array of optionals)

IF       if cond { }  (no parens)              TERNARY  cond ? t : f
IF-LET   if let v = opt { use(v) }            GUARD   guard let v = opt else { return }
SWITCH   switch x { case pat: expr }           (no fallthrough by default)
WHERE    for v in arr where v > 0 { }

STRING   String  (value type, Unicode-correct)  CHAR   Character (grapheme cluster!)
INTERP   "\(var)"  "\(expr)"                    MULTI  """multi"""
RAW      #"raw \(no interp)"#  (raw string)

NULL     nil                                    OPTIONAL  T?  =  Optional<T>
UNWRAP   opt!  (force — crash if nil)           SAFE     opt?.prop
COALESCE opt ?? default                         BIND    opt.map { $0 + 1 }
FLATMAP  opt.flatMap { f($0) }

FUNC     func f(x: Int) -> Int { x }           LABEL  func f(label param: Int) -> Int
CALLED   f(label: 5)  (external label required by default)
CLOSURE  { (x: Int) -> Int in x }  or  { $0 }  (shorthand)
GENERIC  func f<T: Equatable>(_ x: T) -> T { x }
PROTOCOL protocol Foo { func bar() }           EXTENS  extension Int: Foo { }
ASYNC    func f() async -> T { await asyncWork() }
ERROR    func f() throws -> T { }              CATCH  do { try f() } catch { }
         Result<T, E> for value-based error
```

---

### Scala

```
BINDING  late (virtual default)               TYPING  static, strong, nominal
MEMORY   GC (JVM)                             NULL    null (discouraged); use Option

VAL      val x = 5  (immutable)               VAR    var x = 5
TYPE     val x: Int = 5                        LAZY   lazy val x = expensive()
CASE     case class Point(x: Int, y: Int)     OBJECT object Singleton { }

EQUAL    ==  (null-safe, calls .equals())      REF-EQ  eq  (reference)
NOT-EQ   !=                                    COMPARE Ordered: < > <= >=
LOGICAL  && || !                                BITWISE & | ^ ~ << >>

LIST     List(1,2,3)  (immutable linked)       VECTOR  Vector(1,2,3)  (immutable indexed)
ARRAY    Array(1,2,3)  (mutable)               MAP     Map("k" -> 1)
SET      Set(1,2,3)                            TUPLE   (1, 2, 3)   access: t._1 t._2
RANGE    1 to 10  (inclusive)  1 until 10  (exclusive)
SUBSCR   a(0)  NOT a[0]!  (parens for indexing)

IF       if (cond) a [else b]  (expression)    TERNARY (if is expression)
MATCH    x match { case pat => expr; case _ => default }
GUARD    case n if n > 0 => ...
FOR-COMP for { x <- list; if x > 0 } yield x*2

STRING   String  (Java String)                 CHAR   Char
INTERP   s"$var ${expr}"                       RAW    raw"$not_interp"
MULTI    """triple"""                           STRIP  """...""".stripMargin

NULL     null  (exists but avoid)              OPTION  Option[T] = Some(v) | None
MAP-OPT  opt.map(_ + 1)                        GET-OR  opt.getOrElse(0)
EITHER   Either[E, A] = Left(e) | Right(a)    FLATM  opt.flatMap(f)

FUNC     def f(x: Int): Int = x               ANON   (x: Int) => x
CURRIED  def f(x: Int)(y: Int): Int = x+y     PARTIAL f(3)(_)
COMPOSE  g compose f  or  f andThen g         HIGHER  def f[T](x: T): T = x
TRAIT    trait Foo { def bar(): Int }          GIVEN   given Foo with { def bar() = 0 }  (Scala 3)
ERROR    try { } catch { case e: IOException => }
         Try(expr)  Either  ZIO for FP error handling
```

---

### Ruby

```
BINDING  late (always — method lookup via ancestor chain)   TYPING  dynamic, strong
MEMORY   GC (incremental mark-sweep)                        NULL    nil

ASSIGN   x = 5                                 MULTI   a, b = 1, 2
LOCAL    x = 5    (lowercase/underscore)        GLOBAL  $x = 5
INST     @x = 5   (in class)                   CLASS   @@x = 5  (class variable)
CONST    X = 5    (UPPER — mutable by default, warning)

EQUAL    ==  (value, overridable)              ID-EQ   equal?  (same object)
EQL      eql?  (type + value)                  CASE    ===  (case equality, overridable)
NOT-EQ   !=                                    COMPARE <=> (spaceship: -1/0/1)
LOGICAL  && || !   also:  and or not  (lower precedence)
BITWISE  & | ^ ~ << >>

ARRAY    [1, 2, 3]  (mutable)                  HASH    {"k" => v}  or  {k: v} (symbol)
RANGE    (1..10)  (inclusive)  (1...10)  (exclusive)
SYMBOL   :foo  (immutable identifier, like string)

IF       if cond; expr; end    or   expr if cond  (postfix)
UNLESS   unless cond; expr; end  (negated if)
TERNARY  cond ? t : f
CASE     case x when pat then; when pat2 then; else; end
LOOP     loop do; end   while cond do; end   until cond do; end

STRING   String  (MUTABLE)                     CHAR   (no char — 1-char string)
DOUBLE   "interp #{var}"  (double quotes interpolate)
SINGLE   'no #{interp}'   (single quotes do NOT interpolate)
HEREDOC  <<~EOS ... EOS   (stripped heredoc)
CONCAT   "a" + "b"  or   "a" << "b"  (mutates!)

NULL     nil  (object of NilClass)             CHECK   x.nil?  or  if x.nil?
SAFE     x&.method  (safe navigation)          DEFAULT x || default

FUNC     def f(x); x; end                     BLOCK   f { |x| x }  or  f do |x| x end
LAMBDA   lambda { |x| x }  or  ->(x) { x }   PROC    proc { |x| x }
METHOD   def f(x, y=5, *rest, key:, **opts)   SYMBOL  method(:f)
CLASS    class Foo < Bar; def m; end; end      MODULE  module M; end
OPEN     class String; def shout; upcase; end; end  (monkey-patching!)
ERROR    begin; rescue E => e; ensure; end
         raise E.new("msg")
```

---

### SQL

```
PARADIGM declarative; set-based; relational algebra
BINDING  (not applicable — query optimizer decides)
TYPES    static (schema-defined); strong within query

TYPES    INT  BIGINT  DECIMAL(p,s)  FLOAT  BOOLEAN  VARCHAR(n)  TEXT  DATE  TIMESTAMP  UUID
NULL     NULL  (three-valued logic: TRUE / FALSE / UNKNOWN)
         NULL = NULL  →  UNKNOWN  (use IS NULL, not = NULL)

EQUAL    =  (not ==)                          NOT-EQ  <>  or  !=
COMPARE  < > <= >=                            NULL-EQ IS NULL  /  IS NOT NULL
LOGICAL  AND  OR  NOT                         IN      x IN (1,2,3)
BETWEEN  x BETWEEN 1 AND 10  (inclusive)      LIKE    s LIKE 'foo%'
COALESCE COALESCE(x, default)                 NULL-IF NULLIF(x, 0)  (returns NULL if equal)

QUERY    SELECT cols FROM table WHERE cond GROUP BY col HAVING cond ORDER BY col LIMIT n
JOIN     INNER JOIN  /  LEFT JOIN  /  RIGHT JOIN  /  FULL JOIN  /  CROSS JOIN
SUBQ     SELECT * FROM (SELECT ...) sub
CTE      WITH cte AS (SELECT ...) SELECT * FROM cte
WINDOW   ROW_NUMBER() OVER (PARTITION BY x ORDER BY y)
UNION    UNION ALL  (keep dupes)  UNION  (dedupe)

INSERT   INSERT INTO t (cols) VALUES (vals)   MULTI   INSERT INTO t SELECT ...
UPDATE   UPDATE t SET col=val WHERE cond
DELETE   DELETE FROM t WHERE cond             UPSERT  INSERT ... ON CONFLICT DO UPDATE

TYPE-C   CAST(x AS INT)  or  x::INT  (PostgreSQL)
CASE     CASE WHEN cond THEN v WHEN cond2 THEN v2 ELSE default END
STRING   UPPER(s)  LOWER(s)  LENGTH(s)  SUBSTRING(s, start, len)  TRIM(s)
CONCAT   s1 || s2  (ANSI)  or  CONCAT(s1, s2)  (MySQL/SQL Server)
DATE     NOW()  CURRENT_DATE  DATEADD  DATEDIFF  (dialect varies!)
AGGR     COUNT(*)  SUM(x)  AVG(x)  MAX(x)  MIN(x)  STRING_AGG(x, ',')

INDEX    CREATE INDEX idx ON t(col)
EXPLAIN  EXPLAIN (ANALYZE, BUFFERS) SELECT ...  (PostgreSQL)

TRANS    BEGIN;  COMMIT;  ROLLBACK;
ISOLATION READ COMMITTED (default) / REPEATABLE READ / SERIALIZABLE
```
