# 07 — Multimodal Models

## The Big Picture

```
  The Multimodal Landscape — Modalities and Models
  ==================================================

  ┌──────────────┬─────────────────┬────────────────────────────────────────┐
  │  MODALITY    │  REPRESENTATION │  KEY MODELS                            │
  ├──────────────┼─────────────────┼────────────────────────────────────────┤
  │  Text        │  BPE tokens     │  Every LLM (baseline)                  │
  ├──────────────┼─────────────────┼────────────────────────────────────────┤
  │  Image       │  Patch tokens   │  GPT-4V, Claude 3/4, Gemini,           │
  │              │  (ViT patches)  │  LLaVA, Phi-3-Vision                   │
  ├──────────────┼─────────────────┼────────────────────────────────────────┤
  │  Audio/      │  Mel spectrogram│  Whisper, Wav2Vec2, Gemini Live,        │
  │  Speech      │  → tokens       │  GPT-4o Audio                          │
  ├──────────────┼─────────────────┼────────────────────────────────────────┤
  │  Video       │  Sampled frames │  Gemini 1.5 Pro (1M context),          │
  │              │  + temporal     │  GPT-4V (short), Video-LLaMA           │
  ├──────────────┼─────────────────┼────────────────────────────────────────┤
  │  Document    │  Image + OCR    │  Claude 3 (PDF), GPT-4V, DocLLM,       │
  │  (PDF/table) │  token stream   │  LayoutLM, Donut                       │
  ├──────────────┼─────────────────┼────────────────────────────────────────┤
  │  Embeddings  │  Dense vector   │  CLIP, ALIGN, ImageBind, SigLIP        │
  │  (cross-     │  shared space   │  (image and text in same latent space) │
  │   modal)     │                 │                                        │
  └──────────────┴─────────────────┴────────────────────────────────────────┘

  The architectural challenge: different modalities live in different
  representation spaces. Multimodal models bridge them into a shared
  space that a language model can reason over.
```

---

## Vision-Language Models

### CLIP — Contrastive Pretraining

```
  CLIP (Radford et al., OpenAI 2021) — The Foundation
  ──────────────────────────────────────────────────────────────────

  Training objective: given N (image, caption) pairs in a batch,
  maximize similarity of matching pairs, minimize similarity of
  N²-N non-matching pairs.

  Architecture:
  ┌──────────────┐         ┌──────────────────────┐
  │  Image       │         │  Image encoder       │
  │  (224×224)   │────────►│  (ViT or ResNet)     │────────┐
  └──────────────┘         │  Projects to d-dim   │        │
                           └──────────────────────┘        │
                                                    cosine  │
                           ┌──────────────────────┐ sim.  ├──► (match or not)
  ┌──────────────┐         │  Text encoder        │        │
  │  Caption     │────────►│  (Transformer)       │────────┘
  │  "a dog..."  │         │  Projects to d-dim   │
  └──────────────┘         └──────────────────────┘

  Training data: 400M (image, text) pairs from the internet
  Vocabulary: the shared d-dimensional embedding space

  Key property: zero-shot classification
    No training required for new categories
    "A photo of a [cat/dog/car]" → compare to image embedding
    Works because the embedding space encodes semantic similarity

  Applications:
    Image search (embed images + query in same space)
    Zero-shot image classification
    Input to VLMs: CLIP image encoder → frozen → plugged into LLM
```

### Architecture Patterns for Vision-Language Models

```
  Three major patterns for combining vision with LLMs:
  ──────────────────────────────────────────────────────────────────

  PATTERN 1: Linear Projection (LLaVA, early models)
  ──────────────────────────────────────────────────
  Image
    → ViT encoder (e.g., CLIP ViT-L/14) → patch embeddings
    → Linear projection layer (W: d_vision → d_llm)
    → Concatenate with text tokens
    → LLM (Llama, Vicuna, etc.)

  Properties:
    Simplest approach
    Linear projection W is the only trainable component initially
    Fast to train (only W, then optionally full instruction tune)
    Used by: LLaVA-1.0

  PATTERN 2: Querying Transformer / Q-Former (BLIP-2)
  ───────────────────────────────────────────────────
  Image
    → Frozen ViT encoder → image features
    → Q-Former: cross-attention over image features
      (learnable query vectors attend to image features)
    → Fixed-size output (32 query vectors) regardless of image size
    → Linear projection → LLM (OPT, FlanT5, etc.)

  Properties:
    More powerful than linear projection
    Q-Former learns to extract task-relevant image features
    Fixed output size decouples vision from LLM input length
    LLM stays fully frozen — only Q-Former trains first

  PATTERN 3: Native multimodal tokenization (GPT-4V, Claude 3+, Gemini)
  ──────────────────────────────────────────────────────────────────────
  Image
    → Tile/resize to patches (e.g., 16×16 patch grid)
    → Each patch → token embedding via specialized vision encoder
    → Tokens concatenated into sequence with text tokens
    → Full Transformer processes unified token sequence

  Properties:
    End-to-end trained
    Highest capability — no frozen components
    Very expensive to train from scratch
    Image → ~256-2048 tokens depending on resolution

  Which pattern are you using?
    API (GPT-4V, Claude 3/4, Gemini): Pattern 3 (opaque to you)
    Open source (LLaVA, Phi-3-Vision): typically Pattern 1 or 2
    Building your own VLM: start with Pattern 1 (LLaVA approach)
```

