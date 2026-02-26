# JavaScript & TypeScript — A Layered Guide

## The Big Picture

JavaScript is a runtime language. TypeScript is a compile-time layer on top of it. They are not alternatives — TypeScript *becomes* JavaScript.

```
+------------------------------------------------------------------+
|                    THE JS/TS STACK                               |
|                                                                  |
|  YOU WRITE          YOU BUILD            RUNTIME EXECUTES        |
|  ----------         ----------           -----------------        |
|  TypeScript   -->   TypeScript   -->     JavaScript              |
|  (.ts, .tsx)        Compiler             (.js)                   |
|                     (tsc / esbuild                               |
|                      / babel)            +-------------------+   |
|                                          | Browser (V8/SpiderMonkey) |
|                     Strips all          | Node.js (V8)      |   |
|                     type annotations    | Deno (V8)         |   |
|                     Emits plain JS      | Bun (JavaScriptCore) |  |
|                                          +-------------------+   |
|                                                                  |
|  TypeScript types NEVER exist at runtime. They are erased.       |
+------------------------------------------------------------------+
```

**The key insight**: TypeScript is a *static analysis tool* that happens to compile. The output is plain JavaScript. If you want to check a type at runtime, you do it yourself with `typeof` or `instanceof` — TypeScript can't help you there.

<!-- @editor[audience/P1]: This file covers JS language features (destructuring, optional chaining, async/await runtime model, class syntax) and TypeScript type system internals (primitive types, utility types, generics, structural typing deep-dive) that belong in the companion language guides — languages/07-JAVASCRIPT.md and languages/08-TYPESCRIPT.md. This file's distinct value is the toolchain and module system layer: CJS vs ESM, module resolution algorithms, tsconfig settings, the compilation pipeline split between tsc and esbuild. The language-level content should be cut or heavily summarized here with a pointer to the language guides, and the toolchain content expanded (module resolution algorithm, how "moduleResolution": "Bundler" vs "NodeNext" actually differ, path alias resolution, declaration file discovery). See calibration note in CLAUDE.md for this directory. -->

---

## JavaScript: What It Actually Is

### The Language vs the Engine vs the Environment

These are three different things that people blur together:

```
  LANGUAGE SPEC (ECMAScript)
  +-------------------------------------------------+
  | Defines: syntax, semantics, built-in objects    |
  | Who sets it: TC39 committee (annual releases)   |
  | ES2015 (ES6), ES2016... ES2024, ES2025...        |
  +-------------------------------------------------+
             |
             | implemented by
             v
  ENGINE (executes the JS)
  +-------------------------------------------------+
  | V8          -- Chrome, Node.js, Deno, Edge      |
  | SpiderMonkey -- Firefox                         |
  | JavaScriptCore -- Safari, Bun                   |
  | Each engine implements the ECMAScript spec.      |
  +-------------------------------------------------+
             |
             | runs inside
             v
  ENVIRONMENT (provides the APIs)
  +-----------------------------+ +-----------------------------+
  | BROWSER                     | | NODE.JS / DENO / BUN        |
  | - window, document, DOM     | | - fs, path, os (file I/O)   |
  | - fetch, XHR                | | - http, net (servers)       |
  | - localStorage, cookies     | | - process, Buffer           |
  | - Web Workers               | | - require() / import()      |
  +-----------------------------+ +-----------------------------+

  JS the language is the same. The environment gives you different APIs.
  fetch() exists in both browser and Node 18+. DOM does not exist in Node.
```

### ECMAScript Versions — What Changed

```
  ES5 (2009)     The baseline. var, prototypes, JSON. Still everywhere.
  ES6/ES2015     The big one. let/const, arrow functions, classes,
                 Promises, modules (import/export), destructuring,
                 template literals, Map/Set, generators.
  ES2016         Array.includes(), ** exponentiation
  ES2017         async/await, Object.entries/values
  ES2018         Rest/spread, Promise.all settlement
  ES2019         Array.flat(), Object.fromEntries
  ES2020         Optional chaining (?.), nullish coalescing (??),
                 BigInt, Promise.allSettled
  ES2021         Logical assignment (&&=, ||=, ??=), Promise.any
  ES2022         Top-level await, class fields, Array.at()
  ES2023         Array.findLast(), change array (toSorted, toReversed)
  ES2024+        Promise.withResolvers, Object.groupBy, ...
```

