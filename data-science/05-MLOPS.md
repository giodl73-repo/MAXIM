# 05 — MLOps

> MLOps is DevOps applied to ML systems, with one extra dimension:
> the behavior of software changes when data changes, even when code doesn't.
> That's what makes it harder.

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         MLOPS LIFECYCLE                                     │
│                                                                             │
│  DATA        TRAINING         EVALUATION      DEPLOYMENT      MONITORING    │
│                                                                             │
│  ┌────────┐  ┌────────────┐  ┌────────────┐  ┌──────────┐  ┌──────────┐     │
│  │ ingest │→ │ experiment │→ │   eval /   │→ │  model   │→ │  drift   │  │
│  │ validate│  │  track    │  │  register  │  │  serve   │  │  monitor │  │
│  │ version│  │            │  │            │  │          │  │  retrain │  │
│  └────────┘  └────────────┘  └────────────┘  └──────────┘  └──────────┘  │
│       │             │               │               │              │        │
│  DVC/       MLflow/W&B         MLflow            BentoML/       Evidently  │
│  Great       Experiment        Model             Seldon/        / Arize    │
│  Expectations  Tracking        Registry          FastAPI        / WhyLabs  │
│                                                  + K8s                     │
└─────────────────────────────────────────────────────────────────────────────┘
```

The key difference from standard DevOps: **a model is correct only relative to
a data distribution**. Redeploying identical code with new data can produce worse
behavior. This requires versioning data, not just code.

---

## Experiment Tracking

### Why Tracking Matters

Without tracking, ML experiments are ephemeral. You run 50 variants of a model,
the one that worked is in a Jupyter notebook that you accidentally overwrote.
Experiment tracking turns experiments into reproducible, comparable artifacts.

### MLflow

MLflow is open-source, self-hostable, and integrates with Azure ML natively.
The most common choice for enterprises with existing Azure infrastructure.

```python
import mlflow
import mlflow.sklearn
import mlflow.pytorch
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.metrics import roc_auc_score

# Connect to tracking server
mlflow.set_tracking_uri("http://localhost:5000")  # or "azureml://..." for Azure ML
mlflow.set_experiment("customer-churn-prediction")

with mlflow.start_run(run_name="gbm-v3"):
    # Log hyperparameters
    params = {"n_estimators": 200, "max_depth": 4, "learning_rate": 0.05}
    mlflow.log_params(params)

    # Train
    model = GradientBoostingClassifier(**params)
    model.fit(X_train, y_train)

    # Log metrics
    auc = roc_auc_score(y_test, model.predict_proba(X_test)[:, 1])
    mlflow.log_metric("roc_auc", auc)
    mlflow.log_metric("n_train_samples", len(X_train))

    # Log model artifact
    mlflow.sklearn.log_model(
        model,
        artifact_path="model",
        registered_model_name="churn-predictor",  # registers in Model Registry
        input_example=X_train[:5],
        signature=mlflow.models.infer_signature(X_train, model.predict(X_train)),
    )

    # Log arbitrary artifacts (plots, configs, data samples)
    mlflow.log_artifact("feature_importance.png")
    mlflow.log_dict({"feature_names": list(feature_names)}, "features.json")

# Autolog — instruments framework automatically
mlflow.sklearn.autolog()    # captures params, metrics, model for sklearn
mlflow.pytorch.autolog()    # captures train/val loss, optimizer config
mlflow.xgboost.autolog()
```

### MLflow Tracking Server

```bash
# Start locally
mlflow server --backend-store-uri sqlite:///mlflow.db \
              --default-artifact-root ./mlruns \
              --host 0.0.0.0 --port 5000

# UI at http://localhost:5000 — experiment comparison, metric plots, artifact browser
```

### Weights & Biases (W&B)

W&B is cloud-first, with a richer UI and tighter deep learning integration.
Preferred for research teams and long training runs.

```python
import wandb

wandb.init(
    project="image-classifier",
    name="resnet50-run-3",
    config={
        "learning_rate": 1e-3,
        "batch_size": 64,
        "epochs": 50,
        "architecture": "ResNet50",
    }
)

