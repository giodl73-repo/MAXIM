# 03 — scikit-learn & Classical Machine Learning

> scikit-learn's genius is not the algorithms. It is the Estimator API —
> a uniform interface that makes every model, preprocessor, and selector
> composable into a Pipeline. The math you know; this is the API surface.

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    MACHINE LEARNING PROBLEM MAP                             │
│                                                                             │
│  INPUT DATA                                                                 │
│  ┌───────────────────────────────────────────────────────────────────────┐ │
│  │  X: feature matrix  (n_samples × n_features)  — always NumPy/Pandas  │ │
│  │  y: target vector   (n_samples,)   — supervised only                 │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│              │                                                              │
│       Has labels (y)?                                                       │
│       ┌──────┴──────────────────────────────────────┐                      │
│      Yes                                            No                     │
│       │                                              │                      │
│  SUPERVISED                                   UNSUPERVISED                 │
│  ┌────┴───────────────────┐             ┌─────┴─────────────────────┐     │
│  │  y is continuous?      │             │  Clustering               │     │
│  │  ┌───────────────────┐ │             │  KMeans, DBSCAN, Agglom.  │     │
│  │  │ YES → Regression  │ │             │                           │     │
│  │  │   LinearRegression│ │             │  Dimensionality Reduction │     │
│  │  │   Ridge, Lasso    │ │             │  PCA, t-SNE, UMAP         │     │
│  │  │   SVR, GBM, RF    │ │             │                           │     │
│  │  └───────────────────┘ │             │  Density Estimation       │     │
│  │  ┌───────────────────┐ │             │  GaussianMixture          │     │
│  │  │ NO → Classification│ │             └───────────────────────────┘     │
│  │  │   LogisticReg.    │ │                                                │
│  │  │   SVC, KNN        │ │                                                │
│  │  │   RandomForest    │ │                                                │
│  │  │   GradientBoost   │ │                                                │
│  │  └───────────────────┘ │                                                │
│  └────────────────────────┘                                                │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Cross-Framework Bridge

The Estimator API's `fit/transform/predict` contract is universal across ML frameworks — any practitioner from R or Spark will recognize the pattern:

```
Framework         Preprocessing object          Pipeline composition
──────────────    ──────────────────────────    ──────────────────────────────────
sklearn           StandardScaler, OneHotEncoder  Pipeline([("pre", prep),("clf",clf)])
R tidymodels      recipe() + step_*()            workflow() = recipe + model spec
R caret           preProcess()                   train(x, y, preProcess=c("scale"))
Spark MLlib       StandardScaler, StringIndexer  Pipeline(stages=[pre, clf])
H2O               H2OFrame ops                  pipeline via H2OAutoML
```

**R tidymodels ↔ sklearn** is the closest parallel. A tidymodels `recipe` plus a
`workflow` is architecturally identical to `ColumnTransformer` plus `Pipeline`:

```
tidymodels                                sklearn
──────────────────────────────────────    ──────────────────────────────────────────
recipe(outcome ~ ., data = train)         (no formula — specify explicitly)
  step_normalize(all_numeric())           StandardScaler() on numeric columns
  step_dummy(all_nominal(), one_hot=TRUE) OneHotEncoder() on categorical columns
  step_impute_median(all_numeric())       SimpleImputer(strategy="median")

workflow() %>%                            Pipeline(steps=[
  add_recipe(rec) %>%                         ("preprocessor", ColumnTransformer([...])),
  add_model(rand_forest())                    ("classifier", RandomForestClassifier()),
                                          ])

fit(wf, data = train)                     pipeline.fit(X_train, y_train)
predict(wf, new_data = test)              pipeline.predict(X_test)
```

The critical invariant is the same in both: preprocessing parameters (means, category
levels) are learned only on training data and applied to test data. Both frameworks
enforce this when used through the pipeline abstraction.

---

## The Estimator API

Every object in scikit-learn — models, preprocessors, transformers, selectors —
implements the same interface:

