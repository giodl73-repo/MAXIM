# State Management — A Layered Guide

## The Big Picture

State management is the most over-engineered topic in frontend. Most complexity comes from conflating different *categories* of state and trying to manage them all with one tool.

```
+------------------------------------------------------------------+
|                    STATE CATEGORIES                              |
|                                                                  |
|  LOCAL UI STATE        SHARED CLIENT STATE    SERVER STATE       |
|  (this component)      (multiple components)  (from APIs/DB)     |
|  ---------------       -------------------    ------------       |
|  useState              Zustand                TanStack Query     |
|  useReducer            Jotai                  SWR                |
|                        Redux Toolkit          Apollo (GraphQL)   |
|                        Context (small apps)                      |
|                                                                  |
|  URL / ROUTER STATE    FORM STATE             PERSISTENT STATE   |
|  --------------------  ----------             ----------------   |
|  React Router          React Hook Form        Zustand + persist  |
|  Next.js router        Formik                 localStorage       |
|  useSearchParams       Zod (validation)       IndexedDB          |
|                                                                  |
|  SIGNALS (alternative reactivity model — see Signals section)   |
|  SolidJS (signals-first) · Vue 3 (signals under the hood)       |
|  Angular 16+ (adopted signals) · TC39 proposal (stage 1)        |
+------------------------------------------------------------------+

  KEY INSIGHT: Server state (API data) is NOT the same problem
  as client state. TanStack Query handles server state so well
  that most apps need almost NO client state library at all.
```

---

## Categories of State — The Foundation

Before reaching for any library, classify the state:

```
  "Where does this data live and who needs it?"

  +---------------------------+--------------------------------+
  | Category                  | Right tool                     |
  +---------------------------+--------------------------------+
  | One component's UI state  | useState / useReducer          |
  | (open/closed, selected,   |                                |
  |  form field values)       |                                |
  +---------------------------+--------------------------------+
  | Shared across a subtree   | Context (if infrequent change) |
  | (theme, locale, auth)     | Zustand (if frequent change)   |
  +---------------------------+--------------------------------+
  | Global app state          | Zustand, Redux Toolkit         |
  | (cart, user prefs, wizard |                                |
  |  steps)                   |                                |
  +---------------------------+--------------------------------+
  | Data from server / API    | TanStack Query, SWR            |
  | (users, products, posts)  |                                |
  +---------------------------+--------------------------------+
  | Current URL / route       | Router (Next.js, React Router) |
  +---------------------------+--------------------------------+
  | Form field state          | React Hook Form                |
  +---------------------------+--------------------------------+
  | Persisted across sessions | Zustand persist, localStorage  |
  +---------------------------+--------------------------------+

  RULE: Reach for the simplest tool that covers the need.
  Don't put server data in Redux. Don't use Redux for a toggle.
```

---

## React Built-Ins

### useState — Local State

Covered in depth in 05-FRONTEND.md. The default starting point for any state.

```tsx
  const [isOpen, setIsOpen] = useState(false)
  const [user, setUser] = useState<User | null>(null)
  const [items, setItems] = useState<Item[]>([])
```

**Rule**: if only one component (and its direct children via props) needs this state, `useState` is the right answer. Don't elevate state prematurely.

### useReducer — Complex Local State

When `useState` has too much related state that changes together, or update logic is complex:

```tsx
  type State = {
    count: number
    step: number
    history: number[]
  }

  type Action =
    | { type: 'increment' }
    | { type: 'decrement' }
    | { type: 'setStep'; payload: number }
    | { type: 'reset' }

  function reducer(state: State, action: Action): State {
    switch (action.type) {
      case 'increment':
        return {
          ...state,
          count: state.count + state.step,
          history: [...state.history, state.count + state.step]
        }
      case 'decrement':
        return { ...state, count: state.count - state.step }
      case 'setStep':
        return { ...state, step: action.payload }
      case 'reset':
        return { count: 0, step: 1, history: [] }
    }
  }

  function Counter() {
    const [state, dispatch] = useReducer(reducer, { count: 0, step: 1, history: [] })

    return (
      <div>
        <span>{state.count}</span>
        <button onClick={() => dispatch({ type: 'increment' })}>+</button>
        <button onClick={() => dispatch({ type: 'decrement' })}>-</button>
      </div>
    )
  }
```

