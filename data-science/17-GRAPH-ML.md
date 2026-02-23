# Graph Machine Learning
## Spectral Theory, Message Passing, GNNs, and Applications

```
GRAPH ML LANDSCAPE

  Classical graph theory          Spectral GNNs              Spatial GNNs
  ─────────────────────────       ────────────────────       ─────────────────────
  Laplacian, eigenvectors         ChebNet (2016)             GraphSAGE (2017)
  Graph Fourier transform         GCN (Kipf & Welling, 2017) GAT (2018)
  Spectral clustering             Signal processing view     Message passing view
  Random walks                    Convolve in spectral dom   Aggregate neighborhoods

  Modern GNNs                    Applications
  ─────────────────────────       ────────────────────────────────────────────
  MPNN framework (Gilmer 2017)   Molecules, proteins (chemistry)
  Graph Transformer              Social networks, knowledge graphs
  Graph diffusion, scattering    Recommendation systems
  Oversmoothing problem          Traffic, ETA prediction
```

---

## 1. Graph Fundamentals

**Graph**: G = (V, E) with node set V, edge set E ⊆ V×V.
- **Undirected**: (u,v) ∈ E ↔ (v,u) ∈ E
- **Directed**: (u,v) ≠ (v,u) in general
- **Weighted**: w: E → ℝ₊
- **Attributed**: node features X ∈ ℝ^{|V|×d}, edge features

**Adjacency matrix** A ∈ ℝ^{n×n}: Aᵢⱼ = wᵢⱼ if (i,j) ∈ E, else 0.

**Degree matrix** D: diagonal, Dᵢᵢ = Σⱼ Aᵢⱼ (sum of edge weights for node i).

**Graph Laplacian**:
```
  Combinatorial: L = D - A
  Normalized:    L_sym = D^{-1/2} L D^{-1/2} = I - D^{-1/2} A D^{-1/2}
  Random walk:   L_rw = D^{-1} L = I - D^{-1} A

  L_sym has eigenvalues 0 = λ₁ ≤ λ₂ ≤ ... ≤ λₙ ≤ 2
  Eigenvalue 0: trivial, eigenvector = constant function
  λ₂ (Fiedler value): connectivity measure (λ₂=0 iff disconnected)
  Eigenvectors: smooth functions on the graph (low eigenvalue = smooth)
```

**Laplacian as quadratic form**:
```
  For signal f ∈ ℝⁿ (one value per node):

  fᵀLf = Σ_{(i,j)∈E} wᵢⱼ(fᵢ - fⱼ)²   (sum of squared differences across edges)

  ← Measures the "roughness" of f on the graph
  ← Smooth signal (neighbors have similar values): small fᵀLf
  ← This is the graph analog of ∫‖∇f‖² dx
```

---

## 2. Spectral Graph Theory

**Eigendecomposition**: L_sym = U Λ Uᵀ where U = [u₁,...,uₙ] are eigenvectors (orthonormal), Λ = diag(λ₁,...,λₙ).

**Graph Fourier Transform** (analogous to classical Fourier):
```
  Classical:      F(ω) = ∫ f(t) e^{-iωt} dt    (decompose by oscillation frequency)
  Graph analog:   f̂(k) = uₖᵀ f = Σᵢ uₖᵢ fᵢ   (project onto k-th eigenvector)

  Inverse: f = Σₖ f̂(k) uₖ = U f̂

  Low-frequency eigenvectors: smooth variations across the graph
  High-frequency eigenvectors: rapid changes between neighbors
```

**Graph convolution** (in spectral domain):
```
  Convolution theorem: convolution in time ↔ multiplication in frequency

  Graph analog: (f * g)_G = U (Û ⊙ ĝ) = U diag(ĝ(λ₁),...,ĝ(λₙ)) Uᵀ f

  Filter: g_θ = diag(θ₁,...,θₙ)  (n learnable parameters, one per eigenvalue)

  Problems:
  1. O(n) parameters (one per frequency)
  2. Not localized: filter in spectral domain is global in spatial domain
  3. Eigenvectors are not transferable across graphs
```

---

## 3. Chebyshev Networks (ChebNet)

**Approximate spectral filters with polynomials** (Defferrard et al. 2016):