```
┌─────────────────────────────────────────────────────────────────────┐
│  ESTIMATOR INTERFACE                                                │
│                                                                     │
│  .fit(X, y=None)          → self        learns from training data  │
│  .predict(X)              → array       supervised output          │
│  .predict_proba(X)        → array       class probabilities        │
│  .transform(X)            → array       unsupervised transformation│
│  .fit_transform(X, y=None)→ array       fit then transform         │
│  .score(X, y)             → float       default metric (R² or acc) │
│  .get_params() / .set_params(**p)        hyperparameter access     │
└─────────────────────────────────────────────────────────────────────┘

Estimators with .transform():  Transformers  (scalers, encoders, PCA)
Estimators with .predict():    Predictors    (regressors, classifiers)
Both:                          Pipelines     (compose any sequence)
```

```python
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler
import numpy as np

X_train = np.random.rand(100, 5)
y_train = (X_train[:, 0] > 0.5).astype(int)

# Fit
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X_train)   # learn mean/std, then apply

model = LogisticRegression()
model.fit(X_scaled, y_train)               # learn coefficients

# Predict
X_test = np.random.rand(20, 5)
X_test_scaled = scaler.transform(X_test)  # apply learned mean/std — NOT fit_transform
predictions = model.predict(X_test_scaled)
probabilities = model.predict_proba(X_test_scaled)  # shape (20, 2)
```

**Critical invariant**: call `fit` only on training data. Call `transform` on test
data using the parameters learned from training. Never `fit_transform` on test data
— that leaks test statistics into the model.

---

## Pipeline

Pipeline chains transformers and a final estimator. It solves the fit-vs-transform
problem automatically and makes cross-validation correct by default.

```python
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import cross_val_score

# Heterogeneous columns — numeric and categorical
numeric_features = ["age", "income", "score"]
categorical_features = ["region", "plan_tier"]

preprocessor = ColumnTransformer(transformers=[
    ("num", StandardScaler(), numeric_features),
    ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_features),
])

pipeline = Pipeline(steps=[
    ("preprocessor", preprocessor),
    ("classifier",   GradientBoostingClassifier(n_estimators=100, max_depth=4)),
])

# fit / predict / score work exactly like a plain estimator
pipeline.fit(X_train, y_train)
y_pred = pipeline.predict(X_test)
score = pipeline.score(X_test, y_test)

# Cross-validation on the full pipeline — preprocessing is re-fit each fold
cv_scores = cross_val_score(pipeline, X, y, cv=5, scoring="roc_auc")
print(cv_scores.mean(), cv_scores.std())
```

Without Pipeline, fitting the scaler on all data before cross-validation is
data leakage — the model has seen statistics from the validation fold.
Pipeline makes it impossible to make that mistake.

---

## Preprocessing

### Numeric

```python
from sklearn.preprocessing import (
    StandardScaler,       # z-score: (x - mean) / std
    MinMaxScaler,         # scale to [0, 1]
    RobustScaler,         # median + IQR — robust to outliers
    PowerTransformer,     # Box-Cox / Yeo-Johnson → Gaussian shape
    QuantileTransformer,  # maps to uniform or normal distribution
    Normalizer,           # L2-normalize each sample (not each feature)
    PolynomialFeatures,   # add x², x*y, etc.
    SplineTransformer,    # B-spline basis expansion
    FunctionTransformer,  # apply any function: np.log, np.sqrt, etc.
)

# Which scaler when?
# StandardScaler   → model assumes Gaussian (LinearRegression, SVC, LogReg, PCA)
# MinMaxScaler     → model assumes bounded input (neural nets, KNN)
# RobustScaler     → data has outliers you want to keep
# PowerTransformer → right-skewed distributions (income, counts)
# Normalizer       → cosine similarity models (text, embeddings)
```

### Categorical

