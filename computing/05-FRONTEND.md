# Frontend Frameworks — A Layered Guide

## The Big Picture

Frontend frameworks solve one problem: **keeping the UI in sync with data**. Without them, you write imperative DOM manipulation. With them, you declare what the UI *should look like* and the framework figures out how to get there.

```
                  FRONTEND FRAMEWORK LANDSCAPE

  THE PROBLEM:  Data changes → UI must update
  THE SOLUTION: Declare UI as a function of state

  +------------+  +------------+  +------------+  +----------+
  |   REACT    |  |    VUE     |  |  ANGULAR   |  |  SVELTE  |
  +------------+  +------------+  +------------+  +----------+
  | Virtual    |  | Reactive   |  | Zone.js    |  | Compile- |
  | DOM diffing|  | system     |  | change     |  | time     |
  | (runtime)  |  | (runtime)  |  | detection  |  | (no VDOM)|
  +------------+  +------------+  +------------+  +----------+
  | ~46% usage |  | ~18% usage |  | ~17% usage |  | ~6% usage|
  | Meta/Vercel|  | Evan You   |  | Google     |  | Rich     |
  |            |  |            |  |            |  | Harris   |
  +------------+  +------------+  +------------+  +----------+

  ECOSYSTEM LAYER (built on top of frameworks):
  React: Next.js, Remix, Gatsby, Expo (React Native)
  Vue:   Nuxt.js
  Angular: Angular itself (full framework, no separate meta)
```

**Which one matters most**: React has ~46% market share and dominates hiring, libraries, and job descriptions in 2026. This guide covers all four but goes deepest on React. Angular is the most familiar to .NET developers — if you're evaluating enterprise choices, Angular is worth understanding in full.

---

## Why Frameworks Exist — The DOM Problem

### Imperative DOM Manipulation (the old way)

```html
  <!-- HTML -->
  <div id="count">0</div>
  <button id="btn">Increment</button>

  <script>
    let count = 0
    document.getElementById('btn').addEventListener('click', () => {
      count++
      document.getElementById('count').textContent = count  // manual sync
    })
  </script>
```

This works for one counter. Now scale to a real app: hundreds of UI elements, data flowing in from APIs, multiple components sharing state, conditional rendering, lists that update. You're writing the *synchronization logic* manually for every relationship between data and UI. This is the WinForms/Windows Forms model — you manipulate controls imperatively.

### Declarative UI (the framework way)

```jsx
  // React
  function Counter() {
    const [count, setCount] = useState(0)

    return (
      <div>
        <div>{count}</div>
        <button onClick={() => setCount(count + 1)}>Increment</button>
      </div>
    )
  }
```

You declare *what* the UI looks like for a given state. The framework handles *how* to update the DOM when state changes. You never touch the DOM directly.

**The mental model**: `UI = f(state)`. Give the framework a function from state to UI. When state changes, it calls your function again and reconciles the result with what's on screen.

---

## The Component Model

Every framework uses components. A component is the fundamental unit of UI composition.

```
  COMPONENT = Data In + UI Out + Local State + Events Out

  +------------------------------------------+
  |              <UserCard>                  |
  |  Props (inputs):                         |
  |    name: "Alice"                         |
  |    avatarUrl: "..."                      |
  |    role: "Admin"                         |
  |                                          |
  |  Local State:                            |
  |    isExpanded: false                     |
  |                                          |
  |  Renders:                                |
  |    <div class="card">                    |
  |      <img src={avatarUrl} />             |
  |      <h2>{name}</h2>                     |
  |      <span>{role}</span>                 |
  |      {isExpanded && <Details />}         |
  |    </div>                                |
  |                                          |
  |  Events Out (callbacks via props):       |
  |    onSelect: () => void                  |
  +------------------------------------------+

  Compose them into trees:
  <App>
    <Header />
    <Sidebar>
      <NavItem />
      <NavItem />
    </Sidebar>
    <Main>
      <UserCard name="Alice" />
      <UserCard name="Bob" />
    </Main>
  </App>
```

**Bridge to .NET**: A component is analogous to a UserControl in WinForms/WPF. Props are like control properties. Events out are like control events. The composition tree is the visual tree. The difference: components re-render automatically when their data changes — no explicit Invalidate() or DataBind() calls.

---

## React

### JSX — Not HTML

JSX is a syntax extension that lets you write HTML-like markup inside JavaScript. It compiles to function calls — there's no HTML parser involved.

