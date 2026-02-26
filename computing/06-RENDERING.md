# Rendering Patterns — A Layered Guide

## The Big Picture

One question drives all rendering strategy decisions: **where and when is HTML generated?**

```
+------------------------------------------------------------------+
|              THE RENDERING STRATEGY SPECTRUM                     |
|                                                                  |
|  ←— more server work                      more client work —→   |
|                                                                  |
|  Traditional   SSG        ISR        SSR        SPA/CSR         |
|  MVC/Razor   (build)  (build+bg)  (request)   (browser)        |
|    |            |         |           |            |             |
|    v            v         v           v            v             |
|  HTML on      HTML at   HTML at    HTML per     Empty HTML +     |
|  every        build     build,     request      JS bundle        |
|  request      time      refresh    on server    Renders in       |
|               once      in bg                   browser          |
|                                                                  |
|  NEW: React Server Components (RSC) — granular server/client    |
|       split at the component level, not the page level           |
+------------------------------------------------------------------+

  NO ONE STRATEGY WINS. Every application mixes them.
  The skill is knowing which page/route needs which strategy.
```

<!-- @editor[diagram/P1]: The calibration note calls a rendering pipeline diagram "critical" — showing for each mode: where HTML originates, when JS executes, what the browser receives, and when the page becomes interactive. The spectrum above shows WHEN but not the HOW of each pipeline. Add a side-by-side pipeline diagram: for SSG/SSR/CSR/RSC, show the sequence (build/request/browser steps) with timing arrows. This is the mental model gap the learner most needs filled. -->

---

## The Core Question

Every approach is a different answer to: **who generates the HTML, and when?**

```
  SERVER at REQUEST TIME        SERVER at BUILD TIME        CLIENT
  ---------------------         --------------------        ------
  Fresh data every time         Data baked in at deploy     Data fetched after load
  Slower TTFB                   Instant TTFB (CDN)          Slow to interactive
  Always current                Stale until rebuild          Always current
  Can't CDN-cache HTML          Full CDN cache              JS bundle CDN-cached
  SSR                           SSG / ISR                   SPA / CSR
```

---

## Performance Vocabulary

Before the patterns: the metrics that drive these decisions.

```
  TTFB   Time to First Byte
         How long before the browser gets ANY response.
         Server work happens here. CDN-cached = near zero.

  FCP    First Contentful Paint
         First pixel of content the user sees.
         Matters for perceived performance.

  LCP    Largest Contentful Paint
         When the main content (hero image, text) is visible.
         Google Core Web Vital. Affects SEO ranking.

  TTI    Time to Interactive
         When the user can actually click things.
         JS must be downloaded, parsed, executed, hydrated.

  CLS    Cumulative Layout Shift
         How much layout jumps around as content loads.
         Google Core Web Vital. Affects SEO ranking.

  The gap between FCP and TTI is the "uncanny valley":
  User sees content but clicks don't work. Frustrating.

  FCP                    TTI
   |                      |
   v                      v
  [Page visible]---gap---[Page interactive]
                    ^
                    Hydration happening here
```

---

## Traditional Server Rendering (The Baseline)

This is what you know from ASP.NET MVC / Razor Pages.

```
  REQUEST → SERVER PROCESSING → FULL HTML RESPONSE

  Browser          Server (ASP.NET MVC / Node.js)
  -------          ---------------------------
  GET /users  -->  Load controller
                   Query database
                   Render Razor template with data
              <--  Full HTML page

  Then for the next page:
  GET /users/1 --> Full cycle again. Full page reload.

  Characteristics:
  + SEO: search engines get full HTML immediately
  + TTFB: depends on server/DB speed
  + TTI: immediate — no JS hydration needed
  + Always fresh data
  - Full page reload on every navigation
  - Server must be running (can't be static CDN-only)
  - No rich client-side interactivity without bolted-on JS
```

This is Razor Pages, MVC views, PHP, Django templates. Still valid. Still used. The "modern" patterns are largely about solving the limitations of full-page reloads while keeping SSR benefits.

---

## SPA / CSR — Client-Side Rendering

The React/Vue/Angular default mode before SSR frameworks became mainstream.

