# Backend APIs — A Layered Guide

## The Big Picture

A backend API is a contract between a server and its clients. The three dominant paradigms differ in *who defines the contract*, *how queries are shaped*, and *how much type safety you get end-to-end*.

```
+------------------------------------------------------------------+
|                    BACKEND API LANDSCAPE                         |
|                                                                  |
|  PROTOCOL     REST          GraphQL        tRPC                  |
|  ---------    ----          -------        ----                  |
|  Transport    HTTP          HTTP           HTTP                  |
|  Shape        Server        Client         Inferred from         |
|  defined by   defines URLs  defines query  TypeScript            |
|  Contract     OpenAPI spec  SDL schema     TypeScript types      |
|  Clients      Any language  Any language   TypeScript only       |
|  Best for     Public APIs   Flexible data  Full-stack TS mono    |
|               Multi-client  requirements   repos                 |
|                                                                  |
|  FRAMEWORK    Express   Fastify    NestJS     Hono               |
|  ---------    -------   -------    ------     ----               |
|  Style        Minimal   Minimal    Angular-   Minimal            |
|               flexible  fast       like       edge-ready         |
|                                                                  |
|  HOSTING      Node.js server   Serverless functions   Edge       |
|  -------      (always on)      (per-request, scales   (Cloudflare|
|               Azure App Svc    to zero)               Workers)   |
+------------------------------------------------------------------+
```

**Bridge from .NET**: You've consumed REST APIs from Azure services for years. This module is about *building* them in Node.js — and understanding what GraphQL and tRPC add. The patterns (routing, middleware, validation, auth) map directly from ASP.NET MVC.

### WCF → REST → GraphQL → tRPC: The Historical Arc

You lived through this transition at Microsoft. Here it is as a coherent narrative:

```
  WCF (2006 — contract-first, strongly typed, heavyweight)
  --------------------------------------------------------
  Service defined by [ServiceContract] / [OperationContract] interfaces.
  Wire format: SOAP/XML (or NetTcp for internal).
  Contract published as WSDL — machine-readable, generated client stubs.
  "Add Service Reference" in Visual Studio: point at a WSDL, get C# proxies.
  Enforces full contract at both ends: client and server share the same types.
  Cost: heavyweight (WS-* standards stack, XML verbosity, config complexity).

  REST (2010s — resource-oriented, HTTP-native, informal contract)
  ---------------------------------------------------------------
  No WSDL by default. Contract is informal (documentation, convention).
  Wire format: JSON over HTTP. Verbs as actions, URLs as resource addresses.
  Multiple clients (web, mobile) can consume without generated stubs.
  OpenAPI (Swagger) emerged as the REST-era WSDL: machine-readable contract,
  openapi-generator replicates "Add Service Reference" for REST.
  Cost: no enforcement — server can change response shape, clients break silently.

  GraphQL (2015 — client-defined queries, SDL as contract)
  --------------------------------------------------------
  Client specifies exactly what fields it needs.
  Schema Definition Language (SDL) is the contract — typed, introspectable.
  Solves REST's over-fetching/under-fetching: one request, exactly what asked for.
  Used by GitHub, Shopify, Contentful — wherever many client types need flexibility.
  Cost: caching harder, N+1 query problem, overkill for simple CRUD.

  tRPC (2021 — TypeScript IS the contract, no schema language)
  ------------------------------------------------------------
  Define TypeScript functions on the server.
  TypeScript types flow to the client automatically.
  No schema file, no code generation, no "Add Service Reference" step.
  Rename a procedure → TypeScript errors everywhere it's used instantly.
  Constraint: TypeScript only, monorepo or shared package required.
  Cost: not suitable for public APIs or non-TypeScript clients.

  PROGRESSION:
  WCF   → strong typing, code gen required, heavyweight, Windows-heavy
  REST  → flexible, lightweight, informal contract, requires tooling to get typing
  GQL   → strong contract (SDL), client-driven, complex for simple use
  tRPC  → strong typing, no schema, live enforcement, TypeScript-only
```

---

## HTTP — The Foundation

Everything runs on HTTP. Getting the fundamentals right matters.

### Verbs and Their Meaning