When you see `tsconfig.json` saying `"target": "ES2020"`, that controls which of these features TypeScript compiles *down to* vs passes through.

---

## The Module Problem

This is the #1 source of confusion in the JS ecosystem. There are **two incompatible module systems** and the ecosystem is still mid-migration.

### How We Got Here

```
  ORIGINAL JAVASCRIPT (1995-2009)
  No module system at all. One big global scope.
  <script src="jquery.js"></script>  -- jQuery attaches to window.$
  <script src="app.js"></script>     -- app.js reads window.$
  Namespacing was manual: window.MyApp = window.MyApp || {}

          |
          | Node.js arrives (2009)
          v

  COMMONJS (CJS) — Node's solution
  +-----------------------------------------------+
  | const express = require('express')            |
  | const { readFile } = require('fs')            |
  |                                               |
  | module.exports = { myFunction }               |
  | module.exports.name = 'value'                 |
  +-----------------------------------------------+
  Synchronous. Works great on the server (disk is local).
  NOT the browser's native system.
  .js files in Node default to CJS.

          |
          | TC39 standardizes modules in ES2015
          v

  ES MODULES (ESM) — the standard
  +-----------------------------------------------+
  | import express from 'express'                 |
  | import { readFile } from 'fs/promises'        |
  |                                               |
  | export function myFunction() {}               |
  | export default class MyClass {}               |
  +-----------------------------------------------+
  Asynchronous. Works in browsers natively.
  Statically analyzable (bundlers can tree-shake).
  .mjs extension OR "type": "module" in package.json.
```

### CJS vs ESM — Key Differences

```
  +---------------------------+---------------------------+
  |  CommonJS (CJS)           |  ES Modules (ESM)         |
  +---------------------------+---------------------------+
  | require()                 | import                    |
  | module.exports            | export                    |
  | Synchronous               | Asynchronous              |
  | Dynamic (require anywhere)| Static (top of file)      |
  | .js (Node default)        | .mjs or "type":"module"   |
  | exports resolved at       | imports hoisted and        |
  | runtime                   | resolved before execution |
  | No tree-shaking           | Tree-shakeable            |
  | Works in Node             | Works in browser + Node   |
  +---------------------------+---------------------------+

  CJS can require() CJS.
  ESM can import ESM.
  ESM can import CJS (with limitations).
  CJS CANNOT require() ESM (synchronous vs async mismatch).
```

### The Interop Mess

```
  The problem: npm has ~3M packages. Most were written in CJS.
  ESM arrived ~2015. The ecosystem is still transitioning (~2026).

  You will encounter:
  - Pure CJS packages (most legacy)
  - Pure ESM packages (some new packages went ESM-only)
  - Dual-mode packages (ship both CJS + ESM)
  - ESM-only packages that break CJS consumers (pure-esm controversy)

  The error you'll see:
  "ERR_REQUIRE_ESM: require() of ES Module not supported"

  Solutions:
  - Switch your project to ESM ("type":"module" in package.json)
  - Use dynamic import(): const pkg = await import('esm-only-pkg')
  - Find a CJS-compatible alternative
  - Use a bundler (Vite, Webpack) which handles this for you
```

<!-- @editor[content/P2]: Module resolution algorithm is absent. The learner has compiler theory background — the resolution algorithm (how Node/bundlers locate a bare specifier like `import x from 'lodash'`) is the interesting part. The algorithm: (1) check node_modules/ starting from current dir, walking up to filesystem root; (2) find package.json "exports" field (conditional exports: "import" vs "require" vs "browser"); (3) fall back to "main" or "module" fields; (4) for relative imports, check file extension, then index files. The "exports" field is especially important — it's how dual-mode packages expose different entry points to CJS vs ESM consumers. This is the toolchain depth this file is supposed to provide. -->