`useReducer` is a local Redux. Same reducer pattern — action → pure function → new state. No library needed. This is Redux's core pattern, now built into React.

**CQRS / Event Sourcing bridge**: If you've worked with CQRS or event sourcing — and VSTS work items are a textbook example — this pattern is architecturally identical. A command (action) is dispatched. A pure handler function (reducer) folds it into a new aggregate state. The store is the aggregate root. The action log is append-only; current state is derived by replaying it from initial state. Redux DevTools' time-travel debugging works for exactly the same reason event sourcing enables audit replays: you have the full history of state transitions as an immutable sequence, and you can rewind by replaying a prefix of that sequence. React's constraint that you never mutate state in place — always return a new object — is the same invariant that makes event sourcing sound: events describe what happened, they are never edited. `useReducer` at the component level and Redux Toolkit at the app level are both just the Elm architecture applied to UI state, which is event sourcing applied to a single aggregate.

---

## The Prop Drilling Problem

This is what drives developers to state libraries:

```
  <App>                          // has the user data
    <Layout>                     // doesn't need it, but must pass it
      <Sidebar>                  // doesn't need it, but must pass it
        <UserMenu>               // doesn't need it, but must pass it
          <UserAvatar />         // ACTUALLY NEEDS the user data
```

```tsx
  // Prop drilling — tedious and brittle
  function App() {
    const [user] = useState(currentUser)
    return <Layout user={user} />
  }
  function Layout({ user }) {
    return <Sidebar user={user} />
  }
  function Sidebar({ user }) {
    return <UserMenu user={user} />
  }
  function UserMenu({ user }) {
    return <UserAvatar user={user} />
  }
  function UserAvatar({ user }) {
    return <img src={user.avatar} />   // finally used here
  }
```

Four intermediate components that don't use `user` but must accept and pass it. Add a new prop to `UserAvatar` and you touch five files.

**Solutions**: Context (built-in) or an external store (Zustand, Redux).

---

## Context — Built-In Sharing

Covered in 05-FRONTEND.md. Revisited here for the state management perspective.

```tsx
  const UserContext = createContext<User | null>(null)

  // Provide near the top
  function App() {
    const [user, setUser] = useState<User | null>(null)
    return (
      <UserContext.Provider value={user}>
        <Layout />          {/* no user prop needed */}
      </UserContext.Provider>
    )
  }

  // Consume anywhere below — no drilling
  function UserAvatar() {
    const user = useContext(UserContext)
    return <img src={user?.avatar} />
  }
```

### Context Performance Problem

```
  IMPORTANT: Every consumer re-renders when context VALUE changes.

  <ThemeContext.Provider value={theme}>
    <UserContext.Provider value={user}>
      <App />
    </UserContext.Provider>
  </ThemeContext.Provider>

  If user changes → ALL components consuming UserContext re-render.
  This is fine for low-frequency changes (theme, locale, auth user).
  This is a PROBLEM for high-frequency changes (shopping cart qty,
  live data, per-keystroke form state).

  React has no built-in mechanism to subscribe to part of a context
  object. If the context holds { user, cart, notifications } and
  cart changes, user-displaying components also re-render.

  This is why Zustand and Jotai exist: granular subscriptions.
```

---

## Zustand — The Modern Lightweight Store

Zustand ("state" in German) is the dominant choice for shared client state in 2026. Small API, no boilerplate, granular subscriptions.

```tsx
  import { create } from 'zustand'

  // Define the store
  interface CartStore {
    items: CartItem[]
    total: number
    addItem: (item: CartItem) => void
    removeItem: (id: string) => void
    clear: () => void
  }

  const useCartStore = create<CartStore>((set, get) => ({
    items: [],
    total: 0,

    addItem: (item) => set((state) => ({
      items: [...state.items, item],
      total: state.total + item.price
    })),

    removeItem: (id) => set((state) => {
      const items = state.items.filter(i => i.id !== id)
      return {
        items,
        total: items.reduce((sum, i) => sum + i.price, 0)
      }
    }),

    clear: () => set({ items: [], total: 0 })
  }))
```