```
  VERB      MEANING                 SAFE?  IDEMPOTENT?
  ----      -------                 -----  -----------
  GET       Read a resource         Yes    Yes
  POST      Create a new resource   No     No
  PUT       Replace a resource      No     Yes
  PATCH     Partial update          No     No (usually)
  DELETE    Remove a resource       No     Yes
  HEAD      Like GET, no body       Yes    Yes
  OPTIONS   What methods allowed?   Yes    Yes

  Safe = no side effects (read-only)
  Idempotent = calling N times = same result as calling once
    PUT /users/1 { name: "Alice" }  x3 = same as x1 ✓
    POST /users { name: "Alice" }   x3 = three users created ✗
```

### Status Codes That Matter

```
  2xx SUCCESS
  200 OK                    Standard success (GET, PUT, PATCH)
  201 Created               POST that created a resource
  204 No Content            Success, no body (DELETE)

  3xx REDIRECT
  301 Moved Permanently     Resource has a new URL forever
  302 Found                 Temporary redirect
  304 Not Modified          Client cache is still valid (ETag match)

  4xx CLIENT ERROR
  400 Bad Request           Malformed request, validation failure
  401 Unauthorized          Not authenticated (no/bad token)
  403 Forbidden             Authenticated but not authorized
  404 Not Found             Resource doesn't exist
  405 Method Not Allowed    Wrong HTTP verb for this URL
  409 Conflict              State conflict (duplicate, version mismatch)
  422 Unprocessable Entity  Validation error (alternative to 400)
  429 Too Many Requests     Rate limit exceeded

  5xx SERVER ERROR
  500 Internal Server Error Unhandled exception (your bug)
  502 Bad Gateway           Upstream service failed
  503 Service Unavailable   Overloaded or down for maintenance
  504 Gateway Timeout       Upstream service timed out

  COMMON MISTAKE:
  401 vs 403:
  401 = "I don't know who you are" (send credentials)
  403 = "I know who you are, but no" (don't bother retrying)
```

---

## REST

REST (Representational State Transfer) is an architectural style, not a protocol. "RESTful" APIs follow conventions that make them predictable.

### Resource-Based URL Design

```
  RESOURCES ARE NOUNS. VERBS GO IN HTTP METHODS.

  BAD (RPC-style):              GOOD (REST-style):
  POST /getUsers                GET  /users
  POST /createUser              POST /users
  POST /deleteUser/123          DELETE /users/123
  POST /getUserPosts/123        GET  /users/123/posts

  URL CONVENTIONS:
  Collection:   /users                  (all users)
  Item:         /users/{id}             (one user)
  Sub-resource: /users/{id}/posts       (user's posts)
  Sub-item:     /users/{id}/posts/{id}  (one of user's posts)

  Plural nouns.                  /users not /user
  Lowercase, hyphens.            /blog-posts not /blogPosts
  No trailing slash.             /users not /users/
  No verbs in URLs.              /users/123 not /users/getById/123

  FILTERING, SORTING, PAGINATION — query strings:
  GET /users?role=admin
  GET /users?sort=name&order=asc
  GET /users?page=2&limit=20
  GET /posts?search=typescript&tag=react
```

### Request and Response Shape

```
  GET /users/123
  Response 200:
  {
    "id": 123,
    "name": "Alice",
    "email": "alice@example.com",
    "createdAt": "2024-01-15T10:30:00Z"   ← ISO 8601, always UTC
  }

  POST /users
  Request body:
  {
    "name": "Bob",
    "email": "bob@example.com"
  }
  Response 201:
  {
    "id": 124,
    "name": "Bob",
    "email": "bob@example.com",
    "createdAt": "2024-02-22T08:15:00Z"
  }

  PATCH /users/124
  Request body (only fields to update):
  { "name": "Robert" }
  Response 200:
  { "id": 124, "name": "Robert", "email": "bob@example.com", ... }

  DELETE /users/124
  Response 204 (no body)

  ERROR RESPONSE (consistent shape matters):
  {
    "error": {
      "code": "VALIDATION_ERROR",
      "message": "Email is required",
      "details": [
        { "field": "email", "message": "Email is required" }
      ]
    }
  }
```

### Versioning

