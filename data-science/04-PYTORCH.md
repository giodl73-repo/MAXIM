# 04 — PyTorch

> NumPy gives you n-dimensional arrays. PyTorch gives you n-dimensional arrays that
> know how to differentiate themselves and run on GPUs. That's the whole product.

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PYTORCH STACK                                      │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                     YOUR TRAINING CODE                               │   │
│  │   Dataset / DataLoader → nn.Module → Loss → Optimizer → .backward() │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌─────────────────┐  ┌─────────────────┐  ┌──────────────────────────┐    │
│  │   torch.nn      │  │  torch.optim    │  │  torch.utils.data        │    │
│  │  (layers, loss) │  │  (SGD/Adam/...) │  │  (Dataset, DataLoader)   │    │
│  └─────────────────┘  └─────────────────┘  └──────────────────────────┘    │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │                      torch.autograd                                   │   │
│  │    Dynamic computational graph — builds forward, differentiates       │   │
│  │    backward, accumulates gradients                                    │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
│                                                                              │
│  ┌──────────────────────────────────────────────────────────────────────┐   │
│  │              torch.Tensor  (CPU / CUDA / MPS / XPU)                  │   │
│  │              C++ core: LibTorch — ATen tensor library                 │   │
│  └──────────────────────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────────────────────┘
```

**Key design choice**: PyTorch uses *define-by-run* (dynamic graph). The computation
graph is rebuilt every forward pass. This means you can use Python control flow
(`if`, `for`) inside model code — the graph reflects the actual execution path.
TensorFlow 1.x was define-then-run (static graph). PyTorch 2 adds `torch.compile`
to get static-graph performance while keeping dynamic semantics.

---

## Tensors

### Creation

```python
import torch
import numpy as np

# From Python / NumPy
t = torch.tensor([1.0, 2.0, 3.0])              # infers dtype
t = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
t = torch.from_numpy(np_array)                  # shares memory (no copy)

# Factory functions
torch.zeros(3, 4)                               # shape (3, 4)
torch.ones(3, 4)
torch.rand(3, 4)                                # U[0, 1)
torch.randn(3, 4)                               # N(0, 1)
torch.arange(0, 10, 2)                          # [0, 2, 4, 6, 8]
torch.linspace(0, 1, 5)                         # [0, .25, .5, .75, 1]
torch.eye(4)                                    # 4×4 identity

# Like NumPy
torch.zeros_like(other_tensor)
torch.ones_like(other_tensor)
```

### dtype

```
torch.float32   (float)  — default for model params
torch.float16   (half)   — mixed precision training
torch.bfloat16           — better range than float16, hardware-dependent
torch.float64   (double) — scientific, rarely used in ML
torch.int32 / int64
torch.bool
```

```python
t = t.to(torch.float16)          # cast dtype
t = t.float()                    # shorthand for float32
t = t.half()                     # float16
```

### Device

```python
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

t = torch.randn(3, 4, device=device)       # create on device
t = t.to(device)                           # move to device
t = t.cuda()                               # explicit CUDA
t = t.cpu()                                # move to CPU

# Check
print(t.device)     # device(type='cuda', index=0)
```

### Shape Operations

```python
t = torch.randn(2, 3, 4)

t.shape          # torch.Size([2, 3, 4])
t.ndim           # 3
t.numel()        # 24

# Reshape (contiguous required)
t.view(6, 4)             # shares storage (no copy)
t.reshape(6, 4)          # copies if necessary

# Squeeze / unsqueeze
t.unsqueeze(0)           # (1, 2, 3, 4)  — add dim at position 0
t.squeeze(0)             # remove dim of size 1
t.squeeze()              # remove ALL size-1 dims

# Permute (like NumPy transpose but for N dims)
t.permute(2, 0, 1)       # (4, 2, 3)

# Concatenation
torch.cat([a, b], dim=0)         # concat along existing dim
torch.stack([a, b], dim=0)       # stack → new dim