---

## TypeScript

### What TypeScript Adds

TypeScript is a **strict superset** of JavaScript — all valid JS is valid TS. TypeScript adds:

```
  JAVASCRIPT                      TYPESCRIPT ADDS
  -----------                     ---------------
  function add(a, b) {            function add(a: number, b: number): number {
    return a + b                    return a + b
  }                               }

  No contract. a and b could      Compiler verifies callers pass numbers.
  be strings, objects, undefined. Type error caught before runtime.

  let user = fetchUser()          let user: User = fetchUser()
  user.nme  // typo, silent bug   user.nme  // ERROR: Property 'nme' does
                                            // not exist on type 'User'
```

TypeScript finds an entire class of bugs at *edit time* (in your IDE) and *build time* — before the code ever runs. The types are erased before execution.

### The Type System

#### Primitive Types

```typescript
  let name: string = "Alice"
  let age: number = 42          // int, float, NaN, Infinity — all number
  let active: boolean = true
  let nothing: null = null
  let missing: undefined = undefined
  let id: symbol = Symbol("id")
  let big: bigint = 9007199254740993n

  // Any — the escape hatch (avoid)
  let x: any = "could be anything"

  // Unknown — safer than any (must narrow before use)
  let input: unknown = getInput()
  if (typeof input === "string") input.toUpperCase()  // OK

  // Never — a type that can never occur
  // (unreachable code, exhaustive checks)
```