```jsx
  // What you write (JSX):
  const element = <h1 className="title">Hello {name}</h1>

  // What it compiles to (React.createElement):
  const element = React.createElement("h1", { className: "title" }, "Hello ", name)

  // Key differences from HTML:
  class      → className         (class is a reserved word in JS)
  for        → htmlFor           (for is a reserved word in JS)
  onclick    → onClick           (camelCase events)
  style=""   → style={{}}        (object, not string)
  <!-- -->   → {/* comment */}   (JS comment syntax)
  self-close → required          (<img /> not <img>)
```

JSX is not required (you can call `React.createElement` directly) but nobody does that. Babel/esbuild transform JSX to function calls at build time.

### The Virtual DOM and Reconciliation

The virtual DOM is the mechanism that makes `UI = f(state)` practical. Without it, re-running the render function on every state change would mean rebuilding the entire DOM — expensive because real DOM mutations trigger layout, paint, and composite passes in the browser engine. React inserts a diffing layer between your render function and the real DOM.

```
  VIRTUAL DOM: A LIGHTWEIGHT JS OBJECT TREE

  Your component function returns JSX:
  <div className="card">
    <h2>Alice</h2>
    <p>alice@example.com</p>
  </div>

  JSX compiles to React.createElement() calls, producing a plain JS object tree:
  {
    type: 'div', props: { className: 'card' },
    children: [
      { type: 'h2', props: {}, children: ['Alice'] },
      { type: 'p',  props: {}, children: ['alice@example.com'] }
    ]
  }

  This object tree is the virtual DOM — a cheap in-memory description
  of what the real DOM should look like. Creating it is ~10x cheaper
  than touching the real DOM.
```

**Reconciliation — the diff algorithm**:

```
  State changes → React re-runs your component function → new vdom tree

  PREVIOUS VDOM             NEW VDOM                REAL DOM ACTION
  ─────────────             ────────                ───────────────
  <div.card>                <div.card>              no change (same element)
    <h2>Alice</h2>            <h2>Alice</h2>        no change
    <p>alice@ex.com</p>       <p>bob@ex.com</p>     update text node only

  React walks both trees in parallel (O(n) — one pass).
  Only the changed node gets a real DOM mutation.
```

**The two reconciliation heuristics** (what makes it O(n) instead of O(n³)):

```
  HEURISTIC 1: Element type at same position

  <div> → <div>    Same type. React updates props. Keeps DOM node.
  <div> → <span>   Different type. React TEARS DOWN the entire
                   subtree and rebuilds from scratch.
                   This is why swapping a component for a different
                   one causes all child state to reset.

  HEURISTIC 2: Keys for list items

  Without keys:          With keys:
  [A, B, C]              [A(k=1), B(k=2), C(k=3)]
  [A, B, C, D]           [A(k=1), B(k=2), C(k=3), D(k=4)]

  React compares by      React matches by key.
  position. Adding D     New key=4 added at end.
  at end is fine.        Key identifies identity
                         across re-renders.

  [A, B, C]    →  [X, A, B, C] (prepend X)
  Without key: React thinks position 0 changed A→X, 1 changed B→A, etc.
               Destroys and recreates all 4 DOM nodes.
  With key:    React sees key=X new, keys 1/2/3 moved.
               Creates 1 new node, moves 3 existing nodes.
```

**The full pipeline for a state change**:

```
  setState() called
        |
        v
  ┌─────────────────────────────────────────────────────────┐
  │ RENDER PHASE (pure, no side effects)                    │
  │  Component function re-runs → new vdom tree             │
  │  React diffs new tree vs previous (reconciliation)      │
  │  Produces a list of DOM mutations needed                │
  └─────────────────────────────────────────────────────────┘
        |
        v
  ┌─────────────────────────────────────────────────────────┐
  │ COMMIT PHASE (applies changes to real DOM)              │
  │  React applies only the mutations computed in render    │
  │  Runs useLayoutEffect (synchronous, after DOM update)   │
  │  Runs useEffect (asynchronous, after browser paint)     │
  └─────────────────────────────────────────────────────────┘
        |
        v
  Browser paints the updated pixels
```

**Why immutability is required**: React detects changes by reference equality (`===`). If you mutate an object in place, the reference is the same — React sees no change, skips reconciliation, no re-render. `setUser({ ...user, name: "New" })` creates a new reference, React sees a change, reconciliation runs.