# Indexing
t[0]             # first element along dim 0
t[:, 1, :]       # all, index 1, all
t[t > 0]         # boolean mask → 1D tensor
```

---

## Autograd

Autograd is the automatic differentiation engine. Every `torch.Tensor` has a
`requires_grad` flag. When set, PyTorch tracks all operations on it and builds
a dynamic computational graph (DAG of `Function` nodes).

```python
x = torch.tensor([2.0], requires_grad=True)
y = x ** 2 + 3 * x + 1          # y = x² + 3x + 1

y.backward()                     # dL/dy = 1 implicitly; computes dy/dx

print(x.grad)                    # tensor([7.])  — dy/dx at x=2: 2x+3 = 7
```

### Computational Graph

```
Forward:  x → (** 2) → (+ 3x) → (+ 1) → y
Backward: gradient flows from y back through the DAG, applying chain rule
```

Each `.backward()` **accumulates** gradients (adds to `.grad`). Always zero
before the next pass:

```python
optimizer.zero_grad()    # standard — zeros all model parameter grads
# or
for p in model.parameters():
    p.grad = None        # slightly more efficient (skips the fill)
```

### No-Gradient Contexts

```python
# Inference: don't build graph, save memory
with torch.no_grad():
    output = model(x)

# Decorator form
@torch.no_grad()
def predict(x):
    return model(x)

# Detach a tensor from the graph
y = x.detach()     # same data, requires_grad=False, not tracked
```

---

## nn.Module

`nn.Module` is the base class for all models and layers. Contract:

```
class MyModel(nn.Module):
    def __init__(self):
        super().__init__()       # REQUIRED — registers parameter tracking
        # declare all sub-modules and params as attributes

    def forward(self, x):
        # define the computation
        return result
```

```python
import torch.nn as nn

class MLP(nn.Module):
    def __init__(self, in_dim, hidden_dim, out_dim, dropout=0.2):
        super().__init__()
        self.net = nn.Sequential(
            nn.Linear(in_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, hidden_dim),
            nn.ReLU(),
            nn.Dropout(dropout),
            nn.Linear(hidden_dim, out_dim),
        )

    def forward(self, x):
        return self.net(x)

model = MLP(128, 512, 10)
print(model)                              # shows architecture
print(sum(p.numel() for p in model.parameters()))   # param count
```

### Key Layers

```
┌──────────────────────────────────────────────────────────────────────┐
│  LAYER               │  USE CASE                                     │
├──────────────────────┼───────────────────────────────────────────────┤
│  nn.Linear(in, out)  │  Fully connected                              │
│  nn.Embedding(n, d)  │  Lookup table for token IDs                   │
│  nn.Conv2d(c_in,     │  Spatial convolution (images)                 │
│    c_out, k, stride) │                                               │
│  nn.ConvTranspose2d  │  Upsampling (decoder / generator)             │
│  nn.LSTM / GRU       │  Sequential (largely replaced by Transformer) │
│  nn.MultiheadAttn    │  Self-attention block                         │
│  nn.TransformerEncoder│  Full encoder stack                          │
│  nn.LayerNorm        │  Normalizes features (Transformer standard)   │
│  nn.BatchNorm2d      │  Normalizes batch (CNN standard)              │
│  nn.Dropout(p)       │  Regularization (train only)                  │
│  nn.MaxPool2d        │  Spatial downsampling                         │
│  nn.AdaptiveAvgPool2d│  Pool to fixed output size                    │
│  nn.Flatten()        │  Reshape conv output → 1D for linear layers   │
└──────────────────────┴───────────────────────────────────────────────┘
```

### Activations

```python
nn.ReLU()           # max(0, x) — default for CNNs, MLPs
nn.GELU()           # smooth ReLU — standard in Transformers
nn.SiLU()           # sigmoid-weighted linear — used in LLaMA, SDXL
nn.Sigmoid()        # binary output
nn.Softmax(dim=-1)  # multi-class probabilities (use in loss, not layer)
nn.Tanh()
```

### Loss Functions

```python
nn.CrossEntropyLoss()   # classification (combines log-softmax + NLL)
                        # input: raw logits (N, C); target: class indices (N,)
