# Frontend Frameworks — A Layered Guide

## The Big Picture

Frontend frameworks solve one problem: **keeping the UI in sync with data**. Without them, you write imperative DOM manipulation. With them, you declare what the UI *should look like* and the framework figures out how to get there.

```
+------------------------------------------------------------------+
|                    FRONTEND FRAMEWORK LANDSCAPE                  |
|                                                                  |
|  THE PROBLEM:  Data changes → UI must update                    |
|  THE SOLUTION: Declare UI as a function of state                 |
|                                                                  |
|  +------------+  +------------+  +------------+  +----------+   |
|  |   REACT    |  |    VUE     |  |  ANGULAR   |  |  SVELTE  |   |
|  +------------+  +------------+  +------------+  +----------+   |
|  | Virtual    |  | Reactive   |  | Zone.js    |  | Compile- |   |
|  | DOM diffing|  | system     |  | change     |  | time     |   |
|  | (runtime)  |  | (runtime)  |  | detection  |  | (no VDOM)|   |
|  +------------+  +------------+  +------------+  +----------+   |
|  | ~46% usage |  | ~18% usage |  | ~17% usage |  | ~6% usage|   |
|  | Meta/Vercel|  | Evan You   |  | Google     |  | Rich     |   |
|  |            |  |            |  |            |  | Harris   |   |
|  +------------+  +------------+  +------------+  +----------+   |
|                                                                  |
|  ECOSYSTEM LAYER (built on top of frameworks)                    |
|  React: Next.js, Remix, Gatsby, Expo (React Native)             |
|  Vue:   Nuxt.js                                                  |
|  Angular: Angular itself (full framework, no separate meta)      |
+------------------------------------------------------------------+
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
  |              <UserCard>                   |
  |  Props (inputs):                          |
  |    name: "Alice"                          |
  |    avatarUrl: "..."                       |
  |    role: "Admin"                          |
  |                                           |
  |  Local State:                             |
  |    isExpanded: false                      |
  |                                           |
  |  Renders:                                 |
  |    <div class="card">                     |
  |      <img src={avatarUrl} />              |
  |      <h2>{name}</h2>                      |
  |      <span>{role}</span>                  |
  |      {isExpanded && <Details />}          |
  |    </div>                                 |
  |                                           |
  |  Events Out (callbacks via props):        |
  |    onSelect: () => void                   |
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
  | Job market    | ★★★★★   | ★★★☆☆   | ★★★★☆   | ★★☆☆☆   |
  +---------------+----------+----------+----------+----------+
  | Best for      | Anything | Medium   | Large    | Perf-    |
  |               |          | apps,    | enterprise| sensitive|
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
  | Styling           | Tailwind CSS, CSS Modules, styled-components |
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