```
  THREE APPROACHES:

  1. URL versioning (most common, most visible):
     /api/v1/users
     /api/v2/users
     + Easy to route, easy to test, easy for clients
     - URL should represent a resource, not a version (purists object)

  2. Header versioning:
     GET /users
     Accept: application/vnd.myapi.v2+json
     + "Clean" URLs
     - Harder to test in browser, less discoverable

  3. Query string:
     GET /users?version=2
     + Simple
     - Pollutes resource URLs

  Microsoft REST API Guidelines use URL versioning: /v1/, /v2/
  That's what you'll see in Azure APIs. It's the pragmatic choice.

  BREAKING vs NON-BREAKING CHANGES:
  Non-breaking (no version bump needed):
  - Adding new optional fields to response
  - Adding new optional request parameters
  - Adding new endpoints

  Breaking (requires new version):
  - Removing fields from response
  - Renaming fields
  - Changing field types
  - Changing behavior of existing endpoint
```

---

## OpenAPI / Swagger

OpenAPI is the machine-readable contract for REST APIs. What WSDL was for SOAP — but vastly more usable.

```
  WSDL (SOAP era)              OpenAPI (REST era)
  ---------------              ------------------
  XML, verbose                 YAML or JSON
  Auto-generated only          Human-readable and writable
  Complex WS-* standards       Simple HTTP + JSON
  Visual Studio "Add Service   swagger-ui, openapi-generator,
  Reference" → generated code  many tools

  ECOSYSTEM:
  spec file (openapi.yaml)
       |
       +---> swagger-ui          Interactive browser UI (try API live)
       +---> openapi-generator   Generate typed clients in any language
       +---> zod-openapi         Generate Zod schemas from spec
       +---> prism               Mock server from spec
       +---> spectral            Lint your API spec

  CODE-FIRST vs SPEC-FIRST:
  Code-first:  Write routes → decorators generate OpenAPI spec
               (ASP.NET Swashbuckle does this; NestJS @nestjs/swagger)
  Spec-first:  Write openapi.yaml → generate server stubs + clients
               (more disciplined, API design separate from impl)
```

```yaml
  # openapi.yaml (abbreviated)
  openapi: "3.1.0"
  info:
    title: Users API
    version: "1.0"

  paths:
    /users/{id}:
      get:
        summary: Get a user
        parameters:
          - name: id
            in: path
            required: true
            schema: { type: integer }
        responses:
          "200":
            content:
              application/json:
                schema:
                  $ref: "#/components/schemas/User"
          "404":
            description: User not found

  components:
    schemas:
      User:
        type: object
        required: [id, name, email]
        properties:
          id:   { type: integer }
          name: { type: string }
          email: { type: string, format: email }
```

**OpenAPI = modern "Add Service Reference"**: Point `openapi-generator` at an `openapi.yaml`, run the generator, get a typed client in any language. This is exactly the "Add Service Reference" workflow from Visual Studio — the pattern is identical, the toolchain is different. The WSDL → generated C# proxy becomes openapi.yaml → generated TypeScript/C#/Python client. ASP.NET's Swashbuckle and NestJS's `@nestjs/swagger` are the code-first generators, equivalent to how WCF generated WSDL from your `[ServiceContract]` attributes.

---

## GraphQL

GraphQL (Facebook/Meta, 2015) flips the REST model: instead of the server defining what each endpoint returns, the **client specifies exactly what it needs**.

```
  REST: Multiple round trips, over-fetching common

  GET /users/123          → { id, name, email, bio, avatar, role, ... }
  GET /users/123/posts    → [{ id, title, body, tags, comments, ... }]
  GET /posts/456/comments → [{ id, text, author, ... }]

  3 requests. Over-fetch on every one.

  GraphQL: One request, exactly what you asked for

  POST /graphql
  {
    user(id: 123) {
      name
      avatar
      posts(limit: 5) {
        title
        commentCount
      }
    }
  }

  Response:
  {
    "data": {
      "user": {
        "name": "Alice",
        "avatar": "...",
        "posts": [
          { "title": "Intro to React", "commentCount": 12 },
          { "title": "TypeScript Tips", "commentCount": 5 }
        ]
      }
    }
  }

  One request. Exactly the fields requested. No over-fetch.
```

### GraphQL Schema Definition Language (SDL)

```graphql
  # The server defines types and capabilities
  type User {
    id: ID!          # ! = non-nullable
    name: String!
    email: String!
    posts: [Post!]!
    createdAt: String!
  }

  type Post {
    id: ID!
    title: String!
    body: String!
    author: User!
    commentCount: Int!
  }

  # Query = read operations
  type Query {
    user(id: ID!): User
    users(limit: Int, offset: Int): [User!]!
    post(id: ID!): Post
  }

  # Mutation = write operations
  type Mutation {
    createUser(name: String!, email: String!): User!
    updateUser(id: ID!, name: String): User!
    deleteUser(id: ID!): Boolean!
  }

  # Subscription = real-time (WebSocket)
  type Subscription {
    commentAdded(postId: ID!): Comment!
  }
```