```
  REACT'S RENDERING MODEL

  State change (setState called)
         |
         v
  +------------------+
  | Component fn     |
  | re-executes      |
  +------------------+
  Re-runs to produce new JSX tree
         |
         v
  +------------------+     +------------------+
  | New Virtual DOM  |     | Previous Virtual |
  | (JS object tree) |     | DOM (in memory)  |
  +------------------+     +------------------+

  Diff: new vs previous virtual DOM
         |
         v  (reconciliation)
  +------------------+
  | Minimal DOM      |
  | patch applied    |
  +------------------+
  Only changed nodes updated (~10x cheaper than full re-render).

  Re-renders propagate DOWN the tree.
  A parent re-rendering always re-renders its children (unless memoized).
  State change in a leaf component re-renders only that leaf.
```

### When Does React Re-render?

```
  A component re-renders when:
  1. Its own state changes (useState setter called)
  2. Its parent re-renders (even if props didn't change — unless React.memo)
  3. A context it consumes changes (useContext)

  Implications:
  - State high in the tree → expensive (many children re-render)
  - State near the leaf → cheap (only that component re-renders)
  - React.memo() wraps a component: skip re-render if props are shallowly equal
  - useMemo() / useCallback() prevent new references on every render
    (new reference = React thinks prop changed even if value is same)
```

**Re-render cascade — the performance implication**:

```
  COMPONENT TREE                 STATE CHANGES AT <B>

         <A>                            <A>         ← does NOT re-render
         / \                            / \           (state change is in B,
        /   \                          /   \           not A)
      <B>   <E>                      <B>*  <E>     ← <B> re-renders (owns state)
      / \                            / \           ← <E> does NOT re-render
    <C> <D>                        <C>* <D>*      ← <C> and <D> re-render
                                                    (children of B, no memo)

  Default React behavior: parent re-renders → ALL children re-render.
  Even if <C>'s and <D>'s props did not change.

  WITH React.memo:

         <A>
         / \
       <B>   <E>
       / \
  memo(<C>)  <D>

  State changes at <B>:
  <B> re-renders. React checks <C>'s props — shallow equal? Yes → SKIP.
  <D> re-renders (no memo).

  This is the motivation for React.memo, useMemo, useCallback:
  ┌────────────────────────────────────────────────────────────┐
  │ React.memo(Component)  — skip re-render if props unchanged │
  │ useMemo(fn, deps)      — skip re-computation if deps same  │
  │ useCallback(fn, deps)  — stable function reference         │
  │                          (new function ref = React.memo    │
  │                           sees a "changed" prop and        │
  │                           re-renders anyway)               │
  └────────────────────────────────────────────────────────────┘

  Rule: put state as low in the tree as possible.
  State at root → everything re-renders on every change.
  State in a leaf → only that leaf re-renders.
```

### Functional Components

The modern way to write React (since hooks in 2019). Class components still exist but new code should always use functions.

```tsx
  // A complete, real-world component
  interface User {
    id: number
    name: string
    email: string
  }

  interface UserCardProps {
    user: User
    onSelect: (id: number) => void
    isHighlighted?: boolean        // optional prop
  }

  function UserCard({ user, onSelect, isHighlighted = false }: UserCardProps) {
    return (
      <div
        className={`card ${isHighlighted ? 'card--highlighted' : ''}`}
        onClick={() => onSelect(user.id)}
      >
        <h2>{user.name}</h2>
        <p>{user.email}</p>
      </div>
    )
  }
```

### Hooks — State and Side Effects

Hooks are functions that let components use React features. They must be called at the top level of a function component (not inside loops or conditionals).

#### useState

```tsx
  const [value, setValue] = useState(initialValue)
  //     ^        ^
  //     current  updater function (triggers re-render)

  const [count, setCount] = useState(0)
  const [user, setUser] = useState<User | null>(null)
  const [items, setItems] = useState<string[]>([])

  // Updating objects — must create new object (immutability)
  setUser({ ...user, name: "New Name" })    // spread + override
  setItems([...items, "new item"])          // spread + append
  setItems(items.filter(i => i !== "old"))  // spread + remove
```

**Why immutability**: React detects changes by reference equality. If you mutate an object in place (`user.name = "New"`), the reference doesn't change, React doesn't see a change, no re-render.

#### useEffect

Runs side effects after render. Replaces lifecycle methods (componentDidMount, componentDidUpdate, componentWillUnmount).

