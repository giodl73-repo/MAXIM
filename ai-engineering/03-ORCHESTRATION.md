# 03 — LLM Orchestration Frameworks

> "LangChain is the Express.js of LLM engineering — ubiquitous, duct-tapey,
>  and you'll either use it or spend six months building something worse."

---

## The Big Picture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    LLM ORCHESTRATION LANDSCAPE                              │
│                                                                             │
│  ┌──────────────────────────────────────────────────────────────────────┐  │
│  │  YOUR APPLICATION                                                    │  │
│  │                                                                      │  │
│  │  ┌─────────────┐   ┌─────────────┐   ┌──────────────────────────┐  │  │
│  │  │  LangChain  │   │ LlamaIndex  │   │   Semantic Kernel (SK)   │  │  │
│  │  │  (general   │   │ (data +     │   │   (Microsoft, .NET/Py/   │  │  │
│  │  │  purpose)   │   │  RAG focus) │   │    JS, enterprise)       │  │  │
│  │  └─────────────┘   └─────────────┘   └──────────────────────────┘  │  │
│  │         │                 │                        │                  │  │
│  │  ┌──────┴─────────────────┴────────────────────────┴──────────────┐  │  │
│  │  │              SHARED ABSTRACTIONS                                │  │  │
│  │  │  Models  │  Prompts  │  Memory  │  Tools/Fns  │  Vector Stores │  │  │
│  │  └────────────────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────────────┘  │
│                                │                                            │
│  ┌─────────────────────────────┼──────────────────────────────────────┐    │
│  │  PROVIDERS                  │                                       │    │
│  │  Anthropic  OpenAI  Azure   │  Cohere  Ollama  HuggingFace  Bedrock│    │
│  └─────────────────────────────┴──────────────────────────────────────┘    │
└─────────────────────────────────────────────────────────────────────────────┘
```

The core value proposition of all three frameworks: **provider abstraction +
composition primitives**. Swap models without rewriting logic. Chain prompts,
tools, retrieval, and memory into pipelines. The cost: abstraction leakage,
version instability, and framework-specific mental overhead.

---

## Why Orchestration Frameworks Exist

Without a framework, a multi-step LLM pipeline looks like this:

```typescript
// Ad-hoc, no framework — what you're replacing
async function answerQuestion(question: string, docs: string[]) {
  // Step 1: embed the question
  const qEmbed = await openai.embeddings.create({ input: question, model: "text-embedding-3-small" });

  // Step 2: search vector store (custom code)
  const relevant = await pgVectorSearch(qEmbed.data[0].embedding, docs);

  // Step 3: build prompt (string concatenation)
  const context = relevant.map(d => d.content).join("\n\n");
  const prompt = `Answer based on context:\n${context}\n\nQuestion: ${question}`;

  // Step 4: call model
  const response = await anthropic.messages.create({
    model: "claude-sonnet-4-6",
    messages: [{ role: "user", content: prompt }],
    max_tokens: 1024,
  });

  // Step 5: parse + return
  return response.content[0].text;
}
```

This works. For one pipeline. Orchestration frameworks standardize:
- How you define and compose these steps
- How you swap components (different embedder, different store, different model)
- How you add memory, tools, agents
- How you trace and debug what happened

---

## LangChain

LangChain is the oldest and most widely used LLM framework. Started in Python (2022),
then TypeScript/JS port. Heavily influenced by LlamaIndex; now large surface area.

### Core Concepts

```
┌─────────────────────────────────────────────────────────────────────┐
│  LANGCHAIN PRIMITIVES                                               │
│                                                                     │
│  ChatModel    — model abstraction (Claude, GPT-4o, Gemini, etc.)   │
│  PromptTemplate — parameterized prompt with {variable} slots       │
│  Chain        — pipeline: input → steps → output                   │
│  Retriever    — fetch relevant docs (vector, BM25, hybrid)          │
│  Tool         — function the LLM can call                           │
│  Memory       — persist conversation state across turns            │
│  Agent        — LLM-driven loop: think → use tool → observe        │
└─────────────────────────────────────────────────────────────────────┘
```

### LCEL — LangChain Expression Language

Modern LangChain uses LCEL, a pipe-based composition syntax.

```python
from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