### GraphQL Trade-Offs

```
  WINS:
  + Client gets exactly what it needs (no over/under-fetch)
  + Single endpoint (/graphql) for all operations
  + Strongly typed schema = automatic documentation
  + Great for complex, interconnected data (social graphs, CMSes)
  + Multiple clients (web, mobile) can request different shapes

  COSTS:
  - Caching is harder (HTTP GET caching doesn't apply to POST /graphql)
  - N+1 query problem (solved with DataLoader, but added complexity)
  - Complex queries can be expensive — need query depth limiting
  - Over-engineering for simple CRUD APIs
  - Learning curve: schema, resolvers, DataLoader

  BEST FIT:
  - Public APIs consumed by many client types
  - Complex domain with many relationships
  - Backend-for-frontend (BFF) layer aggregating multiple services
  - Content platforms (GitHub, Shopify, Contentful use GraphQL)
```

---

## tRPC — End-to-End Type Safety

tRPC (TypeScript Remote Procedure Call) takes a different approach: no schema language, no code generation. TypeScript IS the contract.

```
  REST:    Define routes → OpenAPI spec → generate client types
  GraphQL: Define SDL schema → generate TypeScript types
  tRPC:    Define TypeScript functions → types flow automatically

  +----------------+         +-------------------+
  | server/router.ts|         | client/component.tsx|
  |                 |         |                   |
  | const appRouter |         | const result =    |
  |  = router({     |  types  |   trpc.users      |
  |   users: {      | ~~~~~~> |     .getById      |
  |    getById:     |         |     .useQuery(123)|
  |     procedure   |         |                   |
  |      .input(    |         | result.data?.name |
  |       z.number()| ←───────|   ↑ TypeScript    |
  |      )          |         |   knows the shape |
  |      .query(...)| ─────── |   of this!        |
  |   }             |         |                   |
  | })              |         |                   |
  +----------------+         +-------------------+
```

```typescript
  // server/router.ts
  import { z } from 'zod'
  import { router, publicProcedure } from './trpc'

  export const appRouter = router({
    users: router({
      getById: publicProcedure
        .input(z.number())
        .query(async ({ input: id }) => {
          return db.user.findUnique({ where: { id } })
          // Return type inferred from Prisma — no manual typing
        }),

      create: publicProcedure
        .input(z.object({
          name: z.string().min(1),
          email: z.string().email(),
        }))
        .mutation(async ({ input }) => {
          return db.user.create({ data: input })
        }),
    })
  })

  export type AppRouter = typeof appRouter  // this type is shared with client
```

```typescript
  // client/UserProfile.tsx
  import { trpc } from '../utils/trpc'

  function UserProfile({ id }: { id: number }) {
    const user = trpc.users.getById.useQuery(id)
    //                               ↑
    //    TypeScript knows: input is number, output shape is Prisma User
    //    No separate type file. No code generation step.

    if (user.isLoading) return <Spinner />
    return <div>{user.data?.name}</div>  // ← autocomplete works here
  }
```

```
  tRPC TRADE-OFFS:

  WINS:
  + Zero-overhead type safety (types inferred, not generated)
  + No schema file to maintain
  + Input validation with Zod built in
  + Integrates with TanStack Query on client
  + Refactor a procedure name → TypeScript errors guide all clients

  COSTS:
  - TypeScript only. Non-TS clients can't use it.
  - Server and client must share code (monorepo or package)
  - Not suitable for public APIs (external consumers)
  - Less ecosystem tooling than REST/GraphQL

  BEST FIT:
  - Full-stack TypeScript monorepo (Next.js app + API)
  - Small-medium team, single codebase
  - Internal APIs not consumed by external clients
  - When you want REST-like simplicity with type safety
```

