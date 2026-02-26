# 11 — Containers & Docker

## The Big Picture

```
The Packaging Problem
=====================

Old World                          New World
=========                          =========

  Dev machine                        Container Image
  ┌──────────────────┐               ┌──────────────────┐
  │ Windows 10       │               │ App code         │
  │ IIS 10           │               │ Runtime (Node 20) │
  │ .NET 6 (GAC)     │   ────────►   │ OS libs          │
  │ App code         │               │ Config           │
  │ web.config       │               └──────────────────┘
  │ Manual installs  │                        │
  └──────────────────┘               runs identically on:
                                     Dev → CI → Staging → Prod
  "Works on my machine"              "Ship the environment, not just the code"
```

<!-- @editor[diagram/P1]: No landscape diagram showing the image layer model (Union FS / overlay filesystem concept). The calibration note specifically calls out: "image layer model, Union FS, Dockerfile instruction caching — need landscape diagram." The two diagrams present are a problem/solution framing and an architecture diagram, neither shows the layered image model as a landscape. That diagram belongs here, between the intro and the first ##, before the Containers vs VMs section. -->

<!-- @editor[bridge/P2]: The "immutable artifacts, port-forward not file-system access" philosophy is the key conceptual shift from IIS deployment (xcopy, web.config, file-system layout). That bridge is implied but never stated explicitly. The learner's mental model is: deploy = copy files to a directory IIS watches. The container model is: build an artifact, run it, the filesystem inside is ephemeral. This needs a named bridge at this intro section: "IIS deployment / xcopy → containerization philosophy." -->

```
Docker Architecture — Three Pieces
===================================

  ┌─────────────────────────────────────────────────────────────────┐
  │  Your machine                                                   │
  │                                                                 │
  │   CLI                  Docker Daemon              Registry      │
  │  ┌─────────┐           ┌───────────────┐         ┌───────────┐ │
  │  │ docker  │──────────►│               │◄────────│Docker Hub │ │
  │  │  build  │   API     │  Manages:     │  push/  │  GHCR     │ │
  │  │  run    │           │  - Images     │  pull   │  ACR      │ │
  │  │  push   │           │  - Containers │         │  ECR      │ │
  │  │  pull   │           │  - Networks   │         └───────────┘ │
  │  │  compose│           │  - Volumes    │                       │
  │  └─────────┘           └───────────────┘                       │
  │                                                                 │
  └─────────────────────────────────────────────────────────────────┘

  CLI = what you type
  Daemon = background service that does the work (dockerd)
  Registry = remote image storage (like NuGet for images)
```

---

## Containers vs VMs

```
Virtual Machines                   Containers
================                   ==========

  ┌────────────────────┐            ┌────────────────────┐
  │  App A             │            │  App A             │
  ├────────────────────┤            ├────────────────────┤
  │  Guest OS (full)   │            │  App libs/deps     │
  │  (2-4 GB)          │            │  (MBs)             │
  ├────────────────────┤            ├────────────────────┤
  │  Hypervisor        │            │  Container Runtime │
  │  (VMware/Hyper-V)  │            │  (containerd)      │
  ├────────────────────┤            ├────────────────────┤
  │  Host OS           │            │  Host OS (shared)  │
  ├────────────────────┤            ├────────────────────┤
  │  Hardware          │            │  Hardware          │
  └────────────────────┘            └────────────────────┘

  Each VM = full OS copy              All containers share host kernel
  Boot time: minutes                  Start time: milliseconds
  Size: GBs                           Size: MBs
  Strong isolation                    Process isolation
  Good for: different OSes            Good for: many instances of same app
```

Key insight: containers are **processes with guardrails**, not lightweight VMs. A container is a Linux process isolated via kernel namespaces (PID, network, filesystem) and limited by cgroups (CPU, memory). On Windows/Mac, Docker runs a lightweight Linux VM to host the daemon — the containers still run Linux.

<!-- @editor[bridge/P3]: The Hyper-V reference is good but the learner ran Azure VMs / Service Fabric on Hyper-V at scale. A one-line note that "Windows Containers exist but the ecosystem is Linux-first — even on AKS, Windows node pools are a second-class citizen" would prevent a common misconception for someone coming from a Windows-first background. -->

---

## Images vs Containers

