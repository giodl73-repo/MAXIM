# 14 — Infrastructure as Code

## The Big Picture

```
The Problem IaC Solves
=======================

Old World                            IaC World
=========                            =========

  Azure Portal clickops               infrastructure defined in code
  "I'll just spin up a VM real quick" tracked in git
  Snowflake servers                   reviewed in PRs
  "Which settings did we use?"        reproducible in any environment
  Manual documentation                auditable history
  Can't reproduce prod in staging     deploy → destroy → redeploy = identical

  Works fine for one person           Works for teams, at scale, across envs
  Breaks at two                       Dev ≡ Staging ≡ Production
```

```
IaC Tool Landscape
===================

              Cloud-Agnostic                    Cloud-Native
              ==============                    ============

  Declarative   Terraform (HCL)                 Bicep (Azure)
                OpenTofu (OSS fork)             CloudFormation (AWS)
                                                Deployment Manager (GCP)

  Imperative    Pulumi (TypeScript/Python/Go)   Azure SDK scripts
  (real code)   CDK (TypeScript/Python)         AWS CDK

  Config Mgmt   Ansible (servers/config)        ─ (not really cloud-native)
  (not infra)   Chef, Puppet


  ┌──────────────────────────────────────────────────────────────┐
  │  If you're Azure-first:   Bicep is the answer               │
  │  If you're multi-cloud:   Terraform                         │
  │  If you want real code:   Pulumi                            │
  └──────────────────────────────────────────────────────────────┘
```

---

## Core Concept: Declarative vs Imperative

```
Imperative (scripts)               Declarative (IaC)
====================               =================

"Do these steps:"                  "This is the desired state:"

  az group create ...                resource "azurerm_resource_group" "rg" {
  az network vnet create ...           name     = "myapp-rg"
  az vm create ...                     location = "eastus"
  az vm extension set ...            }
  ...

  Order matters                      Tool figures out the order
  Not idempotent by default          Idempotent by design
  Hard to know current state         State tracked explicitly
  Drift is invisible                 Drift is detectable (plan)
```

**Idempotent**: run the same definition 10 times → same result. The tool diffs desired state against actual state and only makes the needed changes.

---

## Terraform

The dominant multi-cloud IaC tool. HCL (HashiCorp Configuration Language) — structured, readable, not a full programming language.