```tsx
  // Consume anywhere — no Provider needed
  function CartIcon() {
    const count = useCartStore(state => state.items.length)
    //                          ^-- selector: only re-renders when
    //                              items.length changes, not on total change
    return <span>{count}</span>
  }

  function CartTotal() {
    const total = useCartStore(state => state.total)
    return <span>${total.toFixed(2)}</span>
  }

  function AddToCartButton({ item }: { item: CartItem }) {
    const addItem = useCartStore(state => state.addItem)
    return <button onClick={() => addItem(item)}>Add to Cart</button>
  }
```

### Zustand Key Concepts

```
  create()          Defines the store. Returns a hook.
  set()             Update state (merges by default, like setState)
  get()             Read current state inside actions
  selector          Arrow function passed to the hook.
                    Component re-renders ONLY when selected value changes.

  NO Provider required.  Zustand stores are module-level singletons.
  Works outside React.   Call store.getState() anywhere.
  DevTools.              Works with Redux DevTools extension.
  Middleware.            persist (localStorage), immer (mutations), devtools.
```

### Zustand with Persistence

```tsx
  import { persist } from 'zustand/middleware'

  const useSettingsStore = create<SettingsStore>()(
    persist(
      (set) => ({
        theme: 'light',
        language: 'en',
        setTheme: (theme) => set({ theme }),
      }),
      { name: 'app-settings' }  // localStorage key
    )
  )
  // State survives page refresh. Automatically serialized to localStorage.
```

---

## Redux Toolkit — The Mature Enterprise Option

Plain Redux (2015) required enormous boilerplate. Redux Toolkit (RTK, 2019) is the modern Redux — still the same core pattern but dramatically less code.

```tsx
  import { createSlice, configureStore } from '@reduxjs/toolkit'

  // A "slice" = one piece of state + its reducers/actions
  const cartSlice = createSlice({
    name: 'cart',
    initialState: { items: [] as CartItem[], total: 0 },
    reducers: {
      addItem(state, action: PayloadAction<CartItem>) {
        state.items.push(action.payload)        // Immer allows mutation syntax
        state.total += action.payload.price     // looks like mutation, creates new state
      },
      removeItem(state, action: PayloadAction<string>) {
        state.items = state.items.filter(i => i.id !== action.payload)
        state.total = state.items.reduce((s, i) => s + i.price, 0)
      },
      clear(state) {
        state.items = []
        state.total = 0
      }
    }
  })

  // createSlice auto-generates action creators
  export const { addItem, removeItem, clear } = cartSlice.actions

  // Configure the root store
  export const store = configureStore({
    reducer: { cart: cartSlice.reducer }
  })

  export type RootState = ReturnType<typeof store.getState>
  export type AppDispatch = typeof store.dispatch
```

```tsx
  // Wrap app in Provider (unlike Zustand, Redux requires this)
  function App() {
    return (
      <Provider store={store}>
        <Router />
      </Provider>
    )
  }

  // Consume with typed hooks
  function CartIcon() {
    const count = useSelector((state: RootState) => state.cart.items.length)
    const dispatch = useDispatch<AppDispatch>()
    return (
      <button onClick={() => dispatch(clear())}>
        Cart ({count})
      </button>
    )
  }
```

### Why Redux Still Matters

```
  Redux is the right choice when:

  + Large team, many contributors — strict conventions help
  + Complex state transitions — audit trail is critical
  + Time-travel debugging (Redux DevTools) genuinely needed
  + Existing Redux codebase to maintain
  + State logic must be tested in complete isolation (pure reducers)

  Redux is overkill when:
  - App is small-medium with no complex shared state
  - The "state" is mostly API data (use TanStack Query instead)
  - Team is small, can agree on informal conventions
  - You don't need time-travel debugging

  2026 reality: Zustand has largely replaced Redux for new projects.
  Redux survives in large enterprise codebases and where its structure
  is genuinely valued.
```

---

## Jotai — Atomic State

Bottom-up approach. Instead of one store, define individual atoms. Components subscribe to specific atoms.

```tsx
  import { atom, useAtom, useAtomValue, useSetAtom } from 'jotai'

  // Define atoms
  const countAtom = atom(0)
  const doubledAtom = atom((get) => get(countAtom) * 2)  // derived atom

  // Use in components
  function Counter() {
    const [count, setCount] = useAtom(countAtom)
    const doubled = useAtomValue(doubledAtom)   // read-only

    return (
      <div>
        <span>{count} (doubled: {doubled})</span>
        <button onClick={() => setCount(c => c + 1)}>+</button>
      </div>
    )
  }
```