**tRPC = WCF's typed service contracts without the generation step**: WCF's `[ServiceContract]` + `[OperationContract]` defined a strongly-typed interface, client stubs were generated, and the compiler enforced the contract at both ends. tRPC achieves the same guarantee without any generation step — TypeScript structural typing flows across the client/server boundary at build time via the shared `AppRouter` type. The key improvement over WCF's model: WCF's "Add Service Reference" broke silently if you changed the service contract without re-running the generator. tRPC's type inference is live — rename a procedure and TypeScript immediately errors everywhere it's used, with no generation step. The contract is not a generated artifact; it is the source code itself.

---

## Node.js Backend Frameworks

### Express — The Baseline

```typescript
  import express, { Request, Response, NextFunction } from 'express'
  import cors from 'cors'

  const app = express()

  // Middleware (runs for every request, in order)
  app.use(cors())
  app.use(express.json())              // parse JSON body
  app.use(express.urlencoded({ extended: true }))

  // Route handlers
  app.get('/users', async (req: Request, res: Response) => {
    const users = await db.user.findMany()
    res.json(users)
  })

  app.get('/users/:id', async (req, res) => {
    const user = await db.user.findUnique({
      where: { id: parseInt(req.params.id) }
    })
    if (!user) return res.status(404).json({ error: 'Not found' })
    res.json(user)
  })

  app.post('/users', async (req, res) => {
    const user = await db.user.create({ data: req.body })
    res.status(201).json(user)
  })

  // Error handling middleware (4 params = error handler)
  app.use((err: Error, req: Request, res: Response, next: NextFunction) => {
    console.error(err)
    res.status(500).json({ error: 'Internal server error' })
  })

  app.listen(3000)
```

### The Middleware Pipeline

This is the most important Express concept, and it maps directly to ASP.NET's middleware pipeline:

```
  ASP.NET Core middleware:          Express middleware:
  app.UseHttpsRedirection()         app.use(httpsRedirect())
  app.UseRouting()                  (built in)
  app.UseCors()                     app.use(cors())
  app.UseAuthentication()           app.use(passport.initialize())
  app.UseAuthorization()            app.use(requireAuth())
  app.UseEndpoints(...)             app.get('/route', handler)

  Both are pipelines. Request flows through middleware in order.
  Each middleware can: pass through (next()), respond, or error.

  REQUEST
    │
    ▼
  cors()          sets CORS headers, calls next()
    │
    ▼
  express.json()  parses body, attaches to req.body, calls next()
    │
    ▼
  requireAuth()   checks token, calls next() or returns 401
    │
    ▼
  route handler   runs your business logic, sends response
    │
    ▼
  error handler   catches any errors thrown above
```

### Router Organization

```typescript
  // routes/users.ts
  import { Router } from 'express'

  const router = Router()

  router.get('/',    listUsers)
  router.post('/',   createUser)
  router.get('/:id', getUser)
  router.patch('/:id', updateUser)
  router.delete('/:id', deleteUser)

  export default router

  // app.ts
  app.use('/api/users',    usersRouter)
  app.use('/api/posts',    postsRouter)
  app.use('/api/auth',     authRouter)
```

### Fastify — The Fast Alternative

```typescript
  import Fastify from 'fastify'
  import { z } from 'zod'

  const app = Fastify({ logger: true })

  // Schema validation built in (JSON Schema, faster than manual validation)
  app.get<{ Params: { id: string } }>('/users/:id', {
    schema: {
      params: { type: 'object', properties: { id: { type: 'string' } } },
      response: { 200: { $ref: 'User#' } }
    }
  }, async (request, reply) => {
    const user = await db.user.findUnique({ where: { id: request.params.id } })
    if (!user) return reply.status(404).send({ error: 'Not found' })
    return user
  })

  // Fastify vs Express:
  // + 2-3x faster (benchmarks vary)
  // + Built-in schema validation + serialization
  // + Built-in TypeScript support
  // + Plugin system with encapsulation
  // - Smaller ecosystem than Express
  // - Less familiar to most developers
```

### NestJS — The Angular-Style Framework

The most familiar to .NET/enterprise developers. Decorators, DI, modules — same patterns as Angular and ASP.NET.