# Training loop
for epoch in range(50):
    train_loss = train_epoch(model, train_loader, ...)
    val_loss, val_acc = evaluate(model, val_loader, ...)

    wandb.log({
        "epoch": epoch,
        "train/loss": train_loss,
        "val/loss": val_loss,
        "val/accuracy": val_acc,
        "learning_rate": scheduler.get_last_lr()[0],
    })

    # Log model checkpoint as artifact
    if val_loss < best_val_loss:
        wandb.save("model_best.pt")

# Log summary metrics
wandb.summary["best_val_accuracy"] = best_val_acc
wandb.finish()

# Sweep (hyperparameter search managed by W&B)
sweep_config = {
    "method": "bayes",   # bayesian optimization
    "metric": {"name": "val/accuracy", "goal": "maximize"},
    "parameters": {
        "learning_rate": {"min": 1e-4, "max": 1e-2, "distribution": "log_uniform_values"},
        "batch_size":    {"values": [32, 64, 128]},
        "dropout":       {"min": 0.1, "max": 0.5},
    }
}
sweep_id = wandb.sweep(sweep_config, project="image-classifier")
wandb.agent(sweep_id, function=train_fn, count=30)
```

### MLflow vs W&B

```
┌────────────────────────────────────────────────────────────────────┐
│                  │  MLflow            │  Weights & Biases          │
├──────────────────┼────────────────────┼───────────────────────────┤
│  Hosting         │  Self or Azure ML  │  Cloud (SaaS)             │
│  Open source     │  Yes               │  Client SDK only          │
│  DL integration  │  Good              │  Excellent                │
│  Hyperparameter  │  Basic             │  Sweeps (Bayesian)        │
│  sweep           │                    │                           │
│  Data versioning │  Via DVC           │  W&B Artifacts            │
│  Collaboration   │  Basic             │  Team-oriented            │
│  Azure ML native │  Yes (built-in)    │  No                       │
│  Best for        │  Sklearn/XGBoost/  │  Deep learning, research, │
│                  │  enterprise Azure  │  long GPU runs            │
└────────────────────────────────────────────────────────────────────┘
```

---

## Model Registry

A model registry is a versioned catalog of trained models with lifecycle states.

**Software release lifecycle bridge**: the state machine is identical to standard
software deployment gates — any DevOps engineer maps it immediately:

```
Software release lifecycle       MLflow model registry equivalent
─────────────────────────────    ──────────────────────────────────────────────
Dev / Feature branch             None (experimental run, not yet registered)
QA / Staging environment         Staging  (validated on holdout; ready for test)
Production                       Production  (serving live traffic)
Deprecated / EOL                 Archived  (superseded; kept for reproducibility)

Quality gate (CI/CD):
  PR passes tests → merge to main     ERM run passes eval suite → promote Staging
  Integration test passes → deploy    Integration test passes → promote Production
  New version released → old retires  New model in Prod → old model archived

Version pinning:
  package.json "1.2.3" (exact)        models:/churn-predictor/5 (version number)
  package.json "^1.2"  (compatible)   models:/churn-predictor/Production (alias)
```

The key ML-specific addition: promotion gates are metric-based, not just
test-pass/fail. The eval suite compares the candidate model against the current
Production model on a held-out dataset — a model only moves to Staging if it
wins on the primary metric (AUC, RMSE, etc.) with a statistically meaningful margin.

### MLflow Model Registry

```python
import mlflow
from mlflow.tracking import MlflowClient

client = MlflowClient()

# Register a model (also done in log_model above)
model_uri = f"runs:/{run_id}/model"
mv = mlflow.register_model(model_uri, "churn-predictor")

# Transition through lifecycle stages
client.transition_model_version_stage(
    name="churn-predictor",
    version=mv.version,
    stage="Staging",           # None → Staging → Production → Archived
    archive_existing_versions=False,
)

# Add annotations
client.update_model_version(
    name="churn-predictor",
    version=mv.version,
    description="GBM with feature set v3. AUC=0.91 on Q4 holdout."
)