nn.BCEWithLogitsLoss()  # binary classification (numerically stable)
nn.MSELoss()            # regression
nn.L1Loss()             # MAE regression
nn.HuberLoss()          # robust regression (L2 near 0, L1 far out)
nn.KLDivLoss()          # distributional — VAE, knowledge distillation
```

---

## Optimizers

```python
import torch.optim as optim

# SGD with momentum
optimizer = optim.SGD(model.parameters(), lr=0.01, momentum=0.9,
                      weight_decay=1e-4)

# Adam — default for most deep learning
optimizer = optim.Adam(model.parameters(), lr=1e-3,
                       betas=(0.9, 0.999), weight_decay=1e-5)

# AdamW — Adam with decoupled weight decay (better generalization)
optimizer = optim.AdamW(model.parameters(), lr=1e-3, weight_decay=1e-2)

# Different LR per parameter group (common for fine-tuning)
optimizer = optim.AdamW([
    {"params": model.backbone.parameters(), "lr": 1e-5},
    {"params": model.head.parameters(),     "lr": 1e-3},
], weight_decay=1e-2)
```

### Learning Rate Schedulers

```python
# Step decay
scheduler = optim.lr_scheduler.StepLR(optimizer, step_size=30, gamma=0.1)

# Cosine annealing (standard for long training runs)
scheduler = optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=100)

# Warmup + cosine (Transformers standard)
from torch.optim.lr_scheduler import OneCycleLR
scheduler = OneCycleLR(optimizer, max_lr=1e-3, total_steps=num_train_steps,
                       pct_start=0.1)   # 10% warmup

# Plateau (reduce on stagnation)
scheduler = optim.lr_scheduler.ReduceLROnPlateau(optimizer, mode="min",
                                                  factor=0.5, patience=5)
```

---

## Canonical Training Loop

```python
import torch
import torch.nn as nn
from torch.utils.data import DataLoader

def train_one_epoch(model, loader, optimizer, criterion, device):
    model.train()                           # activates Dropout, BatchNorm train mode
    total_loss, correct = 0, 0

    for batch_x, batch_y in loader:
        batch_x = batch_x.to(device)
        batch_y = batch_y.to(device)

        # 1. Zero gradients
        optimizer.zero_grad()

        # 2. Forward
        logits = model(batch_x)             # raw scores, shape (N, num_classes)

        # 3. Compute loss
        loss = criterion(logits, batch_y)

        # 4. Backward — build gradient DAG, compute grads
        loss.backward()

        # 5. Gradient clipping (optional but standard for Transformers)
        torch.nn.utils.clip_grad_norm_(model.parameters(), max_norm=1.0)

        # 6. Update weights
        optimizer.step()

        total_loss += loss.item() * len(batch_y)
        correct += (logits.argmax(dim=1) == batch_y).sum().item()

    return total_loss / len(loader.dataset), correct / len(loader.dataset)


@torch.no_grad()
def evaluate(model, loader, criterion, device):
    model.eval()                            # deactivates Dropout, uses running stats
    total_loss, correct = 0, 0

    for batch_x, batch_y in loader:
        batch_x, batch_y = batch_x.to(device), batch_y.to(device)
        logits = model(batch_x)
        loss = criterion(logits, batch_y)
        total_loss += loss.item() * len(batch_y)
        correct += (logits.argmax(dim=1) == batch_y).sum().item()

    return total_loss / len(loader.dataset), correct / len(loader.dataset)


# Main training loop
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = MLP(128, 512, 10).to(device)
optimizer = torch.optim.AdamW(model.parameters(), lr=1e-3)
criterion = nn.CrossEntropyLoss()
scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(optimizer, T_max=50)

best_val_acc = 0.0