```
  REQUEST → SERVER → EMPTY SHELL → BROWSER RENDERS EVERYTHING

  Browser              CDN / Server
  -------              ------------
  GET /              → index.html (nearly empty)
  GET /app.abc123.js → JS bundle (large)
  GET /vendor.js     → Framework + deps

  [Browser executes JS]
  [React renders components]
  [Components call API]
  GET /api/users     → JSON data
  [React renders list]
  [User sees content] ← this is slow

  index.html looks like:
  <html>
    <body>
      <div id="root"></div>  <!-- empty -->
      <script src="/app.abc123.js"></script>
    </body>
  </html>
```

```
  TIMELINE:
  0ms    Request made
  50ms   HTML received (empty shell)
  300ms  JS bundle downloaded
  400ms  JS parsed + executed, React initialized
  450ms  API fetch starts
  700ms  API responds
  750ms  Page rendered → user sees content (FCP = 750ms)
  750ms  Page interactive (TTI = 750ms, same as FCP here)

  PROBLEMS:
  - Slow initial load (especially on mobile/slow connections)
  - SEO: search bots see empty HTML (mostly fixed now, but complex)
  - No content without JS (accessibility, resilience)

  ADVANTAGES:
  - Rich interactivity after load
  - Subsequent navigation is instant (client-side routing)
  - Simple deployment (just static files on CDN)
  - Great DX with Vite
```

**When CSR/SPA wins**: internal tools, dashboards, apps behind auth where SEO doesn't matter and users have good connections.

---

## SSR — Server-Side Rendering

Render the React/Vue component tree on the server per request. Send full HTML. Then "hydrate" it into an interactive app.

```
  REQUEST → SERVER RENDERS REACT → FULL HTML → HYDRATION

  Browser              Next.js Server
  -------              --------------
  GET /users      -->  Run React components on server
                       Fetch data (DB direct or API)
                       Render component tree to HTML string
                  <--  Full HTML (user sees content immediately)

  [Browser receives HTML — FCP is fast]
  GET /app.js     -->  Download React bundle
                  <--  JS bundle
  [React "hydrates" — attaches event listeners to existing DOM]
  [Now interactive — TTI]

  TIMELINE:
  0ms    Request made
  150ms  Server fetched DB + rendered HTML
  150ms  HTML received → FCP (fast — user sees content)
  450ms  JS bundle downloaded + hydrated → TTI
  FCP–TTI gap: 300ms (page visible but not yet interactive)
```

### Hydration

Hydration is the process of taking static HTML (from SSR or SSG) and making it interactive by attaching React's event system to it.

```
  SERVER SENDS:
  <button class="btn">Count: 0</button>

  BROWSER RECEIVES:
  The HTML above (renders immediately — FCP)

  HYDRATION:
  React downloads, finds the button in the DOM,
  attaches onClick handler, links up useState.
  Now clicking the button works.

  HYDRATION COST:
  Even though HTML is already there, React must:
  1. Download the JS bundle
  2. Parse + execute it
  3. Walk the entire component tree
  4. Attach event handlers to every interactive element

  On a large page with many components: 200–1000ms gap
  between visible and interactive. The "uncanny valley."

  PARTIAL HYDRATION (emerging solution):
  Only hydrate components that are actually interactive.
  Non-interactive parts (static content) never hydrate.
  Astro's islands architecture does this.
```

<!-- @editor[bridge/P2]: Hydration has a direct ASP.NET analog worth making explicit: UpdatePanel (WebForms) tried to solve partial-page interactivity server-side; ScriptManager managed JS on the page. The modern hydration model is the inversion of that — ship the HTML first, attach behavior after. Also: ASP.NET Blazor Server uses a SignalR-backed model that is conceptually similar to SSR+hydration but keeps UI state on the server. That contrast (Blazor Server vs Next.js SSR hydration) would sharpen the mental model for this reader. -->

---

## SSG — Static Site Generation

Pre-render all pages at build time. Output is plain HTML files. Serve from CDN. No server needed at runtime.