<!-- @editor[audience/P2]: The primitive types, interfaces, generics, utility types, and structural typing sections below are language guide content belonging in languages/08-TYPESCRIPT.md. The structural typing / nominal vs structural comparison is genuinely valuable for this reader (C# background), but it belongs in the TypeScript language guide. This file should either cut these sections with a pointer to 08-TYPESCRIPT.md, or keep only the structural typing bridge (since it has direct toolchain implications in how .d.ts files work) and remove the rest. -->

#### Object Types and Interfaces

```typescript
  // Inline type annotation
  let user: { name: string; age: number }

  // Interface (prefer for objects/classes)
  interface User {
    id: number
    name: string
    email?: string      // optional property
    readonly createdAt: Date  // cannot reassign after creation
  }

  // Type alias (prefer for unions, primitives, tuples)
  type UserId = number
  type Status = "active" | "inactive" | "pending"
  type Coordinate = [number, number]   // tuple

  // Interface vs type alias:
  // - interface: can be extended, merged (declaration merging)
  // - type: can express unions, intersections, more complex types
  // - For objects: either works. interface is idiomatic for public APIs.
```

#### Structural Typing — Not Nominal

This is the biggest conceptual shift from C#/.NET:

```
  C# (nominal typing):                TypeScript (structural typing):
  ------------------------            ----------------------------
  class Dog { bark() {} }             interface Canine { bark(): void }
  class Cat { bark() {} }
                                      class Dog { bark() {} }
  void Pet(Dog d) {}                  class Cat { bark() {} }

  Pet(new Cat())  // COMPILE ERROR     function pet(c: Canine) {}
  Cat is not Dog. Name matters.
                                      pet(new Dog())  // OK
                                      pet(new Cat())  // ALSO OK
                                      // Cat has bark() — it satisfies Canine.
                                      // Shape matters, not name.

  TypeScript cares about SHAPE (what properties/methods exist),
  not IDENTITY (what class something was declared as).
```

#### Unions and Intersections

```typescript
  // Union: A OR B
  type StringOrNumber = string | number
  function format(input: string | number): string {
    if (typeof input === "number") return input.toFixed(2)
    return input.trim()
  }

  // Intersection: A AND B (has all properties of both)
  type AdminUser = User & { permissions: string[] }

  // Discriminated union — the pattern for "tagged" types
  type Shape =
    | { kind: "circle"; radius: number }
    | { kind: "rect"; width: number; height: number }

  function area(s: Shape): number {
    switch (s.kind) {
      case "circle": return Math.PI * s.radius ** 2
      case "rect":   return s.width * s.height
    }
  }
  // TypeScript knows in each case branch which type s is.
```

#### Generics

Same concept as C# generics, same angle-bracket syntax:

```typescript
  // Generic function
  function first<T>(arr: T[]): T | undefined {
    return arr[0]
  }
  const n = first([1, 2, 3])   // T inferred as number
  const s = first(["a", "b"])  // T inferred as string

  // Generic interface
  interface Repository<T> {
    findById(id: number): Promise<T>
    save(item: T): Promise<void>
  }

  // Constraint: T must have an id property
  function getById<T extends { id: number }>(items: T[], id: number): T | undefined {
    return items.find(item => item.id === id)
  }
```

#### Utility Types (the built-in toolkit)

```
  Partial<T>       All properties of T made optional.
  Required<T>      All properties of T made required.
  Readonly<T>      All properties of T made readonly.
  Pick<T, K>       Only the listed keys from T.
  Omit<T, K>       T without the listed keys.
  Record<K, V>     Object with keys K and values V.
  Exclude<T, U>    From T, remove types assignable to U.
  Extract<T, U>    From T, keep types assignable to U.
  NonNullable<T>   Remove null and undefined from T.
  ReturnType<F>    The return type of a function.
  Parameters<F>    The parameter types of a function as tuple.
  Awaited<T>       Unwrap a Promise<T> to T.

  Examples:
  type UserPreview = Pick<User, "id" | "name">
  type UpdateUser = Partial<Omit<User, "id" | "createdAt">>
  type Lookup = Record<string, User>
```

---

## tsconfig.json

This file controls the TypeScript compiler. Key settings:

```json
{
  "compilerOptions": {
    // WHERE TO LOOK
    "rootDir": "./src",          // source files live here
    "outDir": "./dist",          // compiled JS goes here

    // WHAT TO TARGET
    "target": "ES2020",          // what JS version to emit
    "module": "ESNext",          // module format in output (ESNext, CommonJS)
    "moduleResolution": "Bundler", // how to resolve imports
                                  // "Bundler" = modern; "Node16" = Node

    // TYPE CHECKING STRICTNESS
    "strict": true,              // enables all strict checks (DO THIS)
    // strict: true is shorthand for:
    //   strictNullChecks         null/undefined are not assignable to other types
    //   strictFunctionTypes      stricter function parameter checking
    //   noImplicitAny            error on implicit any
    //   strictPropertyInitialization  class props must be initialized

    // LIBRARY TYPES (what globals are available)
    "lib": ["ES2020", "DOM"],    // include DOM types for browser code
                                  // omit DOM for Node-only code

    // INTEROP
    "esModuleInterop": true,     // allows default import from CJS modules
    "allowSyntheticDefaultImports": true,

    // PATHS
    "baseUrl": ".",
    "paths": {
      "@/*": ["./src/*"]         // path alias: import x from '@/utils'
    },

    // OTHER COMMON
    "declaration": true,         // emit .d.ts files alongside .js
    "sourceMap": true,           // emit .map files for debugging
    "noEmit": true               // type-check only, don't write files
                                  // (when bundler handles compilation)
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
```

### The target vs lib vs module Triangle

```
  target    What ECMAScript syntax the OUTPUT uses.
            "ES2017" -> async/await emitted as-is (supported since 2017)
            "ES5"    -> async/await compiled down to generators (verbose)

  lib       What type definitions are available for your SOURCE code.
            Affects what the type checker knows about.
            "DOM" -> window, document, fetch are typed
            "ESNext" -> latest built-ins are typed

  module    What module FORMAT the output uses.
            "CommonJS" -> require/module.exports (Node.js classic)
            "ESNext"   -> import/export (bundlers, modern Node)
            "NodeNext" -> Node.js 12+ native ESM with .js extensions

  Typical combos:
  Browser app (via bundler):  target:ES2020, lib:[ES2020,DOM], module:ESNext
  Node.js app:                target:ES2022, lib:[ES2022],     module:NodeNext
  Library (dual output):      Two tsconfig files, one per output format
```

<!-- @editor[structure/P2]: Missing a diagram showing how "moduleResolution" interacts with the module resolution algorithm. The four values ("Node", "Node16", "NodeNext", "Bundler") have meaningfully different behaviors: "Node" uses the old algorithm (ignores package.json "exports" field); "Node16"/"NodeNext" enforce ESM-compatible resolution with explicit file extensions; "Bundler" allows extensionless imports and respects "exports" but doesn't require .js extensions. A decision table or flow diagram here — pairing which moduleResolution value to use with which runtime/toolchain — is the core of what a toolchain guide for this audience should provide. -->

---

## The Compilation Pipeline

```
  SOURCE               TOOL CHAIN                    OUTPUT
  ------               ----------                    ------

  .ts / .tsx           tsc (TypeScript compiler)     .js + .d.ts + .map
                         |
                         | Type checking (slow-ish)
                         | Code transformation
                         v

  .ts / .tsx           esbuild / SWC                 .js only (no type check)
                         |
                         | Strip types, transform syntax
                         | No type checking — 10-100x faster
                         v

  .ts / .tsx           Babel + @babel/preset-typescript  .js only
                         |
                         | Strip types, transform syntax
                         | No type checking
                         v

  .js (bundled)        Vite / Webpack / Rollup       single .js bundle
  .js (multiple)       (uses esbuild/SWC internally)
```

### Why Two Steps?

```
  Many modern projects split the work:

  TYPE CHECKING          COMPILATION / BUNDLING
  -----------            ----------------------
  tsc --noEmit           esbuild / Vite / SWC
  (just checks types,    (transforms fast, no type check)
   no output)

  Run in parallel in CI:
  +-- tsc --noEmit   --> pass/fail (type errors)
  +-- vite build     --> dist/ (your app bundle)

  This is because esbuild is 10-100x faster than tsc for transformation.
  You get fast builds AND type safety — just not from the same tool.
```

### Declaration Files (.d.ts)

```
  .d.ts files are type information ONLY — no runtime code.

  When you npm install a library, you need its types.
  Three scenarios:

  1. Library ships its own types:
     package.json has "types" field pointing to a .d.ts
     e.g., TypeScript itself, Zod, Prisma

  2. Types in @types/* package:
     npm install --save-dev @types/express
     npm install --save-dev @types/node
     Maintained by DefinitelyTyped (community repo)
     ~10,000 packages covered

  3. No types available:
     Add: declare module 'that-old-package'   in a .d.ts file
     TypeScript treats it as any — no type checking.

  DefinitelyTyped is the @types/* registry.
  It's like NuGet for type stubs. Before TypeScript was popular,
  most packages didn't ship types — @types/* filled the gap.
```

---

## JavaScript Runtime Features You Use Daily

<!-- @editor[audience/P2]: The async/await, destructuring, optional chaining, and classes sections below are JavaScript language content. For this audience (MIT CS, knows async models deeply) the async/await section adds marginal value here — the Promise model is well understood conceptually. The destructuring and optional chaining sections belong in languages/07-JAVASCRIPT.md. The classes section is similarly language-guide territory. Consider replacing these with a single "see languages/07-JAVASCRIPT.md and languages/08-TYPESCRIPT.md for language-level features" pointer, and using the space for deeper toolchain content: the module graph, how bundlers handle dynamic import(), conditional exports in package.json, etc. -->

### Async / Await

```javascript
  // Promises (ES2015) — the foundation
  fetchUser(id)
    .then(user => fetchPosts(user.id))
    .then(posts => render(posts))
    .catch(err => console.error(err))

  // async/await (ES2017) — syntactic sugar over Promises
  async function loadUserPosts(id: number) {
    try {
      const user = await fetchUser(id)       // unwrap Promise<User>
      const posts = await fetchPosts(user.id) // unwrap Promise<Post[]>
      render(posts)
    } catch (err) {
      console.error(err)
    }
  }
  // Same execution model. async functions return a Promise.
  // await pauses the async function (not the thread).
  // Node.js is single-threaded — await yields the event loop.

  // Parallel fetches:
  const [user, config] = await Promise.all([fetchUser(id), fetchConfig()])
```

### Destructuring and Spread

```javascript
  // Object destructuring
  const { name, age, email = "none" } = user   // default value
  const { name: userName } = user              // rename

  // Array destructuring
  const [first, second, ...rest] = items
  const [, , third] = items                    // skip elements

  // Spread — copy/merge objects
  const updated = { ...user, age: 53 }         // shallow merge
  const combined = [...arr1, ...arr2]

  // In function params
  function greet({ name, age }: User) { }
```

### Optional Chaining and Nullish Coalescing

```javascript
  // Before (ES5 era)
  const city = user && user.address && user.address.city

  // Optional chaining (?.) — ES2020
  const city = user?.address?.city   // undefined if any step is null/undefined
  const len  = arr?.length
  const val  = obj?.method?.()       // optional method call

  // Nullish coalescing (??) — ES2020
  // Like ||, but only falls back on null/undefined (not 0, "", false)
  const name = user.name ?? "Anonymous"
  const count = result.count ?? 0

  // Compare:
  const a = "" || "default"    // "default" (empty string is falsy)
  const b = "" ?? "default"    // "" (?? only catches null/undefined)
```

### Classes

```javascript
  // ES2015 class syntax (syntactic sugar over prototypes)
  class Animal {
    #name: string              // Private field (ES2022, hard private)
    protected type: string     // TypeScript access modifier

    constructor(name: string, type: string) {
      this.#name = name
      this.type = type
    }

    get name() { return this.#name }  // getter

    speak(): string {
      return `${this.#name} makes a sound`
    }
  }

  class Dog extends Animal {
    constructor(name: string) {
      super(name, "dog")
    }

    speak(): string {             // override
      return `${this.name} barks`
    }
  }

  // TypeScript access modifiers:
  // public (default) — accessible everywhere
  // private — class only (TypeScript enforced, not JS runtime)
  // protected — class + subclasses
  // #field — JS runtime private (truly private, even at runtime)
  // readonly — assign once