### Image Token Cost — The Critical Practical Constraint

```
  Image tokens are expensive — this drives architecture decisions
  ──────────────────────────────────────────────────────────────────

  GPT-4V token cost (approximate):
    Low detail:   85 tokens per image (fixed)
    High detail:  Image tiled into 512×512 tiles
                  Each tile = 170 tokens + 85 base = 255/tile
                  A 1024×1024 image: 4 tiles → 4×255 + 85 = 1105 tokens
                  A 2048×2048 image: 16 tiles → 16×255 + 85 = 4165 tokens

  Claude 3 vision token cost:
    Roughly: (width/32) × (height/32) tokens
    1024×1024: ~1024 tokens
    Max image: 5MB or 8000px longest edge

  Cost implications:
    At GPT-4o pricing ($2.50/1M input):
      1000 image requests (1024×1024 high detail): ~1100 tokens × 1000 = $2.75
      At scale (1M requests/day): $2750/day on images alone
    Solution: use low detail when you don't need fine-grained visual reasoning

  Practical rules:
    Document parsing (text extraction): high detail
    UI screenshot: high detail
    General image description: low detail
    Thumbnail/icon identification: low detail
```

---

## Audio and Speech

### Whisper — The Speech-to-Text Standard

```
  Whisper (OpenAI 2022) — Architecture
  ──────────────────────────────────────────────────────────────────

  Encoder-decoder Transformer:

  Raw audio (16kHz)
    → Log-mel spectrogram (80 mel bins, 30-second window)
    → CNN feature extractor → patch embeddings
    → Encoder: Transformer processes audio features
    → Decoder: Transformer auto-regressively generates BPE tokens
               (same tokenizer as GPT, same BPE vocabulary)

  Why log-mel spectrogram?
    Raw audio waveform: 16000 samples/second, too long for attention
    Mel spectrogram: compress into perceptually-motivated frequency bins
    Log scale: matches how loudness perception works (Weber–Fechner law)
    Result: 30-second audio → 3000 frames (100× compression)

  Training:
    680,000 hours of supervised (audio, transcript) pairs
    99 languages, including code-switching
    Trained as a multi-task model: transcription, translation, language ID

  Model sizes:
    tiny:   39M params  · fast, lower quality
    base:   74M params
    small:  244M params
    medium: 769M params
    large-v3: 1.55B params · state-of-the-art for most languages
    turbo (large-v3-turbo): pruned large-v3, 8× faster

  Deployment:
    openai-whisper: local, Python, runs on CPU or GPU
    faster-whisper: CTranslate2 backend, 4× faster than openai-whisper
    OpenAI Whisper API: $0.006/minute, managed, no GPU required
    Azure Speech Services: $1/hour (OpenAI or Microsoft model)
```

---

## Video Understanding

```
  Video LLM Challenges
  ──────────────────────────────────────────────────────────────────

  A 60-second video at 30fps = 1800 frames
  At 1000 tokens/frame: 1.8M tokens — impossible in most models

  Frame sampling strategies:
  ┌─────────────────────┬──────────────────┬──────────────────────┐
  │  Strategy           │  Tokens          │  When to use         │
  ├─────────────────────┼──────────────────┼──────────────────────┤
  │  Fixed rate         │  N × img_tokens  │  Action recognition, │
  │  (1 frame/sec)      │  controllable    │  activity detection  │
  ├─────────────────────┼──────────────────┼──────────────────────┤
  │  Keyframe extract   │  Low             │  Summarization,      │
  │  (scene changes)    │                  │  event detection     │
  ├─────────────────────┼──────────────────┼──────────────────────┤
  │  Sparse + dense     │  Medium          │  General video QA    │
  │  (overview + key    │                  │                      │
  │   moments)          │                  │                      │
  ├─────────────────────┼──────────────────┼──────────────────────┤
  │  Long context model │  Full fidelity   │  Gemini 1.5 Pro:     │
  │  (1M+ tokens)       │  ~1M tokens for  │  full movie analysis │
  │                     │  90-min movie    │                      │
  └─────────────────────┴──────────────────┴──────────────────────┘

  Temporal attention:
    Standard attention: treats frame tokens like text, no temporal ordering
    Temporal positional encoding: encode frame index alongside spatial position
    3D attention: attend across both spatial and temporal dimensions (expensive)
    Video-specific models (Video-LLaMA, TimeChat): temporal-aware architectures
```

---

## Cross-Modal Embeddings