```
  BUILD TIME                           REQUEST TIME
  ----------                           ------------
  Next.js / Gatsby runs                Browser
  build process:                       -------
  - Fetches all data                   GET /blog/my-post
  - Renders all pages                      |
  - Outputs HTML files                     v
                                       CDN edge node
  dist/                                (milliseconds away)
    index.html                             |
    blog/                                  v
      my-post.html                    Instant HTML response
      other-post.html                 (pre-built, cached)
    products/
      widget.html

  CHARACTERISTICS:
  + TTFB: near-zero (CDN edge)
  + FCP: very fast
  + SEO: perfect
  + Hosting: dead simple (S3, Netlify, Vercel, GitHub Pages)
  + Security: no server to attack
  - Stale data: content is frozen at build time
  - Rebuild required: any data change needs a new deploy
  - Build time: 10K pages × 100ms each = 16 minutes
```

**When SSG wins**: blogs, marketing sites, docs, anything where content changes infrequently and builds are cheap.

---

## ISR — Incremental Static Regeneration

Next.js invention. SSG pages that automatically regenerate in the background when they go stale.

```
  BUILD TIME:
  Generate HTML for all pages (or just popular ones).
  Tag each page with a revalidation interval.

  FIRST REQUEST (after interval expires):
  GET /products/widget
      |
      v
  CDN: I have a cached copy but it's stale.
  Serve the stale copy immediately (fast!).
  Kick off background regeneration.

  SECOND REQUEST (after background regen finishes):
  GET /products/widget
      |
      v
  CDN: Serve the fresh copy.

  User always gets a fast response.
  Data is fresh within the revalidation window.

  // Next.js config:
  export async function getStaticProps() {
    const data = await fetchProduct()
    return {
      props: { data },
      revalidate: 60  // regenerate at most every 60 seconds
    }
  }

  On-demand revalidation (Next.js 12.2+):
  Trigger a specific page rebuild from a CMS webhook.
  Content editor saves → CMS calls your revalidation API → page regenerates.
  Stale window reduced from minutes to seconds.
```

<!-- @editor[bridge/P2]: ISR is the closest modern analog to ASP.NET's OutputCache with sliding expiration and VaryByParam. The `[OutputCache(Duration=60, VaryByParam="id")]` pattern is exactly what ISR + on-demand revalidation replicates. Worth a one-line explicit call-out here since the learner has that mental model already. The bridge table at the end lists this mapping, but it's more useful inline where the concept is introduced. -->

---

## Streaming SSR

Don't wait for ALL data before sending HTML. Stream it in chunks as it's ready.

```
  TRADITIONAL SSR:
  Wait for ALL data → render ALL HTML → send all at once

  +-----------+
  | Server    |  fetchUser()   — 50ms
  |           |  fetchPosts()  — 200ms  ← blocks everything
  |           |  fetchAds()    — 100ms
  |           |
  |           |  All done: send HTML at 200ms
  +-----------+

  STREAMING SSR (React 18 / Next.js App Router):
  Send HTML in chunks as each piece is ready.

  +-----------+
  | Server    |  Send <html><head>... immediately
  |           |  fetchUser() done (50ms) → stream <header>
  |           |  fetchAds() done (100ms) → stream <sidebar>
  |           |  fetchPosts() done (200ms) → stream <main>
  +-----------+

  User sees the page filling in progressively.
  FCP is at 50ms, not 200ms.
  Implemented with React's <Suspense> boundaries:

  <Suspense fallback={<HeaderSkeleton />}>
    <Header />       {/* streams when ready */}
  </Suspense>
  <Suspense fallback={<PostsSkeleton />}>
    <PostList />     {/* streams when ready */}
  </Suspense>
```

---

## React Server Components (RSC)

The newest model. Not "SSR" in the traditional sense — a fundamentally different component architecture.