# Components
model = ChatAnthropic(model="claude-sonnet-4-6")
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant. Answer concisely."),
    ("human", "{question}"),
])
parser = StrOutputParser()

# Chain: pipe operator composes components left to right
chain = prompt | model | parser

# Invoke
result = chain.invoke({"question": "What is a KV cache?"})
print(result)  # → "A KV cache stores key-value pairs from prior tokens..."

# Stream
for chunk in chain.stream({"question": "Explain RLHF"}):
    print(chunk, end="", flush=True)

# Batch (parallel)
results = chain.batch([
    {"question": "What is LoRA?"},
    {"question": "What is RAG?"},
])
```

The `|` operator is syntactic sugar for `.pipe()`. Each component implements
the Runnable interface: `invoke`, `stream`, `batch`, `astream` (async).

### RAG Chain

```python
from langchain_anthropic import ChatAnthropic
from langchain_anthropic import AnthropicEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# Setup (one-time)
embeddings = AnthropicEmbeddings()   # or OpenAIEmbeddings(), etc.
vectorstore = Chroma.from_documents(docs, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

# RAG prompt
rag_prompt = ChatPromptTemplate.from_messages([
    ("system", """Answer based on context only.
If the context doesn't contain the answer, say "I don't know."

Context:
{context}"""),
    ("human", "{question}"),
])

model = ChatAnthropic(model="claude-sonnet-4-6")

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

# RAG chain
rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | rag_prompt
    | model
    | StrOutputParser()
)

answer = rag_chain.invoke("What does the document say about pricing?")
```

`RunnablePassthrough()` is a pipe no-op — it passes the input through unchanged,
so `"question"` receives the raw user query while `"context"` gets retrieved docs.

### Memory

```python
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory

# Wrap a chain with persistent chat history
store: dict[str, InMemoryChatMessageHistory] = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

chain_with_history = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="question",
    history_messages_key="history",
)

# Each call with the same session_id gets prior conversation
r1 = chain_with_history.invoke(
    {"question": "My name is Gio"},
    config={"configurable": {"session_id": "session-1"}}
)
r2 = chain_with_history.invoke(
    {"question": "What's my name?"},
    config={"configurable": {"session_id": "session-1"}}
)
# r2 → "Your name is Gio."
```

Production note: `InMemoryChatMessageHistory` is process-local. For real
deployments, use `RedisChatMessageHistory` or `PostgresChatMessageHistory`.

### Tools and Tool Calling

```python
from langchain_core.tools import tool
from langchain_anthropic import ChatAnthropic

@tool
def get_stock_price(ticker: str) -> str:
    """Get the current stock price for a ticker symbol."""
    # Real impl would call a financial API
    return f"{ticker}: $142.50"