```typescript
  // users.controller.ts
  @Controller('users')
  export class UsersController {
    constructor(private usersService: UsersService) {}  // DI!

    @Get()
    findAll(): Promise<User[]> {
      return this.usersService.findAll()
    }

    @Get(':id')
    findOne(@Param('id') id: string): Promise<User> {
      return this.usersService.findOne(+id)
    }

    @Post()
    @HttpCode(201)
    create(@Body() createUserDto: CreateUserDto): Promise<User> {
      return this.usersService.create(createUserDto)
    }

    @Patch(':id')
    update(@Param('id') id: string, @Body() dto: UpdateUserDto): Promise<User> {
      return this.usersService.update(+id, dto)
    }

    @Delete(':id')
    @HttpCode(204)
    remove(@Param('id') id: string): Promise<void> {
      return this.usersService.remove(+id)
    }
  }

  // users.service.ts
  @Injectable()
  export class UsersService {
    constructor(private prisma: PrismaService) {}  // DI all the way down

    findAll() { return this.prisma.user.findMany() }
    findOne(id: number) { return this.prisma.user.findUnique({ where: { id } }) }
    create(dto: CreateUserDto) { return this.prisma.user.create({ data: dto }) }
  }

  // users.module.ts
  @Module({
    controllers: [UsersController],
    providers: [UsersService],
    exports: [UsersService]
  })
  export class UsersModule {}
```

```
  NestJS maps to .NET like this:

  ASP.NET MVC               NestJS
  -----------               ------
  Controller                @Controller
  Service / Repository      @Injectable service
  Module / Assembly         @Module
  Dependency Injection      @Injectable + constructor injection
  [FromBody]                @Body()
  [FromRoute]               @Param()
  [FromQuery]               @Query()
  ActionResult / IResult    return value (auto-serialized)
  Middleware                NestJS middleware / interceptors / guards
  Filters (exception)       @Catch() exception filters
  ASP.NET attributes        NestJS decorators (same concept)
  Swagger (Swashbuckle)     @nestjs/swagger (same concept)
```

---

## Input Validation with Zod

Validation at the API boundary is mandatory. Zod is the standard in TypeScript backends.

```typescript
  import { z } from 'zod'

  const CreateUserSchema = z.object({
    name:  z.string().min(1).max(100),
    email: z.string().email(),
    role:  z.enum(['admin', 'user', 'guest']).default('user'),
    age:   z.number().int().min(0).max(150).optional(),
  })

  // Infer TypeScript type from schema
  type CreateUserDto = z.infer<typeof CreateUserSchema>

  // In Express route:
  app.post('/users', async (req, res) => {
    const result = CreateUserSchema.safeParse(req.body)
    if (!result.success) {
      return res.status(400).json({
        error: 'Validation failed',
        details: result.error.flatten()
      })
    }
    const user = await db.user.create({ data: result.data })
    res.status(201).json(user)
  })
```

---

## Serverless and Edge Functions

```
  TRADITIONAL SERVER:
  +------------------+
  | Node.js process  |  Always running
  | (Express/Fastify)|  You pay 24/7
  | Azure App Service|  You manage scaling
  +------------------+

  SERVERLESS FUNCTION:
  +------------------+
  | Function (code)  |  Spins up per request
  | Azure Functions  |  Scales to zero (pay per execution)
  | AWS Lambda       |  Cloud manages scaling
  | Vercel Functions |  Cold start: 100-500ms on first request
  +------------------+

  EDGE FUNCTION:
  +------------------+
  | Function (code)  |  Runs at CDN edge (close to user)
  | Cloudflare       |  ~0ms cold start (V8 isolates, not Node.js)
  | Vercel Edge      |  Restricted APIs (no Node.js built-ins)
  | Deno Deploy      |  ~5-50ms globally
  +------------------+

  Next.js route handlers can run as:
  export const runtime = 'nodejs'   // default, full Node.js
  export const runtime = 'edge'     // edge function (limited APIs)
```

---

## Common Confusion Points

### "REST vs HTTP API — what's the difference?"

```
  All REST APIs are HTTP APIs.
  Not all HTTP APIs are RESTful.

  An HTTP API that does POST /getUser is not REST — it uses
  HTTP as a tunnel, ignoring verbs, status codes, URL conventions.

  REST uses HTTP semantics intentionally:
  verbs as actions, URLs as resource addresses,
  status codes as outcome signals, headers for metadata.

  "REST" is often used loosely to mean "JSON over HTTP."
  Purists will correct you. In practice: design your API to follow
  REST conventions and nobody will complain about terminology.
```

### "PUT vs PATCH — which one?"