for epoch in range(50):
    train_loss, train_acc = train_one_epoch(model, train_loader, optimizer,
                                             criterion, device)
    val_loss, val_acc = evaluate(model, val_loader, criterion, device)
    scheduler.step()

    print(f"Epoch {epoch:3d} | "
          f"train_loss={train_loss:.4f} train_acc={train_acc:.3f} | "
          f"val_loss={val_loss:.4f}  val_acc={val_acc:.3f}")

    # Checkpoint best model
    if val_acc > best_val_acc:
        best_val_acc = val_acc
        torch.save({
            "epoch": epoch,
            "model_state_dict": model.state_dict(),
            "optimizer_state_dict": optimizer.state_dict(),
            "val_acc": val_acc,
        }, "best_model.pt")
```

### `model.train()` vs `model.eval()`

Critical — forgetting this is a common source of bugs:

```
train() mode:  Dropout randomly zeroes activations (regularization)
               BatchNorm uses batch statistics (current mini-batch)

eval() mode:   Dropout is disabled (deterministic inference)
               BatchNorm uses running statistics (accumulated during training)
```

---

## Dataset and DataLoader

```python
from torch.utils.data import Dataset, DataLoader

class MyDataset(Dataset):
    def __init__(self, features, labels, transform=None):
        self.X = torch.tensor(features, dtype=torch.float32)
        self.y = torch.tensor(labels, dtype=torch.long)
        self.transform = transform

    def __len__(self):
        return len(self.X)

    def __getitem__(self, idx):
        x, y = self.X[idx], self.y[idx]
        if self.transform:
            x = self.transform(x)
        return x, y


train_ds = MyDataset(X_train, y_train)
val_ds   = MyDataset(X_val,   y_val)

train_loader = DataLoader(
    train_ds,
    batch_size=64,
    shuffle=True,
    num_workers=4,           # parallel data loading processes
    pin_memory=True,         # locks pages → faster CPU→GPU transfer
    drop_last=True,          # drop last incomplete batch (avoids BatchNorm issues)
    persistent_workers=True, # keep workers alive between epochs
)
val_loader = DataLoader(val_ds, batch_size=256, shuffle=False, num_workers=4)
```

### torchvision.transforms for Images

```python
from torchvision import transforms

train_transform = transforms.Compose([
    transforms.RandomResizedCrop(224),
    transforms.RandomHorizontalFlip(),
    transforms.ColorJitter(brightness=0.2, contrast=0.2, saturation=0.2),
    transforms.ToTensor(),                         # HWC uint8 → CHW float32, [0,1]
    transforms.Normalize(mean=[0.485, 0.456, 0.406],   # ImageNet stats
                         std=[0.229, 0.224, 0.225]),
])

val_transform = transforms.Compose([
    transforms.Resize(256),
    transforms.CenterCrop(224),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.485, 0.456, 0.406],
                         std=[0.229, 0.224, 0.225]),
])
```

---

## Model Persistence

```python
# Save — state dict only (recommended)
torch.save(model.state_dict(), "model.pt")

# Load — must instantiate model first
model = MLP(128, 512, 10)
model.load_state_dict(torch.load("model.pt", map_location=device))
model.to(device)
model.eval()

# Full checkpoint (training state)
torch.save({
    "epoch": epoch,
    "model_state_dict": model.state_dict(),
    "optimizer_state_dict": optimizer.state_dict(),
    "scheduler_state_dict": scheduler.state_dict(),
    "val_loss": val_loss,
}, "checkpoint.pt")

# Resume from checkpoint
ckpt = torch.load("checkpoint.pt", map_location=device)
model.load_state_dict(ckpt["model_state_dict"])
optimizer.load_state_dict(ckpt["optimizer_state_dict"])
scheduler.load_state_dict(ckpt["scheduler_state_dict"])
start_epoch = ckpt["epoch"] + 1
```

---

## Transfer Learning

### torchvision Pretrained Models

```python
import torchvision.models as models
import torch.nn as nn

