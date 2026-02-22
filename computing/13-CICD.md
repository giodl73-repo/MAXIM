# 13 — CI/CD Modern

## The Big Picture

```
CI/CD — What It Actually Is
=============================

  Continuous Integration (CI)          Continuous Delivery/Deployment (CD)
  ============================          =====================================

  Every push → automated pipeline      Verified build → automated deploy

  ┌─────────────────────────┐           ┌──────────────────────────────────┐
  │  push / pull request    │           │  merge to main                   │
  │         ↓               │           │         ↓                        │
  │  lint + type check      │           │  build artifact                  │
  │         ↓               │           │         ↓                        │
  │  unit tests             │           │  deploy to staging               │
  │         ↓               │           │         ↓                        │
  │  integration tests      │           │  smoke tests                     │
  │         ↓               │           │         ↓                        │
  │  security scan          │           │  deploy to production            │
  │         ↓               │           │  (automatic or with approval)    │
  │  ✅ / ❌ status on PR   │           └──────────────────────────────────┘
  └─────────────────────────┘

  CI = fast feedback on every change
  CD = the change reaches production reliably and repeatably
```

```
The Two Major Platforms
========================

  GitHub Actions                       Azure Pipelines
  ==============                       ===============

  Runs where your code lives           Microsoft's platform (VSTS lineage)
  yaml in .github/workflows/           yaml in azure-pipelines.yml
  Native GitHub integration            Native Azure / ADO integration
  Marketplace (10,000+ actions)        Tasks, extensions
  Free tier for public repos           Free tier (parallel jobs)
  Minutes charged for private          Self-hosted agents common
  GitHub-hosted runners                Azure DevOps / self-hosted agents

  Choose if:                           Choose if:
    Already on GitHub                    ADO is your source of truth
    Want ecosystem simplicity            Azure deployments (ARM/Bicep native)
    OSS or mixed cloud                   Enterprise compliance requirements
                                         Need VSTS release gates / approvals
```

---

## GitHub Actions

### Anatomy of a Workflow

```
.github/
└── workflows/
    ├── ci.yml          runs on every push / PR
    ├── release.yml     runs on tag push
    └── deploy.yml      runs on merge to main
```

```yaml
# .github/workflows/ci.yml

name: CI

on:                                    # what triggers this workflow
  push:
    branches: [main, develop]
  pull_request:
    branches: [main]

jobs:
  test:                                # job name (arbitrary)
    runs-on: ubuntu-latest             # runner — GitHub-hosted VM

    steps:
      - name: Checkout code
        uses: actions/checkout@v4      # action from Marketplace

      - name: Setup Node
        uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm                   # cache node_modules between runs

      - name: Install dependencies
        run: npm ci                    # shell command

      - name: Lint
        run: npm run lint

      - name: Type check
        run: npm run typecheck

      - name: Test
        run: npm run test -- --coverage

      - name: Upload coverage
        uses: actions/upload-artifact@v4
        with:
          name: coverage
          path: coverage/
```

### Key Concepts

```
Trigger (on:)
  push, pull_request, schedule (cron), workflow_dispatch (manual),
  release, repository_dispatch (webhook)

Runner (runs-on:)
  ubuntu-latest    GitHub-hosted Linux (most common)
  windows-latest   GitHub-hosted Windows
  macos-latest     GitHub-hosted macOS
  self-hosted      Your own machine/VM registered as a runner

Action (uses:)
  Reusable step from Marketplace or local file
  actions/checkout@v4       — clone the repo
  actions/setup-node@v4     — install Node + optional npm cache
  actions/cache@v4          — general-purpose cache
  docker/build-push-action  — build + push Docker image

Job vs Step
  Workflow → Jobs (run in parallel by default) → Steps (run sequentially)
  Jobs run on separate VMs. Steps share one VM and its filesystem.
```

### Matrix Builds

```yaml
jobs:
  test:
    runs-on: ubuntu-latest
    strategy:
      matrix:
        node-version: [18, 20, 22]
        os: [ubuntu-latest, windows-latest]
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: ${{ matrix.node-version }}
      - run: npm ci && npm test
```

Runs 6 jobs (3 versions × 2 OSes) in parallel automatically.

