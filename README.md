# 🚀 Multimodal RAG Assistant

A production-style **Multimodal Retrieval-Augmented Generation (RAG)** system built with **FastAPI, React, Ollama, ChromaDB, and SQLModel**.

The application allows users to upload documents, create chat sessions, attach specific documents to each session, and ask questions grounded only in the selected documents using a hybrid retrieval pipeline.

---

## ✨ Features

### 📄 Multimodal Document Processing

- PDF text extraction
- OCR for scanned documents
- Table extraction
- Image extraction
- Image caption generation
- Intelligent document chunking

### 🔍 Advanced Retrieval Pipeline

- Vector Search (ChromaDB)
- BM25 Keyword Search
- Reciprocal Rank Fusion (RRF)
- Cross-Encoder Reranking
- Query Rewriting
- Session-aware Retrieval

### 💬 AI Chat

- Streaming responses
- Conversation history
- Source citations
- Multiple chat sessions
- Context-aware answers

### 📂 Document Management

- Upload documents
- Preview documents
- Delete documents
- ChromaDB synchronization
- Session document attachment
- Add/remove documents from existing sessions

---

# 🏗 Architecture

```text
                    +----------------+
                    | React Frontend |
                    +--------+-------+
                             |
                             v
                     FastAPI Backend
                             |
        +--------------------+--------------------+
        |                    |                    |
        v                    v                    v
 Document Pipeline     Session Manager      Chat Service
        |                    |                    |
        |                    |                    |
        v                    |                    |
 OCR • Tables • Images       |                    |
        |                    |                    |
        v                    |                    |
 Chunking & Metadata          |                    |
        |                    |                    |
        +---------+----------+                    |
                  |                               |
                  v                               |
         Embedding Generation                     |
                  |                               |
                  v                               |
             ChromaDB Vector Store                |
                  |                               |
                  +---------------+---------------+
                                  |
                                  v
                         Hybrid Retrieval
                   (Vector + BM25 + RRF)
                                  |
                                  v
                      Cross Encoder Reranker
                                  |
                                  v
                           Ollama LLM
                                  |
                                  v
                          Streaming Answer
```

---

# 🛠 Tech Stack

## Frontend

- React
- Vite
- Tailwind CSS
- Axios
- React Hot Toast

## Backend

- FastAPI
- SQLModel
- SQLite
- ChromaDB
- Ollama
- Sentence Transformers

## AI Models

- Llama 3.2 (Ollama)
- nomic-embed-text
- BLIP Image Captioning
- Cross Encoder (MS MARCO MiniLM)

---

# 📁 Project Structure

```text
backend/
│
├── api/
├── captioning/
├── database/
├── embeddings/
├── llm/
├── loaders/
├── processing/
├── rag/
├── retrieval/
│   ├── vector/
│   ├── keyword/
│   ├── fusion/
│   └── reranker/
├── services/
├── vectordb/
└── app.py

frontend/
│
├── components/
├── hooks/
├── pages/
├── services/
└── App.jsx
```

---

# ⚙ Installation

## Clone

```bash
git clone https://github.com/VardaanThakur-1902/multimodal-rag.git
cd multimodal-rag
```

---

## Backend

```bash
cd backend

conda create -n multimodal-rag python=3.11

conda activate multimodal-rag

pip install -r requirements.txt

uvicorn app:app --reload
```

---

## Frontend

```bash
cd frontend

npm install

npm run dev
```

---

## Ollama

Install Ollama.

Pull the required models.

```bash
ollama pull llama3.2:3b

ollama pull nomic-embed-text
```

---

# 🚀 How It Works

1. Upload one or more documents.
2. Documents are processed into:
   - Text
   - Tables
   - Images
3. Images are captioned.
4. All content is chunked.
5. Chunks are embedded into ChromaDB.
6. Create a chat session.
7. Attach relevant documents.
8. Ask questions.
9. Hybrid Retrieval searches only attached documents.
10. The LLM generates grounded responses with citations.

---


# 🔍 Retrieval Pipeline

```text
User Question
      │
      ▼
Query Rewriting
      │
      ▼
Vector Search
      │
      ▼
BM25 Search
      │
      ▼
Reciprocal Rank Fusion
      │
      ▼
Cross Encoder Reranking
      │
      ▼
Top Chunks
      │
      ▼
Ollama
      │
      ▼
Answer + Citations
```

---

# 🌟 Future Improvements

- User authentication
- Multi-user support
- Document collections
- Audio transcription
- Video understanding
- Agentic workflows
- Cloud deployment
- Semantic caching

---

# 👨‍💻 Author

**Vardaan Thakur**

If you found this project helpful, consider giving it a ⭐ on GitHub.