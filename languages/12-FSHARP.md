# Language: F#

> ML-family functional programming on .NET — algebraic types, pipeline operators, and type inference on the CLR. The C# developer's on-ramp to functional programming.

---

## Type System Snapshot

| Axis | F# |
|------|-----|
| Binding | Early (static) + .NET vtable for OOP interop |
| Typing | Static |
| Strength | Strong |
| Type system | Nominal; structural for anonymous records |
| Type inference | **Full HM** — annotate rarely |
| Memory model | GC (.NET, same as C#) |

---

## Why F# Matters to You

You know C# deeply and you know type theory from MIT TCS. F# is where those worlds meet:
- Same CLR, same libraries — zero interop friction
- ML-family type system — what you studied is the everyday language
- Algebraic data types replace class hierarchies for modeling
- Computation expressions = your known monad concept made concrete
- Pipeline operator `|>` makes data flow explicit and readable

---

## Syntax Reference Card

### Variables & Bindings
```fsharp
// let bindings — immutable by default (C# `const` semantics)
let x = 5
let name = "Alice"
let x: int = 5          // explicit annotation (rarely needed)

// Mutable (explicit opt-in — not the default)
let mutable count = 0
count <- count + 1      // <- is the mutation operator (not =)

// Unit — the F# equivalent of void
let f () = ()           // takes unit, returns unit
do printfn "side effect"

// Tuple unpacking
let (a, b) = (1, 2)
let a, b = 1, 2         // parens optional

// Pattern destructuring on let
let { X = x; Y = y } = { X = 1; Y = 2 }

// Discards
let _ = someExpression
let (_, b) = (1, 2)     // only b
```

### Equality & Comparison
```fsharp
// = for structural equality (NOT == like C#!)
1 = 1                   // true
"hello" = "hello"       // true
[1;2;3] = [1;2;3]       // true
(1,2) = (1,2)           // true

// <> for not-equal (NOT != like C#!)
1 <> 2                  // true

// Reference equality (physical equality)
open System
Object.ReferenceEquals(a, b)
// or
LanguagePrimitives.PhysicalEquality a b

// Comparison
compare 1 2             // -1 (LT)
1 < 2  1 > 2  1 <= 2  1 >= 2

// Records have structural equality by default
type Point = { X: int; Y: int }
{ X=1; Y=2 } = { X=1; Y=2 }    // true ✅ (unlike C# classes)
```

### Logical Operators
```fsharp
&&          // short-circuit AND
||          // short-circuit OR
not         // logical NOT (function, not symbol)

// Bitwise
&&&         // bitwise AND
|||         // bitwise OR
^^^         // bitwise XOR
~~~         // bitwise NOT
<<<         // left shift
>>>         // right shift
```

### Collections
```fsharp
// List — immutable linked list (like Haskell)
let lst = [1; 2; 3]         // semicolons separate elements
let lst = [1; 2; 3; 4; 5]
let lst = [1..5]             // range
let lst = [1; 3 .. 9]       // step range: [1;3;5;7;9]

// List operations
0 :: [1;2;3]                // cons — [0;1;2;3]
[1;2] @ [3;4]               // append — [1;2;3;4]
List.head [1;2;3]           // 1
List.tail [1;2;3]           // [2;3]
List.length [1;2;3]         // 3
List.map (fun x -> x*2) lst
List.filter (fun x -> x > 2) lst
List.fold (fun acc x -> acc + x) 0 lst  // fold left
List.reduce (+) lst

// Pipe operator — F#'s signature style
[1..10]
|> List.filter (fun x -> x % 2 = 0)
|> List.map (fun x -> x * x)
|> List.sum                 // 220

// Array — mutable, O(1) access
let arr = [|1; 2; 3|]      // [| ... |] syntax
arr.[0]  arr.[1..3]         // index and slice
arr.[0] <- 99               // mutation (array is mutable)

// Sequence — lazy IEnumerable (same as C# IEnumerable<T>)
let seq1 = seq { for i in 1..10 do yield i * i }
let seq1 = seq { 1..10 }
// Sequences are lazy — evaluated on demand

// Map (immutable, balanced tree)
open Microsoft.FSharp.Collections
let m = Map.ofList [("a", 1); ("b", 2)]
Map.find "a" m              // 1 (throws if missing)
Map.tryFind "a" m           // Some 1
Map.add "c" 3 m             // new map (immutable)

// Set (immutable)
let s = Set.ofList [3;1;4;1;5;9]    // {1;3;4;5;9}

// Tuple
let t = (1, "hello", true)  // :: int * string * bool
let (a, b, c) = t
fst (1, 2)                  // 1
snd (1, 2)                  // 2
```

### Control Flow
```fsharp
// If — expression (returns a value)
let result = if x > 0 then "positive" else "non-positive"

// if without else returns unit — both branches must have same type
if condition then
    printfn "yes"
// else is unit by default

// Match (F#'s pattern matching — exhaustive by default with warning)
let describe x =
    match x with
    | 0 -> "zero"
    | 1 -> "one"
    | n when n < 0 -> "negative"
    | _ -> "other"

// Active patterns (named patterns — powerful extension)
let (|Positive|Negative|Zero|) n =
    if n > 0 then Positive
    elif n < 0 then Negative
    else Zero

match n with
| Positive -> "pos"
| Negative -> "neg"
| Zero -> "zero"

// Pipeline — the idiomatic F# style
let result =
    input
    |> parse
    |> validate
    |> transform
    |> serialize

// Composition operators
let pipeline = parse >> validate >> transform    // >> left-to-right
let pipeline = serialize << transform << validate // << right-to-left

// Loops (less idiomatic than recursion/map/fold, but exist)
for i in 1..10 do
    printfn "%d" i

while condition do
    doSomething ()
```

### Algebraic Data Types
```fsharp
// Discriminated Unions (DUs) — the core modeling tool
type Shape =
    | Circle of radius: float
    | Rectangle of width: float * height: float
    | Triangle of base: float * height: float

// Pattern matching is exhaustive — compiler warns if case missing
let area shape =
    match shape with
    | Circle r -> System.Math.PI * r * r
    | Rectangle (w, h) -> w * h
    | Triangle (b, h) -> 0.5 * b * h

// Recursive DU (like a linked list)
type MyList<'a> =
    | Empty
    | Cons of head: 'a * tail: MyList<'a>

// Option (built-in DU)
type Option<'a> = Some of 'a | None

// Result (F# 4.1+)
type Result<'T, 'TError> = Ok of 'T | Error of 'TError

// Records (immutable by default)
type Person = {
    Name: string
    Age: int
}
let alice = { Name = "Alice"; Age = 30 }
let older = { alice with Age = 31 }   // non-destructive update ✅

// Anonymous records (F# 4.6+)
let point = {| X = 1; Y = 2 |}
```

### Strings & Characters
```fsharp
// string — same as C# System.String
let s = "hello"
let s = $"{name} is {age} years old"    // interpolation (F# 5+)
let s = @"verbatim \no\escape"
let s = sprintf "%s is %d years old" name age  // printf-style

// Multiline
let s = "line1\nline2"
let s = @"line1
line2"      // verbatim multiline

// char — UTF-16 code unit (like C#)
let c = 'A'
int 'A'                     // 65
char 65                     // 'A'

// String operations
s.Length
s.ToUpper()  s.ToLower()
s.Trim()
s.Contains("sub")
s.Split([|','|])
String.concat ", " ["a";"b";"c"]
```

### Null / Option
```fsharp
// Option<'T> — the right way
let x = Some 42         // :: int option
let y = None            // :: 'a option

// Pattern match
match x with
| Some v -> printfn "%d" v
| None -> printfn "nothing"

// Option module
Option.map (fun v -> v + 1) (Some 5)   // Some 6
Option.bind (fun v -> if v > 0 then Some v else None) x
Option.defaultValue 0 (Some 5)          // 5
Option.defaultValue 0 None              // 0
Option.isSome x  Option.isNone x

// Computation expression (do-notation for Option)
let result = option {
    let! x = Some 5
    let! y = Some 3
    return x + y
}   // Some 8

// Railway-oriented programming (Result)
let result = result {
    let! user = findUser id         // Error propagates
    let! validated = validate user
    return validated.Name
}

// Interop with null (C# code returns null)
let nullable: string = null         // F# allows this for .NET interop
Option.ofObj nullable               // None if null, Some s if not null
```

### Functions
```fsharp
// Auto-curried (like Haskell)
let add x y = x + y         // :: int -> int -> int
let add3 = add 3            // :: int -> int (partial application)
add3 7                      // 10

// Lambda
fun x -> x * 2
fun x y -> x + y

// Higher-order functions
let apply f x = f x
let twice f x = f (f x)
twice (fun x -> x + 1) 5   // 7

// Composition
let double = fun x -> x * 2
let addOne = fun x -> x + 1
let doubleThenAdd = double >> addOne    // compose left-to-right
doubleThenAdd 5             // 11

// Rec (recursive functions must be explicitly marked)
let rec fib n =
    if n <= 1 then n
    else fib (n-1) + fib (n-2)

// Mutually recursive
let rec isEven n = if n = 0 then true else isOdd (n-1)
and isOdd n = if n = 0 then false else isEven (n-1)

// Computation expressions (generalized monad syntax)
// async — the F# async model
let fetchAsync url = async {
    let! response = Http.getAsync url  // let! for async bind
    return response.Body
}
```

### Error Handling
```fsharp
// Exception-based (C#-compatible)
try
    let result = riskyOperation()
    Ok result
with
| :? System.IOException as e -> Error e.Message
| :? System.ArgumentException as e -> Error e.Message
| ex -> Error (ex.ToString())

// Result-based (functional style)
type Result<'T, 'E> = Ok of 'T | Error of 'E

let divide a b =
    if b = 0 then Error "division by zero"
    else Ok (a / b)

// Railway-oriented (chaining Results)
let pipeline input =
    input
    |> parseInput           // returns Result
    |> Result.bind validate // short-circuits on Error
    |> Result.map transform
    |> Result.mapError formatError

// Computation expression (result {})
let result = result {
    let! parsed = parseInput input
    let! valid = validate parsed
    return transform valid
}
```

---

## What Makes It Distinct

1. **Pipeline operator `|>`** — the signature F# idiom. Data flows left to right. `input |> parse |> validate |> serialize` reads like a sentence. C# LINQ is similar but F# `|>` works on any function.
2. **Discriminated Unions** — model your domain as algebraic data types. No more inheritance hierarchies for variants. Pattern matching is exhaustive — the compiler catches unhandled cases.
3. **Computation expressions** — generalized monadic syntax. `async { }`, `seq { }`, `result { }`, `option { }` — all the same mechanism. Write custom ones for your own effects.
4. **Structural equality by default** — records and DUs compare by value out of the box. In C#, you have to implement `IEquatable<T>` or use `record`. In F#, it's free.
5. **Same CLR** — call C# libraries directly. Use NuGet. Run on .NET. This is ML with no ecosystem tax — you get the full .NET ecosystem.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| dotnet CLI | Build and run (same as C#) |
| NuGet | Package management |
| Paket | Alternative package manager |
| FSharp.Core | Standard library |
| Ionide | VS Code extension for F# |
| Giraffe / Saturn | Web frameworks |
| Fable | F# → JavaScript compiler |
| FAKE | Build automation in F# |

---

## F# vs C# Mental Model

| Concept | C# | F# |
|---------|----|----|
| Default | Mutable | Immutable |
| Data modeling | Class hierarchy | Discriminated union + record |
| Null | null + T? | Option<'T> |
| Equality | Must implement | Structural by default |
| Code organization | Classes, interfaces | Modules, types |
| Error handling | try/catch | Result + computation expr |
| Async | async Task<T> | async { let! x = ... } |
| Polymorphism | Interface/virtual | Typeclass via interface |
| Data pipeline | LINQ method chain | |> pipeline |

---

## When to Choose F#

- Data transformation pipelines (ETL, reports)
- Domain modeling with complex variants (replacing inheritance + null)
- Type-safe DSLs (Fable for full-stack F#)
- When you want Haskell-style types but with .NET interop
- Anywhere in the .NET ecosystem where functional style is preferred