```
Image                              Container
=====                              =========

Read-only template                 Running instance of an image
Like a class                       Like an object (instantiation)
Stored on disk / registry          Lives in memory + ephemeral layer
Can have multiple versions/tags    Has its own writable layer on top
Built by: docker build             Created by: docker run

  Image layers (read-only, cached)
  ┌──────────────────────────┐
  │  Your app code (COPY)    │  ← layer 4
  ├──────────────────────────┤
  │  npm install (RUN)       │  ← layer 3 (cached if package.json unchanged)
  ├──────────────────────────┤
  │  OS libs (RUN apt-get)   │  ← layer 2 (rarely changes)
  ├──────────────────────────┤
  │  Base: node:20-alpine    │  ← layer 1 (pulled once, shared by many images)
  └──────────────────────────┘
            +
  ┌──────────────────────────┐
  │  Writable container layer│  ← ephemeral — gone when container stops
  └──────────────────────────┘   (unless you mount a volume)
```

<!-- @editor[bridge/P2]: The layer model here is good but missing the Union FS / overlay filesystem explanation that gives this model its "why." The learner knows how NTFS and GAC work (shared DLLs, file-system overlays at the OS level). The bridge: layers are implemented as an overlay filesystem — each layer is a directory diff, and the Union FS merges them into a single coherent view at runtime. This is the "how" behind why layers are cached and shared across images. One ASCII diagram showing the overlay mount would complete this section. -->

**The caching rule**: Docker rebuilds a layer and all layers below it when that layer's inputs change. Put things that change rarely (OS deps, package install) near the bottom, things that change often (app code) near the top.

---

## Dockerfile

### Basic — Node.js API

```dockerfile
# Start from official Node 20 on Alpine Linux (~50MB vs ~1GB full Debian)
FROM node:20-alpine

# Set working directory inside container
WORKDIR /app

# Copy dependency manifests first (cache optimization)
COPY package.json package-lock.json ./

# Install deps — this layer is cached until package*.json changes
RUN npm ci --only=production

# Copy the rest of the source
COPY . .

# Tell Docker which port the app listens on (documentation only — doesn't publish)
EXPOSE 3000

# Default command to run when container starts
CMD ["node", "src/index.js"]
```

<!-- @editor[bridge/P2]: `EXPOSE` says "documentation only — doesn't publish" but this is the crux of the port-forward model shift. The IIS mental model is: bind to port 80/443, IIS routing handles it at the host OS level. The container mental model is: app binds inside its isolated network namespace, you explicitly map host:container ports with `-p`. The learner will hit this when they wonder "why doesn't my container respond on port 3000?" A one-paragraph bridge here: "Unlike IIS bindings which operate at the host OS level, a container's network is isolated. EXPOSE declares intent; -p 3000:3000 (or ports: in Compose) does the actual mapping at the host." -->

### Why COPY package.json first?

```
Without split COPY:              With split COPY:
===================              ================

COPY . .                         COPY package*.json ./
RUN npm install                  RUN npm install    ← cached until deps change
                                 COPY . .

Every code change →              Code change →
  invalidates npm install          only re-runs COPY . .
  rebuilds all deps                npm install hits cache
  slow rebuild                     fast rebuild
```

### Multi-Stage Build

Build tools and test code should not go into the production image. Multi-stage builds let you compile in one stage and copy only the output.

```dockerfile
# ── Stage 1: Build ──────────────────────────────────────────────
FROM node:20-alpine AS builder

WORKDIR /app
COPY package*.json ./
RUN npm ci                        # full deps including devDependencies

COPY . .
RUN npm run build                 # TypeScript compile → dist/

# ── Stage 2: Production ─────────────────────────────────────────
FROM node:20-alpine AS production

WORKDIR /app
COPY package*.json ./
RUN npm ci --only=production      # production deps only

COPY --from=builder /app/dist ./dist    # copy compiled output from stage 1

EXPOSE 3000
CMD ["node", "dist/index.js"]

# Result: production image has no TypeScript, no ts-node, no test libs
# Image size: ~120MB instead of ~800MB
```

### Next.js Multi-Stage (common pattern)