```python
from sklearn.preprocessing import (
    OrdinalEncoder,    # category → integer (preserves order)
    OneHotEncoder,     # category → binary vector (no order assumed)
    TargetEncoder,     # category → mean(y) per category (leakage-prone — use in pipeline)
    LabelEncoder,      # encode y labels (not features)
    LabelBinarizer,    # binary indicator matrix from y labels
)

# OneHotEncoder gotchas
enc = OneHotEncoder(
    handle_unknown="ignore",  # unknown categories → all zeros at test time
    sparse_output=False,      # return dense array (default is sparse matrix)
    drop="first",             # drop first category (avoids multicollinearity)
)

# High-cardinality categories: TargetEncoder > OneHotEncoder
# OneHotEncoder with 10k cities → 10k columns
# TargetEncoder → 1 column (replace with mean(y) per city — use in pipeline!)
from sklearn.preprocessing import TargetEncoder
enc = TargetEncoder(target_type="continuous", cv=5)  # cross-validated to prevent leakage
```

### Missing Values

```python
from sklearn.impute import (
    SimpleImputer,     # mean / median / most_frequent / constant
    KNNImputer,        # k-nearest-neighbor imputation
    IterativeImputer,  # multivariate (MICE — predict each feature from others)
)

imputer = SimpleImputer(strategy="median")
imputer = KNNImputer(n_neighbors=5)
```

---

## Model Selection and Evaluation

### Train/Test Split and Cross-Validation

```python
from sklearn.model_selection import (
    train_test_split,
    KFold, StratifiedKFold,
    cross_val_score, cross_validate,
    GridSearchCV, RandomizedSearchCV,
)

# Simple split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y  # stratify preserves class ratio
)

# K-Fold cross-validation
cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)
scores = cross_val_score(pipeline, X, y, cv=cv, scoring="roc_auc")

# Multiple metrics at once
results = cross_validate(pipeline, X, y, cv=cv,
                          scoring=["roc_auc", "f1", "precision", "recall"],
                          return_train_score=True)
```

### Scoring Functions

```python
from sklearn.metrics import (
    # Classification
    accuracy_score,
    precision_score, recall_score, f1_score,
    roc_auc_score,          # area under ROC curve
    average_precision_score,# area under PR curve (better for imbalanced)
    classification_report,  # precision/recall/f1 per class, formatted
    confusion_matrix,
    log_loss,               # cross-entropy

    # Regression
    mean_squared_error,    # MSE
    mean_absolute_error,   # MAE
    r2_score,              # R² — proportion of variance explained
    mean_absolute_percentage_error,
)

from sklearn.metrics import roc_curve, precision_recall_curve

# Classification report
print(classification_report(y_test, y_pred, target_names=["neg", "pos"]))

# ROC curve
fpr, tpr, thresholds = roc_curve(y_test, y_prob[:, 1])
auc = roc_auc_score(y_test, y_prob[:, 1])
```

**AUC vs accuracy**: accuracy is misleading on imbalanced datasets (99% class
balance → 99% accuracy by always predicting majority). AUC and average precision
are threshold-independent and handle imbalance better.

### Hyperparameter Search

```python
from sklearn.model_selection import GridSearchCV, RandomizedSearchCV
from scipy.stats import loguniform, randint

# Grid search — exhaustive
param_grid = {
    "classifier__n_estimators": [50, 100, 200],
    "classifier__max_depth": [3, 4, 5],
    "classifier__learning_rate": [0.05, 0.1, 0.2],
}
grid_search = GridSearchCV(
    pipeline, param_grid, cv=5,
    scoring="roc_auc", n_jobs=-1, verbose=1
)
grid_search.fit(X_train, y_train)
print(grid_search.best_params_, grid_search.best_score_)

# Random search — sample from distributions (better for large spaces)
param_dist = {
    "classifier__n_estimators": randint(50, 500),
    "classifier__max_depth": randint(2, 8),
    "classifier__learning_rate": loguniform(0.01, 0.3),
    "classifier__subsample": [0.7, 0.8, 0.9, 1.0],
}
random_search = RandomizedSearchCV(
    pipeline, param_dist, n_iter=50,   # 50 random combinations
    cv=5, scoring="roc_auc", n_jobs=-1, random_state=42
)
random_search.fit(X_train, y_train)
```

**Note prefix `"classifier__"`**: Pipeline parameter names use double-underscore
`stepname__paramname` syntax to refer to parameters of nested estimators.

---

## Algorithm Reference

### Linear Models