### Secrets & Environment Variables

```yaml
steps:
  - name: Deploy
    env:
      NODE_ENV: production                      # plain env var
      DATABASE_URL: ${{ secrets.DATABASE_URL }} # from repo/org secrets
    run: npm run deploy
```

Secrets are set in Settings → Secrets and Variables → Actions. Never logged even if `echo`'d — GitHub redacts them.

### Full CI + Docker Build + Push Pipeline

```yaml
name: CI + Build + Push

on:
  push:
    branches: [main]
  pull_request:
    branches: [main]

env:
  REGISTRY: ghcr.io
  IMAGE_NAME: ${{ github.repository }}

jobs:
  # ── Job 1: Test ────────────────────────────────────────────────
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 20
          cache: npm
      - run: npm ci
      - run: npm run lint && npm run typecheck && npm test

  # ── Job 2: Build & Push (only on main merge) ──────────────────
  build-push:
    needs: test                         # only runs if test passes
    runs-on: ubuntu-latest
    if: github.ref == 'refs/heads/main' # only on main, not PRs
    permissions:
      contents: read
      packages: write                   # needed to push to GHCR

    steps:
      - uses: actions/checkout@v4

      - name: Log in to registry
        uses: docker/login-action@v3
        with:
          registry: ${{ env.REGISTRY }}
          username: ${{ github.actor }}
          password: ${{ secrets.GITHUB_TOKEN }}   # auto-provided

      - name: Extract metadata (tags, labels)
        id: meta
        uses: docker/metadata-action@v5
        with:
          images: ${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}
          tags: |
            type=sha                              # ghcr.io/org/app:abc1234
            type=raw,value=latest

      - name: Build and push
        uses: docker/build-push-action@v5
        with:
          context: .
          push: true
          tags: ${{ steps.meta.outputs.tags }}
          cache-from: type=gha              # GitHub Actions cache for Docker layers
          cache-to: type=gha,mode=max
```

### Deploy to AKS (CD step)

```yaml
  deploy:
    needs: build-push
    runs-on: ubuntu-latest
    environment: production               # requires approval if configured

    steps:
      - uses: actions/checkout@v4

      - name: Azure login
        uses: azure/login@v1
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Get AKS credentials
        uses: azure/aks-set-context@v3
        with:
          resource-group: myRG
          cluster-name: myAKS

      - name: Deploy to AKS
        run: |
          kubectl set image deployment/api \
            api=${{ env.REGISTRY }}/${{ env.IMAGE_NAME }}:${{ github.sha }}
          kubectl rollout status deployment/api
```

---

## Azure Pipelines

Azure Pipelines is the VSTS Build/Release pipeline evolution. If you used it at Microsoft, most concepts map directly — just YAML now instead of the GUI.

### Anatomy

```yaml
# azure-pipelines.yml

trigger:
  branches:
    include:
      - main
      - develop

pool:
  vmImage: ubuntu-latest        # Microsoft-hosted agent

variables:
  nodeVersion: '20'
  imageName: 'myapp'

stages:
  - stage: Build
    jobs:
      - job: Test
        steps:
          - task: NodeTool@0
            inputs:
              versionSpec: $(nodeVersion)

          - script: npm ci
            displayName: Install dependencies

          - script: npm run lint && npm test
            displayName: Lint and test

          - task: PublishTestResults@2
            inputs:
              testResultsFormat: JUnit
              testResultsFiles: '**/test-results.xml'

  - stage: Deploy
    dependsOn: Build
    condition: and(succeeded(), eq(variables['Build.SourceBranch'], 'refs/heads/main'))
    jobs:
      - deployment: DeployProd              # deployment job (not regular job)
        environment: production             # tracks deployments, approval gates
        strategy:
          runOnce:
            deploy:
              steps:
                - task: KubernetesManifest@0
                  inputs:
                    action: deploy
                    manifests: k8s/*.yaml
                    containers: myregistry.azurecr.io/myapp:$(Build.BuildId)
```

### Pipelines vs Releases (Old vs New)