```
  TRADITIONAL SSR / HYDRATION COST:
  All components → rendered on server → sent as HTML
  All components → also sent as JS → hydrated in browser

  You pay the hydration cost for EVERYTHING,
  even components that are purely static.

  RSC MODEL:
  Some components → Server Components (render on server only)
                    NEVER sent as JS to browser
                    Can be async, access DB directly
                    Zero hydration cost

  Other components → Client Components ("use client" directive)
                     Sent as JS, hydrated normally
                     Can use useState, useEffect, events

  +-----------+     +-----------+     +-----------+
  |  Page     |     | UserList  |     | LikeButton|
  | (server)  |     | (server)  |     | (client)  |
  | async,    |     | async,    |     | useState  |
  | DB access |     | DB access |     | onClick   |
  | no JS sent|     | no JS sent|     | JS sent   |
  +-----------+     +-----------+     +-----------+

  // Server Component (default in Next.js App Router)
  async function UserList() {
    const users = await db.query('SELECT * FROM users')  // direct DB!
    return (
      <ul>
        {users.map(u => (
          <li key={u.id}>
            {u.name}
            <LikeButton userId={u.id} />  {/* client component nested */}
          </li>
        ))}
      </ul>
    )
  }

  // Client Component
  "use client"
  function LikeButton({ userId }: { userId: number }) {
    const [liked, setLiked] = useState(false)
    return <button onClick={() => setLiked(!liked)}>...</button>
  }
```

**RSC trade-offs**: More powerful architecture, significantly more complex mental model. The "use client" boundary requires careful thought. Still maturing in 2026.

<!-- @editor[bridge/P2]: RSC has no good .NET equivalent, but the closest mental model is ASP.NET View Components (server-rendered, data-fetching, composable into a page) versus partial views (server-rendered templates) versus Ajax-loaded partials (client-fetched). The distinction RSC introduces — some components are never JS, only HTML — is genuinely novel. Worth a brief note: "This has no .NET equivalent. The closest mental model is a View Component that can be composed freely but whose output is never a JS hydration target." The learner's prior art makes RSC harder to grasp because all prior frameworks (Razor, Blazor WASM, WebForms) have a unified rendering model per page. RSC breaks that assumption. -->

---

## Islands Architecture

Popularized by Astro. The logical extension of partial hydration.

```
  ISLANDS ARCHITECTURE:
  Most of the page is static HTML.
  Only specific "islands" of interactivity are hydrated.

  +----------------------------------------------+
  |          STATIC HTML (no JS)                  |
  |  +----------+  +---------------------------+  |
  |  | ISLAND   |  | ISLAND                    |  |
  |  | Search   |  | Shopping Cart             |  |
  |  | (React)  |  | (React)                   |  |
  |  | hydrated |  | hydrated lazily            |  |
  |  +----------+  +---------------------------+  |
  |          STATIC HTML (no JS)                  |
  +----------------------------------------------+

  // Astro component
  ---
  import SearchBar from './SearchBar.jsx'
  import Cart from './Cart.jsx'
  const posts = await fetchPosts()
  ---
  <html>
    <body>
      <h1>My Blog</h1>          <!-- static, zero JS -->
      <SearchBar client:load /> <!-- hydrated immediately -->
      <Cart client:visible />   <!-- hydrated when visible -->
      {posts.map(p => <p>{p.title}</p>)} <!-- static, zero JS -->
    </body>
  </html>

  hydration directives:
  client:load      hydrate immediately
  client:idle      hydrate when browser is idle
  client:visible   hydrate when scrolled into view
  client:media     hydrate when media query matches
```

---

## Next.js — All Patterns in One Framework

Next.js implements every pattern, per route.

```
  NEXT.JS APP ROUTER (Next.js 13+)
  app/
    layout.tsx           Root layout (server component)
    page.tsx             Home page (server component by default)
    loading.tsx          Suspense fallback for this route
    error.tsx            Error boundary for this route

    blog/
      page.tsx           → SSG by default if no dynamic data
      [slug]/
        page.tsx         → SSR if uses params, SSG if generateStaticParams

    dashboard/
      page.tsx           → SSR (dynamic, auth-gated)

    products/
      [id]/
        page.tsx         → ISR with revalidate

  HOW NEXT.JS DECIDES:
  No dynamic data         → SSG (build-time)
  revalidate: N           → ISR (build + background regen)
  dynamic = 'force-dynamic'  → SSR (per-request)
  cookies() / headers()  → SSR (implies request-time data)
  "use client"            → client component (hydrated)
```