```python
from sklearn.linear_model import (
    LinearRegression,   # OLS: minimize ||y - Xβ||²
    Ridge,              # L2 regularization: + α||β||²
    Lasso,              # L1 regularization: + α||β||₁  → sparse coefficients
    ElasticNet,         # L1 + L2 mix
    LogisticRegression, # classification; C = 1/α (inverse regularization)
    SGDClassifier,      # stochastic gradient descent; scales to large data
    SGDRegressor,
)

# Ridge vs Lasso
# Ridge:  shrinks all coefficients toward 0; never exactly 0
# Lasso:  zeros out unimportant features; automatic feature selection
# ElasticNet: when you have groups of correlated features (Lasso picks one arbitrarily)

# When to use linear models
# - Baseline (always start here)
# - n_features >> n_samples (high-dimensional, sparse text)
# - Interpretability required (coefficients are the model)
# - Very fast; scales to billions of samples with SGD
```

### Tree-Based Models

```python
from sklearn.tree import DecisionTreeClassifier, DecisionTreeRegressor
from sklearn.ensemble import (
    RandomForestClassifier,      # bagging of deep trees
    RandomForestRegressor,
    GradientBoostingClassifier,  # boosting — sklearn's implementation
    GradientBoostingRegressor,
    HistGradientBoostingClassifier,  # histogram-based, faster, handles NaN natively
    HistGradientBoostingRegressor,
    AdaBoostClassifier,
    ExtraTreesClassifier,        # extremely randomized trees
    BaggingClassifier,           # generic bagging wrapper
    VotingClassifier,            # majority vote / averaged probability
    StackingClassifier,          # meta-learner on top of base models
)

# External libraries often beat sklearn's gradient boosting:
# XGBoost:    pip install xgboost   — sklearn-compatible API
# LightGBM:   pip install lightgbm  — faster, better on large datasets
# CatBoost:   pip install catboost  — best native categorical support

from xgboost import XGBClassifier
from lightgbm import LGBMClassifier

# Both are drop-in sklearn estimators
xgb = XGBClassifier(n_estimators=200, max_depth=4, learning_rate=0.05,
                     use_label_encoder=False, eval_metric="logloss")

# Feature importance (all tree models)
model.fit(X_train, y_train)
importances = model.feature_importances_   # shape (n_features,)
```

### Support Vector Machines

```python
from sklearn.svm import SVC, SVR, LinearSVC

# SVC with RBF kernel — the default; good for medium datasets
svc = SVC(C=1.0, kernel="rbf", gamma="scale", probability=True)

# LinearSVC — much faster for large datasets, linear kernel only
linear_svc = LinearSVC(C=1.0, max_iter=2000)

# SVMs need StandardScaler — they are NOT scale-invariant
pipeline = Pipeline([("scaler", StandardScaler()), ("svc", SVC())])
```

### KNN

```python
from sklearn.neighbors import KNeighborsClassifier, KNeighborsRegressor

knn = KNeighborsClassifier(n_neighbors=5, metric="euclidean")
# KNN: no training phase; prediction is O(n_samples) — slow at scale
# Needs scaling; all features contribute equally by distance
```

### Naive Bayes

```python
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB

gnb = GaussianNB()          # features ~ Gaussian; fast; good baseline for continuous
mnb = MultinomialNB()       # features are counts; classic for text classification
bnb = BernoulliNB()         # features are binary; text bag-of-words (presence/absence)
```

---

## Unsupervised Learning

### Clustering

```python
from sklearn.cluster import (
    KMeans,            # centroid-based; requires k; assumes spherical clusters
    MiniBatchKMeans,   # faster KMeans for large datasets
    DBSCAN,            # density-based; finds arbitrary shapes; detects outliers
    AgglomerativeClustering,  # hierarchical; no need to specify k upfront
    GaussianMixture,   # probabilistic; soft cluster assignments
)

# KMeans
kmeans = KMeans(n_clusters=5, init="k-means++", n_init=10, random_state=42)
labels = kmeans.fit_predict(X)
centers = kmeans.cluster_centers_

# Elbow method — find optimal k
inertias = [KMeans(n_clusters=k).fit(X).inertia_ for k in range(2, 11)]

# DBSCAN — no k required; label -1 = outlier
dbscan = DBSCAN(eps=0.5, min_samples=5)
labels = dbscan.fit_predict(X)
n_clusters = len(set(labels)) - (1 if -1 in labels else 0)
```