```
  CLIP-style embedding models — use cases beyond zero-shot classification
  ──────────────────────────────────────────────────────────────────────

  Shared embedding space:
    Same vector space for images and text
    cos_sim("a cat", image_of_cat) > cos_sim("a dog", image_of_cat)

  Applications:
    Image search by text query:
      Embed all images offline → store in vector DB
      At query time: embed text → ANN search → return similar images

    Multi-modal RAG:
      Documents with images: embed both text chunks and images
      Query retrieves relevant text AND relevant images
      Combined context fed to vision-language model

    Cross-modal recommendation:
      User likes image X → find similar text descriptions
      Or: user reads article Y → find visually similar images

  Major cross-modal embedding models:
    CLIP (OpenAI):          ViT-L/14, 768-dim, English-strong
    SigLIP (Google):        improved contrastive loss, better quality
    ALIGN (Google):         1.8B image-text pairs, strong multilingual
    ImageBind (Meta):       6 modalities: image, text, audio, depth,
                            thermal, IMU — all in shared space
```

---

## Practical Constraints and Tradeoffs

### Document Parsing: OCR vs. Vision Model

```
  ┌──────────────────────────────────────────────────────────────────────┐
  │  DECISION: How to extract text/structure from PDFs and images         │
  │                                                                      │
  │  Is the document clearly formatted (standard PDF, clean scan)?       │
  │           │                                                          │
  │      ┌────┴────────┐                                                 │
  │     YES             NO (complex layout, tables, handwritten)         │
  │      │              │                                                │
  │      ▼              ▼                                                │
  │  PDF text      Does it have tables, charts, or                       │
  │  extraction    visual elements that matter?                          │
  │  (pdfplumber,       │                                                │
  │  PyPDF2)       ┌────┴────────┐                                       │
  │  Free, fast   YES             NO                                     │
  │               │              │                                       │
  │               ▼              ▼                                       │
  │         Vision model     OCR (Tesseract,                             │
  │         (GPT-4V, Claude  Azure Form                                  │
  │         3, Gemini)       Recognizer,                                 │
  │         Higher cost      AWS Textract)                               │
  │         but handles      Structured output,                          │
  │         any layout       cheaper than VLM                            │
  └──────────────────────────────────────────────────────────────────────┘
```

---

## Common Confusion Points

**"Multimodal" means the model reasons across modalities, not just accepts them.**
A model that accepts an image and a question is multimodal. A model that can cross-reference a chart in an image against a number mentioned in a text document is reasoning across modalities. Most current VLMs do the former well; the latter is still challenging and task-dependent.

**Vision tokens are much more expensive than text tokens.**
A 1024×1024 image costs ~1000 tokens on Claude. A typical RAG response uses 2000 text tokens. Processing 100 images per second means you're burning ~100k tokens/second in vision alone. Architect for this: cache processed image embeddings where possible, use low-detail mode for non-critical images, resize before sending.

**Whisper is not the same as a real-time speech model.**
Whisper processes audio in 30-second chunks. It's designed for batch transcription, not real-time streaming. For real-time speech (voice interfaces), use streaming-capable models: Deepgram, AssemblyAI, or Azure Speech. GPT-4o Audio is genuinely real-time; Whisper API is batch.

**CLIP embeddings are not substitutes for LLM text embeddings in RAG.**
CLIP was trained on image-caption pairs for zero-shot classification. Its text encoder is weaker than dedicated text embedding models (text-embedding-3-large). For hybrid image+text retrieval: use CLIP for images, a text embedding model for text, combine with reciprocal rank fusion.

**Document vision models don't always beat OCR + structure extraction.**
For structured documents (invoices, forms, tables) with consistent layouts, Azure Form Recognizer or AWS Textract + LLM post-processing often beats GPT-4V at 10% of the cost. Use vision models for unstructured, complex, or visually rich documents where structural extraction fails.

---

## Decision Cheat Sheet

| Task | Approach | Why |
|------|---------|-----|
| OCR clean PDF, extract text | pdfplumber / PyMuPDF | Free, fast, perfect quality for clean PDFs |
| OCR complex form / invoice | Azure Form Recognizer, AWS Textract | Structured extraction, cheaper than VLM |
| Understand image content (QA) | GPT-4V or Claude 3 vision | State-of-the-art VQA |
| Image captioning at scale | LLaVA or Phi-3-Vision (self-hosted) | Cheaper than API for batch work |
| Image search by text query | CLIP/SigLIP embeddings + vector DB | Shared embedding space is the tool for this |
| Speech transcription (batch) | Whisper large-v3 or OpenAI API | Best quality, easy API |
| Real-time voice interface | Deepgram / Azure Speech / GPT-4o Audio | Streaming; Whisper is batch only |
| Video summarization | Frame sampling + GPT-4V or Gemini | Sample key frames, not every frame |
| Long video analysis (full film) | Gemini 1.5 Pro | 1M context handles it |
| Multi-modal RAG (docs + images) | CLIP for images, text-embedding for text, RRF | Separate embeddings, fused ranking |
| Chart / graph interpretation | GPT-4V or Claude 3 (high detail) | Visual reasoning over data visualizations |
