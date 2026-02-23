# Language: JavaScript

> The web's assembly language — designed in 10 days, evolved into a general-purpose runtime. Dynamic, weakly typed, prototype-based OOP, event-loop concurrency.

---

## Type System Snapshot

| Axis | JavaScript |
|------|-----------|
| Binding | Late — prototype chain lookup at runtime |
| Typing | Dynamic |
| Strength | **Weak** — implicit type coercions everywhere |
| Type system | Duck typing |
| Type inference | None at runtime |
| Memory model | GC (V8: incremental mark-sweep + compaction) |

---

## Syntax Reference Card

### Variables & Types
```javascript
let x = 5;              // block-scoped, mutable
const x = 5;            // block-scoped, immutable binding (object internals mutable)
var x = 5;              // function-scoped, hoisted — avoid in modern JS

// Primitives (immutable, passed by value)
undefined               // not set
null                    // intentional absence
boolean: true, false
number: 64-bit IEEE 754 (no int/float split)
bigint: 9007199254740991n  (suffix n)
string: "hello" 'hello' `hello`
symbol: Symbol("desc")  // unique identifier

// Objects (mutable, passed by reference)
typeof x                // "number", "string", "boolean", "undefined", "object", "function"
typeof null             // "object" ← famous JS bug

// Destructuring
const { name, age } = user;
const { name: userName } = user;    // rename
const [first, second, ...rest] = arr;
const { a = 5 } = obj;             // with default

// Spread / rest
const merged = { ...obj1, ...obj2 };
const arr2 = [...arr1, newItem];
```

### Equality & Comparison
```javascript
// === (strict equality) — checks value AND type — always use this
1 === 1         // true
"1" === 1       // false (different types)
null === undefined  // false

// == (loose equality) — TYPE COERCING — almost never use
"1" == 1        // true (coerced!)
null == undefined  // true (special case)
false == 0      // true
"" == false     // true
// The coercion rules are non-obvious — just use ===

// Object.is — handles NaN and -0 correctly
Object.is(NaN, NaN)     // true (=== returns false for NaN)
Object.is(0, -0)        // false (=== returns true for -0)

// Reference equality
{} === {}       // false (different objects)
const a = {}; const b = a;
a === b         // true (same reference)

// null/undefined checks
x == null       // true if x is null OR undefined (intentional == usage)
x === null      // true only if null
x === undefined // true only if undefined
x != null       // true if x is neither null nor undefined

// NaN
NaN === NaN     // false! (the famous NaN bug)
Number.isNaN(x) // correct check
isNaN("abc")    // true (coerces first — avoid)
```

### Logical Operators
```javascript
&&      // AND (returns left if falsy, right if truthy — not always bool!)
||      // OR  (returns left if truthy, right if falsy — not always bool!)
!       // NOT (always returns bool)
??      // Nullish coalescing — returns right only if left is null/undefined
?.      // Optional chaining — short-circuits on null/undefined

// Bitwise
&   |   ^   ~   <<   >>   >>>   // >>> = unsigned right shift

// Short-circuit idioms
const name = user?.name ?? "Anonymous";     // safe chain + default
user && user.activate();                    // safe call (older style)
obj.prop ||= "default";                    // assign if falsy
obj.prop ??= "default";                    // assign if nullish

// Falsy values: false, 0, -0, 0n, "", null, undefined, NaN
// ?? vs || : ?? only triggers on null/undefined (not 0 or "")
const count = value ?? 0;   // 0 stays 0 (value is null/undefined triggers)
const count = value || 0;   // 0 becomes 0 (false-y 0 triggers!)
```

### Collections
```javascript
// Array — ordered, dynamic, heterogeneous
const arr = [1, 2, 3];
arr.push(4);                    // add to end
arr.pop();                      // remove from end
arr.unshift(0);                 // add to start
arr.shift();                    // remove from start
arr.includes(2)                 // true
arr.indexOf(2)                  // 1 (-1 if not found)
arr.slice(1, 3)                 // [2, 3] (non-mutating)
arr.splice(1, 1)                // mutates — removes 1 element at index 1
arr.map(x => x * 2)
arr.filter(x => x > 1)
arr.reduce((acc, x) => acc + x, 0)
arr.find(x => x > 1)            // first match or undefined
arr.findIndex(x => x > 1)
arr.some(x => x > 5)
arr.every(x => x > 0)
arr.flat()  arr.flatMap(f)
[...arr].sort((a, b) => a - b)  // sort (mutates! spread to avoid)

// Object — key/value pairs (prototype-based)
const obj = { name: "Alice", age: 30 };
obj.name  obj["name"]           // access
"name" in obj                   // membership
delete obj.name                 // delete
Object.keys(obj)                // ["name", "age"]
Object.values(obj)              // ["Alice", 30]
Object.entries(obj)             // [["name","Alice"], ["age",30]]
Object.assign({}, obj1, obj2)   // shallow merge
{ ...obj1, ...obj2 }            // spread merge (preferred)

// Map — proper hash map (keys can be anything)
const m = new Map([["k", 1], ["k2", 2]]);
m.set("k3", 3)
m.get("k")
m.has("k")
m.delete("k")
m.size
for (const [k, v] of m) { }

// Set — unique values
const s = new Set([1, 2, 3, 2]);  // {1, 2, 3}
s.add(4)  s.has(2)  s.delete(2)   s.size
```