# Load pretrained ResNet-50
backbone = models.resnet50(weights=models.ResNet50_Weights.IMAGENET1K_V2)

# Strategy 1: Feature extraction — freeze backbone, train head only
for param in backbone.parameters():
    param.requires_grad = False

# Replace final FC layer for your task
num_classes = 5
backbone.fc = nn.Linear(backbone.fc.in_features, num_classes)
# Only backbone.fc params have requires_grad=True

# Strategy 2: Fine-tuning — train everything (or layers from some point)
for param in backbone.layer4.parameters():
    param.requires_grad = True  # unfreeze last residual block

# Use different LRs
optimizer = torch.optim.AdamW([
    {"params": backbone.layer4.parameters(), "lr": 1e-5},
    {"params": backbone.fc.parameters(),     "lr": 1e-3},
])
```

### HuggingFace Transformers

```python
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch

model_name = "microsoft/deberta-v3-base"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(
    model_name, num_labels=3
)

# Tokenize
encoding = tokenizer(
    ["First sentence", "Second sentence"],
    truncation=True,
    max_length=512,
    padding="max_length",
    return_tensors="pt",         # returns PyTorch tensors
)

# Forward
with torch.no_grad():
    outputs = model(**encoding)
logits = outputs.logits          # (batch_size, num_labels)
preds  = logits.argmax(dim=-1)
```

---

## Mixed Precision Training

AMP (Automatic Mixed Precision): computes in float16 where safe, stores master
weights in float32. Typically 2× speedup on Ampere+ GPUs (A100, RTX 3090+).

```python
from torch.cuda.amp import autocast, GradScaler

scaler = GradScaler()    # scales loss to prevent fp16 underflow

for batch_x, batch_y in train_loader:
    batch_x, batch_y = batch_x.to(device), batch_y.to(device)
    optimizer.zero_grad()

    with autocast():                          # forward in fp16
        logits = model(batch_x)
        loss = criterion(logits, batch_y)

    scaler.scale(loss).backward()             # backward in fp16 (scaled)
    scaler.unscale_(optimizer)                # unscale before clipping
    torch.nn.utils.clip_grad_norm_(model.parameters(), 1.0)
    scaler.step(optimizer)                    # step (in fp32)
    scaler.update()                           # update scale factor
```

---

## torch.compile (PyTorch 2.x)

`torch.compile` traces the model and produces optimized machine code (via TorchInductor
→ OpenAI Triton on GPU, C++ on CPU). Typically 1.5–2× speedup with one line:

```python
model = torch.compile(model)    # that's it — works as a decorator too
# or
model = torch.compile(model, mode="reduce-overhead")  # small models
model = torch.compile(model, mode="max-autotune")     # long training runs
```

**Restrictions**: first forward pass is slow (tracing). Incompatible with dynamic
control flow that changes graph structure between calls. Works with DDP.

---

## Distributed Training — DDP

`DistributedDataParallel` (DDP): each GPU gets a copy of the model, processes
different batches, gradients are averaged across GPUs before each parameter update.

```python
import torch.distributed as dist
from torch.nn.parallel import DistributedDataParallel as DDP
from torch.utils.data.distributed import DistributedSampler

# Initialize — AzureML / SLURM injects RANK, WORLD_SIZE, MASTER_ADDR
dist.init_process_group("nccl")       # NCCL: NVIDIA collective comm lib
local_rank = int(os.environ["LOCAL_RANK"])
torch.cuda.set_device(local_rank)

model = MyModel().to(local_rank)
model = DDP(model, device_ids=[local_rank])

# Sampler ensures each GPU sees different data shards
train_sampler = DistributedSampler(train_dataset)
train_loader  = DataLoader(train_dataset, sampler=train_sampler, batch_size=64)

for epoch in range(num_epochs):
    train_sampler.set_epoch(epoch)     # ensures different shuffle each epoch
    train_one_epoch(model, ...)