```
  JOTAI vs ZUSTAND:

  Zustand: one store, define shape upfront, access via selectors.
  Jotai:   many atoms, compose them, no store boundary.

  Jotai is closer to React's useState model (bottom-up).
  Zustand is closer to Redux (top-down store definition).

  Jotai excels at: fine-grained reactivity, atomic updates,
  code-splitting state by feature.

  Zustand excels at: clear store structure, actions as methods,
  simpler mental model.
```

Jotai's atoms are the React-ecosystem tool closest in spirit to **signals** — but they still operate within React's re-render model. See the Signals section below for the architectural distinction.

---

## Signals — A Different Reactivity Model

Signals are gaining traction across the frontend ecosystem and represent a fundamentally different approach to reactivity. Understanding them matters for architecture decisions, not just framework trivia.

### What Is a Signal?

A signal is a **reactive cell** — a value container that tracks which computations read it and pushes updates directly to those computations when the value changes.

```
  REACT MODEL (pull / re-render):
  State changes → React re-runs the entire component function
  → produces a new virtual DOM tree → diffs against previous
  → patches the real DOM

  Component is the unit of re-execution.
  Even if only one value changes, the whole function reruns.

  SIGNALS MODEL (push / fine-grained):
  Signal changes → only the specific DOM nodes (or computations)
  that subscribed to this signal are updated
  → no virtual DOM diff, no component re-run

  The individual reactive value is the unit of update.
```

This is analogous to the difference between polling and event-driven architecture. React polls for changes on each render cycle. Signals push changes directly to subscribers. For a system with many fine-grained updates (live dashboards, real-time collaboration, games), this matters significantly.

### Signal Mechanics

```typescript
  // SolidJS — the reference signal implementation
  import { createSignal, createEffect, createMemo } from 'solid-js'

  const [count, setCount] = createSignal(0)
  const doubled = createMemo(() => count() * 2)  // derived signal — auto-tracked

  createEffect(() => {
    console.log('count changed:', count())   // runs when count changes, nothing else
  })

  // Note: reading a signal requires calling it as a function: count()
  // This is what enables automatic dependency tracking —
  // the signal knows who's reading it at this moment.

  setCount(5)  // → triggers only the effect above and DOM nodes bound to count()
               //    no component re-render, no virtual DOM diff
```

```
  REACTIVE PRIMITIVES IN SIGNALS:

  Signal       Writable reactive value.    createSignal(0)
  Memo         Derived computed value.     createMemo(() => count() * 2)
               Cached, only recomputes
               when dependencies change.
  Effect       Side-effectful subscriber.  createEffect(() => log(count()))
               Runs when any read signal
               in its body changes.
```

### Where Signals Are Today (2026)

```
  FRAMEWORK        STATUS
  ---------        ------
  SolidJS          Signals-first from day one. The reference impl.
                   No virtual DOM. Compiles to direct DOM updates.

  Vue 3            Reactivity system is signals-based under the hood
                   (ref(), reactive(), computed()). Vue calls them
                   "reactive references" but the mechanism is signals.
                   Component still re-renders, but the system is fine-grained.

  Angular 16+      Adopted signals as first-class API (signal(), computed(),
                   effect()). Replacing Zone.js for change detection.
                   Angular 17+ pushes signals as the primary approach.

  Preact Signals   @preact/signals-react: bolt-on signals for React.
                   Works but fights React's rendering model.

  TC39 Proposal    Signals are a Stage 1 TC39 proposal (JavaScript language).
                   Stage 1 = "worth exploring" — not imminent.
                   If it lands, signals become a JS primitive,
                   frameworks share a common reactivity layer.

  React            No signals. React team has explored but not adopted.
                   React's model (re-run function, reconcile) is philosophically
                   different. RSC + compiler (React Forget) are React's answers
                   to the performance concerns signals address.
```

### Push vs Pull — The Architectural Distinction