> **ARM → Terraform bridge**
>
> You know ARM JSON: a JSON document sent to Azure Resource Manager describing desired end-state. Azure RP reconciles reality to match it. ARM state lives in Azure's control plane — you query the portal or `az resource show` to know what actually exists.
>
> Terraform HCL also declares desired state, and the provider reconciles. Key difference: **Terraform state lives in a file you own (`.tfstate`)**. You are responsible for it. It can drift.
>
> Same storage account in ARM vs HCL:
>
> ```json
> // ARM JSON
> {
>   "type": "Microsoft.Storage/storageAccounts",
>   "apiVersion": "2023-01-01",
>   "name": "[parameters('storageAccountName')]",
>   "location": "[parameters('location')]",
>   "sku": { "name": "Standard_LRS" },
>   "kind": "StorageV2"
> }
> ```
>
> ```hcl
> # Terraform HCL
> resource "azurerm_storage_account" "sa" {
>   name                     = var.storage_account_name
>   resource_group_name      = azurerm_resource_group.rg.name
>   location                 = var.location
>   account_tier             = "Standard"
>   account_replication_type = "LRS"
> }
> ```
>
> ARM resource type strings map to Terraform provider resource names. The pattern is consistent but requires a lookup: `Microsoft.Storage/storageAccounts` → `azurerm_storage_account`, `Microsoft.Web/serverfarms` → `azurerm_service_plan`, `Microsoft.Sql/servers` → `azurerm_mssql_server`. Full mapping at [registry.terraform.io/providers/hashicorp/azurerm](https://registry.terraform.io/providers/hashicorp/azurerm).

### How Terraform Works

```
Workflow
=========

  Write .tf files        terraform init          terraform plan
  ───────────────        ──────────────          ──────────────
  Define resources       Download providers      Diff desired vs actual
  in HCL                 (Azure, AWS, GCP,       Shows what will be
                         K8s, GitHub, etc.)      created/changed/destroyed
                                                 Review before applying

  terraform apply        terraform destroy
  ───────────────        ─────────────────
  Execute the plan       Tear everything down
  Update state file      (careful in prod)
```

```
State
======

  terraform.tfstate — JSON file tracking what Terraform created

  local state:   fine for solo/learning, dangerous for teams
  remote state:  store in Azure Blob Storage / S3 / Terraform Cloud
                 enables locking (prevent concurrent applies)

  Never edit tfstate by hand.
  Never commit tfstate with secrets to git.
```

> **ARM state model vs Terraform state model**
>
> ARM template deployment = idempotent apply against **Azure control plane as ground truth**. Azure always knows the real state; you can delete the template and `az resource list` still works.
>
> Terraform plan/apply = diff against **`.tfstate` file as ground truth**. The `.tfstate` file is Terraform's cached view of what it created. If someone changes infrastructure outside of Terraform (portal clickops, `az` CLI), the `.tfstate` file becomes stale — that's **state drift**. `terraform refresh` syncs the state file from reality; then `terraform plan` shows the true delta.
>
> This is the most important conceptual difference from ARM. With ARM, Azure is always the authoritative source. With Terraform, `.tfstate` is the authoritative source, and it can lie. Remote state with locking (Azure Blob + lease) restores ARM-like behavior: one writer at a time, shared across the team.

### HCL Syntax

```hcl
# Variables
variable "location" {
  type        = string
  default     = "eastus"
  description = "Azure region"
}

variable "app_name" {
  type = string                    # no default = required at apply time
}

# Resource
resource "azurerm_resource_group" "rg" {
  name     = "${var.app_name}-rg"  # string interpolation
  location = var.location

  tags = {
    environment = "production"
    managed_by  = "terraform"
  }
}

# Reference another resource's output
resource "azurerm_virtual_network" "vnet" {
  name                = "${var.app_name}-vnet"
  resource_group_name = azurerm_resource_group.rg.name     # reference
  location            = azurerm_resource_group.rg.location
  address_space       = ["10.0.0.0/16"]
}

# Data source — read existing resource (not managed by this TF)
data "azurerm_key_vault" "existing" {
  name                = "myapp-kv"
  resource_group_name = "shared-rg"
}

# Output — expose values after apply
output "resource_group_id" {
  value = azurerm_resource_group.rg.id
}
```

### Complete Azure Example — App + DB

```hcl
# main.tf

terraform {
  required_providers {
    azurerm = {
      source  = "hashicorp/azurerm"
      version = "~> 3.0"
    }
  }
  # Remote state in Azure Blob
  backend "azurerm" {
    resource_group_name  = "tfstate-rg"
    storage_account_name = "tfstate12345"
    container_name       = "tfstate"
    key                  = "myapp.prod.tfstate"
  }
}

provider "azurerm" {
  features {}
}

# Resource Group
resource "azurerm_resource_group" "rg" {
  name     = "${var.app_name}-${var.env}-rg"
  location = var.location
}

# App Service Plan
resource "azurerm_service_plan" "plan" {
  name                = "${var.app_name}-plan"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  os_type             = "Linux"
  sku_name            = "P1v3"
}

# App Service (Web App)
resource "azurerm_linux_web_app" "app" {
  name                = "${var.app_name}-${var.env}"
  resource_group_name = azurerm_resource_group.rg.name
  location            = azurerm_resource_group.rg.location
  service_plan_id     = azurerm_service_plan.plan.id

  site_config {
    application_stack {
      node_version = "20-lts"
    }
  }

  app_settings = {
    DATABASE_URL = "@Microsoft.KeyVault(SecretUri=${azurerm_key_vault_secret.db_url.id})"
    NODE_ENV     = var.env
  }

  identity {
    type = "SystemAssigned"          # Managed Identity for Key Vault access
  }
}

# PostgreSQL Flexible Server
resource "azurerm_postgresql_flexible_server" "db" {
  name                   = "${var.app_name}-${var.env}-db"
  resource_group_name    = azurerm_resource_group.rg.name
  location               = azurerm_resource_group.rg.location
  version                = "16"
  administrator_login    = "pgadmin"
  administrator_password = var.db_password    # from secrets, not hardcoded
  sku_name               = "B_Standard_B1ms"
  storage_mb             = 32768
  zone                   = "1"
}
```

### Modules

Reusable, parameterized chunks of infrastructure. Like functions.

```hcl
# Call a module
module "web_app" {
  source   = "./modules/web-app"        # local module
  # source = "Azure/webapp/azurerm"     # Terraform Registry module

  app_name = var.app_name
  location = var.location
  env      = "production"
}

# modules/web-app/main.tf defines the resources
# modules/web-app/variables.tf defines inputs
# modules/web-app/outputs.tf exposes outputs
```

---

## Bicep

Azure's native IaC language. Compiles to ARM JSON (think TypeScript → JavaScript). First-class Azure Portal and Azure CLI integration. The right choice if you're Azure-only.

```
Bicep vs ARM JSON
==================

ARM JSON (old)                     Bicep (new)
==============                     ===========

{                                  param appName string
  "$schema": "...",                param location string = resourceGroup().location
  "contentVersion": "1.0.0.0",
  "parameters": {                  resource appPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
    "appName": {                     name: '${appName}-plan'
      "type": "string"               location: location
    }                                sku: {
  },                                   name: 'P1v3'
  "resources": [                       tier: 'PremiumV3'
    {                                }
      "type": "Microsoft.Web/...   }
      ...
      (50 more lines of JSON)      // Same result. Much less noise.
    }
  ]
}
```

### Bicep Syntax

```bicep
// Parameters
@description('Environment name: dev, staging, prod')
@allowed(['dev', 'staging', 'prod'])
param env string

param appName string
param location string = resourceGroup().location

// Variables
var planName = '${appName}-${env}-plan'
var webAppName = '${appName}-${env}'

// Resource
resource appPlan 'Microsoft.Web/serverfarms@2022-03-01' = {
  name: planName
  location: location
  kind: 'linux'
  sku: {
    name: 'P1v3'
    tier: 'PremiumV3'
  }
  properties: {
    reserved: true    // required for Linux
  }
}

resource webApp 'Microsoft.Web/sites@2022-03-01' = {
  name: webAppName
  location: location
  properties: {
    serverFarmId: appPlan.id    // reference: symbolic name, not string
    siteConfig: {
      linuxFxVersion: 'NODE|20-lts'
      appSettings: [
        {
          name: 'NODE_ENV'
          value: env
        }
      ]
    }
  }
  identity: {
    type: 'SystemAssigned'
  }
}

// Output
output webAppUrl string = 'https://${webApp.properties.defaultHostName}'
```

### Modules in Bicep

```bicep
// main.bicep
module database 'modules/postgres.bicep' = {
  name: 'databaseDeploy'
  params: {
    serverName: '${appName}-db'
    location: location
    adminPassword: adminPassword
  }
}

// Reference module output
var dbHostname = database.outputs.hostname
```

### Deploy Bicep

```bash
# Deploy to resource group
az deployment group create \
  --resource-group myapp-rg \
  --template-file main.bicep \
  --parameters env=production appName=myapp

# What-if (like terraform plan)
az deployment group what-if \
  --resource-group myapp-rg \
  --template-file main.bicep \
  --parameters env=production appName=myapp

# From Azure Pipelines
- task: AzureResourceManagerTemplateDeployment@3
  inputs:
    deploymentScope: Resource Group
    azureResourceManagerConnection: myServiceConnection
    resourceGroupName: myapp-rg
    templateLocation: Linked artifact
    csmFile: infra/main.bicep
    overrideParameters: -env production -appName myapp
```

---

## Pulumi

Write real code (TypeScript, Python, Go, C#) that provisions infrastructure. The type system, loops, conditionals, and abstraction you already know.

> **Bicep → Pulumi bridge**
>
> Bicep is ARM JSON with better syntax — still declarative, still a DSL, still no loops beyond `for` expressions, still no real type system. It compiles down to ARM JSON.
>
> Pulumi is imperative IaC in real languages. You write TypeScript, Python, Go, or **C#** — with full IntelliSense, real loops, conditionals, generics, and typed resource references. For a C# developer, Pulumi feels like using the Azure SDK except the output is a running infrastructure deployment rather than an HTTP response.
>
> Pulumi C# example — create a storage account:
>
> ```csharp
> using Pulumi;
> using Pulumi.AzureNative.Resources;
> using Pulumi.AzureNative.Storage;
>
> return await Deployment.RunAsync(() =>
> {
>     var rg = new ResourceGroup("rg");
>
>     var sa = new StorageAccount("sa", new StorageAccountArgs
>     {
>         ResourceGroupName = rg.Name,
>         Sku = new SkuArgs { Name = SkuName.Standard_LRS },
>         Kind = Kind.StorageV2,
>     });
>
>     return new Dictionary<string, object?> { ["storageAccountName"] = sa.Name };
> });
> ```
>
> The NuGet package is `Pulumi.AzureNative` — it wraps the full Azure RM API surface with generated C# types. Every ARM resource type has a corresponding strongly-typed C# class.

```typescript
// index.ts — Pulumi TypeScript

import * as pulumi from "@pulumi/pulumi";
import * as azure from "@pulumi/azure-native";

const config = new pulumi.Config();
const appName = config.require("appName");
const env = config.require("env");

// Resource Group
const rg = new azure.resources.ResourceGroup("rg", {
  resourceGroupName: `${appName}-${env}-rg`,
  location: "EastUS",
});

// App Service Plan
const plan = new azure.web.AppServicePlan("plan", {
  name: `${appName}-plan`,
  resourceGroupName: rg.name,
  location: rg.location,
  kind: "Linux",
  reserved: true,
  sku: { name: "P1v3", tier: "PremiumV3" },
});

// Web App
const app = new azure.web.WebApp("app", {
  name: `${appName}-${env}`,
  resourceGroupName: rg.name,
  location: rg.location,
  serverFarmId: plan.id,
  siteConfig: {
    linuxFxVersion: "NODE|20-lts",
  },
});

// Export outputs — accessible after `pulumi up`
export const url = pulumi.interpolate`https://${app.defaultHostName}`;
```

```bash
pulumi up        # preview + deploy (like terraform plan + apply combined)
pulumi preview   # plan only
pulumi destroy   # tear down
pulumi stack     # manage environments (stacks = environments)
```

---

## Environments / Workspaces

All three tools support multiple environments from the same code.

```
Terraform workspaces:
  terraform workspace new staging
  terraform workspace select production
  terraform apply -var-file=production.tfvars

Bicep parameter files:
  az deployment group create --parameters @params.prod.json

Pulumi stacks:
  pulumi stack init production
  pulumi config set env production
  pulumi up --stack production
```

Pattern: same code, different variable files per environment. Never duplicate infrastructure code for environments — parameterize.

---

## GitOps Pattern

Infrastructure changes follow the same PR/review/merge flow as application code.

```
GitOps Workflow
================

  1. Engineer edits .tf / .bicep / Pulumi code
  2. Opens PR
  3. CI runs: terraform plan / az deployment what-if / pulumi preview
     → Posts diff as PR comment: "+ 2 resources, ~ 1 resource, - 0 resources"
  4. Reviewer sees exactly what will change in Azure
  5. PR merges → CD pipeline runs terraform apply / az deploy / pulumi up
  6. All infra changes auditable in git history

  No more "who clicked what in the portal at 3pm Friday"
```

```yaml
# GitHub Actions — Terraform plan on PR
- name: Terraform Plan
  run: terraform plan -out=tfplan
  env:
    ARM_CLIENT_ID: ${{ secrets.ARM_CLIENT_ID }}
    ARM_CLIENT_SECRET: ${{ secrets.ARM_CLIENT_SECRET }}
    ARM_SUBSCRIPTION_ID: ${{ secrets.ARM_SUBSCRIPTION_ID }}
    ARM_TENANT_ID: ${{ secrets.ARM_TENANT_ID }}

- name: Comment plan on PR
  uses: actions/github-script@v7
  with:
    script: |
      const output = `...plan output...`;
      github.rest.issues.createComment({ body: output, ... });
```

---

## Common Confusion Points

**`terraform plan` shows a change you didn't make.**
Someone changed infrastructure outside of Terraform (portal clickops, manual az CLI). This is drift. Plan will show the delta between tfstate and reality. `terraform refresh` updates state from real world; then plan again.

**State file conflicts in a team.**
Two people run `terraform apply` simultaneously → state corruption. Fix: remote state with locking (Azure Blob Storage with lease locking, or Terraform Cloud). The backend config handles this automatically once set up.

**Bicep `what-if` is not always accurate.**
What-if is advisory — some resource providers don't implement it fully. Always test in a non-production environment before applying to prod.

**Terraform destroy in production.**
`terraform destroy` removes everything in the state. It's not scoped to what changed. Never run it in prod without reading the plan output carefully. Most teams add a `prevent_destroy = true` lifecycle block on critical resources.

**Resource drift vs config drift.**
Resource drift: someone changed infra outside IaC → fix by importing or re-applying.
Config drift: IaC code no longer reflects team intent → fix by updating code.

**Pulumi state vs Terraform state.**
Both track what was created. Pulumi defaults to Pulumi Cloud backend; Terraform defaults to local. Both support self-hosted backends. The state concept is identical — the storage location differs.

---

## Old World Bridge

| Azure Portal / Manual Process | IaC Equivalent |
|---|---|
| Click "Create resource group" | `resource "azurerm_resource_group"` / `resource rg` |
| Azure Portal ARM Export | Starting point for Bicep (decompile ARM JSON → Bicep) |
| ARM JSON templates | Bicep (ARM is the compiled output) |
| ARM JSON templates | Terraform HCL — `"type": "Microsoft.Storage/storageAccounts"` → `resource "azurerm_storage_account"`. ARM resource type strings map consistently to `azurerm_*` names; lookup at registry.terraform.io/providers/hashicorp/azurerm |
| PowerShell provisioning scripts | Terraform / Bicep / Pulumi |
| Deployment environments (dev/staging/prod) | Workspaces / stacks / parameter files |
| Azure Blueprints (deprecated) | Bicep modules + Policy-as-code |
| Manual VSTS environment setup | IaC in CI/CD pipeline (13-CICD) |
| "I know what's in prod" | `terraform state list` / Pulumi stack output |
| Azure Resource Manager | What Bicep compiles to; what Terraform's azurerm provider calls |
| ARM as authoritative state store | Terraform remote state in Azure Blob — restores the "Azure is source of truth" property that local `.tfstate` breaks |

---

## Decision Cheat Sheet

| I want to... | Use |
|---|---|
| Provision Azure resources, Azure-only shop | Bicep |
| Provision across Azure + AWS + GCP | Terraform |
| Write infrastructure in TypeScript/Python I already know | Pulumi |
| Write infrastructure in C# with typed Azure SDK objects | Pulumi C# (`Pulumi.AzureNative`) |
| Manage servers/config (not just provisioning) | Ansible (not IaC per se) |
| Preview changes before applying | `terraform plan` / `az deployment what-if` / `pulumi preview` |
| Store state safely for a team | Remote backend (Azure Blob + lock) |
| Reuse infrastructure patterns across projects | Terraform modules / Bicep modules |
| Apply infra changes via CI/CD on PR merge | GitOps pipeline pattern |
| Import existing Azure resource into Terraform | `terraform import` |
| Convert existing ARM JSON to Bicep | `az bicep decompile` |
| Protect a critical resource from accidental destroy | `lifecycle { prevent_destroy = true }` |
| Manage multiple environments (dev/staging/prod) | Workspaces (TF) / stacks (Pulumi) / parameter files (Bicep) |
| Look up ARM resource type → Terraform resource name | registry.terraform.io/providers/hashicorp/azurerm |
