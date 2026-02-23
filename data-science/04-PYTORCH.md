# 04 — PyTorch

> PyTorch is a differentiable programming framework.
> The neural network is a side effect of having autograd.

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PYTORCH STACK                                       │
│                                                                             │
│  Your model code (Python)                                                   │
│       │                                                                     │
│  ┌────▼────────────────────────────────────────────────────────────────┐   │
│  │  torch.nn          — layers, loss functions, containers            │   │
│  │  torch.optim       — SGD, Adam, schedulers                         │   │
│  │  torch.utils.data  — Dataset, DataLoader, samplers                 │   │
│  └────┬────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│  ┌────▼────────────────────────────────────────────────────────────────┐   │
│  │  torch.autograd    — dynamic computation graph, backward()         │   │
│  └────┬────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│  ┌────▼────────────────────────────────────────────────────────────────┐   │
│  │  torch.Tensor      — strided array (same layout as NumPy ndarray)  │   │
│  └────┬────────────────────────────────────────────────────────────────┘   │
│       │                                                                     │
│  ┌────▼────────────────────────────────────────────────────────────────┐   │
│  │  C++ / CUDA kernel dispatch                                        │   │
│  │  CPU (ATen) or GPU (cuBLAS / cuDNN / custom CUDA)                 │   │
│  └────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## Tensors

PyTorch tensors are NumPy ndarrays with two additions: they can live on GPU,
and they can carry a gradient. The memory model is identical to NumPy.

```python
import torch
import numpy as np

# Creation
t = torch.tensor([1.0, 2.0, 3.0])              # from Python list
t = torch.from_numpy(np.array([1.0, 2.0, 3.0]))# zero-copy from NumPy (shared memory)
t = torch.zeros(3, 4)                           # 3×4 of 0.0 float32
t = torch.ones(3, 4, dtype=torch.float64)
t = torch.rand(3, 4)                            # uniform [0, 1)
t = torch.randn(3, 4)                           # N(0, 1)
t = torch.arange(0, 10, 2)                      # [0, 2, 4, 6, 8]
t = torch.linspace(0, 1, 5)                     # [0.0, 0.25, 0.5, 0.75, 1.0]
t = torch.eye(4)                                # 4×4 identity

# Properties
t.shape    # torch.Size([3, 4])  — same as t.size()
t.dtype    # torch.float32
t.device   # device(type='cpu')
t.requires_grad  # False by default

# NumPy interop
arr = t.numpy()         # share memory if CPU tensor, no copy
t2 = torch.from_numpy(arr)  # share memory

# Device transfer
t_gpu = t.to("cuda")   # or t.cuda()
t_cpu = t_gpu.cpu()
t_gpu = t.to("cuda:0") # specific GPU
```

### Default dtype

PyTorch defaults to `float32` (not `float64` like NumPy). This matters when
mixing PyTorch and NumPy — `from_numpy` preserves the NumPy dtype.

```python
torch.set_default_dtype(torch.float64)  # change globally (rarely done)

# Per-tensor
x = torch.tensor([1.0], dtype=torch.float64)
```

---

## Autograd — The Core

Autograd builds a dynamic computation graph as you perform operations on tensors
with `requires_grad=True`. Calling `.backward()` traverses the graph in reverse
and accumulates gradients in `.grad`.

```python
# Scalar function: f(x) = x² + 2x + 1
x = torch.tensor(3.0, requires_grad=True)
f = x**2 + 2*x + 1

f.backward()   # df/dx = 2x + 2 = 8.0
print(x.grad)  # tensor(8.)

# Vector function: accumulate over batch
x = torch.tensor([1.0, 2.0, 3.0], requires_grad=True)
loss = (x**2).sum()   # scalar loss (required for .backward())
loss.backward()
print(x.grad)         # [2., 4., 6.]  — dL/dx = 2x element-wise

# Gradient accumulation — gradients ADD on each backward()
x.grad.zero_()        # zero before next backward — CRITICAL
```

### The Computation Graph

```
x ──► x² ──► + ──► sum ──► loss
             ↑
          2*x
```