# Load a specific version for inference
model = mlflow.sklearn.load_model("models:/churn-predictor/Production")
predictions = model.predict(X_new)

# Load by version number
model = mlflow.sklearn.load_model("models:/churn-predictor/5")
```

### Lifecycle State Machine

```
None (experimental)
  │
  ▼
Staging (validated, ready for integration testing)
  │
  ▼
Production (serving live traffic)
  │
  ▼
Archived (superseded, kept for reproducibility)
```

Promotion between stages should be gated on eval metrics, not manual judgment.
Wire the registry transitions into CI: a pipeline runs the eval suite, and on
pass automatically promotes from Staging to Production.

---

## Data Versioning — DVC

Data Version Control (DVC) extends Git to large files and ML datasets.
Git tracks code; DVC tracks data and model artifacts (storing them in S3/Azure
Blob/GCS with only a small pointer file in Git).

```bash
# Initialize in a Git repo
git init && dvc init

# Track a dataset
dvc add data/training.csv       # creates data/training.csv.dvc (tracked by Git)
git add data/training.csv.dvc .gitignore
git commit -m "Add training dataset v1"

# Push data to remote storage
dvc remote add -d azure_store azure://mycontainer/dvc-cache
dvc remote modify azure_store connection_string "DefaultEndpointsProtocol=..."
dvc push                        # uploads data/training.csv to Azure Blob

# Reproduce — pull data + run pipeline
dvc pull                        # downloads the data
dvc repro                       # runs the pipeline defined in dvc.yaml
```

### DVC Pipeline (dvc.yaml)

```yaml
# dvc.yaml — tracks data transformations as a DAG
stages:
  prepare:
    cmd: python src/prepare.py
    deps:
      - src/prepare.py
      - data/raw.csv
    outs:
      - data/prepared.csv

  train:
    cmd: python src/train.py
    deps:
      - src/train.py
      - data/prepared.csv
    params:
      - params.yaml:
          - model.n_estimators
          - model.max_depth
    outs:
      - models/model.pkl
    metrics:
      - metrics/eval.json:
          cache: false   # track in Git, not DVC

  evaluate:
    cmd: python src/evaluate.py
    deps:
      - src/evaluate.py
      - models/model.pkl
      - data/test.csv
    metrics:
      - metrics/eval.json:
          cache: false
```

```bash
dvc repro          # re-runs only changed stages (like Make, but for ML)
dvc dag            # show pipeline graph
dvc metrics show   # display tracked metrics
dvc metrics diff   # compare metrics between Git commits
```

---

## Data Validation — Great Expectations

Great Expectations (GX) defines test suites for data — the same discipline
as unit testing, applied to datasets.

```python
import great_expectations as gx

context = gx.get_context()

# Define expectations (what "good data" means)
suite = context.add_expectation_suite("training_data_suite")

validator = context.sources.pandas_default.read_csv("data/training.csv")

validator.expect_column_values_to_not_be_null("customer_id")
validator.expect_column_values_to_be_between("age", min_value=18, max_value=120)
validator.expect_column_values_to_be_in_set("status", ["active", "churned", "trial"])
validator.expect_column_pair_values_A_to_be_greater_than_B("end_date", "start_date")
validator.expect_table_row_count_to_be_between(min_value=10_000, max_value=5_000_000)

validator.save_expectation_suite()

# Validate new data against the suite
results = validator.validate()
if not results.success:
    raise ValueError(f"Data validation failed: {results}")
```

Run data validation as the first step in every training pipeline — before any
model code runs. A training run on corrupted data is far more expensive than
catching the corruption early.

---

## Model Serving

### Patterns

```
┌─────────────────────────────────────────────────────────────────────┐
│  SERVING PATTERN       │  LATENCY │  THROUGHPUT │  USE CASE         │
├────────────────────────┼──────────┼─────────────┼──────────────────┤
│  REST API (sync)       │  Low     │  Medium     │  Interactive UX  │
│  Batch inference       │  High    │  Very high  │  Nightly scoring │
│  Streaming (Kafka)     │  Medium  │  High       │  Event-driven    │
│  Edge / embedded       │  Ultra   │  Variable   │  Mobile, IoT     │
└────────────────────────┴──────────┴─────────────┴──────────────────┘
```

### FastAPI + MLflow Serving (Simple)

```python
from fastapi import FastAPI
import mlflow.sklearn
import numpy as np
from pydantic import BaseModel