```
  PUT:   Replace the ENTIRE resource.
         Fields not included are set to null/default.
         PUT /users/1 { name: "Alice" }  → email is now null
         Client must send the complete representation.

  PATCH: Partial update. Send only changed fields.
         PATCH /users/1 { name: "Alice" }  → email unchanged
         Client sends only what changed.

  Rule of thumb: Use PATCH for updates.
  Use PUT only when you genuinely mean "replace everything."
```

### "How do I handle auth in an Express API?"

```
  Auth is covered fully in 10-AUTH.md.
  Short version:

  1. Client sends JWT in Authorization header:
     Authorization: Bearer eyJhbGci...

  2. Middleware extracts + verifies token:
     app.use(authMiddleware)

  3. Middleware attaches user to request:
     req.user = { id: 123, role: 'admin' }

  4. Route handlers use req.user:
     if (req.user.role !== 'admin') return res.status(403).json(...)
```

### "GraphQL vs REST — just pick one?"

```
  They solve different things and can coexist.

  Many large systems use REST for simple CRUD and GraphQL for
  complex data-fetching scenarios.

  GitHub API has both: REST v3 and GraphQL v4.
  The GraphQL API is preferred for complex queries;
  REST is fine for simple operations (create issue, get repo).

  For a new project:
  - Simple CRUD app with a few clients → REST + OpenAPI
  - Complex data, many client types, mobile + web → GraphQL
  - Full-stack TypeScript monorepo, internal API → tRPC
```

---

## Old World → New World Bridge

| ASP.NET / WCF / .NET concept | Node.js backend equivalent | Notes |
|---|---|---|
| ASP.NET MVC Controller | Express Router / NestJS Controller | Same concept |
| `[HttpGet]`, `[HttpPost]` | `app.get()`, `app.post()` | HTTP verb routing |
| `[Route("api/users/{id}")]` | `app.get('/api/users/:id')` | Route templates |
| `[FromBody]` | `req.body` (with `express.json()`) | Body parsing middleware |
| `[FromQuery]` | `req.query` | Query string params |
| `[FromRoute]` | `req.params` | Route params |
| `ActionResult` / `IResult` | `res.json()`, `res.status(n).json()` | Response helpers |
| `ModelState.IsValid` | Zod `safeParse()` | Input validation |
| Data Annotations (`[Required]`) | Zod schema | Declarative validation |
| `IActionFilter` / Middleware | Express middleware | Request/response pipeline |
| `IExceptionFilter` | Express error handler `(err, req, res, next)` | Global error handling |
| WCF `[ServiceContract]` / `[OperationContract]` | tRPC router + procedures | tRPC = live TypeScript contract; no generation step |
| WCF service contract (public) | OpenAPI spec / GraphQL SDL | Machine-readable API contract |
| WSDL | openapi.yaml | Contract file |
| "Add Service Reference" | `openapi-generator` / `graphql-codegen` | Point at spec, get typed client |
| `HttpClient` (consuming) | `fetch()` / `axios` | HTTP client |
| IIS hosting | Azure App Service (Node.js) / Vercel / Railway | Cloud hosting |
| Azure Functions (.NET) | Azure Functions (Node.js) / Vercel Functions | Serverless |
| Swagger UI (Swashbuckle) | swagger-ui-express / built into NestJS | Interactive API docs |
| `appsettings.json` | `.env` + `dotenv` | Environment config |
| Dependency Injection container | NestJS DI / manual composition | DI pattern |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Build a public API consumed by many clients | REST + OpenAPI |
| Build an internal API in a TypeScript monorepo | tRPC |
| Build an API for a complex graph of data (social, CMS) | GraphQL |
| Get started quickly with minimal boilerplate | Express |
| Need maximum performance in Node.js | Fastify |
| Want Angular/ASP.NET-style structure with DI | NestJS |
| Deploy to edge (Cloudflare Workers, Vercel Edge) | Hono |
| Validate incoming request body | Zod `safeParse()` |
| Document my REST API | OpenAPI spec + swagger-ui |
| Generate typed client from REST API | `openapi-generator` or `orval` (same as "Add Service Reference") |
| Handle real-time (chat, live updates) | WebSockets (`ws`) or Server-Sent Events |
| Scale to zero, pay per request | Serverless (Azure Functions, Vercel) |
| Run code close to the user globally | Edge functions |
| Need ASP.NET-style error filters and guards | NestJS |
| Consume an external REST API | `fetch()` (built-in) or `axios` |