```
  Chebyshev polynomial approximation:
    g_θ(λ) ≈ Σ_{k=0}^K θₖ Tₖ(λ̃)    where λ̃ = 2λ/λmax - 1 ∈ [-1,1]

  Tₖ(x) = 2x Tₖ₋₁(x) - Tₖ₋₂(x),  T₀=1, T₁=x

  In matrix form:
    g_θ(L) * f = Σ_{k=0}^K θₖ Tₖ(L̃) f

  Key: Tₖ(L̃) can be computed by recursion without eigendecomposition:
    f̄ₖ = 2L̃ f̄ₖ₋₁ - f̄ₖ₋₂,  f̄₀ = f, f̄₁ = L̃f

  Benefits:
    O(K|E|) computation (sparse L, K hops)
    K-localized: depends only on K-hop neighborhood
    Only K+1 parameters (not n)
    Transferable across graphs
```

---

## 4. Graph Convolutional Network (GCN)

**Kipf & Welling (2017)**: first-order approximation of ChebNet:

```
  Setting K=1 and λmax≈2:
    g_θ * f ≈ θ₀ f + θ₁ (L̃) f = θ₀ f - θ₁ D^{-1/2} A D^{-1/2} f

  Constraint θ = θ₀ = -θ₁ (reduce to one parameter):
    g_θ * f = θ (I + D^{-1/2} A D^{-1/2}) f

  Renormalization: Ã = A + I (add self-loops), D̃ᵢᵢ = Σⱼ Ãᵢⱼ

  GCN layer:
    H^{(l+1)} = σ( D̃^{-1/2} Ã D̃^{-1/2} H^{(l)} W^{(l)} )
                ↑                               ↑         ↑
           normalized adjacency          features    weights

  For node i: h^{(l+1)}_i = σ( W^{(l)} Σ_{j∈N(i)∪{i}} h^{(l)}_j / √(d̃ᵢd̃ⱼ) )
              ← normalized mean aggregation over neighbors + self
```

**GCN as low-pass filter**:
```
  D̃^{-1/2} Ã D̃^{-1/2} = I - L̃_sym   ← smoothing operator
  Applying k times → progressively smoother features
  This is spectral graph convolution with a specific filter (1 - λ̃)
```

**Oversmoothing**: with too many GCN layers, all node representations converge to the same value:
```
  L GCN layers → features are (D̃^{-1/2}Ã D̃^{-1/2})^L x → principal eigenvector of Ã

  Practical: 2-3 GCN layers typically optimal. Deeper = worse.
  Solutions: skip connections (residual), JK-Net (jumping knowledge), PairNorm, DropEdge
```

---

## 5. Message Passing Neural Networks (MPNN)

Spatial / message passing view — unifies GCN, GAT, GraphSAGE, etc.

**MPNN framework** (Gilmer et al. 2017):
```
  For each node v, at each layer:

  1. MESSAGE:   mᵛₜ = Σ_{u∈N(v)} M_t(hᵛₜ, hᵘₜ, eᵛᵘ)

  2. AGGREGATE: aᵛₜ = AGG({mᵛₜ for u ∈ N(v)})

  3. UPDATE:    hᵛₜ₊₁ = U_t(hᵛₜ, aᵛₜ)

  M: message function (can use edge features eᵛᵘ)
  AGG: aggregation — must be permutation invariant (sum, mean, max)
  U: update function (often GRU or MLP)

  4. READOUT (for graph-level tasks):
     ŷ = R({hᵛT | v ∈ G})   ← permutation invariant aggregation over all nodes
```

**Instantiations of MPNN**:
```
  GCN:      M = Wh_u / √(d_v d_u),  AGG = sum,  U = σ(Σ msg)
  GraphSAGE: M = h_u,  AGG = {mean, max, LSTM},  U = σ(W · concat(h_v, agg))
  GAT:      M = α_vu Wh_u,  α_vu = attention weight, AGG = sum, U = σ(Σ)
  MPNN(QM9): M = MLP(h_u, h_v, e_uv),  AGG = sum, U = GRU(h_v, Σ msg)
```

---

## 6. Graph Attention Networks (GAT)

**Problem with GCN**: symmetric normalization `1/√(d̃ᵢd̃ⱼ)` weights neighbors by degree, not relevance.

