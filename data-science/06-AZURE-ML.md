# Azure Machine Learning — Complete Reference

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        AZURE MACHINE LEARNING                               │
│                    ML Platform-as-a-Service on Azure                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │                        STUDIO UI / CLI v2 / SDK v2                    │  │
│  │           (all three surface the same underlying API)                 │  │
│  └──────────────┬───────────────────────────────────────────────────────┘  │
│                 │                                                           │
│  ┌──────────────▼───────────────────────────────────────────────────────┐  │
│  │                         WORKSPACE                                     │  │
│  │  ┌───────────┐  ┌───────────┐  ┌────────────┐  ┌─────────────────┐  │  │
│  │  │  Assets   │  │  Compute  │  │  Data      │  │  Connections     │  │  │
│  │  │           │  │           │  │            │  │                  │  │  │
│  │  │ • Models  │  │ • Cluster │  │ • Datastores│  │ • Storage acct  │  │  │
│  │  │ • Envs    │  │ • Instance│  │ • Datasets │  │ • Key Vault     │  │  │
│  │  │ • Comps   │  │ • Serverls│  │            │  │ • ACR           │  │  │
│  │  └───────────┘  └───────────┘  └────────────┘  └─────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                                                             │
│  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  ┌──────────────┐  │
│  │  TRAINING    │  │  PIPELINES   │  │  REGISTRY    │  │  ENDPOINTS   │  │
│  │              │  │              │  │              │  │              │  │
│  │ • Jobs       │  │ • Components │  │ • Versioned  │  │ • Real-time  │  │
│  │ • Sweeps     │  │ • DAG graph  │  │   models     │  │ • Batch      │  │
│  │ • AutoML     │  │ • Reuse/cache│  │ • Stages     │  │              │  │
│  └──────────────┘  └──────────────┘  └──────────────┘  └──────────────┘  │
│                                                                             │
│  Azure backbone: RBAC, Private Link, Managed Identity, Key Vault, ACR      │
└─────────────────────────────────────────────────────────────────────────────┘
```

**AzureML vs raw infra**: AzureML wraps Azure compute (VMs, AKS, serverless) with
ML-specific orchestration — experiment tracking, model registry, dataset versioning,
managed endpoints. You still run your PyTorch/sklearn/MLflow code; AzureML handles
provisioning, logging, artifact storage, deployment, and governance.

---

## SDK v2 vs CLI v2 vs Studio

| Surface | When to use | Format |
|---------|-------------|--------|
| **SDK v2** (`azure-ai-ml`) | Python scripts, notebooks, pipelines-as-code | Python objects |
| **CLI v2** (`az ml`) | CI/CD, DevOps scripts, imperative automation | YAML files |
| **Studio UI** | Exploration, debugging, reviewing runs, drag-n-drop pipelines | Browser |
| **ARM / Bicep** | Workspace provisioning (infra-level) | Bicep/ARM |

**SDK v2 is the primary surface for ML engineers.** CLI v2 is for CI/CD pipelines.

```python
from azure.ai.ml import MLClient
from azure.identity import DefaultAzureCredential

ml_client = MLClient(
    credential=DefaultAzureCredential(),
    subscription_id="<sub-id>",
    resource_group_name="<rg>",
    workspace_name="<workspace>",
)
```

`DefaultAzureCredential` tries, in order: env vars → managed identity → VS Code →
Azure CLI → browser. In CI/CD use a Service Principal or Workload Identity.

---

## Workspace Architecture

```
┌─────────────────────────────────────────────────────────────────┐
│                         WORKSPACE                               │
│  Azure resource group anchor — everything lives inside          │
│                                                                 │
│  ┌─────────────────┐  Created automatically at workspace        │
│  │  Storage Acct   │  creation. Stores:                         │
│  │  (default)      │  • Training artifacts / outputs            │
│  │                 │  • Dataset profiles                        │
│  └─────────────────┘  • Logs                                    │
│                                                                 │
│  ┌─────────────────┐  Stores all Docker images for              │
│  │  Container Reg  │  environments + custom base images         │
│  │  (ACR)          │                                            │
│  └─────────────────┘                                            │
│                                                                 │
│  ┌─────────────────┐  Secrets: storage keys, connection         │
│  │  Key Vault      │  strings. Never hardcoded.                  │
│  └─────────────────┘                                            │
│                                                                 │
│  ┌─────────────────┐  Training telemetry, custom metrics,       │
│  │  App Insights   │  endpoint latency                          │
│  └─────────────────┘                                            │
└─────────────────────────────────────────────────────────────────┘
```

### Workspaces: Hub-and-Spoke (Enterprise Pattern)

```
Hub Workspace
├── Shared compute clusters
├── Shared registries (curated models)
└── Spoke Workspace A  (team A)
    Spoke Workspace B  (team B)  — isolated experiments, same shared infra
    Spoke Workspace C  (team C)