```
  PULL (React):
  +-----------+       re-render        +-----------+
  | Component |  <------ triggered --- | setState  |
  |  function |                        |  called   |
  +-----------+                        +-----------+
        |
        v  runs entire function, builds vDOM, diffs
        |
  +----------+
  | DOM patch|
  +----------+

  PUSH (Signals):
  +--------+         +------------+         +----------+
  | Signal |  value  | Subscriber | direct  | DOM node |
  |  count | ~~~~~~> |  (effect)  | ~~~~~~> |  update  |
  +--------+         +------------+         +----------+
   setCount(5)        only runs if           only this
                      it read count          node updates

  For high-frequency updates or large component trees,
  signals' surgical updates outperform React's batch re-render.
  For typical CRUD UIs, the difference is imperceptible.
```

### When Signals Matter for Architecture

Signals are not a replacement for React in most applications. They matter when:

- Rendering performance is the bottleneck (not API latency, not business logic)
- State changes are high-frequency (per-frame animations, real-time collaboration, live metrics)
- You're choosing a framework for a new project and want minimal JS overhead
- The team is comfortable with a different mental model

For the learner's context: if you're evaluating Angular 16+ for a new Microsoft-adjacent project, the signals-based change detection is a meaningful architectural shift from Zone.js. SolidJS is worth understanding as the clean reference implementation even if you never use it — it clarifies what React is actually doing.

---

## TanStack Query — Server State

This is the most important state library most developers learn too late. It changes how you think about "state management."

### The Key Insight

```
  Most of what developers put in Redux is SERVER STATE:
  - Users fetched from /api/users
  - Products fetched from /api/products
  - Current user fetched from /api/me

  Server state has fundamentally different properties:
  +-------------------------+---------------------------+
  | CLIENT STATE            | SERVER STATE              |
  +-------------------------+---------------------------+
  | You own it              | Server owns it            |
  | Always synchronous      | Asynchronous (fetch)      |
  | Always up to date       | Can go stale              |
  | Simple to update        | Update requires API call  |
  | No loading/error state  | Loading and error states  |
  | No caching needed       | Caching is critical       |
  +-------------------------+---------------------------+

  Trying to manage server state with Redux means you're manually
  writing: loading flags, error handling, cache invalidation,
  background refresh, deduplication of identical requests,
  stale-while-revalidate logic...

  TanStack Query does all of this for you.
```

### useQuery — Fetching Data

```tsx
  import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query'

  // Simple fetch
  function UserList() {
    const { data, isLoading, isError, error } = useQuery({
      queryKey: ['users'],           // cache key — unique identifier
      queryFn: () => fetchUsers(),   // the async function
    })

    if (isLoading) return <Spinner />
    if (isError) return <Error message={error.message} />

    return <ul>{data.map(u => <li key={u.id}>{u.name}</li>)}</ul>
  }

  // With parameters — refetches automatically when userId changes
  function UserProfile({ userId }: { userId: number }) {
    const { data: user } = useQuery({
      queryKey: ['users', userId],   // include params in key
      queryFn: () => fetchUser(userId),
      staleTime: 5 * 60 * 1000,     // consider fresh for 5 minutes
      gcTime: 10 * 60 * 1000,       // garbage collect after 10 min
    })

    return <div>{user?.name}</div>
  }
```

### What TanStack Query Handles Automatically

```
  DEDUPLICATION:
  3 components call useQuery(['users']) simultaneously.
  → 1 network request, all 3 get the same data.

  CACHING:
  Navigate away from /users, come back.
  → Instant display of cached data + background refetch.

  STALE-WHILE-REVALIDATE:
  Show cached data immediately (stale).
  Refetch in background.
  Update UI when fresh data arrives.
  User never sees a loading spinner on return visits.

  BACKGROUND REFETCH:
  User switches tabs, comes back.
  → Query refetches automatically (window focus refetch).

  RETRY:
  Network request fails.
  → Automatic retry with exponential backoff (3 times by default).

  SYNCHRONIZATION:
  Same query key used in multiple components.
  → All components stay in sync. One update, all update.
```

### useMutation — Updating Data

```tsx
  function DeleteUserButton({ userId }: { userId: number }) {
    const queryClient = useQueryClient()

    const deleteMutation = useMutation({
      mutationFn: (id: number) => deleteUser(id),

      onSuccess: () => {
        // Invalidate cache → triggers refetch → UI updates
        queryClient.invalidateQueries({ queryKey: ['users'] })
      },

      onError: (error) => {
        toast.error(`Delete failed: ${error.message}`)
      }
    })

    return (
      <button
        onClick={() => deleteMutation.mutate(userId)}
        disabled={deleteMutation.isPending}
      >
        {deleteMutation.isPending ? 'Deleting...' : 'Delete'}
      </button>
    )
  }
```

