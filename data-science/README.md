# Data Science Track

A complete technical reference for the Python data science and machine learning stack.
Peer-level depth throughout — assumes graduate statistics, linear algebra, and software engineering background.

---

## Module Index

| # | File | What it covers |
|---|------|----------------|
| 01 | [01-NUMPY.md](01-NUMPY.md) | ndarray memory model, strides, views vs copies, broadcasting, ufuncs, linalg, FFT, performance patterns |
| 02 | [02-PANDAS.md](02-PANDAS.md) | DataFrame internals, .loc/.iloc semantics, GroupBy/merge/reshape, time series, Polars comparison |
| 03 | [03-SKLEARN.md](03-SKLEARN.md) | Estimator API, Pipeline, preprocessing, model selection, CV, hyperparameter search, SHAP interpretability |
| 04 | [04-PYTORCH.md](04-PYTORCH.md) | Tensors, autograd DAG, nn.Module, training loop, DataLoader, AMP, DDP, Lightning |
| 05 | [05-MLOPS.md](05-MLOPS.md) | MLflow, W&B, model registry lifecycle, DVC, Great Expectations, serving patterns, drift detection |
| 06 | [06-AZURE-ML.md](06-AZURE-ML.md) | AzureML workspace, SDK v2, training jobs, pipelines, endpoints, AutoML, vs ADF pipelines |
| 07 | [07-STATISTICAL-LEARNING.md](07-STATISTICAL-LEARNING.md) | ERM, bias-variance, VC dimension, PAC learning, Rademacher complexity, double descent, NFL |
| 08 | [08-PROBABILISTIC-ML.md](08-PROBABILISTIC-ML.md) | Bayesian inference, conjugate priors, graphical models, MCMC/HMC, variational inference, VAE, flows, GPs |
| 09 | [09-INFORMATION-THEORY.md](09-INFORMATION-THEORY.md) | Shannon entropy, KL divergence, mutual information, Fisher information, MDL, ML big map |
| 10 | [10-OPTIMIZATION-THEORY.md](10-OPTIMIZATION-THEORY.md) | Convex analysis, GD convergence rates, SGD, momentum, Adam/AdamW, second-order methods, loss landscape |
| 11 | [11-DEEP-LEARNING-THEORY.md](11-DEEP-LEARNING-THEORY.md) | UAT, depth/expressivity, attention math, BatchNorm/LayerNorm, NTK, scaling laws, emergent abilities, diffusion models |
| 12 | [12-REINFORCEMENT-LEARNING.md](12-REINFORCEMENT-LEARNING.md) | MDPs, Bellman equations, Q-learning/DQN, policy gradients, PPO, SAC, RLHF/DPO |
| 13 | [13-CAUSAL-INFERENCE.md](13-CAUSAL-INFERENCE.md) | Potential outcomes, DAGs, do-calculus, RCT, PSM/DiD/IV/RD, DML, causal forests, sensitivity analysis |
| 14 | [14-TIME-SERIES.md](14-TIME-SERIES.md) | Stationarity, ARIMA/SARIMA, VAR/VECM, GARCH, Kalman filter, spectral analysis, Python tooling stack |
| 15 | [15-COMPUTER-VISION.md](15-COMPUTER-VISION.md) | CNN theory, ResNet/ViT architectures, detection (YOLO/DETR), segmentation, self-supervised (MAE/CLIP) |
| 16 | [16-NLP-FOUNDATIONS.md](16-NLP-FOUNDATIONS.md) | N-grams, Word2Vec/GloVe, LSTM, seq2seq attention, tokenization (BPE/WordPiece), Transformer, BERT/GPT, scaling laws |
| 17 | [17-GRAPH-ML.md](17-GRAPH-ML.md) | Graph Laplacian, spectral GNNs, GCN/GAT/GraphSAGE, MPNN framework, WL expressiveness, graph construction from tabular data |

---

## Reading Progression

### Foundation (start here)
```
01-NUMPY  →  02-PANDAS  →  03-SKLEARN  →  04-PYTORCH
```
NumPy is the memory substrate. Pandas is labeled NumPy with a query engine.
scikit-learn is the Estimator API over NumPy arrays. PyTorch adds autograd and GPU execution.
These four form the complete practical stack — everything else builds on them.

### Applied ML Engineering
```
03-SKLEARN  →  05-MLOPS  →  06-AZURE-ML
```
From model training to experiment tracking, registry, serving, and monitoring.
06 is Azure-specific supplement; 05 covers the universal open-source tooling.

### Theory Track (can run in parallel with applied)
```
07-STATISTICAL-LEARNING  →  08-PROBABILISTIC-ML  →  09-INFORMATION-THEORY
         ↓
10-OPTIMIZATION-THEORY  →  11-DEEP-LEARNING-THEORY
```
07 is the generalization theory foundation. 08 adds the Bayesian lens. 09 grounds both in
information theory. 10 is the optimization mechanics behind training. 11 synthesizes
representation, expressivity, and scaling into a unified theory of deep learning.

### Specialization Tracks
```
12-REINFORCEMENT-LEARNING     ← builds on 10+11; prerequisite for RLHF
13-CAUSAL-INFERENCE           ← independent; builds on stats background
14-TIME-SERIES                ← partially independent; connects to 08 (SSMs)
15-COMPUTER-VISION            ← builds on 04+11
16-NLP-FOUNDATIONS            ← builds on 04+11; prerequisite for LLM work
17-GRAPH-ML                   ← builds on 09+11; can follow 07
```

### Recommended First Pass (VP/technical leader reading order)
1. **01–04** — Get the stack in your hands (foundation)
2. **07** — Understand why generalization works at all (theory anchor)
3. **10** — Understand how models are actually trained (optimization)
4. **11** — Understand why deep learning scales (synthesis)
5. Then pick specializations based on immediate project relevance