```dockerfile
FROM node:20-alpine AS deps
WORKDIR /app
COPY package*.json ./
RUN npm ci

FROM node:20-alpine AS builder
WORKDIR /app
COPY --from=deps /app/node_modules ./node_modules
COPY . .
RUN npm run build

FROM node:20-alpine AS runner
WORKDIR /app
ENV NODE_ENV production
COPY --from=builder /app/public ./public
COPY --from=builder /app/.next/standalone ./
COPY --from=builder /app/.next/static ./.next/static
EXPOSE 3000
CMD ["node", "server.js"]
```

---

## .dockerignore

Like `.gitignore` — prevents bloating the build context sent to the daemon. Without it, Docker copies your entire project directory (including `node_modules`, `.git`, etc.) before the build starts.

```
node_modules
.git
.gitignore
Dockerfile
docker-compose*.yml
*.md
.env
.env.*
dist
.next
coverage
```

---

## Key Docker CLI Commands

### Build

```bash
# Build image from Dockerfile in current directory
docker build -t myapp:latest .

# Build with specific Dockerfile
docker build -f Dockerfile.prod -t myapp:prod .

# Build specific stage only (useful for CI)
docker build --target builder -t myapp-builder .

# Build with build args (not for secrets)
docker build --build-arg NODE_ENV=production -t myapp .
```

### Run

```bash
# Run container (pulls image if not local)
docker run myapp:latest

# Run in background (detached)
docker run -d myapp:latest

# Run with port mapping (host:container)
docker run -d -p 3000:3000 myapp:latest

# Run with env vars
docker run -d -e DATABASE_URL=postgres://... myapp:latest

# Run with volume mount
docker run -d -v $(pwd)/data:/app/data myapp:latest

# Run interactively (debug / explore)
docker run -it myapp:latest sh

# Run with name (easier to reference)
docker run -d --name api myapp:latest

# Run and auto-remove when stopped
docker run --rm myapp:latest
```

### Inspect Running Containers

```bash
docker ps                          # running containers
docker ps -a                       # all containers (including stopped)
docker logs api                    # stdout/stderr of container "api"
docker logs -f api                 # follow (tail -f equivalent)
docker exec -it api sh             # open shell in running container
docker inspect api                 # full JSON config and state
docker stats                       # live CPU/memory/network usage
```

### Images

```bash
docker images                      # list local images
docker image rm myapp:latest       # delete image
docker image prune                 # remove dangling (untagged) images
docker system prune                # nuclear option — removes stopped containers,
                                   # unused networks, dangling images
```

### Registry

```bash
# Docker Hub
docker login
docker tag myapp:latest username/myapp:latest
docker push username/myapp:latest

# Azure Container Registry
az acr login --name myregistry
docker tag myapp myregistry.azurecr.io/myapp:latest
docker push myregistry.azurecr.io/myapp:latest
docker pull myregistry.azurecr.io/myapp:latest
```

---

## Docker Compose

Docker Compose defines multi-container applications as code. One file describes your whole local stack — app, database, cache — and `docker compose up` boots all of it.

<!-- @editor[structure/P1]: Missing explicit Docker Compose vs Kubernetes scope boundary. The calibration note flags: "Docker Compose vs K8s distinction must be clear." Compose is a local-dev / single-host tool; K8s is a production orchestrator. This belongs as a named box at the start of this section — not a footnote. The learner will naturally conflate them (both define multi-container apps as YAML). A clear "Compose scope: one machine, one developer" vs "K8s scope: cluster, production, auto-healing" diagram is needed here. -->

### Full Example: App + Postgres + Redis

```yaml
# docker-compose.yml
version: "3.9"

services:
  # ── Your application ─────────────────────────────────────────
  api:
    build:
      context: .
      dockerfile: Dockerfile
      target: production            # use production stage of multi-stage build
    ports:
      - "3000:3000"                 # host:container
    environment:
      NODE_ENV: production
      DATABASE_URL: postgres://postgres:password@postgres:5432/mydb
      REDIS_URL: redis://redis:6379
    env_file:
      - .env.local                  # load additional secrets from file
    depends_on:
      postgres:
        condition: service_healthy  # wait for healthcheck, not just startup
      redis:
        condition: service_started
    volumes:
      - ./uploads:/app/uploads      # bind mount for user uploads
    restart: unless-stopped

  # ── PostgreSQL ───────────────────────────────────────────────
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_DB: mydb
      POSTGRES_USER: postgres
      POSTGRES_PASSWORD: password
    volumes:
      - postgres_data:/var/lib/postgresql/data  # named volume (persists)
      - ./init.sql:/docker-entrypoint-initdb.d/init.sql  # seed on first start
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U postgres"]
      interval: 5s
      timeout: 5s
      retries: 5
    ports:
      - "5432:5432"                 # expose for local tools (TablePlus, etc.)

  # ── Redis ────────────────────────────────────────────────────
  redis:
    image: redis:7-alpine
    volumes:
      - redis_data:/data
    ports:
      - "6379:6379"

volumes:
  postgres_data:                    # Docker manages this volume's location
  redis_data:
```