dist.destroy_process_group()
```

Launch:
```bash
torchrun --nproc_per_node=4 train.py    # 4 GPUs on one node
# Multi-node: add --nnodes, --node_rank, --master_addr, --master_port
```

---

## Debugging Toolkit

### Check gradient flow

```python
# Register hook to inspect gradients
def print_grad_hook(name):
    def hook(grad):
        print(f"{name}: grad norm = {grad.norm():.4f}, "
              f"has nan = {grad.isnan().any()}")
    return hook

for name, param in model.named_parameters():
    param.register_hook(print_grad_hook(name))
```

### Check for NaN/Inf

```python
# After forward
assert not torch.isnan(loss), f"NaN loss at step {step}"
assert not torch.isinf(loss), f"Inf loss at step {step}"

# Check activations
for name, module in model.named_modules():
    def hook(m, inp, out, name=name):
        if isinstance(out, torch.Tensor) and torch.isnan(out).any():
            print(f"NaN in {name}")
    module.register_forward_hook(hook)
```

### GPU memory

```python
# Current usage
print(torch.cuda.memory_allocated() / 1e9, "GB")
print(torch.cuda.max_memory_allocated() / 1e9, "GB peak")

# Clear cache (useful in notebooks between experiments)
torch.cuda.empty_cache()

# Profile memory timeline
with torch.profiler.profile(
    activities=[torch.profiler.ProfilerActivity.CUDA],
    profile_memory=True,
) as prof:
    output = model(input)
print(prof.key_averages().table(sort_by="cuda_memory_usage"))
```

---

## PyTorch Lightning

Lightning wraps the training loop boilerplate into a structured `LightningModule`,
handling multi-GPU, logging, checkpointing, and mixed precision automatically.

```python
import lightning as L
import torch.nn.functional as F

class LitModel(L.LightningModule):
    def __init__(self, in_dim, hidden_dim, num_classes):
        super().__init__()
        self.save_hyperparameters()           # logs hparams to TensorBoard/MLflow
        self.model = MLP(in_dim, hidden_dim, num_classes)

    def forward(self, x):
        return self.model(x)

    def training_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        acc = (logits.argmax(dim=1) == y).float().mean()
        self.log("train/loss", loss, prog_bar=True)
        self.log("train/acc",  acc,  prog_bar=True)
        return loss

    def validation_step(self, batch, batch_idx):
        x, y = batch
        logits = self(x)
        loss = F.cross_entropy(logits, y)
        acc = (logits.argmax(dim=1) == y).float().mean()
        self.log("val/loss", loss, prog_bar=True)
        self.log("val/acc",  acc,  prog_bar=True)

    def configure_optimizers(self):
        optimizer = torch.optim.AdamW(self.parameters(), lr=1e-3)
        scheduler = torch.optim.lr_scheduler.CosineAnnealingLR(
            optimizer, T_max=self.trainer.max_epochs
        )
        return {"optimizer": optimizer, "lr_scheduler": scheduler}