```

---

## Common Confusion Points

### "TypeScript says it's fine but it crashes at runtime"

```
  TypeScript checks types at compile time against the DECLARED types.
  Runtime data (API responses, user input) is untyped.

  interface User { name: string; age: number }
  const data: User = await fetch('/api/user').then(r => r.json())
  // TypeScript trusts your assertion. If the API returns { name: null },
  // TypeScript won't catch it — the cast is yours to verify.

  Solutions:
  - Zod, Valibot — parse and validate at runtime with type inference
  - Type guards — write runtime checks that TypeScript understands
  function isUser(x: unknown): x is User {
    return typeof x === 'object' && x !== null && 'name' in x
  }
```

### "Cannot use import statement in a module" (Node.js)

```
  Node.js defaults to CommonJS. You wrote ESM syntax.

  Fix options:
  1. Rename file to .mjs
  2. Add "type": "module" to package.json
  3. Use require() instead (CJS)
  4. Use a bundler/transpiler that handles it for you
```

### "Type 'string' is not assignable to type 'never'"

```
  You narrowed a union type so much that nothing is left.
  Often seen in exhaustive switch statements or when a type
  has been overconstrained.

  type Status = "active" | "inactive"
  function handle(s: Status) {
    if (s === "active") { ... }
    if (s === "inactive") { ... }
    // here: s is type 'never' — all cases handled
    const _check: never = s  // exhaustiveness check pattern
  }