```
  // SSG: no params, no dynamic data
  export default async function BlogIndex() {
    const posts = await fetchPosts()   // runs at build time
    return <PostList posts={posts} />
  }

  // ISR: revalidate every 60s
  export const revalidate = 60
  export default async function ProductPage({ params }) {
    const product = await fetchProduct(params.id)
    return <ProductDetail product={product} />
  }

  // SSG with known paths
  export async function generateStaticParams() {
    const products = await fetchAllProducts()
    return products.map(p => ({ id: p.id.toString() }))
  }

  // SSR: force dynamic (per-request)
  export const dynamic = 'force-dynamic'
  export default async function Dashboard() {
    const user = await getCurrentUser()   // needs request context
    return <DashboardPage user={user} />
  }
```

---

## Pattern Comparison

```
  +----------+--------+--------+---------+---------+--------+
  |          | Trad.  |  CSR   |   SSR   |   SSG   |  ISR   |
  |          |  MVC   |  SPA   |         |         |        |
  +----------+--------+--------+---------+---------+--------+
  | TTFB     | Medium | Fast   | Slow-   | Fast    | Fast   |
  |          |        | (CDN)  | Medium  | (CDN)   | (CDN)  |
  +----------+--------+--------+---------+---------+--------+
  | FCP      | Medium | Slow   | Fast    | Fast    | Fast   |
  +----------+--------+--------+---------+---------+--------+
  | TTI      | Fast   | Slow   | Medium  | Medium  | Medium |
  +----------+--------+--------+---------+---------+--------+
  | SEO      | ✅     | ⚠️     | ✅      | ✅      | ✅     |
  +----------+--------+--------+---------+---------+--------+
  | Fresh    | ✅     | ✅     | ✅      | ❌      | ⚠️     |
  | data     |        |        |         | build   | window |
  +----------+--------+--------+---------+---------+--------+
  | Hosting  | Server | CDN    | Server  | CDN     | Server |
  +----------+--------+--------+---------+---------+--------+
  | Interac- | Full   | Full   | Full    | Full    | Full   |
  | tivity   | reload |        |         |         |        |
  +----------+--------+--------+---------+---------+--------+
```

<!-- @editor[content/P2]: This comparison table omits RSC and Islands, which are covered in depth above. Either add columns for them or add a note explaining why they're excluded (they operate at the component level, not the page level, so they don't fit cleanly into this matrix). The learner will notice the gap. At minimum, a one-line callout: "RSC and Islands don't appear here because they operate at the component level — they compose with the page-level strategies above rather than replacing them." -->

---

## Common Confusion Points

### "SSR vs SSG — the server still runs for SSG, right?"

```
  SSG: the server runs ONCE at build time. At request time,
  a CDN serves a pre-built file. No Node.js process handles
  each request. The "server" is just an object storage bucket.

  SSR: a Node.js process (or serverless function) runs for
  EVERY request. React renders the component tree, fetches data,
  produces HTML, sends it.

  Analogy:
  SSG = publishing a printed book (work done once, readers get copies)
  SSR = printing a book on demand (work done per reader request)
```

### "If SSR sends HTML, why is there still a JS bundle?"

```
  SSR solves the first load (FCP).
  Interactivity requires JS (TTI).

  After the HTML arrives, React downloads, takes over the DOM,
  and becomes a SPA for all subsequent navigation (client-side routing).

  The JS bundle is required for:
  - Hydration (attaching event handlers)
  - Client-side navigation (no full page reloads after first load)
  - Any interactivity (state, effects, events)

  RSC reduces this by not hydrating server components.
  But client components still need their JS.
```

### "What's the difference between Next.js pages/ and app/?"

```
  PAGES ROUTER (Next.js ≤12, still supported)
  pages/
    index.tsx          getStaticProps → SSG
                       getServerSideProps → SSR
                       (no data fn) → SSG
    blog/[slug].tsx    getStaticPaths → SSG with params

  APP ROUTER (Next.js 13+, current)
  app/
    page.tsx           Server component by default
                       async/await for data fetching
                       export revalidate → ISR
                       export dynamic → SSR
                       "use client" → client component

  App Router is the future. Pages Router is legacy but stable.
  New projects: use App Router.
  Migrating: Pages Router still works, migrate incrementally.
```