# Train
lit_model = LitModel(128, 512, 10)
trainer = L.Trainer(
    max_epochs=50,
    accelerator="auto",       # cpu / gpu / tpu — detected automatically
    devices="auto",           # 1 GPU or all available
    precision="16-mixed",     # AMP
    log_every_n_steps=10,
    callbacks=[
        L.pytorch.callbacks.ModelCheckpoint(monitor="val/loss", save_top_k=3),
        L.pytorch.callbacks.EarlyStopping(monitor="val/loss", patience=10),
        L.pytorch.callbacks.LearningRateMonitor(),
    ],
)
trainer.fit(lit_model, train_loader, val_loader)
trainer.test(lit_model, test_loader)
```

---

## GPU Checklist

```
☐  All tensors on same device (cpu/cuda mismatch → runtime error)
☐  model.to(device) called
☐  model.train() before training loop, model.eval() before inference
☐  optimizer.zero_grad() before loss.backward()
☐  loss.item() to extract scalar (not loss itself — avoids retaining graph)
☐  @torch.no_grad() on inference / evaluation functions
☐  num_workers > 0 in DataLoader (but 0 in Windows/notebooks if spawning issues)
☐  pin_memory=True when training on GPU
☐  torch.compile() added for 1.5–2× free speedup (PyTorch 2.x)
☐  Checkpoint .pt saves state_dict, not full model
```

---

## Old World → New World

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  CONCEPT              │  .NET / C# World          │  PyTorch World           │
├───────────────────────┼───────────────────────────┼──────────────────────────┤
│  Compute graph        │  LINQ expression trees    │  autograd DAG            │
│  Layer / transform    │  LINQ operator / EF query │  nn.Module               │
│  Model params         │  class fields             │  nn.Parameter (tracked)  │
│  Training step        │  for loop + delegate      │  forward() + backward()  │
│  GPU execution        │  CUDA via ML.NET / TorchSharp│ .to(device)           │
│  Serialization        │  BinaryFormatter / JSON   │  state_dict + torch.save │
│  Parallel batches     │  PLINQ / Parallel.For     │  DataLoader num_workers  │
└──────────────────────┴───────────────────────────┴──────────────────────────┘
```

---

## Decision Cheat Sheet

```
┌──────────────────────────────────────────────────────────────────────────────┐
│  TASK                              │  WHAT TO USE                            │
├────────────────────────────────────┼─────────────────────────────────────────┤
│  Tabular ML (<1M rows)             │  scikit-learn (03-SKLEARN.md)           │
│  Tabular ML (millions of rows)     │  XGBoost / LightGBM — still not PyTorch │
│  Image classification              │  torchvision pretrained + fine-tune     │
│  Text classification               │  HuggingFace AutoModel + fine-tune      │
│  Custom architecture               │  PyTorch nn.Module from scratch         │
│  Training loop boilerplate         │  PyTorch Lightning                      │
│  Hyperparameter search             │  W&B Sweeps or Optuna                   │
│  Multi-GPU single node             │  DDP via torchrun / Lightning           │
│  Multi-GPU multi-node              │  DDP + AzureML (06-AZURE-ML.md)         │
│  Fast inference                    │  ONNX Runtime (see 05-MLOPS.md)         │
│  Speedup (free)                    │  torch.compile(model)                   │
│  Memory efficiency                 │  AMP (autocast + GradScaler)            │
│  Reproducibility                   │  torch.manual_seed + DataLoader seeds   │
└────────────────────────────────────┴─────────────────────────────────────────┘
```

---

## Common Confusion Points

**`model(x)` calls `forward()` indirectly**: Never call `model.forward(x)` directly.
`model(x)` goes through `__call__`, which runs forward hooks, backward hooks, and
calls `forward()`. Calling `.forward()` directly skips those hooks.

**Gradient accumulation across batches**: PyTorch adds to `.grad`, it does not replace.
If you forget `optimizer.zero_grad()`, gradients from previous batches persist.
This can be intentional (gradient accumulation for large effective batch sizes) or
a bug. Know which you're doing.

**`.item()` on loss**: `loss.backward()` needs the loss tensor. But when logging,
use `loss.item()` to get the Python float — this releases the graph node from memory.
Storing `loss` tensors (e.g., in a list) holds the entire computation graph in memory.

**`requires_grad` propagates**: If any input has `requires_grad=True`, the output
will too. This is why `with torch.no_grad()` is needed for inference — without it,
you're building (and retaining) a graph even during eval, wasting memory.

**DataLoader `num_workers` on Windows**: Multiprocessing spawn (Windows) causes
issues when the dataset or transforms aren't picklable. Start with `num_workers=0`
to debug, then increase.

**`model.state_dict()` vs saving the whole model**: Saving the whole model with
`torch.save(model, path)` pickles the class definition — brittle across code changes.
Always save `model.state_dict()` and reconstruct the model from code.