```

### "Property does not exist on type {}"

```
  You declared something as {} or object — too broad.

  const config: {} = getConfig()
  config.apiUrl  // ERROR: {} has no properties TypeScript knows about

  Fix: use a proper interface/type, or unknown with narrowing, or Record<string, unknown>
```

### "any vs unknown — what's the difference?"

```
  any       Opts out of type checking entirely.
            TypeScript won't check what you do with it.
            Use as last resort (JS migration, untyped library).

  unknown   Type-safe "I don't know yet."
            You MUST narrow before using.
            if (typeof x === 'string') x.toUpperCase()  // OK
            x.toUpperCase()  // ERROR: must narrow first

  unknown is any's safer cousin. Prefer unknown in APIs you control.
```

### "interface vs type — when to use which?"

```
  interface:
  - Best for object shapes (especially public API surfaces)
  - Supports extends (inheritance)
  - Supports declaration merging (libraries augment them)
  - Familiar to OOP developers

  type:
  - Required for unions: type Result = Success | Failure
  - Required for tuples: type Point = [number, number]
  - Better for mapped/conditional types (advanced)
  - More flexible for composition

  Rule of thumb for 80% of cases:
  - Objects/classes → interface
  - Unions/aliases/complex → type
  - Either works for simple objects — be consistent per codebase