app = FastAPI()
model = mlflow.sklearn.load_model("models:/churn-predictor/Production")

class PredictRequest(BaseModel):
    features: list[list[float]]

class PredictResponse(BaseModel):
    predictions: list[int]
    probabilities: list[float]

@app.post("/predict", response_model=PredictResponse)
def predict(request: PredictRequest):
    X = np.array(request.features)
    preds = model.predict(X)
    probs = model.predict_proba(X)[:, 1]
    return PredictResponse(
        predictions=preds.tolist(),
        probabilities=probs.tolist(),
    )

@app.get("/health")
def health():
    return {"status": "ok"}
```

```bash
# Serve with gunicorn + uvicorn workers
gunicorn app:app -k uvicorn.workers.UvicornWorker -w 4 --bind 0.0.0.0:8000

# Or MLflow's built-in server
mlflow models serve -m "models:/churn-predictor/Production" -p 5001 --no-conda
```

### BentoML (Production Serving Framework)

```python
import bentoml
from bentoml.io import NumpyNdarray, JSON

# Save model to BentoML store
bentoml.sklearn.save_model("churn_predictor", model,
                            signatures={"predict": {"batchable": True}})

# Define service
svc = bentoml.Service("churn_predictor_svc",
                       runners=[bentoml.sklearn.get("churn_predictor:latest").to_runner()])

@svc.api(input=NumpyNdarray(), output=NumpyNdarray())
async def predict(input_arr):
    return await runner.predict.async_run(input_arr)
```

```bash
bentoml serve service:svc --reload
bentoml build                 # package into a Bento (deployable artifact)
bentoml containerize churn_predictor_svc:latest  # → Docker image
```

### ONNX — Model Format for Portable Inference

Convert a PyTorch or sklearn model to ONNX for framework-independent deployment:

```python
import torch
import onnx
import onnxruntime as ort

# Export PyTorch model
dummy_input = torch.randn(1, 128)
torch.onnx.export(
    model, dummy_input,
    "model.onnx",
    input_names=["features"],
    output_names=["logits"],
    dynamic_axes={"features": {0: "batch_size"}, "logits": {0: "batch_size"}},
    opset_version=17,
)

# Run with ONNX Runtime (no PyTorch dependency)
session = ort.InferenceSession("model.onnx",
                                providers=["CUDAExecutionProvider",
                                           "CPUExecutionProvider"])
outputs = session.run(None, {"features": X_test.numpy()})
```

ONNX Runtime is often 2–10× faster than PyTorch for inference (no Python overhead,
graph-level optimizations). Standard for edge, mobile, and high-throughput serving.

---

## Model Monitoring and Drift Detection

### What to Monitor

```
┌─────────────────────────────────────────────────────────────────────┐
│  SIGNAL                │  MEASURES              │  TOOL             │
├────────────────────────┼────────────────────────┼──────────────────┤
│  Prediction drift      │  Output distribution   │  Evidently       │
│                        │  shifts over time      │  Arize / WhyLabs │
│  Data drift            │  Input features shift  │  Evidently       │
│  (covariate shift)     │  from training dist.   │  Alibi Detect    │
│  Concept drift         │  P(y|X) changes        │  Requires labels │
│  Model performance     │  Accuracy / AUC on     │  MLflow / W&B    │
│  (with labels)         │  labeled prod sample   │                  │
│  Infrastructure        │  Latency, error rate,  │  Prometheus /    │
│                        │  throughput, OOM       │  OTel            │
└─────────────────────────────────────────────────────────────────────┘
```

### Evidently — Drift Reports

```python
from evidently import ColumnMapping
from evidently.report import Report
from evidently.metric_preset import DataDriftPreset, ClassificationPreset