**GAT** (Veličković et al. 2018): learn attention weights:
```
  Unnormalized attention (additive):
    eᵢⱼ = LeakyReLU( aᵀ [W hᵢ ‖ W hⱼ] )    ← shared attention vector a, weight matrix W

  Normalized:
    αᵢⱼ = exp(eᵢⱼ) / Σ_{k∈N(i)} exp(eᵢₖ)    ← softmax over neighbors of i

  Aggregation:
    h'ᵢ = σ( Σ_{j∈N(i)} αᵢⱼ W hⱼ )

  Multi-head: K heads, concatenate (intermediate layers) or average (final layer):
    h'ᵢ = ‖_{k=1}^K σ( Σ_{j∈N(i)} αᵏᵢⱼ Wᵏ hⱼ )
```

**GATv2** (Brody et al. 2022): original GAT has "static attention" (eᵢⱼ separable in i,j). GATv2 fixes:
```
  eᵢⱼ = aᵀ LeakyReLU( W [hᵢ ‖ hⱼ] )    ← attention is truly dynamic (joint function)
```

---

## 7. GraphSAGE — Inductive Learning

**Problem with transductive GNNs** (GCN, GAT): require the full graph during training. Can't generalize to new nodes not seen in training.

**GraphSAGE** (Hamilton et al. 2017) — inductive:
```
  SAMPLE: for each node, sample fixed-size neighborhood (not all neighbors)
  AGGREGATE: aggregate sampled neighbors' features
  COMBINE: concatenate node's own features with aggregated representation

  h^k_v = UPDATE^k( h^{k-1}_v, AGG^k({h^{k-1}_u | u ∈ N_k(v)}) )

  Three aggregators:
    Mean:  h_N(v) = mean({h^{k-1}_u | u ∈ N(v)})     ← cheap, isotropic
    LSTM:  apply LSTM on shuffled neighbors            ← more expressive, order matters
    Max:   h_N(v) = max({σ(W h^{k-1}_u) | u ∈ N(v)}) ← selects most salient
```

**Inductive**: at inference, run the sampling + aggregation procedure on new nodes using learned weights W. The learned aggregation function generalizes.

**Minibatch training**: sample computation graph (2-hop neighborhood), form a mini-batch of nodes, compute features bottom-up.

---

## 8. Expressive Power of GNNs

**Key question**: what graph structures can GNNs distinguish?

**Weisfeiler-Leman (1-WL) graph isomorphism test**:
```
  Iterative: refine node colors by hashing (node color, sorted multiset of neighbor colors)
  Until stable. Two graphs are isomorphic if they produce the same coloring.

  Not complete: 1-WL can't distinguish all non-isomorphic graphs.
  Fails on regular graphs (all nodes same degree), cycles of same length.
```

**GNN expressiveness theorem** (Xu et al. 2019 — "How Powerful are GNNs?"):
```
  Any GNN with mean/max aggregation ≤ 1-WL in power.
  GIN (Graph Isomorphism Network) achieves 1-WL:

  h^k_v = MLP^k( (1 + ε^k) h^{k-1}_v + Σ_{u∈N(v)} h^{k-1}_u )
                  ↑
          learned or fixed; injective aggregation

  Key: SUM aggregation is injective (unlike MEAN which conflates cardinality)
  GIN with SUM is as powerful as 1-WL.
```

**Beyond 1-WL**: k-WL hierarchy, higher-order GNNs, random features, graph transformers.

---

## 9. Graph Transformers

**Problem with standard attention**: O(n²) — impractical for large graphs.

**Graph Transformer** (Dwivedi & Bresson 2021): transformer + graph structure as attention bias:
```
  Attention with graph structure:
    Aᵢⱼ = softmax( (QᵢKⱼᵀ/√d) + bias(eᵢⱼ) )    ← edge features as attention bias
    If (i,j) ∉ E: bias = -∞ (or learned absence embedding)
```

**Graphormer** (Ying et al. 2021 — used in AlphaFold-related work):
```
  Spatial encoding: bias(i,j) = learned function of shortest path distance
  Edge encoding: attention bias from edge features along the shortest path
  Centrality encoding: degree-based node bias added to input features

  Performance: SOTA on molecular property prediction benchmarks
```