```

Hub provides shared resources; spokes isolate team experiments and data access.
Controlled via RBAC: Contributor = full access, Reader = view only,
AzureML Data Scientist = train/deploy but not manage infra.

---

## Compute

```
┌──────────────────────────────────────────────────────────────────────┐
│                         COMPUTE TYPES                                │
│                                                                      │
│  ┌─────────────────────────────┐  ┌─────────────────────────────┐   │
│  │     COMPUTE INSTANCE         │  │     COMPUTE CLUSTER          │   │
│  │  (Interactive dev)           │  │  (Training at scale)         │   │
│  │                              │  │                              │   │
│  │  • Single VM (1 person)      │  │  • Min/max nodes (0 → N)     │   │
│  │  • Pre-configured: Jupyter,  │  │  • Autoscales up + idles     │   │
│  │    VS Code, terminals        │  │    down to 0                 │   │
│  │  • Persistent (billed when   │  │  • Multi-node distributed    │   │
│  │    running)                  │  │    training                  │   │
│  │  • Stop when not in use!     │  │  • Best for batch jobs       │   │
│  └─────────────────────────────┘  └─────────────────────────────┘   │
│                                                                      │
│  ┌─────────────────────────────┐  ┌─────────────────────────────┐   │
│  │     SERVERLESS COMPUTE       │  │     ATTACHED COMPUTE         │   │
│  │  (No cluster to manage)      │  │  (Bring your own)            │   │
│  │                              │  │                              │   │
│  │  • AzureML allocates VM      │  │  • Attach existing AKS       │   │
│  │    on demand                 │  │  • Attach Arc-enabled K8s    │   │
│  │  • Pay per second            │  │  • Synapse Spark pool        │   │
│  │  • Cold-start latency        │  │  • HDInsight                 │   │
│  │  • Best for: infrequent jobs │  │  • Best: existing infra      │   │
│  └─────────────────────────────┘  └─────────────────────────────┘   │
└──────────────────────────────────────────────────────────────────────┘
```

### Compute SKU Decision

| Workload | Recommended SKU |
|----------|-----------------|
| Development / small experiments | `Standard_DS3_v2` (4 vCPU, 14 GB) |
| GPU training (single) | `Standard_NC6s_v3` (V100, 112 GB RAM) |
| GPU training (high-end) | `Standard_ND96asr_A100_v4` (8× A100) |
| Distributed training | Cluster of `Standard_NC*` with InfiniBand |
| CPU inference (batch) | `Standard_F16s_v2` (compute-optimized) |
| Memory-heavy (large models) | `Standard_M*` series |

```python
from azure.ai.ml.entities import AmlCompute

cluster = AmlCompute(
    name="gpu-cluster",
    type="amlcompute",
    size="Standard_NC6s_v3",
    min_instances=0,       # scales to zero — important for cost
    max_instances=4,
    idle_time_before_scale_down=120,  # seconds
    tier="Dedicated",      # or "LowPriority" (cheaper, preemptible)
)
ml_client.begin_create_or_update(cluster).result()
```

**LowPriority**: ~60-80% cheaper. Preemptible — AzureML checkpoints and resumes
automatically if you enable it. Good for long training runs where restartability is coded.

---

## Data: Datastores and Data Assets

```
┌──────────────────────────────────────────────────────────────┐
│  DATA LAYER                                                  │
│                                                              │
│  Datastore (connection)                                      │
│  ┌──────────────────┐  ┌──────────────────┐                 │
│  │  Azure Blob /    │  │  ADLS Gen2       │                 │
│  │  Storage         │  │  (hierarchical)  │                 │
│  └────────┬─────────┘  └────────┬─────────┘                 │
│           │                     │                           │
│           └──────────┬──────────┘                           │
│                      │                                      │
│  Data Asset (versioned reference)                           │
│  ┌──────────────────────────────────────┐                   │
│  │  URI File  │  URI Folder  │  Table   │                   │
│  │  (single)  │  (directory) │  (MLTable│                   │
│  │            │              │   format)│                   │
│  └──────────────────────────────────────┘                   │
└──────────────────────────────────────────────────────────────┘
```

### Registering a Data Asset

```python
from azure.ai.ml.entities import Data
from azure.ai.ml.constants import AssetTypes

# Register a versioned folder in blob storage
data_asset = Data(
    name="my-training-data",
    version="1",
    description="Processed features for model v3",
    path="azureml://datastores/workspaceblobstore/paths/data/train/",
    type=AssetTypes.URI_FOLDER,
)
ml_client.data.create_or_update(data_asset)