column_mapping = ColumnMapping(
    target="churn",
    prediction="prediction",
    numerical_features=["age", "tenure", "monthly_charges"],
    categorical_features=["contract_type", "region"],
)

# Weekly drift report
report = Report(metrics=[DataDriftPreset(), ClassificationPreset()])
report.run(
    reference_data=training_data,   # the distribution the model was trained on
    current_data=production_week,   # this week's production data
    column_mapping=column_mapping,
)
report.save_html("drift_report.html")

# Programmatic drift check (for CI/alerting)
result = report.as_dict()
drift_detected = result["metrics"][0]["result"]["dataset_drift"]
if drift_detected:
    trigger_retraining_pipeline()
```

### Statistical Tests for Drift

```
┌─────────────────────────────────────────────────────────────────────┐
│  TEST               │  FOR               │  WHEN               │
├─────────────────────┼────────────────────┼─────────────────────┤
│  Kolmogorov-Smirnov │  Continuous feat.  │  Enough samples     │
│  PSI (Pop. Stab.)   │  Continuous        │  Credit/risk models │
│  Chi-squared        │  Categorical       │  Standard           │
│  MMD                │  High-dimensional  │  Embeddings         │
│  CUSUM / Page-Hinkley│ Online detection  │  Streaming          │
└─────────────────────┴────────────────────┴─────────────────────┘

PSI < 0.1:  no significant shift
PSI 0.1–0.2:  moderate shift — monitor closely
PSI > 0.2:  significant shift — consider retraining
```

---

## Retraining Pipelines

```
┌─────────────────────────────────────────────────────────────────────┐
│  RETRAINING TRIGGER                │  PATTERN                       │
├────────────────────────────────────┼───────────────────────────────┤
│  Scheduled (e.g., weekly)          │  Simple, predictable          │
│  Data volume threshold             │  Retrain when N new samples   │
│  Drift detected (automated)        │  Evidently → trigger CI       │
│  Performance degradation           │  Requires ground truth labels │
│  Manual (team decision)            │  Major distribution change    │
└────────────────────────────────────┴───────────────────────────────┘
```

### Continuous Training Pipeline (sketch)

```python
# Triggered by Airflow / Azure ML Schedule / GitHub Actions cron
def retraining_pipeline():
    # 1. Validate new data
    validate_data("data/new_batch.parquet")

    # 2. Merge with existing training set
    new_data = prepare_data("data/new_batch.parquet")

    # 3. Train with same hyperparameters (or re-tune if drifted)
    with mlflow.start_run():
        model = train_model(new_data)
        auc = evaluate_model(model)
        mlflow.log_metric("roc_auc", auc)
        mlflow.sklearn.log_model(model, "model",
                                  registered_model_name="churn-predictor")

    # 4. Compare against current production model
    prod_model = mlflow.sklearn.load_model("models:/churn-predictor/Production")
    prod_auc = evaluate_model(prod_model)  # on same holdout

    # 5. Auto-promote if new model wins
    if auc > prod_auc + 0.002:             # require meaningful improvement
        promote_to_production(run_id)
    else:
        notify_team(f"Retrain did not improve: {auc:.4f} vs {prod_auc:.4f}")
```

---

## CI/CD for ML (CI/ML)

```yaml
# .github/workflows/train-and-deploy.yml
name: Train + Deploy

on:
  schedule:
    - cron: "0 2 * * 1"   # weekly Monday 2am
  workflow_dispatch:        # manual trigger

jobs:
  validate-data:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Great Expectations
        run: |
          pip install great_expectations
          python scripts/validate_data.py

  train:
    needs: validate-data
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Train model
        env:
          MLFLOW_TRACKING_URI: ${{ secrets.MLFLOW_URI }}
        run: python scripts/train.py --register

  evaluate-and-promote:
    needs: train
    runs-on: ubuntu-latest
    steps:
      - name: Compare vs production
        run: python scripts/compare_and_promote.py --threshold 0.002

  deploy:
    needs: evaluate-and-promote
    runs-on: ubuntu-latest
    steps:
      - name: Deploy to staging
        run: |
          mlflow models build-docker -m "models:/churn-predictor/Staging" -n churn-model
          kubectl set image deployment/churn-model churn-model=churn-model:${{ github.sha }}
