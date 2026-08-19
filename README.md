# AI-Powered Assistant

An intelligent assistant using Retrieval-Augmented Generation (RAG) — upload documents, ask questions, get accurate answers grounded in your data.

## Features

- Upload PDF, TXT, Markdown documents
- Document chunking and vector embedding
- Semantic search across your knowledge base
- LLM-powered Q&A with source citations
- Chat history and conversation management
- REST API + web chat interface

## Tech Stack

| Component | Technology |
|---|---|
| **Backend** | Python, FastAPI |
| **LLM** | OpenAI GPT / Ollama (local) |
| **Embeddings** | sentence-transformers |
| **Vector DB** | ChromaDB |
| **Frontend** | React, TypeScript |
| **Containerization** | Docker, Docker Compose |

## Architecture

```
┌──────────────┐     ┌──────────────────────────────┐
│  Chat UI     │────▶│  FastAPI Backend              │
│  (React)     │◀────│  ├── Document Processor       │
└──────────────┘     │  ├── Embedding Generator      │
                     │  ├── RAG Pipeline             │
                     │  └── LLM Interface            │
                     └──────┬──────────┬─────────────┘
                            │          │
                     ┌──────▼───┐ ┌────▼──────┐
                     │ ChromaDB │ │ LLM       │
                     │ (vectors)│ │ (GPT/     │
                     └──────────┘ │  Ollama)  │
                                  └───────────┘
```

## How It Works

1. **Upload** → Documents are chunked into passages
2. **Embed** → Each chunk is converted to a vector embedding
3. **Store** → Vectors stored in ChromaDB
4. **Query** → User question is embedded, similar chunks retrieved
5. **Generate** → LLM generates answer using retrieved context

## API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/api/documents/upload` | Upload document |
| GET | `/api/documents` | List uploaded documents |
| POST | `/api/chat` | Ask a question |
| GET | `/api/chat/history` | Get conversation history |
| DELETE | `/api/documents/:id` | Remove document |

## Getting Started

```bash
# With Ollama (local, free)
docker-compose -f docker-compose.local.yml up

# With OpenAI
export OPENAI_API_KEY=your-key
docker-compose up

# API at http://localhost:8000
# Chat UI at http://localhost:3000
```

## Roadmap

- [x] Project setup
- [ ] Document upload & chunking
- [ ] Vector embedding pipeline
- [ ] ChromaDB integration
- [ ] RAG query pipeline
- [ ] LLM integration (OpenAI + Ollama)
- [ ] Chat API with history
- [ ] React chat interface
- [ ] Docker deployment

## License

MIT