### Dimensionality Reduction

```python
from sklearn.decomposition import PCA, NMF, TruncatedSVD
from sklearn.manifold import TSNE

# PCA — linear, orthogonal projections onto variance-maximizing axes
pca = PCA(n_components=50)
X_reduced = pca.fit_transform(X)           # shape (n, 50)
explained = pca.explained_variance_ratio_  # fraction of variance per component
cumulative = explained.cumsum()

# Choose n_components by explained variance threshold
pca_95 = PCA(n_components=0.95)            # keep components explaining 95% variance
X_95 = pca_95.fit_transform(X)

# t-SNE — nonlinear, for visualization only (2-D or 3-D)
# Do NOT use t-SNE coordinates as features for downstream models
tsne = TSNE(n_components=2, perplexity=30, learning_rate=200, random_state=42)
X_2d = tsne.fit_transform(X)              # for scatter plot only

# TruncatedSVD — like PCA but works on sparse matrices (text/TF-IDF)
svd = TruncatedSVD(n_components=100)
X_lsa = svd.fit_transform(tfidf_matrix)   # latent semantic analysis
```

---

## Feature Engineering and Selection

```python
from sklearn.feature_selection import (
    SelectKBest,          # keep k highest-scoring features
    SelectPercentile,     # keep top % of features
    f_classif,            # ANOVA F-test (classification)
    mutual_info_classif,  # mutual information (handles nonlinear)
    chi2,                 # chi-squared test (count features only)
    RFE,                  # recursive feature elimination
    SelectFromModel,      # use model's feature_importances_
    VarianceThreshold,    # remove near-zero variance features
)

# Filter method — fast, model-agnostic
selector = SelectKBest(score_func=mutual_info_classif, k=20)
X_selected = selector.fit_transform(X, y)

# Wrapper method — slow but accounts for feature interactions
rfe = RFE(estimator=LogisticRegression(), n_features_to_select=20)
X_rfe = rfe.fit_transform(X, y)

# Embedded method — fastest; use model's own importance
from sklearn.ensemble import RandomForestClassifier
sfm = SelectFromModel(RandomForestClassifier(n_estimators=100), threshold="median")
X_sfm = sfm.fit_transform(X, y)
```

---

## Imbalanced Classes

```python
# Class weights — built into most sklearn classifiers
model = LogisticRegression(class_weight="balanced")  # auto-reweight
model = RandomForestClassifier(class_weight={0: 1, 1: 10})  # manual

# Resampling — imbalanced-learn library (sklearn-compatible)
from imblearn.over_sampling import SMOTE, RandomOverSampler
from imblearn.under_sampling import RandomUnderSampler
from imblearn.pipeline import Pipeline as ImbPipeline

smote = SMOTE(random_state=42)
X_resampled, y_resampled = smote.fit_resample(X_train, y_train)

# In pipeline (imblearn Pipeline supports samplers)
pipeline = ImbPipeline([
    ("smote", SMOTE()),
    ("classifier", RandomForestClassifier()),
])
```

---

## Model Interpretability — SHAP

SHAP (SHapley Additive exPlanations) computes each feature's contribution to
a single prediction. It is grounded in Shapley values from cooperative game theory:
the unique fair allocation of a coalition's total payoff to its members.

**Intuition**: for a model prediction f(x), the SHAP value φ_j for feature j is
the average marginal contribution of feature j across all possible orderings of
features. It satisfies three axioms — efficiency (values sum to f(x) − E[f(x)]),
symmetry, and dummy — that uniquely determine the allocation.