```
VSTS / Classic ADO                     Modern YAML Pipelines
==================                     =====================

GUI-built pipelines                    Code in azure-pipelines.yml
"Build Definition"                     pipeline (stages + jobs + steps)
"Release Pipeline"                     stages with deployment jobs
Environments as tabs                   environment: keyword + approvals
Artifacts dropdown                     pipeline artifacts / container images
Variable Groups (UI)                   variables + variable groups + Key Vault
Agent Queues                           pool: vmImage or name: (self-hosted)
```

### Azure-Native Integrations

```yaml
# ACR Docker build
- task: Docker@2
  inputs:
    containerRegistry: myACRServiceConnection
    repository: myapp
    command: buildAndPush
    tags: $(Build.BuildId)

# Key Vault secrets (link variable group to KV in Library)
variables:
  - group: production-secrets       # maps to Azure Key Vault

# ARM/Bicep deployment
- task: AzureResourceManagerTemplateDeployment@3
  inputs:
    deploymentScope: Resource Group
    azureResourceManagerConnection: myServiceConnection
    resourceGroupName: myRG
    location: eastus
    templateLocation: Linked artifact
    csmFile: infra/main.bicep
    overrideParameters: -appName myapp -env production
```

---

## Runners / Agents

```
GitHub-Hosted Runners              Self-Hosted Runners
=====================              ===================

VM spun up fresh per job           Your machine/VM registered as runner
2-core CPU, 7GB RAM (standard)     Any spec you want
~2000 free minutes/month           Unlimited, you pay compute
Linux / Windows / macOS            Any OS, any arch
Software pre-installed             You control the environment
Gone after job completes           Persistent (can cache between runs)

When to self-host:
  - Need private network access (no public internet)
  - Large builds that exhaust free minutes
  - Specialized hardware (GPU for ML, ARM for mobile)
  - Compliance requires no code on shared infra
```

For Azure Pipelines, self-hosted agents run as services. Common pattern: Azure VM Scale Set agents (auto-scale with pipeline queue depth).

---

## Environments & Approvals

Environments represent deployment targets (staging, production). Gate them with required reviewers.

```
GitHub Actions                         Azure Pipelines
==============                         ===============

Settings → Environments                Pipelines → Environments
  → Required reviewers                   → Approvals and checks
  → Wait timer                           → Required templates
  → Deployment branches                  → Exclusive lock (only one deploy)
                                         → Azure Monitor gates
                                         → ServiceNow/Jira gates (enterprise)
```

```yaml
# GitHub Actions — environment gate
jobs:
  deploy:
    environment:
      name: production
      url: https://myapp.example.com    # shows link in GitHub UI
```

When a job targets a protected environment, the workflow pauses and sends a notification to required reviewers. Deploy doesn't proceed until approved.

---

## Caching

CI is slow when it re-downloads dependencies every run. Cache them.

```yaml
# GitHub Actions — npm cache (built into setup-node)
- uses: actions/setup-node@v4
  with:
    node-version: 20
    cache: npm                      # caches ~/.npm based on package-lock.json hash

# Manual cache (for anything else)
- uses: actions/cache@v4
  with:
    path: ~/.cache/pip
    key: ${{ runner.os }}-pip-${{ hashFiles('requirements.txt') }}
    restore-keys: |
      ${{ runner.os }}-pip-
```

Cache key strategy: hash the lockfile. If `package-lock.json` changes → cache miss → fresh install. If unchanged → cache hit → skip install entirely. Typical npm install: 60–90s cold, 5–10s cached.

---

## Artifacts

Outputs from one job passed to another, or kept for download.

```yaml
# Upload
- uses: actions/upload-artifact@v4
  with:
    name: build-output
    path: dist/
    retention-days: 7

# Download in another job
- uses: actions/download-artifact@v4
  with:
    name: build-output
    path: dist/
```

In Azure Pipelines, the equivalent is `PublishPipelineArtifact` / `DownloadPipelineArtifact`. Artifacts are how CD stages consume what CI built — build once, deploy the same artifact everywhere.

---

## Common Patterns

### Branch Strategy → Pipeline Strategy