```tsx
  useEffect(() => {
    // runs after every render (rarely what you want)
  })

  useEffect(() => {
    // runs once after first render (componentDidMount equivalent)
  }, [])   // empty dependency array

  useEffect(() => {
    // runs when userId changes
    fetchUser(userId).then(setUser)
  }, [userId])   // dependency array — re-run when these change

  useEffect(() => {
    const subscription = subscribe(topic)

    return () => {
      subscription.unsubscribe()  // cleanup = componentWillUnmount
    }
  }, [topic])

  // Common pattern: fetch data
  useEffect(() => {
    let cancelled = false
    async function load() {
      const data = await fetchUser(id)
      if (!cancelled) setUser(data)  // guard against stale closures
    }
    load()
    return () => { cancelled = true }
  }, [id])
```

#### useRef

A mutable container that persists across renders without triggering re-renders. Two uses:

```tsx
  // 1. Access a DOM element directly
  const inputRef = useRef<HTMLInputElement>(null)
  <input ref={inputRef} />
  // later: inputRef.current?.focus()

  // 2. Store a value across renders without re-rendering
  const countRef = useRef(0)
  countRef.current++   // mutate freely — won't trigger re-render
  // Use for: timers, previous values, mutable state that doesn't affect UI
```

#### useMemo and useCallback

Performance optimization — memoize expensive computations or stable function references.

```tsx
  // useMemo: recompute only when dependencies change
  const sortedItems = useMemo(
    () => [...items].sort(compareFn),
    [items]  // only re-sort when items changes
  )

  // useCallback: stable function reference across renders
  const handleSelect = useCallback(
    (id: number) => { onSelect(id); setSelected(id) },
    [onSelect]  // new function only when onSelect changes
  )
  // Needed when passing callbacks to memoized child components
```

**Don't prematurely optimize**: useMemo/useCallback add complexity. Use them after profiling shows a real perf problem, or when passing callbacks to components wrapped in React.memo.

#### useContext

Share data without passing props down through every level (prop drilling).

```tsx
  // 1. Create the context
  const ThemeContext = createContext<'light' | 'dark'>('light')

  // 2. Provide it high up in the tree
  function App() {
    const [theme, setTheme] = useState<'light' | 'dark'>('light')
    return (
      <ThemeContext.Provider value={theme}>
        <Router />
      </ThemeContext.Provider>
    )
  }

  // 3. Consume anywhere in the tree (no prop drilling)
  function Button() {
    const theme = useContext(ThemeContext)
    return <button className={`btn btn--${theme}`}>Click</button>
  }
```

### Custom Hooks — Reusable Logic

Extract stateful logic into reusable functions. The key innovation over class components.

```tsx
  // Custom hook: encapsulate fetch logic
  function useUser(id: number) {
    const [user, setUser] = useState<User | null>(null)
    const [loading, setLoading] = useState(true)
    const [error, setError] = useState<Error | null>(null)

    useEffect(() => {
      setLoading(true)
      fetchUser(id)
        .then(setUser)
        .catch(setError)
        .finally(() => setLoading(false))
    }, [id])

    return { user, loading, error }
  }

  // Use it anywhere — logic is encapsulated
  function UserProfile({ id }: { id: number }) {
    const { user, loading, error } = useUser(id)
    if (loading) return <Spinner />
    if (error) return <ErrorMessage error={error} />
    return <UserCard user={user!} />
  }
```

### Rendering Lists and Conditional Rendering

```tsx
  // Lists — always provide a key
  function ItemList({ items }: { items: Item[] }) {
    return (
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.name}</li>   // key = stable unique id
        ))}
      </ul>
    )
  }
  // key helps React reconcile which items changed/added/removed.
  // Don't use array index as key if list can reorder.

  // Conditional rendering
  function Panel({ isAdmin, user }: Props) {
    return (
      <div>
        {isAdmin && <AdminControls />}          // short-circuit
        {user ? <UserInfo user={user} /> : <LoginPrompt />}  // ternary
        {error !== null && <ErrorBanner msg={error} />}
      </div>
    )
  }
```

### Component Lifecycle Summary

```
  MOUNT                    UPDATE                   UNMOUNT
  -----                    ------                   -------
  Component first          State or props           Component removed
  appears in tree          changes                  from tree

  useEffect(() => {        useEffect(() => {        useEffect(() => {
    // setup               }, [dep])                  return () => {
  }, [])                   // runs when dep            // cleanup
                           // changes                }
                                                    }, [])
```

---

## Vue

Vue 3 with the Composition API is the closest to React in feel. The Options API (Vue 2 style) is more opinionated and structured — closer to Angular.