```

---

## Old World → New World Bridge

| .NET / C# concept | JavaScript / TypeScript equivalent | Notes |
|---|---|---|
| `int`, `string`, `bool`, `double` | `number`, `string`, `boolean` | JS has one numeric type |
| `null`, `Nullable<T>` | `null`, `undefined`, `T \| null` | JS has both null AND undefined |
| `object` | `object`, `{}`, `unknown` | Avoid `{}` and `object` — use `unknown` |
| Class with access modifiers | Same syntax in TS | `private` is compile-time only unless using `#` |
| Generics `List<T>` | `Array<T>` or `T[]` | Same concept |
| `interface` (nominal) | `interface` (structural) | Shape matters in TS, not class name |
| `async Task<T>` | `async function(): Promise<T>` | Same concept, different syntax |
| `IEnumerable<T>` | `Iterable<T>`, `Generator` | Iterators/generators |
| `var` (inferred) | `const`/`let` with inference | Prefer `const`, use `let` when reassigning |
| LINQ | Array methods: `.map()`, `.filter()`, `.reduce()`, `.find()` | Chained; no lazy eval by default |
| `using` (IDisposable) | `try/finally` or `using` (stage 3 proposal, TS 5.2+) | `await using` for async resources |
| `enum` | TS `enum`, or string union `"a" \| "b"` | String unions are preferred — enums have footguns |
| `Assembly`, `.dll` | npm package, `.js` module | |
| `.csproj` | `package.json` | |
| MSBuild → `bin/Release` | `tsc` / bundler → `dist/` | |
| XML doc comments `///` | JSDoc `/** */` or just TypeScript types | TS types are the primary docs |
| NuGet `packages.lock.json` | `package-lock.json` / `pnpm-lock.yaml` | Same purpose |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Write type-safe code | TypeScript (always, for non-trivial projects) |
| Type-check only (no emit) | `tsc --noEmit` |
| Fast transpile (CI/bundler) | esbuild or SWC |
| Share types between packages | `.d.ts` declarations or shared types package |
| Type an API response | `interface` + Zod for runtime validation |
| Handle null safely | Enable `strictNullChecks` (via `strict: true`) |
| Use a library with no types | `npm install @types/<library>` |
| Represent a value that could be multiple things | Union type: `type X = A \| B` |
| Make all properties optional | `Partial<T>` |
| Pick just a few fields from a type | `Pick<T, "field1" \| "field2">` |
| Call browser APIs from TypeScript | Add `"DOM"` to `lib` in tsconfig |
| Write for Node.js | Add `@types/node`, set `lib` without DOM |
| Use import/export in Node.js | `"type": "module"` in package.json or `.mjs` |
| Import a CJS package in ESM | `esModuleInterop: true` + default import |
| Write an enum-like thing | String union type (avoid TS `enum`) |