```python
import shap
import numpy as np

# TreeExplainer — exact SHAP for any tree-based model (RF, XGBoost, LightGBM)
# O(T · L²) where T = trees, L = leaves per tree
explainer = shap.TreeExplainer(model)  # model = GradientBoosting, RandomForest, XGB

shap_values = explainer.shap_values(X_test)
# shap_values: shape (n_samples, n_features) for regression/binary
# For multiclass: list of arrays, one per class

# For a single prediction: sum of SHAP values = deviation from base rate
print(f"Base value (E[f(x)]): {explainer.expected_value:.4f}")
print(f"Prediction:           {model.predict_proba(X_test[:1])[0,1]:.4f}")
print(f"Sum of SHAP + base:   {shap_values[0].sum() + explainer.expected_value:.4f}")

# LinearExplainer — for linear models (LogisticRegression, Ridge, etc.)
explainer_linear = shap.LinearExplainer(linear_model, X_train)
shap_values_linear = explainer_linear.shap_values(X_test)

# KernelExplainer — model-agnostic (works on any model; slow)
explainer_kernel = shap.KernelExplainer(
    model.predict_proba, shap.sample(X_train, 100)  # background dataset
)
shap_values_kernel = explainer_kernel.shap_values(X_test[:10])
```

### Key Plots

```python
# Waterfall plot — single prediction breakdown (ideal for stakeholder communication)
shap.waterfall_plot(shap.Explanation(
    values=shap_values[0],
    base_values=explainer.expected_value,
    data=X_test.iloc[0],
    feature_names=feature_names,
))
# Shows: base rate → contribution of each feature → final prediction

# Beeswarm plot — global feature importance + direction of effect
shap.summary_plot(shap_values, X_test, feature_names=feature_names)
# Each dot = one sample. Color = feature value (red=high, blue=low).
# X position = SHAP value (contribution direction and magnitude).
# Features sorted by mean(|SHAP|) — global importance.

# Bar plot — mean absolute SHAP (simpler global importance)
shap.summary_plot(shap_values, X_test, plot_type="bar", feature_names=feature_names)

# Dependence plot — how feature j affects the model across its range
shap.dependence_plot("income", shap_values, X_test)
# X = feature value, Y = SHAP value, color = automatically chosen interaction feature

# Force plot — interactive single-prediction visualization
shap.force_plot(explainer.expected_value, shap_values[0], X_test.iloc[0])
```

### SHAP vs. Permutation Importance vs. MDI

```
┌─────────────────────┬──────────────────────────────────────────────────────┐
│  Method             │  What it measures + caveats                         │
├─────────────────────┼──────────────────────────────────────────────────────┤
│  SHAP               │  Per-sample, per-feature contribution. Handles       │
│                     │  correlated features. Exact for trees.              │
│  Permutation        │  Drop in score when feature is shuffled.            │
│  Importance         │  Biased toward correlated features (shuffling one   │
│                     │  of two correlated features still leaks the other). │
│  MDI (tree splits)  │  model.feature_importances_ — fast, biased toward  │
│                     │  high-cardinality features. Never use alone.        │
└─────────────────────┴──────────────────────────────────────────────────────┘
```

**SHAP for stakeholder communication**: the waterfall plot answers "why did this
customer get a high churn score?" — each feature's bar is its contribution in
natural units (probability points). This is the explainability format that
satisfies regulatory requirements (model cards, GDPR right-to-explanation).

---

## Model Persistence

```python
import joblib

# Save
joblib.dump(pipeline, "model_v1.joblib")

# Load
pipeline = joblib.load("model_v1.joblib")
predictions = pipeline.predict(X_new)

# Note: pickle/joblib models are NOT portable across sklearn versions.
# Log sklearn version alongside every saved model.
# For production serving: ONNX or BentoML for version-independent format.
```

---

## The ML Workflow