```
Trunk-based development (recommended)
=====================================
  feature/* → main (via PR)

  PR push:   run CI (test, lint, typecheck)
  Merge:     run CI + build image + deploy to staging
  Tag v*.*:  deploy to production (with approval gate)

GitFlow (more gates, slower)
============================
  feature/* → develop → release/* → main

  develop push:   CI + deploy to dev env
  release push:   CI + deploy to staging
  main merge:     CI + deploy to production
```

### Monorepo — Only Run What Changed

```yaml
# GitHub Actions — path filters
on:
  push:
    paths:
      - 'apps/api/**'
      - 'packages/shared/**'

# Or use Nx/Turborepo affected commands
- run: npx nx affected --target=test --base=origin/main
```

### Fail Fast vs Fail Safe

```
fail-fast: true (default)          fail-fast: false
======================             =================

Matrix: first failure cancels      All matrix jobs run to completion
all other jobs                     Useful for: cross-browser tests where
Saves runner minutes               you want full picture of failures
```

---

## Common Confusion Points

**`on: push` fires on every branch, including feature branches.**
If you only want CI on main and PRs: use `branches` filter under `push` and `pull_request`. Otherwise every `git push` to any branch triggers a run.

**Jobs run in parallel by default; steps are sequential.**
If Job B needs Job A's output, use `needs: job-a`. Without it, both start simultaneously.

**`GITHUB_TOKEN` is auto-provided, but has limited permissions by default.**
Reading code: always allowed. Pushing packages, creating releases, writing PRs: requires `permissions:` block in the workflow. Don't store a PAT as a secret just to push to GHCR — use `permissions: packages: write` with the built-in token.

**Environment protection rules don't apply to `workflow_dispatch`** unless you explicitly set deployment branches. A manual trigger can bypass gates if you don't configure it.

**Azure Pipelines `deployment` job vs regular `job`.**
Regular jobs have no deployment semantics. `deployment` jobs are tracked in the Environment, support approval gates, and have a structured `strategy` (runOnce, rolling, canary). Use `deployment` for anything that goes to a real environment.

**Pipeline YAML lives in the repo — treat it as code.**
Review changes to CI/CD files in PRs. A compromised pipeline file can exfiltrate secrets or push malicious images. In GitHub Actions, `pull_request` from forks runs with read-only token by default (safe). `pull_request_target` has write access — be careful with untrusted forks.

---

## Old World Bridge

| VSTS / Azure DevOps (Classic) | Modern CI/CD Equivalent |
|---|---|
| Build Definition (GUI) | Workflow YAML / azure-pipelines.yml |
| Build Agent Queue | `runs-on:` / `pool:` |
| Hosted Agent | GitHub-hosted runner / Microsoft-hosted agent |
| Private Agent | Self-hosted runner / self-hosted agent |
| Release Pipeline | CD stage in same YAML / `deploy` job |
| Release Environment | `environment:` keyword with approval gates |
| Artifact drop | `upload-artifact` / `PublishPipelineArtifact` |
| Variable Group | `secrets` context / variable group + Key Vault link |
| Service Connection | Stored credential for Azure/Docker/K8s |
| Gated check-in | Branch protection + required status checks |
| Test Results tab | `PublishTestResults` / Codecov integration |
| Deployment slots swap | Rolling deploy to K8s or App Service slot action |
| Build number | `github.run_number` / `Build.BuildId` |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Run tests on every PR | GitHub Actions `on: pull_request` |
| Block merge if CI fails | Branch protection → required status checks |
| Build & push Docker image on merge | `build-push-action` in `on: push` + `needs: test` |
| Deploy to K8s on merge | `kubectl set image` or `KubernetesManifest` task |
| Require human approval before prod deploy | Environment protection rules / ADO approvals |
| Pass build output between jobs | `upload-artifact` + `download-artifact` |
| Speed up slow installs | `cache:` in `setup-node` / `actions/cache` |
| Test across Node 18, 20, 22 | Matrix strategy |
| Deploy only when tests pass | `needs: test` + `if: success()` |
| Access Azure resources from pipeline | OIDC federated identity (no stored secrets) |
| Run on private network | Self-hosted runner in your VNet |
| Both GitHub + Azure together | GitHub Actions for CI → Azure Pipelines for CD (or GitHub Actions throughout with `azure/login`) |