# Use in a job
from azure.ai.ml import Input
my_data = Input(
    type=AssetTypes.URI_FOLDER,
    path="azureml:my-training-data:1",
)
```

**MLTable** (the `Table` type): a YAML manifest that describes how to load tabular
data with transformations (column selection, filtering). Think of it as a Power Query
M query but stored as YAML alongside the data. Supports Parquet, CSV, Delta.

```yaml
# MLTable file (saved next to the data)
paths:
  - pattern: ./*.parquet
transformations:
  - read_parquet:
      include_path_column: false
  - filter: col("label") != -1
  - select_columns: [feature_1, feature_2, label]
```

---

## Environments

**Environment** = Docker image + conda/pip packages. Versioned, cached in ACR.

```
Curated Environments (Microsoft-managed, ready to use)
├── AzureML-sklearn-1.5-ubuntu22.04-py38-cpu
├── AzureML-pytorch-2.2-ubuntu22.04-py38-cuda11.8-gpu
├── AzureML-tensorflow-2.16-ubuntu22.04-py38-cuda11.8-gpu
└── ... (full list in Studio UI)

Custom Environment
├── From Dockerfile (full control)
└── From conda YAML + base image (faster builds)
```

```python
from azure.ai.ml.entities import Environment, BuildContext

# Option 1: conda YAML (faster, preferred for iteration)
env = Environment(
    name="my-training-env",
    version="3",
    conda_file="conda.yaml",
    image="mcr.microsoft.com/azureml/openmpi4.1.0-cuda11.8-cudnn8-ubuntu22.04",
)

# Option 2: Dockerfile (full control)
env = Environment(
    name="my-custom-env",
    build=BuildContext(path="./docker/"),
)

ml_client.environments.create_or_update(env)
```

```yaml
# conda.yaml
name: training-env
channels:
  - conda-forge
dependencies:
  - python=3.10
  - pip:
    - torch==2.2.0
    - torchvision
    - scikit-learn
    - mlflow
    - azureml-mlflow      # AzureML MLflow integration
    - azure-ai-ml
```

**Cost tip**: Curated environments have pre-built layers cached in the region's ACR.
First job with a custom env triggers a Docker build (5-15 min); subsequent jobs use
the cached image.

---

## Training Jobs

### Command Job — Single Node

```python
from azure.ai.ml import command, Input
from azure.ai.ml.entities import ResourceConfiguration

job = command(
    display_name="train-classifier-v3",
    description="XGBoost classifier on feature set v3",

    # Code: uploaded to blob, mounted at /code in container
    code="./src",
    command="python train.py --data ${{inputs.data}} --lr ${{inputs.lr}}",

    # Named inputs → mounted paths or environment variables
    inputs={
        "data": Input(type="uri_folder", path="azureml:my-training-data:1"),
        "lr": 0.01,
    },

    # Environment: curated or custom
    environment="AzureML-sklearn-1.5-ubuntu22.04-py38-cpu@latest",

    # Compute
    compute="gpu-cluster",
    resources=ResourceConfiguration(instance_count=1),

    # Experiment grouping
    experiment_name="xgboost-classifier",
)

returned_job = ml_client.jobs.create_or_update(job)
ml_client.jobs.stream(returned_job.name)   # tail logs
```

### Distributed Training — PyTorch DDP

```python
from azure.ai.ml import TorchDistribution

job = command(
    command="python train_ddp.py --epochs 50",
    environment="AzureML-pytorch-2.2-ubuntu22.04-py38-cuda11.8-gpu@latest",
    compute="gpu-cluster",
    distribution=TorchDistribution(process_count_per_instance=4),  # 4 GPUs/node
    resources=ResourceConfiguration(instance_count=2),             # 2 nodes → 8 GPUs
    # AzureML sets: MASTER_ADDR, MASTER_PORT, RANK, LOCAL_RANK, WORLD_SIZE
)
```

**Inside train_ddp.py**: use `torch.distributed.init_process_group("nccl")` — AzureML
injects the env vars. Log only on `rank == 0` to avoid duplicate metrics.

### Sweep Job — Hyperparameter Tuning

```python
from azure.ai.ml.sweep import (
    Uniform, Choice, BayesianSamplingAlgorithm,
    BanditEarlyTermination
)

base_job = command(
    command="python train.py --lr ${{search_space.lr}} --depth ${{search_space.depth}}",
    environment="...",
    compute="gpu-cluster",
)

sweep_job = base_job.sweep(
    sampling_algorithm=BayesianSamplingAlgorithm(),
    search_space={
        "lr":    Uniform(min_value=1e-5, max_value=0.1),
        "depth": Choice([3, 5, 7, 10]),
    },
    primary_metric="val_accuracy",
    goal="maximize",
    max_total_trials=40,
    max_concurrent_trials=4,
    early_termination=BanditEarlyTermination(slack_factor=0.15, evaluation_interval=5),
)
ml_client.jobs.create_or_update(sweep_job)
```

**Bandit termination**: stops runs where primary metric falls more than `slack_factor`
(15%) below the best run so far. Saves ~30-50% of compute on unpromising configs.

---

## AutoML

AzureML AutoML: automated feature engineering + algorithm selection + hyperparameter
tuning. Useful for tabular ML when you want a baseline fast.

```python
from azure.ai.ml import automl, Input
from azure.ai.ml.constants import AssetTypes

# Classification task
classification_job = automl.classification(
    compute="cpu-cluster",
    experiment_name="automl-churn-classification",
    training_data=Input(type=AssetTypes.MLTABLE, path="azureml:churn-data:1"),
    target_column_name="churned",
    primary_metric="AUCWeighted",
    n_cross_validations=5,
    enable_model_explainability=True,
    # Featurization
    featurization="auto",    # or custom FeaturizationSettings
    # Budget
    max_trials=20,
    timeout_minutes=60,
    max_concurrent_trials=4,
)
returned_job = ml_client.jobs.create_or_update(classification_job)
```

**AutoML task types**: `classification`, `regression`, `forecasting`, `image_classification`,
`image_object_detection`, `text_classification`, `text_ner`.

**What AutoML does internally**:
1. Data guard rails (class imbalance, missing values, high cardinality detection)
2. Featurization (numeric scaling, categorical encoding, datetime cyclical features)
3. Algorithm iteration (LightGBM, XGBoost, Ridge, SVM, ensemble stacking)
4. Ensembling: VotingEnsemble + StackEnsemble on top of top-N models

---

## Pipelines

AzureML Pipelines = DAG of **components**. Each component is a reusable unit:
`code + command + inputs/outputs + environment`. Same as Kubeflow, but Azure-native.

```
Pipeline DAG example:

  [data_prep]  ──► [feature_eng] ──► [train_model] ──► [evaluate]
       │                                    │
  outputs:                            outputs:
  train_data                          model artifact
  val_data                                  │
                                       [register_model] (conditional)
```

### Defining a Component (YAML)

```yaml
# components/train/spec.yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandComponent.schema.json
name: train_xgboost
version: "1"
display_name: Train XGBoost Classifier

inputs:
  train_data:
    type: uri_folder
  val_data:
    type: uri_folder
  learning_rate:
    type: number
    default: 0.1
  max_depth:
    type: integer
    default: 6

outputs:
  model_dir:
    type: uri_folder
  metrics:
    type: uri_file

environment: azureml:my-training-env:3
code: ./
command: >-
  python train.py
  --train-data ${{inputs.train_data}}
  --val-data ${{inputs.val_data}}
  --lr ${{inputs.learning_rate}}
  --depth ${{inputs.max_depth}}
  --output-dir ${{outputs.model_dir}}
  --metrics-file ${{outputs.metrics}}
```

### Defining a Component (Python decorator)

```python
from azure.ai.ml import command, Input, Output
from azure.ai.ml.dsl import pipeline
from azure.ai.ml.entities import CommandComponent

@command(
    name="prep_data",
    display_name="Data Preparation",
    inputs={"raw_data": Input(type="uri_folder")},
    outputs={"processed_data": Output(type="uri_folder")},
    code="./prep",
    command="python prep.py --input ${{inputs.raw_data}} --output ${{outputs.processed_data}}",
    environment="AzureML-sklearn-1.5-ubuntu22.04-py38-cpu@latest",
)
def prep_component():
    ...

# Load YAML-defined component
train_component = load_component(source="./components/train/spec.yaml")
```

### Assembling the Pipeline

```python
from azure.ai.ml.dsl import pipeline
from azure.ai.ml import Input

@pipeline(
    name="training-pipeline",
    description="End-to-end training pipeline",
    default_compute="cpu-cluster",
)
def training_pipeline(raw_data: Input(type="uri_folder"), lr: float = 0.1):
    # Step 1
    prep = prep_component(raw_data=raw_data)

    # Step 2 — consumes output of step 1
    train = train_component(
        train_data=prep.outputs.processed_data,
        learning_rate=lr,
    )
    train.compute = "gpu-cluster"  # override per-step

    # Step 3
    evaluate = evaluate_component(
        model_dir=train.outputs.model_dir,
        val_data=prep.outputs.processed_data,
    )

    return {"model": train.outputs.model_dir, "metrics": evaluate.outputs.metrics}

# Instantiate and submit
pipeline_job = training_pipeline(
    raw_data=Input(type="uri_folder", path="azureml:my-training-data:1"),
    lr=0.05,
)
pipeline_job = ml_client.jobs.create_or_update(pipeline_job)
```

**Component reuse + caching**: AzureML fingerprints component code + inputs.
If both are unchanged, the cached output is reused — no recomputation. Critical
for pipelines that re-run on the same data. Disable with `force_rerun=True`.

---

## Model Registry

```
Model lifecycle in AzureML registry:

  [Job output]
      │
      ▼
  [Register]  ──► stage: Development
      │
      ▼ (pass evals)
  [Promote]   ──► stage: Staging
      │
      ▼ (integration tests pass)
  [Promote]   ──► stage: Production   ──► [Deploy to endpoint]
      │
      ▼ (superseded)
  [Archive]
```

### Registering a Model

```python
from azure.ai.ml.entities import Model
from azure.ai.ml.constants import AssetTypes

# From a training job output
model = Model(
    name="churn-classifier",
    version="5",
    description="XGBoost v3 feature set, AUC=0.912",
    path=f"azureml://jobs/{job.name}/outputs/model_dir",
    type=AssetTypes.CUSTOM_MODEL,
    properties={"val_auc": "0.912", "train_date": "2026-02-22"},
    tags={"framework": "xgboost", "task": "classification"},
)
registered_model = ml_client.models.create_or_update(model)
```

**MLflow flavors**: If you log with `mlflow.sklearn.log_model()` or
`mlflow.pytorch.log_model()`, the model type is `MLFLOW_MODEL`. These get
auto-wrappers for the MLflow `pyfunc` interface — deploy without a custom scoring script.

### Listing and Promoting

```python
# List all versions
for m in ml_client.models.list("churn-classifier"):
    print(m.version, m.tags, m.properties)

# Get specific version
model = ml_client.models.get("churn-classifier", version="5")

# Promote stage (via tags — AzureML doesn't have hard stages like MLflow)
model.tags["stage"] = "Production"
ml_client.models.create_or_update(model)
```

**Note**: AzureML v2 uses tags for stage tracking (unlike MLflow's explicit stage enum).
The Studio UI shows a "stage" column if you tag consistently.

---

## Online Endpoints (Real-Time Inference)

```
┌───────────────────────────────────────────────────────────────────┐
│                    MANAGED ONLINE ENDPOINT                        │
│                                                                   │
│  https://<endpoint-name>.<region>.inference.ml.azure.com/score   │
│                                                                   │
│         traffic split (100% blue / 0% green)                     │
│              │                  │                                 │
│    ┌─────────▼──────┐  ┌────────▼────────┐                       │
│    │  Deployment A  │  │  Deployment B   │                       │
│    │  (blue)        │  │  (green)        │                       │
│    │  model v5      │  │  model v6       │                       │
│    │  DS3_v2 × 2    │  │  DS3_v2 × 1    │                       │
│    └────────────────┘  └─────────────────┘                       │
│                                                                   │
│  Traffic split → canary / blue-green deployments                 │
└───────────────────────────────────────────────────────────────────┘
```

### Scoring Script

```python
# score.py — required for CUSTOM_MODEL, optional for MLFLOW_MODEL
import os, json, joblib
import numpy as np

model = None

def init():
    global model
    model_path = os.path.join(os.environ["AZUREML_MODEL_DIR"], "model.pkl")
    model = joblib.load(model_path)

def run(raw_data):
    data = json.loads(raw_data)
    X = np.array(data["data"])
    predictions = model.predict(X).tolist()
    return {"predictions": predictions}
```

### Deploy

```python
from azure.ai.ml.entities import (
    ManagedOnlineEndpoint, ManagedOnlineDeployment,
    Model, Environment, CodeConfiguration,
    ResourceRequirementsSettings, ResourceSettings,
)

# 1. Create endpoint (DNS name + auth)
endpoint = ManagedOnlineEndpoint(
    name="churn-endpoint",
    auth_mode="key",            # or "aml_token"
    description="Churn prediction endpoint",
)
ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# 2. Create deployment
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name="churn-endpoint",
    model="azureml:churn-classifier:5",
    environment="azureml:my-training-env:3",
    code_configuration=CodeConfiguration(
        code="./inference",
        scoring_script="score.py",
    ),
    instance_type="Standard_DS3_v2",
    instance_count=2,
    # Autoscaling
    scale_settings=ResourceRequirementsSettings(
        request_settings=ResourceSettings(request_cpu_milli_cores=500),
    ),
)
ml_client.online_deployments.begin_create_or_update(deployment).result()

# 3. Route 100% traffic to blue
endpoint.traffic = {"blue": 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
```

### Invoke

```python
import json
from azure.ai.ml.entities import OnlineRequestProperties

# SDK
response = ml_client.online_endpoints.invoke(
    endpoint_name="churn-endpoint",
    request_file="./sample_request.json",
    deployment_name="blue",
)

# HTTP directly
import requests
endpoint_url = ml_client.online_endpoints.get("churn-endpoint").scoring_uri
headers = {
    "Authorization": f"Bearer {ml_client.online_endpoints.get_keys('churn-endpoint').primary_key}",
    "Content-Type": "application/json",
}
response = requests.post(endpoint_url, json={"data": [[1.2, 3.4, 5.6]]}, headers=headers)
```

### Blue/Green + Canary

```python
# Deploy canary (green) alongside blue
green = ManagedOnlineDeployment(name="green", endpoint_name="churn-endpoint", ...)
ml_client.online_deployments.begin_create_or_update(green).result()

# Canary: 10% to green
endpoint.traffic = {"blue": 90, "green": 10}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()

# Promote green to full traffic after validation
endpoint.traffic = {"blue": 0, "green": 100}
ml_client.online_endpoints.begin_create_or_update(endpoint).result()
```

### MLflow Model Deployment (No Scoring Script)

```python
# If model was logged with mlflow.pyfunc / mlflow.sklearn / mlflow.pytorch
deployment = ManagedOnlineDeployment(
    name="blue",
    endpoint_name="churn-endpoint",
    model="azureml:churn-classifier-mlflow:5",   # MLFLOW_MODEL type
    # No code_configuration needed!
    instance_type="Standard_DS3_v2",
    instance_count=1,
)
```

AzureML generates the scoring script from the MLflow `pyfunc` interface automatically.
Input format: `{"input_data": {"columns": [...], "data": [[...]]}}`.

---

## Batch Endpoints

For large-scale offline scoring — millions of rows, files on blob storage.

```python
from azure.ai.ml.entities import (
    BatchEndpoint, BatchDeployment, BatchRetrySettings,
    BatchDeploymentSettings,
)

# Endpoint
batch_endpoint = BatchEndpoint(name="churn-batch-endpoint")
ml_client.batch_endpoints.begin_create_or_update(batch_endpoint).result()

# Deployment
batch_deployment = BatchDeployment(
    name="batch-v1",
    endpoint_name="churn-batch-endpoint",
    model="azureml:churn-classifier:5",
    code_configuration=CodeConfiguration(code="./batch_score", scoring_script="score.py"),
    environment="azureml:my-training-env:3",
    compute="cpu-cluster",
    instance_count=4,
    max_concurrency_per_instance=2,
    mini_batch_size=10,                 # files per mini-batch
    output_action="append_row",         # all outputs → single file
    retry_settings=BatchRetrySettings(max_retries=3, timeout=300),
)
ml_client.batch_deployments.begin_create_or_update(batch_deployment).result()

# Invoke
from azure.ai.ml import Input
job = ml_client.batch_endpoints.invoke(
    endpoint_name="churn-batch-endpoint",
    input=Input(type="uri_folder", path="azureml:scoring-data:1"),
)
ml_client.jobs.stream(job.name)
```

**Batch vs Online decision**:
- Online: latency < 1 sec, real-time serving, REST endpoint
- Batch: throughput > latency, large datasets, scheduled/triggered jobs

---

## Experiment Tracking Integration

AzureML integrates MLflow natively — the workspace is an MLflow tracking server.

```python
import mlflow
import os

# In a training job, AzureML injects these env vars automatically:
# MLFLOW_TRACKING_URI → points to workspace
# MLFLOW_EXPERIMENT_NAME → set from job.experiment_name

# Just use mlflow normally — no extra config in training code
with mlflow.start_run():
    mlflow.log_params({"lr": 0.01, "depth": 6})
    mlflow.log_metric("val_auc", 0.912)
    mlflow.sklearn.log_model(model, "model")   # registers artifact

# From outside (e.g., local dev connecting to workspace)
mlflow.set_tracking_uri(ml_client.workspaces.get(workspace_name).mlflow_tracking_uri)
mlflow.set_experiment("xgboost-classifier")
```

**What gets auto-logged** without any code changes:
```python
mlflow.autolog()    # in training script
# sklearn: params (n_estimators, max_depth...), metrics (accuracy, AUC), confusion matrix
# pytorch: training/val loss per epoch
# xgboost: eval results
```

### Accessing Run Data Programmatically

```python
from mlflow.tracking import MlflowClient

client = MlflowClient(tracking_uri=workspace.mlflow_tracking_uri)

# Get best run from an experiment
experiment = client.get_experiment_by_name("xgboost-classifier")
runs = client.search_runs(
    experiment_ids=[experiment.experiment_id],
    order_by=["metrics.val_auc DESC"],
    max_results=1,
)
best_run = runs[0]
print(best_run.data.metrics, best_run.data.params)
```

---

## Responsible AI Dashboard

AzureML ships a Responsible AI (RAI) dashboard — model interpretability, fairness,
error analysis, causal analysis — all in one UI panel.

```python
from azure.ai.ml.entities import (
    ResponsibleAIInsights,
    ResponsibleAIComponentParameter,
)

# Add as a pipeline component after training
rai_job = pipeline(...)
rai_insights = ResponsibleAIInsights(
    target_column_name="churned",
    task_type="classification",
    model_info={"model_name": "churn-classifier", "model_version": "5"},
    train_dataset=prep.outputs.train_data,
    test_dataset=prep.outputs.test_data,
    components=[
        "model_overview",        # metrics breakdown
        "error_analysis",        # error tree + heatmap
        "data_explorer",         # distribution analysis
        "feature_importances",   # SHAP values
        "causal_analysis",       # causal effect estimates
        "counterfactual",        # what-if exploration
    ],
)
```

**When to use**: Required for Azure Responsible AI compliance in regulated industries.
SHAP-based feature importances work for tree models and neural nets.

---

## CLI v2 — YAML-First Workflow

CLI v2 is the CI/CD surface. Everything that can be done in SDK v2 can also be
expressed as a YAML file and submitted with `az ml`.

```yaml
# job.yaml
$schema: https://azuremlschemas.azureedge.net/latest/commandJob.schema.json
type: command
display_name: train-xgboost
experiment_name: xgboost-classifier
code: ./src
command: >-
  python train.py
  --data ${{inputs.data}}
  --lr ${{inputs.lr}}
inputs:
  data:
    type: uri_folder
    path: azureml:my-training-data:1
  lr: 0.01
environment: azureml:my-training-env:3@latest
compute: azureml:gpu-cluster
resources:
  instance_count: 1
```

```bash
# Submit
az ml job create -f job.yaml --workspace-name my-ws --resource-group my-rg

# Stream logs
az ml job stream -n <job-name> -w my-ws -g my-rg

# Download outputs
az ml job download -n <job-name> --output-name model_dir -w my-ws -g my-rg
```

### GitHub Actions CI/CD Pipeline

```yaml
# .github/workflows/train-deploy.yml
name: Train and Deploy Model

on:
  push:
    branches: [main]
    paths: ["src/**", "components/**"]

jobs:
  train-deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Azure Login
        uses: azure/login@v2
        with:
          creds: ${{ secrets.AZURE_CREDENTIALS }}

      - name: Set AzureML defaults
        run: |
          az configure --defaults \
            workspace=${{ vars.AML_WORKSPACE }} \
            resource-group=${{ vars.AML_RG }}

      - name: Submit training job
        id: train
        run: |
          JOB_NAME=$(az ml job create -f job.yaml --query name -o tsv)
          az ml job stream -n $JOB_NAME
          echo "job_name=$JOB_NAME" >> $GITHUB_OUTPUT

      - name: Register model
        run: |
          az ml model create \
            --name churn-classifier \
            --path azureml://jobs/${{ steps.train.outputs.job_name }}/outputs/model_dir \
            --type custom_model

      - name: Deploy to staging
        run: az ml online-deployment create -f deployment-staging.yaml
```

---

## Azure AI Studio vs AzureML Studio

```
┌─────────────────────────────────────────────────────────────────────┐
│  Two portals — different focus, converging                          │
│                                                                     │
│  AzureML Studio (ml.azure.com)                                      │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │  • Classic ML: training, pipeline, model registry         │     │
│  │  • Compute management, datastores                         │     │
│  │  • AutoML, sweep jobs                                     │     │
│  │  • Responsible AI dashboard                               │     │
│  └───────────────────────────────────────────────────────────┘     │
│                                                                     │
│  Azure AI Studio (ai.azure.com)                                     │
│  ┌───────────────────────────────────────────────────────────┐     │
│  │  • Generative AI: Azure OpenAI, Phi, Llama fine-tuning    │     │
│  │  • Prompt Flow — LLM orchestration                        │     │
│  │  • AI Search integration                                  │     │
│  │  • Safety evaluations (content safety, groundedness)      │     │
│  │  • Model catalog (400+ models from Hugging Face/OpenAI)   │     │
│  └───────────────────────────────────────────────────────────┘     │
│                                                                     │
│  Use AzureML Studio for classical ML + custom training             │
│  Use Azure AI Studio for LLM/GenAI workloads                       │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Prompt Flow (Azure AI Studio)

Prompt Flow is AzureML Pipelines but for LLM applications — DAG where nodes are
LLM calls, Python tools, or prompt templates.

```yaml
# flow.dag.yaml
inputs:
  question:
    type: string
outputs:
  answer:
    type: string
    reference: ${generate_answer.output}

nodes:
  - name: retrieve_context
    type: python
    source:
      type: code
      path: retrieve.py
    inputs:
      question: ${inputs.question}

  - name: generate_answer
    type: llm
    source:
      type: code
      path: generate.py
    inputs:
      prompt: ${generate_answer.template}
      context: ${retrieve_context.output}
      question: ${inputs.question}
    connection: azure-openai-connection
    api: chat
    model: gpt-4o
```

```bash
# Run locally
pf flow test --flow . --inputs question="What is the capital of France?"

# Batch eval against dataset
pf run create --flow . --data ./eval_data.jsonl --column-mapping question='${data.question}'

# Deploy to endpoint
pf flow build --source . --output ./build --format docker
az ml online-deployment create -f deployment.yaml
```

**Prompt Flow vs LangChain**: Prompt Flow is Azure-native with built-in evaluation,
connection management, and Studio visualization. LangChain is more flexible but
requires more wiring. For Azure-committed teams, Prompt Flow reduces ops burden.

---

## Security and Governance

```
┌─────────────────────────────────────────────────────────────────────┐
│  SECURITY LAYERS                                                    │
│                                                                     │
│  Identity & Access                                                  │
│  ├── Managed Identity (workspace → ACR/Storage, no secrets)        │
│  ├── RBAC (Owner/Contributor/Reader + 5 AzureML-specific roles)    │
│  └── Entra ID integration (SSO, conditional access)                │
│                                                                     │
│  Network                                                            │
│  ├── Private Endpoint (workspace accessible only from VNet)        │
│  ├── No public internet from training compute                      │
│  └── Egress → Azure Firewall or NAT Gateway                        │
│                                                                     │
│  Data                                                               │
│  ├── Encryption at rest (ADE + CMK via Key Vault)                  │
│  ├── Encryption in transit (TLS everywhere)                        │
│  └── Data exfiltration prevention (outbound rules)                 │
│                                                                     │
│  Compliance                                                         │
│  ├── Audit logs → Azure Monitor (every API call)                   │
│  ├── Policy (deny non-compliant VM SKUs, enforce tags)             │
│  └── Private link workspace + no public access = FedRAMP-ready     │
└─────────────────────────────────────────────────────────────────────┘
```

### Managed Identity Pattern (preferred)

```python
# In a training job — no credentials in code
from azure.identity import ManagedIdentityCredential
from azure.keyvault.secrets import SecretClient

# The compute VM has a managed identity assigned by AzureML
credential = ManagedIdentityCredential()
kv_client = SecretClient("https://my-kv.vault.azure.net", credential)
api_key = kv_client.get_secret("openai-api-key").value

# Storage access — also via managed identity, no SAS tokens
from azure.storage.blob import BlobServiceClient
blob_client = BlobServiceClient("https://mystorge.blob.core.windows.net", credential)
```

---

## Cost Management

| Resource | Cost driver | Optimization |
|----------|-------------|--------------|
| Compute Cluster | VM hours (billed per second) | `min_instances=0` always; use LowPriority for non-critical jobs |
| Compute Instance | Running VM (even idle) | **Stop when not in use** — auto-shutdown schedules |
| Managed Online Endpoint | Per-hour per-instance | Scale to 0 not supported for ManagedOnline; use ACA or K8s attach for scale-to-zero |
| Batch Endpoint | Only billed during job execution | Natural scale-to-zero — no cost between runs |
| Storage (artifacts) | GB stored + transactions | Set lifecycle policies to tier old artifacts to Cool/Archive |
| ACR (environments) | Image storage | Share base images; curated envs = no ACR cost |

```python
# Auto-shutdown for Compute Instance
from azure.ai.ml.entities import ComputeInstance, ComputeInstanceAutoStopSettings

instance = ComputeInstance(
    name="dev-instance",
    size="Standard_DS3_v2",
    auto_stop_settings=ComputeInstanceAutoStopSettings(enabled=True, idle_time_before_shutdown="PT30M"),
)
```

---

## AzureML vs Alternatives

| Dimension | AzureML | SageMaker | Vertex AI | Databricks |
|-----------|---------|-----------|-----------|------------|
| **Cloud** | Azure | AWS | GCP | Multi-cloud |
| **ML framework** | Any | Any | Any | Spark-first |
| **LLM/GenAI** | Azure AI Studio | Bedrock | Vertex Generative AI | MLflow + DBRX |
| **Pipeline** | AzureML Pipelines / Prompt Flow | Pipelines / SageMaker Studio | Vertex Pipelines (Kubeflow) | Delta + Job clusters |
| **Model Registry** | AzureML Registry | SageMaker Model Registry | Vertex Model Registry | MLflow Registry |
| **AutoML** | Native | Autopilot | AutoML | AutoML (via sklearn) |
| **Pricing model** | VM hours + endpoint hours | Instance hours + inference | Node hours + prediction | DBU-based |
| **Azure integration** | Native (ADX, Synapse, Fabric) | — | — | Native ADF integration |

**When to choose AzureML**: Azure-committed shop, regulatory compliance needs, tight
Entra ID / RBAC integration, existing .NET/Azure DevOps pipelines.

---

## Decision Cheat Sheet

| Need | Use |
|------|-----|
| Interactive dev / notebook | Compute Instance + Studio |
| Train a model (single GPU) | Command Job on Compute Cluster |
| Train (multi-GPU / multi-node) | Command Job + TorchDistribution |
| Hyperparameter search | Sweep Job (Bayesian + Bandit termination) |
| No ML code, just tabular classification | AutoML |
| Reusable pipeline with caching | AzureML Pipelines + Components |
| Real-time inference (<1s latency) | Managed Online Endpoint |
| Batch scoring (millions of rows) | Batch Endpoint |
| LLM orchestration + eval | Prompt Flow (Azure AI Studio) |
| Fine-tune GPT-4o / Phi / Llama | Azure AI Studio fine-tuning |
| Govern data access | Datastores + Managed Identity + Private Endpoints |
| Blue/green deploy | Traffic split on Online Endpoint |
| CI/CD for ML | CLI v2 YAML + GitHub Actions |
| Cost: dev machine | Compute Instance auto-stop (30 min idle) |
| Cost: training | Compute Cluster min=0 + LowPriority tier |

---

## Common Confusion Points

**`az ml` vs `az cognitiveservices`**: AzureML (`az ml`) is for training + classical ML.
Azure OpenAI / Azure AI Services use a different resource type and CLI namespace.

**AzureML Studio vs Azure AI Studio**: Two different portals. `ml.azure.com` for
classical ML. `ai.azure.com` for GenAI/LLM/Prompt Flow. They share the model registry
and some compute resources.

**SDK v1 vs SDK v2**: If you see `from azureml.core import Workspace` — that's SDK v1
(deprecated). The current SDK is `from azure.ai.ml import MLClient`. The namespace
change is intentional — v2 is a redesign, not a version bump.

**MLflow tracking URI**: Inside a training job, `MLFLOW_TRACKING_URI` is auto-set.
Outside (local dev connecting to workspace), you must set it explicitly via
`ml_client.workspaces.get().mlflow_tracking_uri`.

**Compute Instance ≠ Compute Cluster**: Instance is one VM for one person.
Cluster autoscales, multi-user, scales to zero. Don't run training on an Instance.

**Environment build time**: First job with a new environment triggers a Docker build
in ACR (5-15 min cold start). Pin environment versions in production to avoid surprises.

**`AZUREML_MODEL_DIR` env var**: Inside a scoring script, the model artifact is
mounted at `os.environ["AZUREML_MODEL_DIR"]`. Path is not predictable without this var.

**Managed Identity for compute**: Assign a user-assigned managed identity to compute
so training code can access Key Vault, Storage, and other services without credentials
in code. This is the AzureML equivalent of "run under service account" from old VSTS.