```vue
  <!-- Single File Component (.vue) — template + script + style in one file -->
  <template>
    <div class="card" @click="handleClick">
      <h2>{{ user.name }}</h2>
      <p v-if="isExpanded">{{ user.email }}</p>
      <ul>
        <li v-for="tag in user.tags" :key="tag">{{ tag }}</li>
      </ul>
    </div>
  </template>

  <script setup lang="ts">
  import { ref, computed } from 'vue'

  const props = defineProps<{ user: User }>()
  const emit = defineEmits<{ select: [id: number] }>()

  const isExpanded = ref(false)                          // reactive primitive
  const displayName = computed(() => props.user.name.toUpperCase())

  function handleClick() {
    isExpanded.value = !isExpanded.value                 // .value required
    emit('select', props.user.id)
  }
  </script>

  <style scoped>
  .card { border: 1px solid #ccc; }    /* scoped = only this component */
  </style>
```

**Key Vue concepts:**
- `ref()` — reactive primitive (access via `.value`)
- `reactive()` — reactive object (no `.value` needed, but can't destructure)
- `computed()` — derived value, cached until deps change
- `v-if` / `v-for` / `v-model` — template directives
- `@click` shorthand for `v-on:click`
- `:prop` shorthand for `v-bind:prop`
- Single File Components (`.vue`) colocate template, script, style

**Vue reactivity → Rx.NET / IObservable bridge**:

Vue 3's reactivity is a signal-based dependency graph — conceptually identical to `IObservable<T>` chains in Rx.NET, and to Angular 16+ signals. This is the opposite of React's model:

```
  REACT MODEL                        VUE 3 / SIGNALS MODEL
  ===========                        =====================

  State changes → re-run the         State changes → propagate ONLY
  entire component function.         through the reactive graph nodes
  Framework decides what's           that depend on the changed state.
  actually different via vdom diff.

  Coarse-grained (component level)   Fine-grained (value level)

  ──────────────────────────────     ──────────────────────────────

  RX.NET MAPPING:

  ref(0)                             new BehaviorSubject<int>(0)
    ↓                                  ↓
  computed(() => x.value * 2)        .Select(x => x * 2)  ← derived stream
    ↓                                  ↓
  watchEffect(() => render())        .Subscribe(v => render(v))

  Vue tracks dependencies at READ time (like Rx Subscribe):
  when computed() runs, Vue records every ref() it reads.
  When those refs change, only that computed() re-evaluates.

  REACTIVE GRAPH EXAMPLE:

  const price = ref(100)                // BehaviorSubject<number>(100)
  const qty   = ref(3)                  // BehaviorSubject<number>(3)
  const total = computed(               // derived observable
    () => price.value * qty.value       // subscribes to price AND qty
  )
  // total.value === 300

  price.value = 200
  // Vue sees: total depends on price → re-evaluate total only
  // total.value === 600
  // qty did not change → nothing else runs

  // Compare React: you'd call setState({price: 200}),
  // entire component re-runs, total recomputed as part of render.
```

**Why you can't destructure `reactive()`**:

```typescript
  const state = reactive({ price: 100, qty: 3 })

  const { price } = state    // WRONG: price is now a plain number,
                              // not a reactive ref — loses reactivity

  const { price } = toRefs(state)  // CORRECT: price is now a Ref<number>

  // Analogy: reactive() is like IObservable<T> where T is an object.
  // Destructuring pulls out the current VALUE of one property,
  // not a subscription to that property's changes.
  // toRefs() wraps each property in its own BehaviorSubject.
```

**Angular 16+ signals** follow the same model as Vue refs — `signal(0)` is `BehaviorSubject<int>(0)`, `computed(() => x() * 2)` is `.Select(x => x * 2)`. The convergence toward fine-grained reactivity across frameworks (Vue refs, Angular signals, Solid.js) represents the industry move away from React's coarse re-render model for performance-sensitive code.

---

## Angular

The most opinionated of the three. Full framework — routing, forms, HTTP, DI all built in. Closest to ASP.NET MVC in philosophy.

```typescript
  // app.component.ts
  import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core'
  import { UserService } from './user.service'

  @Component({
    selector: 'app-user-card',
    template: `
      <div class="card" (click)="handleClick()">
        <h2>{{ user?.name }}</h2>
        <p *ngIf="isExpanded">{{ user?.email }}</p>
        <li *ngFor="let tag of user?.tags">{{ tag }}</li>
      </div>
    `,
    styleUrls: ['./user-card.component.scss']
  })
  export class UserCardComponent implements OnInit {
    @Input() userId!: number           // input property (like React prop)
    @Output() selected = new EventEmitter<number>()  // output event

    user: User | null = null
    isExpanded = false

    constructor(private userService: UserService) {}  // dependency injection

    ngOnInit(): void {                 // lifecycle hook
      this.userService.getUser(this.userId).subscribe(u => this.user = u)
    }

    handleClick(): void {
      this.isExpanded = !this.isExpanded
      this.selected.emit(this.userId)
    }
  }
```

**Angular concepts that map cleanly to .NET:**

```
  .NET / C#                        Angular
  ---------                        -------
  Dependency Injection (DI)        DI container built-in (same concept)
  Controllers                      Components
  Services / repositories          Services (Injectable classes)
  Attributes / decorators          @Component, @Injectable, @Input
  Module system                    NgModules (or standalone components)
  Interfaces                       TypeScript interfaces (same)
  RxJS Observable                  IObservable<T> / IEnumerable<T> async
  async/await                      async pipe in templates
  ASP.NET MVC view                 Component template
  ASP.NET routing                  Angular Router
  HttpClient                       HttpClient (literally same name)
```

**Angular DI → .NET DI lifetime bridge**:

Angular's DI maps directly to `Microsoft.Extensions.DependencyInjection`. The same three lifetimes, the same constructor injection pattern, and a hierarchical injector tree that mirrors `IServiceProvider` scope nesting.

| Angular | .NET DI (Microsoft.Extensions.DI) | Notes |
|---|---|---|
| `providedIn: 'root'` | `services.AddSingleton<T>()` | One instance for the entire application lifetime. |
| Provided in an `NgModule` | `services.AddScoped<T>()` (module-scoped) | One instance per module load. Conceptually scoped to that module's lifetime. |
| Provided in a `@Component` (`providers: [UserService]`) | `services.AddTransient<T>()` / `IServiceScope` | New instance per component. Destroyed when the component is destroyed. |
| `constructor(private svc: UserService)` | `public MyClass(IUserService svc)` | Identical constructor injection pattern. Angular resolves from the injector; .NET DI resolves from `IServiceProvider`. |

**Hierarchical injector** — this is where Angular goes further than typical .NET DI:

```
  Angular DI tree mirrors the component tree:

  AppModule injector (root)
  ├── Router
  ├── HttpClient
  └── UserService  (providedIn: 'root' → lives here, singleton)

      FeatureModule injector (child of root)
      └── FeatureSpecificService  (provided in module → module-scoped)

          AdminComponent injector (child of module)
          └── AdminService  (provided in component → component-scoped)
              ┌────────────────────────────────────────────────────┐
              │ AdminComponent can see:                            │
              │  - AdminService (own)                              │
              │  - FeatureSpecificService (parent)                 │
              │  - UserService (root)                              │
              │                                                    │
              │ A child injector can OVERRIDE a parent service     │
              │ by providing the same token.                       │
              └────────────────────────────────────────────────────┘

  .NET equivalent: IServiceProvider scope hierarchy
  var scope = rootProvider.CreateScope()
  scope.ServiceProvider.GetService<T>()
  // scope-level registrations shadow root registrations for same interface
```

The override behavior (child injector shadows parent for same token) maps to `IServiceScope` overrides in .NET — a child scope can register its own `IMyService` that takes precedence over the root registration within that scope's lifetime. Angular just makes this happen automatically along the component tree.

Angular is TypeScript-first by design. It was built at Google for large enterprise apps — strong opinions, strong structure, great tooling. The learning curve is steeper but the structure pays off at scale.

---

## Svelte

Different approach: the compiler eliminates the runtime. No virtual DOM, no reactivity system shipped to the browser.

```svelte
  <!-- UserCard.svelte -->
  <script lang="ts">
    export let user: User        // props via export
    export let onSelect: (id: number) => void

    let isExpanded = false       // local state — just a variable
    $: displayName = user.name.toUpperCase()   // $: = reactive declaration
  </script>

  <div on:click={() => { isExpanded = !isExpanded; onSelect(user.id) }}>
    <h2>{displayName}</h2>
    {#if isExpanded}
      <p>{user.email}</p>
    {/if}
    {#each user.tags as tag}
      <li>{tag}</li>
    {/each}
  </div>
```

**Svelte's trade-offs:**
- No virtual DOM — direct DOM updates, faster at runtime
- Smaller bundle — no framework runtime shipped
- Simpler mental model — `let x = 5` is reactive state
- Smaller ecosystem — fewer libraries, less community
- SvelteKit = the Next.js equivalent

---

## Framework Comparison

```
  +---------------+----------+----------+----------+----------+
  |               |  React   |   Vue    | Angular  |  Svelte  |
  +---------------+----------+----------+----------+----------+
  | Learning      | Medium   | Easy     | Hard     | Easy     |
  | curve         |          |          |          |          |
  +---------------+----------+----------+----------+----------+
  | Bundle size   | ~40KB    | ~35KB    | ~130KB   | ~2KB     |
  | (framework)   |          |          |          |          |
  +---------------+----------+----------+----------+----------+
  | Opinioned?    | Low      | Medium   | High     | Medium   |
  +---------------+----------+----------+----------+----------+
  | DI built-in?  | No       | No       | Yes      | No       |
  +---------------+----------+----------+----------+----------+
  | TypeScript    | Good     | Good     | Native   | Good     |
  | support       |          |          |          |          |
  +---------------+----------+----------+----------+----------+
  | Meta-framework| Next.js  | Nuxt     | Built-in | SvelteKit|
  |               | Remix    |          | Router   |          |
  +---------------+----------+----------+----------+----------+
  | Job market    | ★★★★★    | ★★★☆☆    | ★★★★☆    | ★★☆☆☆    |
  +---------------+----------+----------+----------+----------+
  | Best for      | Anything | Medium   | Large    | Perf-    |
  |               |          | apps,    | enterprz | sensitive|
  |               |          | fast DX  | teams    | apps     |
  +---------------+----------+----------+----------+----------+
```

---

## The React Ecosystem

React is a *library*, not a framework. It handles components and rendering. Everything else you bolt on:

```
  REACT CORE
  - Components + JSX
  - State (useState, useReducer)
  - Side effects (useEffect)
  - Context (useContext)
  That's it.

  WHAT YOU ADD:
  +-------------------+------------------------------------------+
  | Routing           | React Router, TanStack Router            |
  | Server framework  | Next.js, Remix                           |
  | Data fetching     | TanStack Query (React Query), SWR        |
  | Global state      | Zustand, Jotai, Redux Toolkit            |
  | Forms             | React Hook Form, Formik                  |
  | UI components     | shadcn/ui, MUI, Radix, Chakra            |
  | Animation         | Framer Motion                            |
  | Testing           | React Testing Library + Vitest/Jest      |
  | Styling           | Tailwind CSS, CSS Modules, styled-comps  |
  +-------------------+------------------------------------------+

  This is both the strength (composable, flexible) and the weakness
  (decision fatigue, "JavaScript fatigue"). Angular bundles most
  of this. React leaves it to you.
```

### React Server Components (RSC)

New in React 18/19, central to Next.js 13+. Changes the component model significantly.

```
  TRADITIONAL REACT (Client Components)
  +-----------+                    +-----------+
  | Browser   | -- fetch data -->  | Server    |
  |           | <-- JSON data  --- |           |
  | Runs all  |                    |           |
  | components|                    |           |
  | renders   |                    |           |
  +-----------+                    +-----------+

  REACT SERVER COMPONENTS
  +-----------+                    +-----------+
  | Browser   |                    | Server    |
  |           | <-- HTML/RSC  ---- | Runs      |
  | Runs only |     payload        | server    |
  | client    |                    | components|
  | components|                    | (async,   |
  |           |                    | DB access)|
  +-----------+                    +-----------+

  Server Components:
  - Run on the server only. Zero JS shipped to browser.
  - Can be async — directly await database calls.
  - Cannot use useState, useEffect, browser APIs.

  Client Components:
  - "use client" directive at top of file.
  - Interactive — can use hooks, events.
  - Can be nested inside server components.

  This is a significant architectural shift. RSC is still maturing
  in 2026. Next.js App Router uses RSC by default.
```

---

## Styling in Component Frameworks

```
  APPROACH          HOW IT WORKS                   EXAMPLE
  ---------         ------------                   -------
  Global CSS        Traditional .css files         styles.css
                    Class name collisions possible  .btn { color: red }

  CSS Modules       Per-file scoped CSS            Button.module.css
                    Class names auto-prefixed       .btn → .Button_btn_a3f1c
                    Import as object               import s from './Button.module.css'
                                                   <div className={s.btn}>

  CSS-in-JS         Style objects in JS            styled-components, Emotion
                    Dynamic styling easy            const Btn = styled.button`color: red`
                    Runtime overhead               (being replaced by compile-time solutions)

  Tailwind CSS      Utility classes in markup      <button className="px-4 py-2 bg-blue-500">
                    No separate .css files          Highly composable
                    Learn the utilities once        Almost no custom CSS needed

  Scoped (Vue)      <style scoped> in .vue file    Automatic per-component scope
```

Tailwind is the dominant choice for new projects in 2026. Strong opinions about it exist. The practical reality: most teams that adopt it don't go back.

---

## Common Confusion Points

### "Why does my state update not appear immediately?"

```tsx
  const [count, setCount] = useState(0)

  function handleClick() {
    setCount(count + 1)
    console.log(count)    // still 0! state updates are async/batched

    // React batches state updates and re-renders once.
    // The new value is available on the NEXT render.
  }

  // If new state depends on previous state, use the updater form:
  setCount(prev => prev + 1)   // always correct, even in batched updates
```

### "My useEffect runs too often / causes infinite loop"

```tsx
  // Infinite loop: object created fresh on every render
  useEffect(() => {
    fetchData(options)
  }, [options])   // options = {} inline = new reference every render

  // Fix: useMemo the object, or use primitive values as deps
  useEffect(() => {
    fetchData({ page, size })
  }, [page, size])   // primitives compare by value, not reference
```

### "What's the difference between state and props?"

```
  PROPS                           STATE
  -----                           -----
  Passed IN from parent           Owned BY this component
  Read-only (don't mutate them)   Mutable (via setState)
  Component is controlled         Component controls itself
  Like function parameters        Like local variables

  Data flows DOWN via props.
  Events flow UP via callback props.
  Never modify props. Never pass state up directly.
```

### "When do I use context vs a state library?"

```
  useContext:
  - Infrequently changing data: theme, locale, auth user
  - Simple app-level config
  - Not for high-frequency updates (every context consumer re-renders)

  Zustand / Jotai / Redux Toolkit:
  - Shared state that changes often
  - Multiple components that read/write the same state
  - Complex update logic
  - Time-travel debugging needed (Redux DevTools)
```

### "React vs Next.js — which do I learn first?"

```
  React is the foundation. Next.js is built on React.
  Learn React first — components, hooks, state, effects.
  Then Next.js adds: routing, SSR, SSG, API routes.

  Most tutorials start with plain React (Vite template).
  Most real production apps use Next.js.
  The React fundamentals transfer directly.
```

---

## Old World → New World Bridge

| WinForms / WPF / XAML concept | React / Vue / Angular equivalent | Notes |
|---|---|---|
| UserControl / Custom Control | Component | Same idea — reusable UI unit |
| Control properties (Width, Text) | Props | Pass data in |
| Control events (Click, Changed) | Callback props (onClick, onChange) | Pass functions in |
| Code-behind (.cs file) | Component function body | Logic lives with UI |
| DataContext / binding source | Props + state | Data flows down |
| INotifyPropertyChanged | useState / reactive() | Trigger re-render on change |
| BindingMode.TwoWay | Controlled inputs (`value` + `onChange`) | Explicit in React |
| ItemsControl / DataTemplate | `.map()` returning JSX | List rendering |
| Visibility.Collapsed | `{condition && <Component />}` | Conditional render |
| DataTrigger / VisualState | Conditional className or CSS | Style based on state |
| Dispatcher.Invoke (UI thread) | Not needed — JS is single-threaded | No threading model |
| Window / Page | Route component (React Router / Next.js) | Navigation unit |
| MVVM ViewModel | Component + hooks | State + behavior |
| DI container (Unity, Autofac) | Angular DI; React: hook composition | |
| Power Apps formula (reactive) | Computed values: `useMemo`, Vue `computed` | Same reactive concept |
| Storybook for .NET (none) | Storybook.js | Component development in isolation |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Start a new web app today | Vite + React (`npm create vite@latest`) |
| Build a production app with SSR / SEO | Next.js |
| Build for an enterprise team with Angular background | Angular |
| Build a Vue app | Nuxt (has SSR) or plain Vite + Vue |
| Fetch and cache server data in React | TanStack Query (React Query) |
| Handle forms | React Hook Form |
| Share state across components (small app) | useContext |
| Share state across components (real app) | Zustand |
| Style components | Tailwind CSS (new) or CSS Modules (conservative) |
| Build a component library | React + Storybook |
| Render a list | `.map()` with a `key` prop |
| Show/hide something | `{condition && <Component />}` |
| Respond to user input | Controlled component: `value` + `onChange` |
| Run code after render | `useEffect` with appropriate deps |
| Avoid re-computing on every render | `useMemo` |
| Avoid re-creating callbacks on every render | `useCallback` |
| Access a DOM element directly | `useRef` |