### Optimistic Updates

```tsx
  const updateMutation = useMutation({
    mutationFn: updateUser,

    onMutate: async (newUser) => {
      // Cancel any in-flight refetches
      await queryClient.cancelQueries({ queryKey: ['users', newUser.id] })

      // Snapshot the current value
      const previousUser = queryClient.getQueryData(['users', newUser.id])

      // Optimistically update the cache
      queryClient.setQueryData(['users', newUser.id], newUser)

      // Return snapshot for rollback
      return { previousUser }
    },

    onError: (err, newUser, context) => {
      // Roll back on error
      queryClient.setQueryData(['users', newUser.id], context?.previousUser)
    },

    onSettled: () => {
      // Always refetch to sync with server
      queryClient.invalidateQueries({ queryKey: ['users'] })
    }
  })

  // User sees the update immediately. If the server fails, it rolls back.
```

### Setup

```tsx
  // main.tsx
  import { QueryClient, QueryClientProvider } from '@tanstack/react-query'
  import { ReactQueryDevtools } from '@tanstack/react-query-devtools'

  const queryClient = new QueryClient({
    defaultOptions: {
      queries: {
        staleTime: 60 * 1000,   // 1 minute default stale time
        retry: 2,
      }
    }
  })

  function App() {
    return (
      <QueryClientProvider client={queryClient}>
        <Router />
        <ReactQueryDevtools />   {/* visual cache inspector, dev only */}
      </QueryClientProvider>
    )
  }
```

---

## The Realistic Modern Stack

```
  WHAT MOST NEW REACT APPS USE IN 2026:

  Server state (API data):   TanStack Query
  Shared client state:       Zustand
  Local UI state:            useState / useReducer
  Form state:                React Hook Form
  URL state:                 Next.js router / React Router
  Persistent state:          Zustand + persist middleware

  WHAT YOU DON'T NEED ANYMORE (usually):
  Redux — for server state (TanStack Query replaces this use case)
  Redux — for simple shared state (Zustand is simpler)
  Context for performance-sensitive state (Zustand is faster)

  WHAT REDUX IS STILL GOOD FOR:
  Complex domain state with many actions and transitions
  Large teams needing enforced conventions
  When you need time-travel debugging for complex state bugs
```

---

## State Colocation — The Underrated Principle

Before reaching for any library, ask: **can this state live lower?**

```
  WRONG: hoist everything to the top

  function App() {
    const [modalOpen, setModalOpen] = useState(false)   // only UserCard needs this
    const [selectedTab, setSelectedTab] = useState(0)   // only UserProfile needs this
    const [searchQuery, setSearchQuery] = useState('')  // only SearchBar needs this
    // App re-renders on ALL of these changes
  }

  RIGHT: keep state as close to where it's used as possible

  function UserCard() {
    const [modalOpen, setModalOpen] = useState(false)   // local
  }
  function UserProfile() {
    const [selectedTab, setSelectedTab] = useState(0)   // local
  }
  function SearchBar() {
    const [searchQuery, setSearchQuery] = useState('')  // local
  }
  // App only re-renders for its own state changes

  ESCALATION LADDER:
  1. useState in the component that needs it
  2. Lift to nearest common ancestor if siblings need it
  3. Context if it needs to skip many levels (low-frequency data)
  4. Zustand if many components need it or it changes frequently
  5. TanStack Query if it's server data
```

---

## Common Confusion Points

### "Why doesn't my component update when I mutate state?"

```tsx
  // WRONG: mutating in place
  const [items, setItems] = useState(['a', 'b'])
  items.push('c')       // mutates array, same reference
  setItems(items)       // React sees same reference — no re-render

  // RIGHT: create new reference
  setItems([...items, 'c'])          // new array
  setItems(prev => [...prev, 'c'])   // functional update form

  // Objects:
  // WRONG
  user.name = 'New'
  setUser(user)

  // RIGHT
  setUser({ ...user, name: 'New' })
```

### "I put API data in Redux and it's a lot of boilerplate"

