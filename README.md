# Agentic AI RAG Demo (No API Key Required)

[![Build Status](https://img.shields.io/badge/build-passing-brightgreen)]()
[![Python](https://img.shields.io/badge/python-3.10+-blue)]()
[![Repo Size](https://img.shields.io/github/repo-size/graccelle/agentic-ai-rag-demo)](https://github.com/graccelle/agentic-ai-rag-demo)
[![Last Commit](https://img.shields.io/github/last-commit/graccelle/agentic-ai-rag-demo)](https://github.com/graccelle/agentic-ai-rag-demo/commits/main)
[![Code Style: Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![License: MIT](https://img.shields.io/badge/license-MIT-purple)](LICENSE)
[![Streamlit App](https://img.shields.io/badge/app-Streamlit-ff4b4b?logo=streamlit)](#streamlit-demo)

A lightweight demonstration of **agentic-style reasoning** combined with a simple **Retrieval-Augmented Generation (RAG)** pipeline,
implemented entirely with **local embeddings and vector search** (no external LLM or API keys required).

This repo is designed as a portfolio project to show:

- Agent-like reasoning over documents  
- Embedding & vector search (SBERT + FAISS)  
- Clean, modular Python code  
- A minimal Streamlit UI for interactive exploration  

---

## 🔧 High-Level Architecture Diagram

```mermaid
flowchart TD
    Q[User Query] --> A[Agent Core]
    A --> R[Retriever]
    R --> E[Embedder - SBERT Model]
    E --> VS[Vector Store - FAISS]
    VS --> R
    R --> D[Top-k Retrieved Documents]
    D --> A
    A --> S[Local Summarizer]
    S --> O[Final Answer]
```

---

## 📜 UML Sequence Diagram (Agent + RAG)

```mermaid
sequenceDiagram
    participant User
    participant Agent
    participant Retriever
    participant Embedder
    participant VectorStore
    participant Summarizer

    User->>Agent: run(query)
    Agent->>Retriever: retrieve(query)
    Retriever->>Embedder: embed([query])
    Embedder-->>Retriever: query_embedding
    Retriever->>VectorStore: search(query_embedding, k)
    VectorStore-->>Retriever: doc_indices
    Retriever-->>Agent: docs
    Agent->>Summarizer: summarize(docs)
    Summarizer-->>Agent: summary
    Agent-->>User: final response
```

---

## 🎯 Key Features

- **Agentic Core** – Simple agent orchestrator that decides: _retrieve → summarize_.  
- **RAG Components** – Embedder, vector store, and retriever built with `sentence-transformers` + `faiss`.  
- **Local Summarizer** – Deterministic, purely local heuristic summarizer (no external API).  
- **Streamlit UI** – Quick way to interact with the agent and inspect behavior.  

---

## 📁 Repository Structure

```text
agentic-ai-rag-demo/
│
├── README.md
├── requirements.txt
│
├── src/
│   ├── app.py                # CLI entrypoint
│   ├── rag/
│   │   ├── embedder.py       # Embedding model wrapper
│   │   ├── vector_store.py   # FAISS vector index
│   │   └── retriever.py      # Retrieval logic
│   └── agent/
│       ├── agent_core.py     # Orchestrating "agent"
│       └── tools.py          # Local summarizer tool
│
├── streamlit_app/
│   └── app.py                # Streamlit UI
│
├── data/
│   └── sample_docs/
│       └── sample_1.txt
│
└── notebooks/
    └── demo.ipynb            # Walkthrough notebook
```

---

## 🛠️ Installation

```bash
pip install -r requirements.txt
```

---

## ▶️ CLI Demo

```bash
python src/app.py
```

---

## 🌐 Streamlit Demo

<a name="streamlit-demo"></a>

```bash
streamlit run streamlit_app/app.py
```

You will get a simple web UI where you can:
- Type a question  
- Run the local agent  
- See how relevant chunks are summarized  

---

## 🧪 What This Demonstrates

- Basic **agentic reasoning pattern**: break a task into retrieval + summarization.  
- A working **RAG pipeline**: embeddings → FAISS → top-k docs.  
- No reliance on external proprietary models – everything runs locally.  
- Engineering practices appropriate for a small but realistic ML prototype.  

---

## 🧑‍💻 Tech Stack

- Python 3.10+  
- [sentence-transformers](https://www.sbert.net/)  
- [FAISS](https://github.com/facebookresearch/faiss)  
- [Streamlit](https://streamlit.io/)  

---

## 📄 License

This project is licensed under the MIT License.

---

## 👤 Author

**Grace Babalola**  
GitHub: [@graccelle](https://github.com/graccelle)
