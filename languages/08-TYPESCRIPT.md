# Language: TypeScript

> Structural types layered on JavaScript — the type system does heavy lifting at compile time, disappears at runtime. Microsoft's answer to JavaScript's type chaos.

---

## Type System Snapshot

| Axis | TypeScript |
|------|-----------|
| Binding | Late (JavaScript runtime underneath) |
| Typing | Gradual (static + escape hatch via `any`) |
| Strength | Strong when typed; `any` exits the type system |
| Type system | **Structural** (unlike C#, which is nominal) |
| Type inference | Partial — bidirectional in many contexts |
| Memory model | GC (V8, same as JS) |

---

## TypeScript Compilation Landscape

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     TYPESCRIPT COMPILATION PIPELINE                         │
│                                                                             │
│  ┌─────────────────────┐                                                    │
│  │   SOURCE  (.ts)     │  Types, interfaces, generics, decorators           │
│  │                     │  Type annotations on every binding                 │
│  │  function add(      │                                                    │
│  │    a: number,       │                                                    │
│  │    b: number        │                                                    │
│  │  ): number { ... }  │                                                    │
│  └──────────┬──────────┘                                                    │
│             │                                                               │
│             ▼                                                               │
│  ┌─────────────────────────────────────────────────────────────────────┐   │
│  │                    tsc  (TypeScript Compiler)                       │   │
│  │                                                                     │   │
│  │   Parse → Build symbol table → Type check → Emit                    │   │
│  └──────────────────────┬──────────────────────┬────────────────────────┘  │
│                         │                      │                            │
│              ┌──────────▼──────────┐  ┌────────▼────────────────────────┐  │
│              │  TYPE CHECK ERRORS  │  │  JS OUTPUT  (.js)               │  │
│              │  (compile-time only)│  │  (types fully erased)           │  │
│              │                     │  │                                 │  │
│              │  error TS2345:      │  │  function add(a, b) {           │  │
│              │  Argument of type   │  │    return a + b;                │  │
│              │  'string' is not    │  │  }                              │  │
│              │  assignable to      │  │                                 │  │
│              │  parameter of type  │  │  No type annotations.           │  │
│              │  'number'           │  │  No interfaces.                 │  │
│              │                     │  │  No generics.                   │  │
│              │  These errors do    │  │  Identical to hand-written JS.  │  │
│              │  NOT stop emit      │  │                                 │  │
│              │  by default.        │  └────────────────┬────────────────┘  │
│              └─────────────────────┘                   │                   │
│                                                        ▼                   │
│                              ┌──────────────────────────────────────────┐  │
│                              │   RUNTIME  (V8 / Node.js / browser)      │  │
│                              │                                          │  │
│                              │   Pure JavaScript. Zero type awareness.  │  │
│                              │   Types DO NOT EXIST here.               │  │
│                              │                                          │  │
│                              │   • No interface checks                  │  │
│                              │   • No generic type parameters           │  │
│                              │   • 'as T' is a no-op at runtime         │  │
│                              │   • instanceof works only for classes    │  │
│                              └──────────────────────────────────────────┘  │
└─────────────────────────────────────────────────────────────────────────────┘
```

**The central fact**: TypeScript is a compile-time lint pass over JavaScript. Everything it adds — interfaces, type aliases, generics, union types, decorators — is erased before V8 sees one byte. This is categorically different from C# generics (reified at runtime) or C# interfaces (vtable entries checked at runtime).

### Structural vs. Nominal Typing

TypeScript's type system is **structural** — compatibility is determined by shape, not by name or declaration. C# is **nominal** — you must explicitly declare that a type implements an interface.

```
C# — NOMINAL                          TypeScript — STRUCTURAL
─────────────────────────────────      ─────────────────────────────────
interface IAnimal {                    interface Animal {
    string Name { get; }                 name: string;
}                                      }

class Dog : IAnimal {           ←─ MUST DECLARE     class Dog {
    public string Name { get; set; }                  name: string;
}                                                     constructor(n: string) {
                                                        this.name = n;
class Cat {                                           }
    public string Name { get; set; }     }
}
                                       class Cat {
// Cat does NOT implement IAnimal.        name: string = "Whiskers";
// This fails to compile:              }
void Greet(IAnimal a) { }
Greet(new Cat());  // ERROR            // Cat has the right shape.
                                       // This compiles fine:
                                       function greet(a: Animal) { }
                                       greet(new Cat());  // OK [OK]
                                       greet({ name: "Rex" }); // OK [OK]
```

Any object that has the required properties — regardless of where it was defined or what it declared — satisfies the type. This is duck typing promoted to the type system level.

**Practical consequences**:

| Scenario | C# behavior | TypeScript behavior |
|----------|-------------|---------------------|
| Passing an object literal to a typed function | Must match a declared type | Shape must match — no explicit type needed |
| Two interfaces with identical shapes | Not interchangeable without explicit implementation | Fully interchangeable |
| Extra properties on an object | Checked structurally (covariance rules apply) | **Excess property check** applies at assignment sites only |
| Library type compatibility | Explicit adapter/wrapper often needed | Often "just works" if shapes align |

**The excess property check surprise** — TypeScript applies a stricter check specifically at object literal assignment sites. This catches typos but can be confusing:

```typescript
interface Point { x: number; y: number; }

// Direct assignment — excess property check fires:
const p: Point = { x: 1, y: 2, z: 3 };  // ERROR: 'z' not in Point

// Via intermediate variable — structural check only, passes:
const obj = { x: 1, y: 2, z: 3 };
const p: Point = obj;  // OK [OK] — shape is compatible

// Via function argument — excess property check fires again:
function move(p: Point) { }
move({ x: 1, y: 2, z: 3 });  // ERROR at call site

// But not if the object comes from elsewhere:
const config = getConfig();     // returns { x, y, z }
move(config);                   // OK [OK]
```

The rule: excess property checks apply when you write an object literal **directly** into a typed position. Intermediate variables bypass it. This is intentional — object literals are assumed to be "fresh" with no intended extras; variables might be wider types being narrowed.

---

## Syntax Reference Card

### Variables & Types
```typescript
let x: number = 5;
const x = 5;            // type inferred as literal: 5 (not number)
const x = 5 as number;  // widened to number
const x = [1,2,3] as const;  // readonly [1,2,3] — preserves literal types

// Type annotations
let name: string;
let count: number;
let active: boolean;
let nothing: null;
let missing: undefined;
let anything: any;      // escape hatch — opts out of type checking
let safer: unknown;     // unknown is safer — must narrow before use

// Type aliases
type ID = string;
type Point = { x: number; y: number };
type Result<T> = { ok: true; value: T } | { ok: false; error: string };

// Interfaces (prefer for object shapes that may be extended)
interface User {
    id: string;
    name: string;
    age?: number;           // optional
    readonly createdAt: Date;
}

// Enums
enum Direction { North, South, East, West }
const d: Direction = Direction.North;
// Prefer const enum or union types over enums:
type Dir = "north" | "south" | "east" | "west";
```

### Equality & Comparison
```typescript
// Same as JavaScript — use ===
x === y         // strict equality
x !== y         // strict inequality

// TypeScript adds compile-time type checking on comparisons
declare let a: string;
declare let b: number;
a === b         // TypeScript error: This comparison appears unintentional

// Type guards — TypeScript narrows types in branches
if (typeof x === "string") {
    x.toUpperCase()         // TypeScript knows x: string here
}

if (x instanceof Error) {
    x.message               // TypeScript knows x: Error here
}

// User-defined type guard
function isString(x: unknown): x is string {
    return typeof x === "string";
}

// satisfies operator (TypeScript 4.9+) — check without widening
const config = {
    port: 8080,
    host: "localhost"
} satisfies Record<string, number | string>;
config.port     // still typed as number, not number | string
```

### Logical Operators
```typescript
// Same as JavaScript
&&  ||  !  ??  ?.

// TypeScript type operators (confusingly use same symbols)
type A = { x: number } & { y: number };    // INTERSECTION type (both)
type B = string | number;                   // UNION type (either)
// These are type-level operators — no runtime equivalent
```

### Collections & Types
```typescript
// Arrays
number[]                    // array of numbers
Array<number>               // same
[number, string]            // TUPLE type — fixed length, fixed types

const arr: number[] = [1, 2, 3];
const tuple: [string, number] = ["Alice", 30];
const [name, age] = tuple;  // destructuring with type safety

// Readonly
readonly number[]           // ReadonlyArray<number>
Readonly<T>                 // makes all properties readonly
ReadonlyArray<number>

// Object types
const user: { name: string; age: number } = { name: "Alice", age: 30 };
const user = { name: "Alice", age: 30 } satisfies User;

// Record type
const scores: Record<string, number> = { alice: 95, bob: 87 };
const lookup: { [key: string]: number } = {};  // index signature

// Map and Set
const m = new Map<string, number>([["k", 1]]);
const s = new Set<number>([1, 2, 3]);
```

### Control Flow
```typescript
// Same syntax as JavaScript, but TypeScript does type narrowing in branches

// Discriminated unions — the TypeScript pattern for variants
type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "rect"; width: number; height: number };

function area(s: Shape): number {
    switch (s.kind) {
        case "circle": return Math.PI * s.radius ** 2;
        case "rect": return s.width * s.height;
        // TypeScript ensures exhaustiveness — omitting a case = error
    }
}

// Exhaustiveness check
function assertNever(x: never): never {
    throw new Error("Unhandled case: " + x);
}
```

### Type System Features
```typescript
// Union types
type StringOrNumber = string | number;
type Nullable<T> = T | null;
type Optional<T> = T | undefined;

// Intersection types
type AdminUser = User & { adminLevel: number };

// Conditional types
type NonNullable<T> = T extends null | undefined ? never : T;
type ReturnType<T extends (...args: any) => any> =
    T extends (...args: any) => infer R ? R : never;

// Mapped types
type Readonly<T> = { readonly [K in keyof T]: T[K] };
type Partial<T> = { [K in keyof T]?: T[K] };
type Pick<T, K extends keyof T> = { [P in K]: T[P] };

// Template literal types (TypeScript 4.1+)
type EventName = `on${Capitalize<string>}`;
type CSSProperty = `${string}-${string}`;
type RouteId = `${string}Id`;

// Utility types
Partial<User>               // all fields optional
Required<User>              // all fields required
Readonly<User>              // all fields readonly
Pick<User, "id" | "name">  // subset of fields
Omit<User, "password">     // all fields except
Record<string, number>      // dictionary
NonNullable<string | null>  // string
ReturnType<typeof f>        // infer function return type
Parameters<typeof f>        // infer function parameters
```

### Strings & Characters
```typescript
// Same as JavaScript — string type
const s: string = "hello";
const msg = `Hello, ${name}!`;  // template literal

// Template literal TYPES (type system only)
type Greeting = `Hello, ${string}!`;
// "Hello, Alice!" satisfies Greeting [OK]
// "Hi, Alice!" does NOT [OK]

// String narrowing
type Color = "red" | "green" | "blue";
function setColor(c: Color) { }
setColor("red")         // [OK]
setColor("purple")      // TypeScript error [OK]

// char: same as JS — no char type
```

### Null / Undefined
```typescript
// TypeScript strict null checks (tsconfig: "strictNullChecks": true)
let s: string = null;       // ERROR with strict null checks
let s: string | null = null; // [OK]

// Optional property
interface User {
    name: string;
    email?: string;     // string | undefined
}

// Non-null assertion (! suffix) — tells TypeScript "trust me, not null"
const el = document.getElementById("app")!;  // may be null at runtime

// Nullish operators
const val = x ?? "default";
const nested = obj?.prop?.nested;
obj?.method();
```

### Functions
```typescript
function add(a: number, b: number): number {
    return a + b;
}

// Optional and default parameters
function f(x: number, y?: number, z = 5) { }

// Rest parameters
function f(...args: number[]): number { }

// Function overloads
function f(x: string): string;
function f(x: number): number;
function f(x: string | number): string | number {
    return x;   // implementation must handle all overload types
}

// Generic functions
function identity<T>(x: T): T { return x; }
function first<T extends unknown[]>(arr: T): T[0] { return arr[0]; }

// Arrow functions with types
const double = (x: number): number => x * 2;
const f: (x: number) => number = x => x;

// Async
async function fetch(url: string): Promise<string> {
    const r = await fetch(url);
    return r.text();
}
```

### Error Handling
```typescript
try {
    const data = JSON.parse(input);
} catch (e: unknown) {      // TypeScript 4+: catch is 'unknown', not 'any'
    if (e instanceof Error) {
        console.error(e.message);
    } else {
        console.error(String(e));
    }
}

// Result pattern (common in TypeScript)
type Result<T, E = Error> =
    | { ok: true; value: T }
    | { ok: false; error: E };

function divide(a: number, b: number): Result<number, string> {
    if (b === 0) return { ok: false, error: "division by zero" };
    return { ok: true, value: a / b };
}

const r = divide(10, 2);
if (r.ok) { console.log(r.value); }
else { console.error(r.error); }
```

---

## What Makes It Distinct

1. **Structural typing** — two types are compatible if they have the same shape, regardless of name. `interface Foo { x: number }` and `interface Bar { x: number }` are interchangeable. Fundamentally different from C#.
2. **Types exist only at compile time** — TypeScript compiles to plain JavaScript. No runtime type information. `as T` and type guards are purely static; you can't do `typeof at runtime to check an interface`.
3. **`any` is a type system escape hatch** — unlike `unknown`, `any` turns off all checks. `unknown` forces you to narrow. Prefer `unknown` for inputs you don't control.
4. **Conditional and template literal types** — the type system is a Turing-complete computation engine (see `computing/23-PL-THEORY.md` for the proof). This enables very precise library typings.
5. **Declaration files (`.d.ts`)** — types for JavaScript libraries are distributed separately via `@types/*`. The type system is bolted onto a runtime that has no type awareness.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| tsc | TypeScript compiler |
| ts-node / tsx | Run TypeScript directly |
| vitest | Testing (TypeScript-native) |
| zod / yup | Runtime schema validation + type inference |
| trpc | Type-safe API (server → client) |
| @types/* | Type definitions for JS libraries |

---

## Gotchas from C#

| C# behavior | TypeScript behavior | Consequence |
|-------------|---------------------|-------------|
| Nominal types: `Dog != Cat` even if same shape | Structural types: same shape = same type | Different mental model |
| Runtime type checking via reflection | No runtime types — types erased | `instanceof` only works for classes |
| `interface` is a contract | `interface` describes shape, no vtable | TS interfaces work at compile time only |
| `null` is one thing | `null` and `undefined` are different | Need both: `T \| null \| undefined` |
| Generics reified at runtime | Generics erased — no `T` at runtime | Can't do `new T()` or check `is T` |
| `as` is a safe cast (throws if wrong) | `as` is a type assertion (no runtime check) | TypeScript `as` can lie |

---

## Decision Cheat Sheet

### `interface` vs `type` alias

| Use | When |
|-----|------|
| `interface` | Object shapes that will be extended or merged; public API contracts; class `implements` targets |
| `type` | Unions, intersections, mapped types, conditional types, aliases for primitives, tuples |

`interface` supports **declaration merging** — two `interface User` blocks in the same scope merge their properties. `type` aliases do not merge. This makes `interface` the right choice for library-defined shapes that consumers may need to augment (e.g., module augmentation).

`type` can express things `interface` cannot: `type ID = string`, `type Either<A,B> = A | B`, `type Keys = keyof SomeType`.

When in doubt for object shapes: `interface`. When you need type algebra: `type`.

### `any` vs `unknown` vs `never`

| Type | Meaning | When to use |
|------|---------|-------------|
| `any` | Opt out of type checking entirely | Migrating JS to TS; third-party code with no types (last resort) |
| `unknown` | A value exists but its type is unknown — must narrow before use | Function parameters from external input, `catch (e: unknown)`, JSON.parse results |
| `never` | This code path cannot be reached; this type has no values | Exhaustiveness checks (`assertNever`), function that always throws, impossible union branches |

```typescript
function handle(x: unknown) {
    x.toUpperCase();            // ERROR — must narrow first
    if (typeof x === "string") {
        x.toUpperCase();        // OK — TypeScript narrowed to string
    }
}

function handle(x: any) {
    x.toUpperCase();            // No error — TypeScript trusts you (dangerously)
}
```

`unknown` is `any` with a safety gate. Prefer it for all external inputs.

### `enum` vs `const enum` vs union literal type

| Use | When |
|-----|------|
| `enum` | Rarely — generates a runtime object; useful if you need to iterate enum members or interop with older code |
| `const enum` | Compile-time only — inlines numeric values at use sites; no runtime object; cannot be iterated; breaks with `isolatedModules` |
| Union literal type `"north" \| "south"` | Default — zero runtime cost, full type safety, works everywhere, serializes naturally as strings |

```typescript
// enum — generates runtime JS object, values are numbers
enum Dir { North, South }   // compiles to: var Dir; Dir[Dir["North"] = 0] = "North"; ...

// const enum — inlined, no runtime object
const enum Dir { North, South }  // all uses replaced with 0, 1 — no object in output

// Union literal — preferred
type Dir = "north" | "south" | "east" | "west";
// Pure compile-time. Serializes as readable strings. Works with JSON.
```

`enum` without `const` has a well-known footgun: numeric enums allow any number to be assigned without error. `Direction.North` is 0, and `const d: Direction = 42` compiles fine.

### `as` type assertion vs type guard function

| Use | When |
|-----|------|
| `as T` | You have information TypeScript does not — and you are certain. Use sparingly. |
| `x is T` type guard | Runtime check that also narrows the type in the calling scope — the safe path |

```typescript
// as — no runtime check, you take responsibility
const el = document.getElementById("my-input") as HTMLInputElement;
el.value;   // if el is actually a div, this is undefined at runtime — no error thrown

// Type guard — runtime check + type narrowing
function isHTMLInput(el: Element): el is HTMLInputElement {
    return el instanceof HTMLInputElement;
}
if (isHTMLInput(el)) {
    el.value;   // safe — runtime-verified
}
```

`as` is a lie to the compiler. It is sometimes the right lie (e.g., when parsing JSON you have validated). Type guards are always the safer alternative when you need runtime certainty.

A double assertion `x as unknown as T` is a red flag — it means you are forcing a conversion the compiler rejected even with a single cast.

### `strict` mode flags

`"strict": true` in `tsconfig.json` enables a bundle of checks. Understanding each individually:

| Flag | What it catches |
|------|----------------|
| `strictNullChecks` | `null` and `undefined` are not assignable to non-nullable types — the single most valuable flag |
| `noImplicitAny` | Variables/parameters with no type annotation that can't be inferred default to `any` — flag forces you to be explicit |
| `strictFunctionTypes` | Function parameter types are checked contravariantly — catches subtle callback type mismatches |
| `strictBindCallApply` | `.bind()`, `.call()`, `.apply()` are type-checked against the function signature |
| `strictPropertyInitialization` | Class properties must be initialized in constructor or marked `!` — catches "property used before set" |
| `noImplicitThis` | `this` in functions must have an explicit type annotation — catches the dynamic `this` footgun |
| `useUnknownInCatchVariables` | `catch (e)` is typed as `unknown` rather than `any` (TS 4.4+) |
| `alwaysStrict` | Emits `"use strict"` in JS output and parses files in strict mode |

Start with `"strict": true`. Disable individual flags only when migrating a large existing JS codebase incrementally — in that case, enable them one at a time.