```
  That's a sign you're using the wrong tool.
  Server state (API data) belongs in TanStack Query.
  Redux is for client state that you own and modify.

  Before TanStack Query, people put API data in Redux because
  there was no better option. RTK Query (bundled with Redux Toolkit)
  is Redux's answer to this, but TanStack Query is framework-agnostic
  and generally preferred for new projects.
```

### "Context vs Zustand — when does Context become a problem?"

```
  Context is fine for:
  - Theme (changes rarely)
  - Locale / i18n (changes rarely)
  - Auth user (changes on login/logout)
  - Feature flags (static after app load)

  Switch to Zustand when:
  - State changes frequently (per keystroke, per scroll, real-time)
  - Multiple independent slices that shouldn't cause cross-component renders
  - You need to read state outside React (in utility functions)
  - Performance profiling shows context re-renders are a bottleneck
```

### "What's the difference between staleTime and gcTime in TanStack Query?"

```
  staleTime    How long data is considered "fresh."
               During this window: no background refetch on mount.
               After: refetch in background on next mount.
               Default: 0 (always stale — always refetches)

  gcTime       How long unused cached data is kept in memory.
  (formerly    After no component subscribes for this long, data is removed.
  cacheTime)   Default: 5 minutes.

  Example:
  staleTime: 5min, gcTime: 10min

  0:00  Fetch users → cached, considered fresh
  3:00  Navigate away → data in cache but no subscribers
  5:01  Data is now "stale" (but still in cache)
  7:00  Navigate back → show stale data instantly, refetch in bg
  10:01 Cache garbage collected → next visit shows loading spinner
```

---

## Old World → New World Bridge

| .NET / WPF / WinForms concept | React state management equivalent | Notes |
|---|---|---|
| ViewModel (MVVM) | Component state + Zustand store | ViewModel = component's local state + store slice |
| INotifyPropertyChanged | useState setter / Zustand set() | Trigger re-render on change |
| ObservableCollection<T> | State array + setState | Reactive list — immutable update in React |
| WPF Binding TwoWay | Controlled input: `value` + `onChange` | Explicit in React |
| DependencyProperty | Props | Passed down, not owned |
| MVC ViewBag / ViewData | Props passed to component | Per-render data, not persistent |
| TempData | Could use URL state or short-lived Zustand | Survives one redirect |
| Session state | Zustand + persist / server-side session | Depends on auth strategy |
| HttpContext.Items | Request-scoped context (server) / React context (client) | |
| ASP.NET Cache / MemoryCache | TanStack Query cache | Both: TTL, invalidation, stale-while-revalidate |
| Redux pattern | `useReducer` (local) or Redux Toolkit (global) | Same Elm-inspired pattern |
| Command pattern | Action dispatch (Redux/useReducer) | Explicit intent → state change |
| Service layer | Zustand actions / TanStack Query queryFn | Business logic outside UI |
| Undo/Redo | Redux DevTools time travel / custom history state | |
| CQRS command → handler → event | Redux/useReducer action → reducer → new state | Isomorphic: immutable action log + pure fold function. VSTS work item history IS this pattern. Time-travel debugging works because you replay the action log — same reason event sourcing enables audit replays. |
| Event sourcing aggregate root | Redux store / useReducer state | Current state = initial state folded over action log |

---

## Decision Cheat Sheet

| State scenario | Use |
|---|---|
| Toggle, local counter, form field in one component | `useState` |
| Complex related state in one component | `useReducer` |
| Theme, locale, auth user (low-frequency shared data) | `useContext` |
| Cart, preferences, wizard steps (shared, changes often) | Zustand |
| Data from an API / database | TanStack Query |
| Large enterprise app, team needs strict conventions | Redux Toolkit |
| Fine-grained atom-level reactivity | Jotai |
| Complex async state flows / state machines | XState |
| Form state, validation | React Hook Form + Zod |
| Current route / URL params | Next.js `useRouter` / React Router |
| State that survives page refresh | Zustand + persist middleware |
| State shared between React and non-React code | Zustand (works outside React) |
| Optimistic UI updates | TanStack Query `onMutate` |
| Prefetch data before navigation | TanStack Query `prefetchQuery` |
| High-frequency fine-grained updates, minimal JS overhead | Consider SolidJS (signals-first) or Angular 16+ signals |