```

---

## Feature Stores

For teams where features are expensive to compute and shared across models:

```
┌─────────────────────────────────────────────────────────────────────┐
│  FEATURE STORE ARCHITECTURE                                         │
│                                                                     │
│  ┌──────────────────────────────┐                                   │
│  │  OFFLINE STORE               │  ← training, batch inference      │
│  │  (S3/Parquet/Snowflake)      │    point-in-time correct joins    │
│  └──────────────────────────────┘                                   │
│  ┌──────────────────────────────┐                                   │
│  │  ONLINE STORE                │  ← real-time inference            │
│  │  (Redis / DynamoDB)          │    low-latency feature lookup     │
│  └──────────────────────────────┘                                   │
│                                                                     │
│  TOOLS: Feast (open source), Tecton, Vertex AI Feature Store,      │
│         Azure ML Feature Store                                      │
└─────────────────────────────────────────────────────────────────────┘
```

Feature stores solve **training-serving skew**: the features computed at
training time must exactly match the features computed at inference time.
Without a feature store, this often silently diverges.

---

## Common Confusion Points

**Experiment tracking vs. model registry**: Tracking captures every run (params,
metrics, artifacts). The registry is a curated catalog of models that are
candidates for deployment. Not every run becomes a registered model version.

**Data drift vs. concept drift**: Data drift (covariate shift) means P(X) changed —
the input distribution shifted. Concept drift means P(y|X) changed — the same
inputs now have different correct outputs. Data drift is detectable without labels.
Concept drift requires ground truth, which is often delayed or absent.

**Training-serving skew**: The model performs well on the test set but poorly in
production. Most common cause: preprocessing or feature computation is implemented
differently in the training pipeline vs. the serving pipeline. Solution: use the
same Pipeline object for both (sklearn Pipeline, BentoML runner), or use a feature
store.

**Reproducibility requires more than code**: A training run is reproducible only if
you version code (Git), data (DVC), dependencies (requirements.txt + Docker), and
random seeds. Missing any one of these makes the run non-reproducible.

**Model staleness is not the same as model decay**: A model can be stale (trained
on old data) without decaying in performance, if the distribution is stable. Monitor
prediction drift and actual performance, not just model age.

---

## Decision Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────┐
│  TASK                           │  TOOL                             │
├─────────────────────────────────┼──────────────────────────────────┤
│  Experiment tracking (Azure)    │  MLflow (Azure ML backend)       │
│  Experiment tracking (DL/GPU)   │  W&B                             │
│  Hyperparameter sweep           │  W&B Sweeps or Optuna            │
│  Data versioning                │  DVC + S3/Azure Blob             │
│  Data validation                │  Great Expectations              │
│  Model registry                 │  MLflow Model Registry           │
│  Serving (quick/simple)         │  FastAPI + MLflow load_model     │
│  Serving (production grade)     │  BentoML or Seldon Core          │
│  Portable inference format      │  ONNX + ONNX Runtime             │
│  Batch scoring (large scale)    │  Azure ML pipelines (06-AZURE-ML)│
│  Drift detection                │  Evidently                       │
│  Feature store                  │  Feast or Azure ML Feature Store │
│  Retraining trigger             │  Drift alert → GitHub Actions    │
├─────────────────────────────────┼──────────────────────────────────┤
│  MONITORING                     │                                  │
│  Infrastructure metrics         │  Prometheus + Grafana            │
│  Prediction distribution        │  Evidently / Arize               │
│  Data quality in production     │  Great Expectations + scheduling │
│  Model performance (w/ labels)  │  MLflow custom metrics on sample │
└─────────────────────────────────┴──────────────────────────────────┘
```