### "When does hydration fail / cause errors?"

```
  Hydration mismatch: server-rendered HTML doesn't match
  what React would render on the client.

  Common causes:
  - Using Date.now() or Math.random() in render
    (different values server vs client)
  - Checking window or localStorage during render
    (doesn't exist on server)
  - Browser extensions that modify DOM before React hydrates

  Error: "Hydration failed because the initial UI does not
  match what was rendered on the server."

  Fix:
  // Use useEffect for browser-only code
  const [mounted, setMounted] = useState(false)
  useEffect(() => setMounted(true), [])
  if (!mounted) return null  // skip server render of this part
```

### "SPA vs MPA — what's an MPA?"

```
  MPA = Multi-Page Application
  Each URL = a server request = a full HTML page.
  Navigation causes a full page reload.
  Traditional ASP.NET MVC is an MPA.

  SPA = Single-Page Application
  One HTML shell. JS handles routing.
  Navigation = JS swaps out content, no page reload.
  Browser history API (pushState) updates the URL.

  Modern hybrid (Next.js, Nuxt):
  First load = SSR or SSG (MPA behavior — full HTML)
  Subsequent navigation = SPA behavior (JS routing, no reload)
  Best of both: fast first load + smooth subsequent navigation.
```

---

## Old World → New World Bridge

| ASP.NET concept | Modern web rendering equivalent | Notes |
|---|---|---|
| Razor Pages / MVC Views | SSR (Next.js) | Same model: server renders HTML per request |
| ASPX / WebForms | SSR + heavy client JS | WebForms had server-side state; closest modern = SSR + RSC |
| Response caching / OutputCache | ISR / CDN caching | Cache rendered output, invalidate on change |
| CDN / Azure CDN | SSG served from CDN | Same concept, now HTML instead of just assets |
| Blazor Server | SSR + SignalR | Server renders, client updates via WebSocket |
| Blazor WASM | SPA/CSR | Full .NET runtime in browser, like React SPA |
| `@Html.RenderPartial()` | React components / RSC | Composable server-rendered units |
| `[OutputCache(Duration=60)]` | `export const revalidate = 60` | ISR equivalent |
| View components | React Server Components | Server-rendered, data-fetching components |
| Ajax UpdatePanel | React state + fetch | Partial page update without full reload |
| JavaScript bundling (System.Web.Optimization) | Vite / Next.js bundling | Same problem, modern solution |
| Azure Static Web Apps | Vercel / Netlify (SSG hosting) | Deploy SSG output to global CDN |
| Azure App Service (Node.js) | Vercel / Railway / Fly.io | Host SSR Next.js server |

<!-- @editor[structure/P2]: The bridge table is placed at the end, after Common Confusion Points. In 01-PACKAGE.md (the gold standard), the bridge is integrated inline near relevant concepts OR placed before the Decision Cheat Sheet. Here it follows Common Confusion Points, breaking the established section order. Move bridge before Common Confusion Points to match the pattern used by 07-STATE.md, 08-BACKEND.md, 09-DATABASE.md, and 10-AUTH.md (all place bridge → then Decision Cheat Sheet last). -->

---

## Decision Cheat Sheet

| I'm building... | Use |
|---|---|
| Blog / docs / marketing site | SSG (Next.js, Astro) |
| Blog with frequent author updates | ISR with on-demand revalidation |
| E-commerce product pages (semi-static) | ISR |
| E-commerce cart / checkout (dynamic) | SSR or CSR |
| Dashboard / internal tool (behind auth) | CSR/SPA or SSR |
| News site (real-time content) | SSR |
| Page that must rank in Google | SSR or SSG (not CSR) |
| App where users have slow connections | SSG or SSR (not CSR — too much JS) |
| Page with lots of user interaction after load | SSR + client components |
| Page that's mostly static with a few widgets | Islands (Astro) |
| I'm using Next.js App Router | Default = server component + SSG, opt into SSR/ISR per route |
| I want the simplest possible setup | Vite SPA (accept the SEO trade-off) |