### Control Flow
```javascript
if (cond) { } else if (cond2) { } else { }

// Ternary
const max = a > b ? a : b;

// Switch (fall-through by default!)
switch (x) {
    case 1:
        break;
    case 2:
    case 3:     // intentional fall-through
        break;
    default:
        break;
}

// Optional chaining — short-circuits
user?.address?.city         // undefined if any is null/undefined
arr?.[0]                    // safe array access
fn?.()                      // safe function call

// Nullish coalescing
const val = maybeNull ?? "default";

// Loops
for (let i = 0; i < n; i++) { }
for (const item of arr) { }         // values
for (const key in obj) { }          // keys (prototype chain included — careful!)
arr.forEach((item, index) => { });

// No do-while needed in practice (exists though)
```

### Strings & Characters
```javascript
// Template literals (backtick)
const msg = `Hello, ${name}! You have ${count} messages.`;
const multiline = `line one
line two`;
const tagged = html`<div>${content}</div>`;    // tagged templates

// Regular strings
"hello" + " " + "world"    // concatenation
`${"hello"}`               // embed in template literal

// String methods
s.length
s.toUpperCase()  s.toLowerCase()
s.trim()  s.trimStart()  s.trimEnd()
s.includes("sub")
s.startsWith("prefix")
s.endsWith("suffix")
s.indexOf("sub")           // -1 if not found
s.replace("old", "new")    // replaces first
s.replaceAll("old", "new") // replaces all
s.split(",")               // array of strings
s.slice(1, 3)              // substring (negative indices work!)
s.padStart(10, "0")        // "0000000042"
s.repeat(3)
s.at(-1)                   // last character (ES2022)

// No char type — indexing returns string
s[0]                       // "h" (string, length 1)
```

### Null / Undefined
```javascript
null        // intentional absence — you set this
undefined   // not yet set — JS sets this

// Both are falsy
// Use == null to check for either:
x == null               // true if x is null OR undefined ← idiomatic

// Optional chaining
user?.profile?.avatar ?? "/default.jpg"

// Nullish assignment
obj.val ??= computeDefault();   // only if null/undefined

// Spread to avoid null
const safe = obj ?? {};
```

### Functions
```javascript
// Function declaration (hoisted)
function add(a, b) { return a + b; }

// Function expression
const add = function(a, b) { return a + b; };

// Arrow function (no own this, no arguments object)
const add = (a, b) => a + b;           // implicit return for single expression
const double = x => x * 2;            // parens optional for single param
const getObj = () => ({ key: val });   // return object: wrap in parens

// Default parameters
function f(x, y = 5) { }

// Rest parameters
function f(...args) { }

// Destructuring parameters
function f({ name, age = 0 }) { }

// Async/await
async function fetch(url) {
    const response = await fetch(url);
    return response.json();
}

// Generators
function* gen() {
    yield 1;
    yield 2;
}

// this context — arrow functions capture lexical this
class Timer {
    start() {
        setTimeout(() => this.tick(), 1000);  // ✅ arrow captures this
        setTimeout(function() { this.tick(); }, 1000);  // ❌ this is undefined
    }
}
```

### Error Handling
```javascript
try {
    JSON.parse("{bad json}");
} catch (e) {
    // e is untyped — check before using
    if (e instanceof SyntaxError) {
        console.error("parse error:", e.message);
    }
    throw e;    // re-throw
} finally {
    cleanup();
}

// Custom errors
class AppError extends Error {
    constructor(message, code) {
        super(message);
        this.name = "AppError";
        this.code = code;
    }
}

// Async error handling
async function main() {
    try {
        const data = await fetchData();
    } catch (e) {
        console.error(e);
    }
}
// Unhandled promise rejections crash in Node.js
process.on("unhandledRejection", (reason) => { ... });
```

---

## What Makes It Distinct

1. **Prototype chain** — objects inherit from other objects directly (no class hierarchy at runtime). `class` syntax in ES6+ is syntactic sugar over prototype chains.
2. **Event loop** — single-threaded, non-blocking I/O via event loop + microtask queue + macrotask queue. Blocking the event loop blocks everything.
3. **`this` is dynamic** — in regular functions, `this` depends on *how* the function is called (not *where* it's defined). Arrow functions fix this by capturing lexical `this`.
4. **Type coercion** — `==` and many operators coerce types. `[] + {}` = "[object Object]". `{} + []` = 0 (because `{}` is parsed as a block). Just use `===`.
5. **Everything is an object** (almost) — including functions (`typeof f === "function"` but also `f instanceof Object`). Functions have `.call()`, `.apply()`, `.bind()`.

---

## Ecosystem

| Tool | Purpose |
|------|---------|
| Node.js / Deno / Bun | Runtime |
| npm / yarn / pnpm | Package management |
| Express / Fastify / Hono | Web frameworks |
| React / Vue / Svelte | UI frameworks |
| Jest / Vitest | Testing |
| Webpack / Vite / esbuild | Bundlers |

---

## Gotchas from C#

| C# behavior | JavaScript behavior | Consequence |
|-------------|---------------------|-------------|
| `==` is value equality (for strings) | `==` coerces types | Use `===` always |
| `null` — one null | Two: `null` AND `undefined` | Check with `== null` |
| No automatic type coercions | `"5" - 3 = 2` | Arithmetic coercions are quiet |
| `Dictionary<K,V>` has only string-compatible keys | `{}` keys are strings/symbols; use `Map` for anything else | Object keys coerce to string |
| Non-virtual methods are stable | `this` can change based on call site | Arrow functions or `.bind(this)` |
| Integer division: `5/2 = 2` | `5/2 = 2.5` (one number type) | Use `Math.floor(5/2)` for int division |