```
┌─────────────────────────────────────────────────────────────────────┐
│  STANDARD ML WORKFLOW                                               │
│                                                                     │
│  1. Explore (EDA)                                                   │
│     df.describe(), df.corr(), distribution plots                   │
│     Find: missing values, outliers, class imbalance, data types    │
│                                                                     │
│  2. Split FIRST                                                     │
│     train_test_split before any analysis on test set               │
│     Test set = unseen until final evaluation                        │
│                                                                     │
│  3. Build baseline                                                  │
│     DummyClassifier(strategy="most_frequent") — floor score        │
│     LinearRegression / LogisticRegression — interpretable baseline  │
│                                                                     │
│  4. Preprocess in Pipeline                                          │
│     Scaler + encoder + imputer all inside Pipeline                 │
│     Never fit preprocessors outside the cross-validation loop      │
│                                                                     │
│  5. Cross-validate (not test set yet)                               │
│     5-fold StratifiedKFold for classification                      │
│     Score: validation folds only                                   │
│                                                                     │
│  6. Tune hyperparameters                                            │
│     RandomizedSearchCV first (find the ballpark)                   │
│     GridSearchCV to refine around best region                      │
│                                                                     │
│  7. Evaluate on test set — ONCE                                     │
│     Final evaluation on held-out test set                          │
│     No tuning after seeing test results                             │
│                                                                     │
│  8. Analyze errors                                                  │
│     confusion_matrix, classification_report                        │
│     What types of errors? Is the cost asymmetric?                  │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Algorithm Selection Guide

```
┌──────────────────────────────────────────────────────────────────────┐
│  SITUATION                      │  START WITH                       │
├─────────────────────────────────┼───────────────────────────────────┤
│  Any problem                    │  LinearRegression / LogisticReg   │
│                                 │  (always build a baseline)        │
│  Tabular, medium size           │  HistGradientBoosting / XGBoost  │
│  Tabular, need interpretability │  LogisticRegression + SHAP        │
│  High-dimensional text/sparse   │  LogisticRegression (L1/L2) or   │
│                                 │  LinearSVC                        │
│  Complex boundaries, medium n   │  SVC (RBF) or RandomForest        │
│  Very large n (>1M)             │  SGDClassifier / LightGBM        │
│  Many irrelevant features       │  Lasso or tree-based (auto select)│
│  Strongly correlated features   │  Ridge or ElasticNet              │
│  Clustering (know k)            │  KMeans                           │
│  Clustering (unknown k/noise)   │  DBSCAN                           │
│  Visualization only             │  t-SNE or UMAP                    │
│  Dimensionality reduction       │  PCA (linear) or UMAP (nonlinear) │
├─────────────────────────────────┼───────────────────────────────────┤
│  COMMON GOTCHAS                 │                                   │
│  Imbalanced classes             │  class_weight="balanced" first    │
│  Features not scaled for SVM    │  StandardScaler in Pipeline       │
│  Data leakage                   │  Scaler inside Pipeline, not before│
│  Overfitting                    │  Reduce depth / increase alpha    │
│  Underfitting                   │  More features / reduce alpha     │
└──────────────────────────────────┴───────────────────────────────────┘
```

---

## Common Confusion Points

**`fit_transform` on test data is data leakage**: Fitting a scaler on test data
makes the scaler parameters (mean, std) derived from test data. The model then
has indirect knowledge of test statistics. Always `fit` on training data only,
then `transform` test data. Pipeline enforces this automatically.

**Cross-validation with pipeline vs. without**: If you scale before splitting
into folds (`StandardScaler().fit_transform(X)` then `cross_val_score`), each
fold's test data has seen the scaler fitted on the full dataset including that
fold. Data leakage. Pipeline re-fits the scaler on training folds only.

**Probability calibration**: `predict_proba` scores from many classifiers (SVM,
GradientBoosting) are not calibrated probabilities. A score of 0.8 does not mean
"80% likely to be class 1." Use `CalibratedClassifierCV` if you need reliable
probability estimates.

**`n_jobs=-1`**: Parallelizes over all CPU cores. Standard for GridSearchCV,
RandomizedSearchCV, and most ensemble methods. Always use it.

**Metric choice for imbalanced data**: Accuracy hides imbalance problems.
Use `roc_auc_score` (threshold-independent), `average_precision_score`
(area under PR curve, better for severe imbalance), or `f1_score` with
`average="macro"` for per-class balance.

**XGBoost / LightGBM are not sklearn built-ins**: They provide sklearn-compatible
APIs but are separate packages. LightGBM generally wins on speed for large datasets;
XGBoost has more ecosystem tooling; sklearn's HistGradientBoosting is a reasonable
built-in alternative.