---

## 10. Applications

### Molecular Property Prediction
```
  Atoms = nodes, bonds = edges
  Node features: atom type, charge, hybridization
  Edge features: bond type, bond order

  Task: predict drug properties (toxicity, solubility, binding affinity)
  MPNN → QM9 quantum chemistry, ZINC drug discovery
  GNN trained on molecules generalizes across chemical space

  AlphaFold 2 (protein structure): not a GNN per se, but uses pair representation
  and triangle updates that are structurally similar to message passing
```

### Social Network Analysis
```
  Users = nodes, friendships = edges
  Node features: profile data
  Tasks: link prediction, community detection, influence estimation

  Link prediction: P(edge u,v) = σ(hᵤᵀ hᵥ)  or  MLP(concat(hᵤ, hᵥ))
  Community detection: graph clustering on learned representations
```

### Knowledge Graphs
```
  Entities = nodes, relations = edge types (heterogeneous graph)
  Triples: (head entity, relation, tail entity)

  Tasks: knowledge graph completion (link prediction with relation types)
  R-GCN (Schlichtkrull et al.): separate W per relation type
  RotatE, DistMult, ComplEx: shallow embedding methods (often competitive with GNNs)
```

### Recommender Systems
```
  Users and items = bipartite graph nodes
  Interactions = edges (ratings, clicks)

  PinSage (Pinterest): GraphSAGE on Pinterest graph, importance-based neighborhood sampling
  LightGCN: simplified GCN (no feature transformation, only aggregation) for collaborative filtering
```

---

## 11. Decision Cheat Sheet

| Scenario | Method | Why |
|----------|--------|-----|
| Node classification, transductive | GCN, GAT | Simple, effective |
| Node classification, inductive | GraphSAGE, GIN | Generalizes to new nodes |
| Graph classification | GIN + readout | Maximally expressive (1-WL) |
| Molecular property prediction | MPNN, Graphormer | Edge features, 3D geometry |
| Heterogeneous graph | R-GCN, HAN, HGT | Different relation types |
| Link prediction | GraphSAGE + dot product | Standard approach |
| Large-scale (millions of nodes) | GraphSAGE (minibatch) | Sampling-based training |
| Long-range dependencies | Graph Transformer | Direct attention, no stacking |

---

## 12. Common Confusion Points

1. **"GCN is a graph generalization of CNN"** — In the spectral sense, yes: both convolve signals via learned filters. But the analogy is imperfect. CNNs have spatial locality and translation equivariance; GCN has permutation equivariance (nodes can be in any order) but not translation equivariance.

2. **"More GNN layers = better performance"** — The opposite, typically. Oversmoothing: L layers → all nodes converge to same representation. 2-3 layers is usually optimal. Receptive field grows exponentially with layers (already seeing all 6-hop neighbors with 6 layers on dense graphs).

3. **"GAT learns which neighbors matter"** — GAT learns attention weights over neighbors. But the key finding of GATv2 is that the original GAT has "static attention" — the ranking of neighbors doesn't depend on the query node's features. GATv2 fixes this with truly dynamic attention.

4. **"GNNs can distinguish all graphs"** — Most GNNs are upper-bounded by 1-WL in expressive power. 1-WL fails on regular graphs, Rook's graphs, etc. GIN achieves 1-WL but not more. Real molecules rarely require 2-WL, so this is mostly a theoretical concern.

5. **"Sum aggregation is better than mean"** — Sum is more expressive (GIN proof). Mean loses cardinality (can't distinguish between one feature-rich neighbor and many identical ones). But for large, dense graphs, sum can dominate with high-degree nodes; normalization (mean or degree-normalized) can help stability.

6. **"Spectral GNNs and spatial GNNs are different models"** — They're different views of the same thing. GCN can be derived from the spectral perspective (ChebNet → K=1) or the spatial perspective (average normalized neighbors). The spectral view provides theoretical grounding; the spatial view provides the efficient implementation.

7. **"Graph neural networks work on any graph"** — GNNs work well when the graph structure is informative for the task. If edges are random (don't encode meaningful relationships), GNNs perform no better than ignoring the graph. The inductive bias of GNNs (similar nodes have similar neighbors) must match the data.