@tool
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email to the specified recipient."""
    # Real impl would use SMTP/SendGrid/etc.
    return f"Email sent to {to}"

# Bind tools to model
model = ChatAnthropic(model="claude-sonnet-4-6")
model_with_tools = model.bind_tools([get_stock_price, send_email])

# The model will emit tool_use blocks; LangChain handles the dispatch loop
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="chat_history"),
    ("human", "{input}"),
    MessagesPlaceholder(variable_name="agent_scratchpad"),
])

agent = create_tool_calling_agent(model, [get_stock_price, send_email], prompt)
executor = AgentExecutor(agent=agent, tools=[get_stock_price, send_email], verbose=True)

result = executor.invoke({"input": "What's Apple's stock price?", "chat_history": []})
```

### LangChain's Problems

```
┌─────────────────────────────────────────────────────────────────────┐
│  KNOWN PAIN POINTS                                                  │
│                                                                     │
│  Version churn    — v0.1 → v0.2 → v0.3 broke APIs repeatedly       │
│  Abstraction tax  — simple things require knowing 5 class names     │
│  Magic behavior   — errors surface far from their source            │
│  Dependency bloat — `langchain` pulls in hundreds of transitive deps│
│  LCEL learning curve — pipe composition is elegant but non-obvious  │
└─────────────────────────────────────────────────────────────────────┘
```

Many teams use LangChain for prototyping then extract the chains into direct API
calls for production. That's a legitimate pattern — use it as scaffolding, not
as permanent architecture, unless you need the full agent/memory machinery.

---

## LlamaIndex

LlamaIndex (originally GPT Index) has a narrower focus than LangChain: it is
purpose-built for indexing, retrieval, and building knowledge systems over your
own data. More opinionated about the retrieval problem; less opinionated about
agent orchestration.

### Core Concepts

```
┌─────────────────────────────────────────────────────────────────────┐
│  LLAMAINDEX PRIMITIVES                                              │
│                                                                     │
│  Document       — raw data (PDF, web page, DB record, etc.)        │
│  Node           — chunk of a document with metadata + embedding    │
│  Index          — organized structure over nodes (vector, keyword) │
│  Retriever      — query an index → top-k nodes                     │
│  QueryEngine    — retriever + response synthesis                   │
│  ChatEngine     — stateful conversation over an index              │
│  Pipeline       — Ingestion DAG (load → transform → embed → store) │
└─────────────────────────────────────────────────────────────────────┘
```

### Basic RAG

```python
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.llms.anthropic import Anthropic
from llama_index.embeddings.openai import OpenAIEmbedding

# Configure globally (or per-index)
Settings.llm = Anthropic(model="claude-sonnet-4-6")
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.chunk_size = 512
Settings.chunk_overlap = 64

# Load and index documents
documents = SimpleDirectoryReader("./data").load_data()
index = VectorStoreIndex.from_documents(documents)

# Query
query_engine = index.as_query_engine(similarity_top_k=4)
response = query_engine.query("What are the pricing tiers?")
print(response)
print(response.source_nodes)  # the retrieved chunks — inspect retrieval quality
```

That's it for a working RAG system. LlamaIndex handles chunking, embedding,
storage, retrieval, and synthesis. The opinionated defaults are well-tuned.

### Ingestion Pipeline

For production, use the explicit pipeline:

```python
from llama_index.core.ingestion import IngestionPipeline
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core.extractors import TitleExtractor, QuestionsAnsweredExtractor
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.vector_stores.postgres import PGVectorStore

# Persistent vector store (PostgreSQL + pgvector)
vector_store = PGVectorStore.from_params(
    database="mydb", host="localhost", port=5432,
    table_name="document_embeddings", embed_dim=1536,
)

pipeline = IngestionPipeline(
    transformations=[
        SentenceSplitter(chunk_size=512, chunk_overlap=64),
        TitleExtractor(),                  # LLM extracts title per chunk
        QuestionsAnsweredExtractor(),      # LLM generates Q&A pairs per chunk
        OpenAIEmbedding(model="text-embedding-3-small"),
    ],
    vector_store=vector_store,
)

nodes = pipeline.run(documents=documents, show_progress=True)
# Nodes now in PostgreSQL — persistent across restarts
```

`QuestionsAnsweredExtractor` is a key LlamaIndex differentiator: it uses an LLM
to generate hypothetical questions each chunk answers, then embeds those questions
alongside the chunk. At query time, your question matches against the stored
hypothetical questions → better retrieval precision.

### Sub-Question Query Engine

LlamaIndex's answer to complex multi-part questions:

```python
from llama_index.core.query_engine import SubQuestionQueryEngine
from llama_index.core.tools import QueryEngineTool

# Multiple indexes over different data sources
financials_engine = financials_index.as_query_engine()
contracts_engine = contracts_index.as_query_engine()

tools = [
    QueryEngineTool.from_defaults(financials_engine, name="financials",
        description="Financial data, revenue, costs, margins"),
    QueryEngineTool.from_defaults(contracts_engine, name="contracts",
        description="Customer contracts, terms, SLAs"),
]

# SubQuestionQueryEngine decomposes complex questions
sq_engine = SubQuestionQueryEngine.from_defaults(tools)

response = sq_engine.query(
    "Compare our revenue growth with contract renewal rates last year."
)
# Internally: generates sub-questions for each tool, synthesizes combined answer
```

### When to Use LlamaIndex vs LangChain

```
LlamaIndex excels at:
  - Complex retrieval pipelines (hybrid search, re-ranking, hypothetical embeddings)
  - Multi-document reasoning (sub-questions, agent-over-index)
  - Production ingestion pipelines with transformations
  - Structured data sources (SQL, Pandas DataFrames, APIs)

LangChain excels at:
  - General-purpose agent orchestration
  - Wide provider coverage (they wrap everything)
  - Tool-calling agents with custom tools
  - Teams already invested in LangChain ecosystem

Using both: common. LlamaIndex for retrieval layer, LangChain for agent layer.
```

---

## Semantic Kernel

Semantic Kernel (SK) is Microsoft's answer — open source, enterprise-grade, with
first-class SDKs in Python, C#, and Java. Designed for .NET shops adding AI to
existing systems, and for Azure-native deployments.

### Core Concepts

```
┌─────────────────────────────────────────────────────────────────────┐
│  SEMANTIC KERNEL PRIMITIVES                                         │
│                                                                     │
│  Kernel        — central orchestrator, holds services + plugins    │
│  Plugin        — collection of related functions (= tool namespace)│
│  KernelFunction — either a semantic function (prompt) or native fn │
│  Memory        — context store (volatile or persistent)            │
│  Planner       — generates and executes multi-step plans           │
│  Filter        — interceptor hooks (prompt, function, result)      │
└─────────────────────────────────────────────────────────────────────┘
```

### Kernel Setup and Basic Invocation (Python)

```python
import asyncio
from semantic_kernel import Kernel
from semantic_kernel.connectors.ai.anthropic import AnthropicChatCompletion
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion

kernel = Kernel()

# Add AI service (multiple services can coexist)
kernel.add_service(AnthropicChatCompletion(
    ai_model_id="claude-sonnet-4-6",
    service_id="claude",
))

# Semantic function — a prompt template registered as a callable function
summarize_fn = kernel.add_function(
    function_name="summarize",
    plugin_name="TextPlugin",
    prompt="Summarize the following in one sentence:\n\n{{$input}}",
    description="Summarize text",
)

# Invoke
async def main():
    result = await kernel.invoke(
        summarize_fn,
        input="LangChain is a Python/TypeScript framework for building LLM applications..."
    )
    print(result)

asyncio.run(main())
```

### Plugins — Native Functions

```python
from semantic_kernel.functions import kernel_function
from typing import Annotated

class StockPlugin:
    @kernel_function(description="Get the current stock price for a ticker")
    def get_price(
        self,
        ticker: Annotated[str, "The stock ticker symbol"]
    ) -> str:
        return f"{ticker}: $142.50"

    @kernel_function(description="Get recent news headlines for a company")
    def get_news(
        self,
        company: Annotated[str, "Company name or ticker"]
    ) -> str:
        return f"Latest {company} headline: Q4 earnings beat estimates."

# Register plugin
kernel.add_plugin(StockPlugin(), plugin_name="StockPlugin")

# Now the kernel can call these via tool use
```

### Auto Function Calling (Tool Calling Loop)

```python
from semantic_kernel.connectors.ai.function_choice_behavior import FunctionChoiceBehavior
from semantic_kernel.connectors.ai.anthropic import AnthropicChatPromptExecutionSettings
from semantic_kernel.contents.chat_history import ChatHistory

settings = AnthropicChatPromptExecutionSettings(
    function_choice_behavior=FunctionChoiceBehavior.Auto(),  # let model choose tools
    max_tokens=1024,
)

chat_history = ChatHistory()
chat_history.add_user_message("What's the stock price and latest news for Apple?")

service = kernel.get_service("claude")
response = await service.get_chat_message_content(
    chat_history=chat_history,
    settings=settings,
    kernel=kernel,    # kernel provides the tool catalog
)
# SK automatically handles the tool_use → tool_result → continue loop
print(response)
```

### Planner

SK's Planner is its differentiator for complex multi-step tasks: given a goal,
it generates an execution plan (JSON or XML), then executes it.

```python
from semantic_kernel.planners import FunctionCallingStepwisePlanner

planner = FunctionCallingStepwisePlanner(service_id="claude")

result = await planner.invoke(
    kernel,
    "Summarize Apple's latest news and check if the stock is up today."
)
print(result.final_answer)
print(result.chat_history)  # full reasoning trace
```

The planner uses a think-act-observe loop similar to ReAct (see 01-LLM-CONCEPTS.md).
The difference: the plan is explicit and inspectable before execution.

### SK in C# (the .NET bridge)

For the learner's .NET background — SK is a first-class .NET library:

```csharp
using Microsoft.SemanticKernel;
using Microsoft.SemanticKernel.Connectors.Anthropic;

// Build the kernel (DI-friendly)
var builder = Kernel.CreateBuilder();
builder.AddAnthropicChatCompletion(
    modelId: "claude-sonnet-4-6",
    apiKey: Environment.GetEnvironmentVariable("ANTHROPIC_API_KEY")!
);
var kernel = builder.Build();

// Invoke a prompt
var result = await kernel.InvokePromptAsync(
    "Summarize in one sentence: {{$input}}",
    new KernelArguments { ["input"] = "Semantic Kernel is Microsoft's AI orchestration framework..." }
);
Console.WriteLine(result);
```

SK integrates naturally with ASP.NET Core DI, Azure SDK, Azure OpenAI Service,
and Microsoft.Extensions.AI. If you have a .NET service and need to add LLM
capabilities, SK is the natural fit — no Python process boundary.

### Azure-Native SK Pattern

```csharp
// Azure OpenAI instead of direct Anthropic (common in enterprise)
builder.AddAzureOpenAIChatCompletion(
    deploymentName: "gpt-4o",
    endpoint: "https://my-instance.openai.azure.com/",
    apiKey: Environment.GetEnvironmentVariable("AZURE_OPENAI_KEY")!
);

// Azure AI Search as memory store
builder.AddAzureAISearchVectorStore(
    new Uri(Environment.GetEnvironmentVariable("AZURE_SEARCH_ENDPOINT")!),
    new AzureKeyCredential(Environment.GetEnvironmentVariable("AZURE_SEARCH_KEY")!)
);
```

This is the recommended pattern for enterprises on Azure — all services under
managed identity, auditable, within Azure compliance boundaries.

---

## Framework Comparison

```
┌────────────────────────────────────────────────────────────────────────┐
│                    FRAMEWORK COMPARISON                                │
├──────────────────┬────────────────┬────────────────┬───────────────── │
│                  │   LangChain    │   LlamaIndex   │ Semantic Kernel  │
├──────────────────┼────────────────┼────────────────┼─────────────────┤
│ Primary language │ Python, JS/TS  │ Python, TS     │ Python, C#, Java│
│ Origin           │ Open source    │ Open source    │ Microsoft        │
│ Focus            │ General agents │ Retrieval/RAG  │ Enterprise, .NET │
│ Abstraction      │ High (leaky)   │ Medium         │ Medium           │
│ Stability        │ Low (churn)    │ Medium         │ High             │
│ RAG quality      │ Good           │ Excellent      │ Good             │
│ Agent quality    │ Excellent      │ Good           │ Excellent        │
│ Azure integration│ Good           │ Good           │ Native           │
│ .NET support     │ None           │ None           │ First-class      │
│ Enterprise fit   │ Medium         │ Medium         │ High             │
│ Community size   │ Largest        │ Large          │ Growing          │
│ Tracing          │ LangSmith      │ LlamaTrace     │ Built-in filters │
├──────────────────┴────────────────┴────────────────┴─────────────────┤
│ VERDICT                                                               │
│ LangChain  → most ecosystem, best for general agent patterns         │
│ LlamaIndex → best retrieval pipeline, complex RAG, data-heavy        │
│ Sem Kernel → best for .NET shops, Azure-native, enterprise compliance│
└───────────────────────────────────────────────────────────────────────┘
```

---

## The Orchestration Stack in Production

```
┌─────────────────────────────────────────────────────────────────────┐
│  PRODUCTION LLM SERVICE ARCHITECTURE                                │
│                                                                     │
│  API Layer                                                          │
│  FastAPI / ASP.NET Core / Express                                   │
│       │                                                             │
│  Orchestration Layer                                                │
│  LangChain / LlamaIndex / Semantic Kernel                          │
│       │                         │                                   │
│  Retrieval Layer           Tool Layer                               │
│  pgvector / Pinecone /     REST APIs, DBs,                          │
│  Weaviate / Azure AI Search  code execution, webhooks              │
│       │                                                             │
│  Model Layer                                                        │
│  Anthropic API / Azure OpenAI / Bedrock / Ollama (local)           │
│       │                                                             │
│  Observability Layer                                                │
│  LangSmith / Braintrust / OpenTelemetry traces                     │
└─────────────────────────────────────────────────────────────────────┘
```

### The "No Framework" Option

For many production systems, the right answer is the Anthropic SDK directly:

```python
from anthropic import Anthropic

client = Anthropic()

# Tool use without a framework
tools = [
    {
        "name": "get_stock_price",
        "description": "Get the current stock price for a ticker symbol",
        "input_schema": {
            "type": "object",
            "properties": {
                "ticker": {"type": "string", "description": "Stock ticker (e.g. AAPL)"}
            },
            "required": ["ticker"]
        }
    }
]

messages = [{"role": "user", "content": "What's Apple's stock price?"}]

# Manual tool-use loop
while True:
    response = client.messages.create(
        model="claude-sonnet-4-6",
        max_tokens=1024,
        tools=tools,
        messages=messages,
    )

    if response.stop_reason == "end_turn":
        # Final text response
        print(response.content[0].text)
        break

    if response.stop_reason == "tool_use":
        # Execute tools and append results
        messages.append({"role": "assistant", "content": response.content})
        tool_results = []
        for block in response.content:
            if block.type == "tool_use":
                result = dispatch_tool(block.name, block.input)
                tool_results.append({
                    "type": "tool_result",
                    "tool_use_id": block.id,
                    "content": result,
                })
        messages.append({"role": "user", "content": tool_results})
```

This is 40 lines of explicit, debuggable, zero-dependency code. An orchestration
framework's version of this is shorter to write, harder to debug when it breaks.

**Rule of thumb**: start without a framework. Add one when you hit friction
(complex retrieval, multi-agent orchestration, memory management across sessions).

---

## Chunking and Embedding — The Foundation

These aren't framework-specific but underpin every RAG pipeline:

### Chunking Strategies

```
┌─────────────────────────────────────────────────────────────────────┐
│  CHUNKING STRATEGY         │  WHEN TO USE                          │
├────────────────────────────┼────────────────────────────────────────┤
│  Fixed size (512 tokens)   │  Baseline; fast; uniform              │
│  Sentence splitter         │  Prose documents; preserves sentences  │
│  Recursive character       │  LangChain default; tries paragraphs   │
│  Semantic (embed + cluster)│  Best quality; expensive to compute   │
│  Document structure-aware  │  PDFs with headings; HTML; Markdown   │
│  Agentic chunking          │  LLM proposes splits; highest quality │
└────────────────────────────┴────────────────────────────────────────┘

Always add overlap (e.g., 10% of chunk size) so context at chunk
boundaries doesn't get lost.
```

### Embedding Model Selection

```
┌───────────────────────────┬────────────┬───────────────────────────┐
│  Model                    │  Dim       │  Notes                    │
├───────────────────────────┼────────────┼───────────────────────────┤
│  text-embedding-3-small   │  1536      │  Good quality, cheap      │
│  text-embedding-3-large   │  3072      │  Best OpenAI quality       │
│  cohere-embed-v3-english  │  1024      │  Strong, supports search  │
│  nomic-embed-text         │  768       │  Open source, local-run   │
│  Azure AI embeddings      │  varies    │  Same models, Azure VNet  │
└───────────────────────────┴────────────┴───────────────────────────┘

Mismatching embedding models between index time and query time
is the #1 production RAG bug. Pin the model version.
```

---

## Common Confusion Points

**LangChain vs LangGraph**: LangChain is the chain/pipeline framework.
LangGraph is a separate library (by the same team) for stateful, graph-based
agent workflows with explicit state machines. LangGraph is newer and more
suitable for complex multi-agent systems. Think of LangGraph as LangChain's
attempt to add XState-style explicit state to agents.

**Semantic Kernel vs Azure OpenAI SDK**: Azure OpenAI SDK is just the raw
model API. Semantic Kernel is the orchestration layer on top. You can use
SK with the Azure OpenAI SDK underneath — that's the standard enterprise pattern.

**LlamaIndex Nodes vs LangChain Documents**: Both are "chunk with metadata" but
with different interfaces. LlamaIndex's Node has more built-in metadata fields
(relationships, source doc, score). LangChain's Document is simpler. Not compatible.

**Vector store ≠ the retrieval strategy**: Switching from Chroma to pgvector
doesn't change retrieval quality significantly. What matters is: chunk size,
overlap, embedding model, top-k, reranking, and whether you use hybrid search
(vector + BM25). The vector store is just storage.

**Temperature = 0 for agents**: For tool-calling agents, set temperature to 0.
You want deterministic tool selection, not creative interpretation of when to
call which function.

**Context window creep**: Each agent loop iteration appends more messages.
With 128K context windows, this isn't an immediate crisis, but unchecked memory
strategies will eventually push you into prompt truncation or OOM. LangChain's
`ConversationSummaryBufferMemory` compresses history when it exceeds a threshold.

---

## Decision Cheat Sheet

```
┌─────────────────────────────────────────────────────────────────────┐
│  TASK                              │  APPROACH                      │
├────────────────────────────────────┼────────────────────────────────┤
│  Simple LLM call, one step         │  SDK directly, no framework    │
│  Basic RAG over docs               │  LlamaIndex (fastest path)     │
│  Complex retrieval pipeline        │  LlamaIndex ingestion pipeline │
│  General-purpose agent             │  LangChain + AgentExecutor     │
│  Multi-agent, stateful graph       │  LangGraph                     │
│  .NET existing codebase            │  Semantic Kernel C#            │
│  Azure-native, compliance matters  │  Semantic Kernel + Azure AOAI  │
│  Custom logic, zero deps           │  SDK directly + roll your own  │
│  Tracing production calls          │  LangSmith or OTEL SDK         │
│  RAG + evals                       │  LlamaIndex + RAGAS            │
│  Prototyping fast                  │  LangChain (widest docs/stack) │
├────────────────────────────────────┼────────────────────────────────┤
│  CHUNKING                          │                                │
│  Quick prototype                   │  Fixed size, 512 + overlap 64 │
│  Production prose                  │  SentenceSplitter              │
│  Mixed structure (PDF, HTML)       │  Structure-aware + overlap     │
│  Max retrieval quality             │  Semantic chunking + HyDE      │
└────────────────────────────────────┴────────────────────────────────┘
```

---

## Connection Forward

```
01-LLM-CONCEPTS.md:   the models and primitives
02-EVALS-HARNESS.md:  how to measure quality
03-ORCHESTRATION.md:  frameworks that compose models + retrieval (this guide)
04-AGENTS.md (next):  agent patterns — the ReAct loop, tool use,
                      memory, multi-agent; what happens when you push
                      orchestration frameworks to their limits
```