### Compose Commands

```bash
docker compose up                   # start all services (foreground)
docker compose up -d                # start all services (background)
docker compose up api               # start only the api service
docker compose down                 # stop and remove containers
docker compose down -v              # also remove named volumes (wipes DB)
docker compose logs -f api          # follow logs for one service
docker compose exec api sh          # shell into running api container
docker compose build                # rebuild images
docker compose pull                 # pull latest base images
docker compose ps                   # status of all services
```

### Note: `docker-compose` vs `docker compose`

- `docker-compose` — old standalone binary (v1, Python, deprecated)
- `docker compose` — new plugin built into Docker CLI (v2, Go)

Use `docker compose` (no hyphen). The old binary is being phased out.

---

## Volumes — Named vs Bind Mount

```
Named Volume                       Bind Mount
============                       ==========

volumes:                           volumes:
  - postgres_data:/var/lib/pgsql     - ./src:/app/src

Docker manages location            Host path maps directly
Survives container removal         Changes on host = immediate in container
Best for: databases, state         Best for: development hot-reload
Opaque to host                     Transparent to host
```

```bash
docker volume ls                   # list named volumes
docker volume inspect postgres_data
docker volume rm postgres_data     # manual removal (also: compose down -v)
```

---

## Environment Variables & Secrets

**Rule: never bake secrets into an image.** Images are often pushed to registries. Anything in the image layer is readable.

```
Wrong:                             Right:
======                             ======

ENV DATABASE_URL=postgres://       Pass at runtime:
  user:realpassword@host/db          docker run -e DATABASE_URL=...

                                   Use env_file:
RUN echo "secret" > /app/.env        env_file: [.env.local]

                                   Use Docker Secrets (Swarm/K8s):
                                     secrets: [db_password]
```

Build args (`--build-arg`) are slightly better but still baked into image history. Use them only for non-sensitive values like `NODE_ENV`, `BUILD_VERSION`.

---

## Registries

```
Registry           Hosted By       Use Case
────────────────────────────────────────────────────────
Docker Hub         Docker          Public images, official base images
GHCR               GitHub          Private images tied to GitHub repos
ACR                Azure           Azure-native, integrates with AKS/ACA
ECR                AWS             AWS-native, integrates with ECS/EKS
GAR                GCP             GCP-native
Self-hosted        You             Air-gapped, on-prem (Harbor, Nexus)
```

Image naming convention:
```
registry/organization/image:tag
────────────────────────────────────────────────────────
nginx                              → Docker Hub official image
username/myapp:1.2.3               → Docker Hub user image
ghcr.io/org/myapp:latest           → GHCR
myregistry.azurecr.io/myapp:v1.0   → ACR
```

---

## Networking

Containers on the same Compose network can reach each other by **service name**. No IPs needed.

```yaml
services:
  api:
    ...
    environment:
      # "postgres" resolves to the postgres container's IP automatically
      DATABASE_URL: postgres://postgres:5432/mydb
      #                       ^^^^^^^^
      #                       service name, not localhost
```

```
External request                   Internal traffic
================                   ================

  Browser → localhost:3000           api → postgres:5432
                 ↓                   (resolved by Docker's internal DNS)
  Host port 3000
                 ↓
  Container port 3000 (api service)

ports: ["3000:3000"] exposes        No ports: needed for internal-only
```

<!-- @editor[bridge/P2]: No bridge to IIS binding / host header routing model. The learner configured IIS with site bindings, ARR for reverse proxy, and host headers extensively. The Docker networking model (every container gets a virtual NIC on a bridge network, service names resolve via embedded DNS) is a different mental model entirely. Worth a named comparison: "IIS: all apps share the host's network stack, differentiated by port/host header. Docker: each container has an isolated network namespace; inter-container traffic goes through a virtual bridge." -->