Each operation creates a node. `.backward()` calls each node's backward function
in reverse topological order (chain rule). The graph is rebuilt fresh each forward
pass — "define by run" (vs TensorFlow 1's static graph).

```python
# Context manager for gradient tracking
with torch.no_grad():
    y = model(x)   # no graph built — faster, less memory
    # used for inference

# Detach from graph
z = x.detach()     # new tensor sharing storage, no grad history
```

---

## `nn.Module` — Building Blocks

Every layer, loss function, and model inherits from `nn.Module`:

```python
import torch.nn as nn

# Built-in layers
nn.Linear(in_features, out_features, bias=True)
nn.Conv2d(in_channels, out_channels, kernel_size, stride=1, padding=0)
nn.ConvTranspose2d(...)           # upsampling convolution
nn.BatchNorm1d(num_features)      # normalize over batch dimension
nn.BatchNorm2d(num_channels)
nn.LayerNorm(normalized_shape)    # normalize over feature dimension (Transformers)
nn.Dropout(p=0.5)
nn.Embedding(num_embeddings, embedding_dim)
nn.MultiheadAttention(embed_dim, num_heads)
nn.LSTM(input_size, hidden_size, num_layers, batch_first=True)
nn.Transformer(d_model, nhead, ...)

# Activation functions
nn.ReLU(), nn.GELU(), nn.SiLU()  # SiLU = Swish = x * sigmoid(x)
nn.Sigmoid(), nn.Tanh(), nn.Softmax(dim=-1)

# Containers
nn.Sequential(layer1, layer2, ...)     # linear chain
nn.ModuleList([layer1, layer2, ...])   # indexable, registered
nn.ModuleDict({"fc": nn.Linear(...)})  # named, registered
```

### Defining a Model

```python
class MLP(nn.Module):
    def __init__(self, input_dim: int, hidden_dim: int, output_dim: int):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(input_dim, hidden_dim),
            nn.BatchNorm1d(hidden_dim),
            nn.GELU(),
            nn.Dropout(0.2),
            nn.Linear(hidden_dim, hidden_dim),
            nn.GELU(),
            nn.Linear(hidden_dim, output_dim),
        )

    def forward(self, x: torch.Tensor) -> torch.Tensor:
        return self.net(x)

model = MLP(input_dim=128, hidden_dim=256, output_dim=10)

# Inspect
print(model)                             # layer tree
print(sum(p.numel() for p in model.parameters()))  # parameter count
print(sum(p.numel() for p in model.parameters() if p.requires_grad))

# Module methods
model.train()    # enable Dropout, BatchNorm uses batch stats
model.eval()     # disable Dropout, BatchNorm uses running stats
model.to("cuda") # move all parameters to GPU
```

**Every `nn.Module` must define `forward()`**. The `__call__` method invokes
`forward()` and runs registered hooks — never call `forward()` directly.

---

## Loss Functions

```python
# Classification
nn.CrossEntropyLoss()     # log-softmax + NLL; input: logits (NOT probabilities)
nn.BCEWithLogitsLoss()    # binary CE with logits (numerically stable)
nn.BCELoss()              # binary CE; input: probabilities (use logits version instead)
nn.NLLLoss()              # negative log-likelihood; input: log-probabilities

# Regression
nn.MSELoss()              # mean squared error
nn.L1Loss()               # mean absolute error
nn.SmoothL1Loss()         # Huber loss — MAE outside δ, MSE inside (robust)
nn.HuberLoss(delta=1.0)

# Contrastive / embedding
nn.TripletMarginLoss()
nn.CosineEmbeddingLoss()

# With class weights (for imbalance)
weights = torch.tensor([1.0, 10.0])  # class 1 is rare
criterion = nn.CrossEntropyLoss(weight=weights)
```

`CrossEntropyLoss` expects **raw logits**, not softmax probabilities. Passing
softmax outputs to it is a common bug — the function applies log-softmax internally.

---

## Optimizers

```python
import torch.optim as optim

# Create (pass model parameters)
optimizer = optim.Adam(model.parameters(), lr=1e-3, weight_decay=1e-4)
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9, weight_decay=1e-4)
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)  # preferred over Adam

# AdamW vs Adam:
# Adam applies weight decay to the adapted gradient (incorrect mathematically)
# AdamW applies weight decay directly to weights (correct L2 regularization)
# AdamW is now the default for most modern models

# Per-layer learning rates
optimizer = optim.Adam([
    {"params": model.encoder.parameters(), "lr": 1e-4},  # lower for pretrained
    {"params": model.head.parameters(),    "lr": 1e-3},  # higher for new layers
])
```

### Learning Rate Schedulers

```python
# Cosine annealing — the standard for modern training
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100, eta_min=1e-6)

# Warmup + cosine (common pattern for large models)
scheduler = optim.lr_scheduler.OneCycleLR(
    optimizer, max_lr=1e-3,
    steps_per_epoch=len(train_loader), epochs=50,
    pct_start=0.1,  # 10% of training is warmup
)

# Step decay
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)

# Reduce on plateau
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, patience=5, factor=0.5)

# Call after each batch (OneCycleLR) or each epoch (most others)
scheduler.step()
```

---

## Data Loading

```python
from torch.utils.data import Dataset, DataLoader, random_split
import torchvision.transforms as T

# Custom Dataset
class TabularDataset(Dataset):
    def __init__(self, X: np.ndarray, y: np.ndarray):
        self.X = torch.from_numpy(X).float()
        self.y = torch.from_numpy(y).long()

    def __len__(self) -> int:
        return len(self.X)

    def __getitem__(self, idx: int):
        return self.X[idx], self.y[idx]

# DataLoader — batching, shuffling, parallel loading
dataset = TabularDataset(X_train, y_train)
train_loader = DataLoader(
    dataset,
    batch_size=64,
    shuffle=True,
    num_workers=4,       # parallel data loading processes
    pin_memory=True,     # faster CPU→GPU transfer
    prefetch_factor=2,   # batches to prefetch per worker
)

# Image dataset with transforms
train_dataset = torchvision.datasets.ImageFolder(
    root="data/train",
    transform=T.Compose([
        T.RandomHorizontalFlip(),
        T.RandomCrop(32, padding=4),
        T.ToTensor(),                     # HWC uint8 → CHW float32 [0,1]
        T.Normalize(mean=[0.5], std=[0.5]),
    ])
)
```

---

## The Training Loop

```python
def train_epoch(model, loader, criterion, optimizer, device, scaler=None):
    model.train()
    total_loss = 0.0

    for batch_idx, (X, y) in enumerate(loader):
        X, y = X.to(device), y.to(device)

        optimizer.zero_grad()     # 1. clear accumulated gradients

        if scaler:                # mixed precision path
            with torch.autocast(device_type="cuda", dtype=torch.float16):
                logits = model(X)
                loss = criterion(logits, y)
            scaler.scale(loss).backward()  # 2. backward (scaled)
            scaler.unscale_(optimizer)
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            scaler.step(optimizer)         # 3. update weights
            scaler.update()
        else:
            logits = model(X)
            loss = criterion(logits, y)
            loss.backward()                # 2. backward
            torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)
            optimizer.step()               # 3. update weights

        total_loss += loss.item()

    return total_loss / len(loader)


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()                  # disable Dropout, use running BatchNorm stats
    total_loss, correct = 0.0, 0

    for X, y in loader:
        X, y = X.to(device), y.to(device)
        logits = model(X)
        loss = criterion(logits, y)
        total_loss += loss.item()
        correct += (logits.argmax(dim=1) == y).sum().item()

    return total_loss / len(loader), correct / len(loader.dataset)


# Full training script
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MLP(128, 256, 10).to(device)
criterion = nn.CrossEntropyLoss()
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=0.01)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)
scaler = torch.cuda.amp.GradScaler()  # mixed precision

best_val_loss = float("inf")
for epoch in range(50):
    train_loss = train_epoch(model, train_loader, criterion, optimizer, device, scaler)
    val_loss, val_acc = evaluate(model, val_loader, criterion, device)
    scheduler.step()

    if val_loss < best_val_loss:
        best_val_loss = val_loss
        torch.save(model.state_dict(), "best_model.pt")

    print(f"Epoch {epoch:3d} | train_loss={train_loss:.4f} "
          f"| val_loss={val_loss:.4f} | val_acc={val_acc:.4f}")
```

### The Four-Step Loop

Every training iteration is always exactly:
1. `optimizer.zero_grad()` — clear accumulated gradients
2. `loss.backward()` — compute gradients
3. `clip_grad_norm_()` — optional but recommended
4. `optimizer.step()` — update parameters

Forgetting `zero_grad()` is the most common PyTorch bug — gradients accumulate
across batches, loss explodes.

---

## Mixed Precision Training

```python
# float16 for forward/backward, float32 for optimizer state
# ~2× speedup, ~50% memory reduction on modern GPUs

scaler = torch.cuda.amp.GradScaler()

with torch.autocast(device_type="cuda", dtype=torch.float16):
    output = model(input)
    loss = criterion(output, target)

scaler.scale(loss).backward()   # scale to prevent float16 underflow
scaler.unscale_(optimizer)      # unscale before gradient clipping
torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
scaler.step(optimizer)
scaler.update()
```

bfloat16 (Brain Float) is preferred over float16 on A100/H100 GPUs — same range
as float32 (8-bit exponent), lower precision mantissa, no overflow issues:

```python
with torch.autocast(device_type="cuda", dtype=torch.bfloat16):
    ...
# No GradScaler needed for bfloat16 — no underflow risk
```

---

## Model Persistence

```python
# Save / load state dict (recommended)
torch.save(model.state_dict(), "model.pt")
model.load_state_dict(torch.load("model.pt", map_location="cpu"))

# Save full checkpoint (includes optimizer, scheduler, epoch)
checkpoint = {
    "epoch": epoch,
    "model_state": model.state_dict(),
    "optimizer_state": optimizer.state_dict(),
    "scheduler_state": scheduler.state_dict(),
    "val_loss": val_loss,
}
torch.save(checkpoint, "checkpoint.pt")

# Resume training
ckpt = torch.load("checkpoint.pt", map_location=device)
model.load_state_dict(ckpt["model_state"])
optimizer.load_state_dict(ckpt["optimizer_state"])
start_epoch = ckpt["epoch"] + 1
```

---

## Transfer Learning

The standard workflow for most applied deep learning:

```python
import torchvision.models as models

# Load pretrained backbone
backbone = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)

# Freeze all layers
for param in backbone.parameters():
    param.requires_grad = False

# Replace final classifier head
num_classes = 5
backbone.fc = nn.Linear(backbone.fc.in_features, num_classes)
# Only backbone.fc has requires_grad=True

# Two-phase training:
# Phase 1: train head only (frozen backbone)
optimizer_head = optim.Adam(backbone.fc.parameters(), lr=1e-3)
# ... train for N epochs ...

# Phase 2: unfreeze and fine-tune all layers with lower LR
for param in backbone.parameters():
    param.requires_grad = True

optimizer_full = optim.AdamW([
    {"params": backbone.layer4.parameters(), "lr": 1e-4},
    {"params": backbone.fc.parameters(),     "lr": 1e-3},
], weight_decay=0.01)
```

---

## Common Architectures — Building Blocks

```python
# Residual block (ResNet style)
class ResidualBlock(nn.Module):
    def __init__(self, dim: int):
        super().__init__()
        self.block = nn.Sequential(
            nn.LayerNorm(dim),
            nn.Linear(dim, dim * 4),
            nn.GELU(),
            nn.Linear(dim * 4, dim),
        )

    def forward(self, x):
        return x + self.block(x)   # skip connection

# Self-attention (Transformer style)
class SelfAttention(nn.Module):
    def __init__(self, embed_dim: int, num_heads: int):
        super().__init__()
        self.attn = nn.MultiheadAttention(embed_dim, num_heads, batch_first=True)
        self.norm = nn.LayerNorm(embed_dim)

    def forward(self, x):
        attn_out, _ = self.attn(x, x, x)   # query=key=value=x (self-attention)
        return self.norm(x + attn_out)       # pre-norm residual
```

---

## Debugging Toolkit

```python
# Shape debugging — the most common issue
print(x.shape)   # everywhere, always

# NaN/Inf detection
torch.isnan(loss).any()
torch.isinf(loss).any()

# Gradient flow check
for name, param in model.named_parameters():
    if param.grad is not None:
        print(f"{name}: grad_norm={param.grad.norm().item():.4f}")
    else:
        print(f"{name}: NO GRAD")

# Hook for intermediate activations
activations = {}
def make_hook(name):
    def hook(module, input, output):
        activations[name] = output.detach()
    return hook

model.layer1.register_forward_hook(make_hook("layer1"))

# torch.compile() — PyTorch 2.0+ JIT compilation
model = torch.compile(model)   # ~30-50% speedup; works on most models
```

---

## GPU Workflow Checklist

```
┌─────────────────────────────────────────────────────────────────────┐
│  GPU BEST PRACTICES                                                 │
│                                                                     │
│  ✅ model.to(device)  — move model to GPU at init                  │
│  ✅ X.to(device) in training loop                                   │
│  ✅ pin_memory=True in DataLoader                                   │
│  ✅ num_workers > 0 (usually 4–8)                                   │
│  ✅ Mixed precision (autocast + GradScaler or bfloat16)             │
│  ✅ torch.compile(model) for PyTorch 2.0+                          │
│  ✅ optimizer.zero_grad(set_to_none=True)  — slightly faster        │
│                                                                     │
│  ❌ .item() or .cpu() inside training loop (sync GPU→CPU)          │
│  ❌ np.array(tensor) without .detach().cpu().numpy()               │
│  ❌ Storing tensors in lists (keeps graph alive → memory leak)     │
│  ❌ Forgetting model.eval() during validation                       │
│  ❌ Forgetting optimizer.zero_grad() each step                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## Ecosystem Map

```
┌─────────────────────────────────────────────────────────────────────┐
│  PYTORCH ECOSYSTEM                                                  │
│                                                                     │
│  Hugging Face Transformers  — pretrained LLMs, vision, audio       │
│  torchvision                — image models, datasets, transforms   │
│  torchaudio                 — audio processing                     │
│  torchtext                  — text utilities                        │
│  Lightning (PyTorch Lightning) — training loop boilerplate removed │
│  TIMM                       — hundreds of image models             │
│  einops                     — readable tensor rearrangement        │
│  wandb / MLflow             — experiment tracking (→ 05-MLOPS.md)  │
│  ONNX                       — model export for inference servers   │
│  TorchScript                — serialize for C++ / mobile deploy    │
└─────────────────────────────────────────────────────────────────────┘
```

### PyTorch Lightning (Boilerplate Removal)

```python
import lightning as L

class LitModel(L.LightningModule):
    def __init__(self):
        super().__init__()
        self.model = MLP(128, 256, 10)
        self.criterion = nn.CrossEntropyLoss()

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        X, y = batch
        loss = self.criterion(self(X), y)
        self.log("train_loss", loss)
        return loss

    def validation_step(self, batch, batch_idx):
        X, y = batch
        loss = self.criterion(self(X), y)
        self.log("val_loss", loss)

    def configure_optimizers(self):
        opt = optim.AdamW(self.parameters(), lr=1e-3)
        sched = optim.lr_scheduler.CosineAnnealingLR(opt, T_max=50)
        return [opt], [sched]

trainer = L.Trainer(max_epochs=50, accelerator="auto", precision="16-mixed")
trainer.fit(lit_model, train_loader, val_loader)
```

Lightning handles the training loop, device placement, mixed precision, gradient
clipping, logging, and checkpointing — eliminating the boilerplate above.

---

## Common Confusion Points

**`model.eval()` does not disable gradient computation**: It disables Dropout
and switches BatchNorm to use running statistics. Gradient computation is separate —
disable with `torch.no_grad()`. Both are needed during validation.

**`loss.backward()` accumulates gradients**: Each call to `.backward()` adds to
`.grad`. Always call `optimizer.zero_grad()` (or `zero_grad(set_to_none=True)`)
before each new backward pass.

**`CrossEntropyLoss` expects logits, not probabilities**: Passing `softmax(logits)`
to `CrossEntropyLoss` applies softmax twice. Pass raw logits.

**`tensor.detach().cpu().numpy()`**: This is the correct sequence to convert a GPU
tensor to NumPy. `.detach()` removes it from the graph, `.cpu()` moves it to host
memory, `.numpy()` creates the NumPy view.

**`.item()` inside training loops causes GPU synchronization**: `loss.item()`
forces the GPU to flush and return the scalar to the CPU. Accumulate the raw tensor
loss and call `.item()` only for logging, outside the hot path.

**`num_workers` on Windows**: PyTorch's multiprocessing DataLoader workers use
`spawn` on Windows (vs `fork` on Linux). Code in workers must be inside
`if __name__ == "__main__":` or a function — not module-level executable code.

---

## Decision Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────┐
│  TASK                           │  APPROACH                        │
├─────────────────────────────────┼──────────────────────────────────┤
│  Tabular data, < 100k rows      │  sklearn (03-SKLEARN.md)         │
│  Tabular, > 100k or complex     │  XGBoost / LightGBM first        │
│  Images                         │  Transfer learning (ResNet/ViT)  │
│  Text / language                │  HuggingFace Transformers        │
│  Custom architecture research   │  PyTorch nn.Module from scratch  │
│  Standard training loop         │  PyTorch Lightning               │
├─────────────────────────────────┼──────────────────────────────────┤
│  OPTIMIZER                      │                                  │
│  Default                        │  AdamW(lr=1e-3, wd=0.01)         │
│  Fine-tuning pretrained         │  AdamW with lr warmup + decay    │
│  SGD when                       │  CV tasks where SGD + momentum   │
│                                 │  generalizes better than Adam    │
├─────────────────────────────────┼──────────────────────────────────┤
│  MIXED PRECISION                │                                  │
│  A100/H100 GPU                  │  bfloat16 (no scaler needed)     │
│  V100/RTX GPU                   │  float16 + GradScaler            │
│  CPU / MPS (Apple Silicon)      │  float32 (default)               │
├─────────────────────────────────┼──────────────────────────────────┤
│  MEMORY REDUCTION               │                                  │
│  Batch too large                │  Gradient accumulation           │
│  Model too large                │  Mixed precision + gradient ckpt │
│  Inference only                 │  torch.no_grad() always          │
└─────────────────────────────────┴──────────────────────────────────┘
```