Common mistake: using `localhost` inside a container to reach another container. `localhost` inside the api container means *the api container itself*, not the host machine or postgres. Use the service name.

---

## Common Confusion Points

**Changes to code aren't appearing in the running container.**
You edited `src/index.js` on the host. The running container has a baked-in copy from `docker build`. You need to rebuild: `docker compose build api && docker compose up -d api`. Or use a bind mount in dev so the container reads live files.

**Container exits immediately after `docker run`.**
The process in `CMD` finished. Containers run as long as their main process runs. If your `CMD` is a one-shot script, the container exits when it completes. For a server, the process must stay in the foreground — `node server.js`, not `npm start` wrapping a script that backgrounded itself.

**`docker compose` vs `docker-compose`.**
See above. Use `docker compose` (space, not hyphen). The hyphenated version is legacy.

**`COPY` vs `ADD`.**
`COPY` copies files from build context to image. `ADD` does everything `COPY` does plus: auto-extracts tar archives, supports URLs. Use `COPY` unless you specifically need `ADD`'s extra features.

**`CMD` vs `ENTRYPOINT`.**
```
ENTRYPOINT ["node"]          # fixed executable — cannot override with docker run args
CMD ["src/index.js"]         # default arg — overridable: docker run myapp other.js

# Most common: use ENTRYPOINT for the binary, CMD for default args
# Or just use CMD ["node", "src/index.js"] for simplicity
```

**Build context is huge / build is slow.**
The first `docker build` step is "sending build context to daemon." Everything not in `.dockerignore` gets sent. Add `node_modules`, `.git`, `dist` to `.dockerignore`.

**"Port already in use" error.**
Another process (or previous container) is bound to that host port. `docker ps` to find it. `docker stop <name>` to stop it. Or change the host port mapping.

<!-- @editor[content/P2]: Missing confusion point: "Docker Compose is not a replacement for Kubernetes." This is the most common conceptual conflation for someone learning both. Compose has no health-based restart (only `restart: unless-stopped`), no rolling updates, no cross-host networking, no resource scheduling. It belongs in Common Confusion Points given the calibration note explicitly flags the Compose vs K8s distinction. -->

---

## Old World Bridge

| Azure / IIS / Windows Concept | Docker Equivalent |
|-------------------------------|-------------------|
| VM image (VHD/VHDX) | Docker image |
| Provisioned VM | Running container |
| MSI installer | Dockerfile / base image |
| IIS + App Pool | App server embedded in container (Kestrel, Express) |
| web.config / app.config | Environment variables / mounted config files |
| Azure App Service Plan | Azure Container Apps / AKS Node Pool |
| Azure Container Registry | ACR (same name, now for containers not packages) |
| NuGet feed | Container registry |
| Shared assemblies (GAC) | Base image layers (shared, cached) |
| Deployment slot | Blue/green containers behind a load balancer |
| VSTS Build pipeline | CI pipeline → `docker build` → `docker push` |

<!-- @editor[bridge/P2]: The Old World Bridge table is missing the xcopy / robocopy deployment → immutable image build bridge. The learner's deep mental model for deployment is: build artifacts, xcopy to target directory, recycle App Pool. The container model inverts this: the image IS the deployment artifact (immutable), you don't copy files to a running container. This is the single most important conceptual shift and it isn't in the table. Add: "xcopy deploy / App Pool recycle → docker build + docker run (image is immutable; you replace the container, not the files inside it)." -->

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Package my app for consistent deploys | `Dockerfile` + `docker build` |
| Run my app locally | `docker run` or `docker compose up` |
| Run app + database + cache locally | `docker-compose.yml` with services |
| Keep database data between restarts | Named volume |
| Edit code and see changes immediately | Bind mount (`./src:/app/src`) |
| Reduce production image size | Multi-stage build |
| Share image with team / CI | Push to registry (GHCR, ACR) |
| Pull latest base images | `docker compose pull` |
| Debug inside a running container | `docker exec -it <name> sh` |
| See what's eating disk space | `docker system df` |
| Nuclear cleanup | `docker system prune -a` |
| Deploy to Azure serverless | Azure Container Apps (ACA) |
| Deploy to Azure Kubernetes | AKS — next module |
