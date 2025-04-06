# 🧠 Multi-User Document Search & Q&A System with Local Language Model (Offline RAG)

This project is developed as part of the **Associate Architect interview at Quantiphi**. It demonstrates a modular, secure, and scalable **Retrieval-Augmented Generation (RAG)** system that allows users to query and converse with enterprise documents **locally**, without relying on any external APIs or internet connectivity.

## 🎯 Problem Statement

Organizations often deal with sensitive documents (e.g., financial reports, contracts) that must be queried intelligently without compromising security or data access control. This system solves that by:

- Allowing users to ask natural language questions
- Restricting responses to only those documents they are authorized to access
- Generating responses using a **local language model** (e.g., Falcon, Flan-T5)
- Preserving chat history for context continuity

## 🛠️ Tech Stack

| Layer          | Technology                            |
|----------------|----------------------------------------|
| Embedding      | `SentenceTransformers (MiniLM)`        |
| Vector Search  | `FAISS`                                |
| Language Model | `HuggingFace Transformers (offline)`   |
| Backend Logic  | `Python`, `pickle`                     |
| Frontend       | `Streamlit`                            |

## 🧩 Features

- 🔐 Per-user document access control using email-to-company mapping.
- 🧠 Semantic search on document chunks via FAISS.
- 💬 Local LLM-based response generation (RAG).
- 📂 Chat history memory per user session.
- ⚙️ Offline-only, privacy-first design.

## 🗂️ Project Structure

multiuser-doc-search/
├── app.py                    # Streamlit frontend
├── scripts/
│   ├── preprocess_docs.py    # Extracts text, chunks and indexes
│   ├── access_control.py     # Email-based access check
│   └── query_handler.py      # Vector search + local LLM inference
├── users/
│   └── user_access.json      # Maps email to company access
├── data/raw_pdfs/            # Upload your PDFs here
├── embeddings/faiss_index/   # Output of document embedding
├── chat_context/             # Saved conversation history
├── requirements.txt
└── README.md

## ⚙️ Setup Instructions

1. Clone & Install Requirements
```bash
git clone https://github.com/yourusername/multiuser-doc-search.git
cd multiuser-doc-search
pip install -r requirements.txt
```

2. Add PDFs
Place earnings reports or internal documents in:
```
data/raw_pdfs/
```

3. Preprocess Documents
```bash
cd scripts
python preprocess_docs.py
cd ..
```

4. Run the App
```bash
streamlit run app.py
```

## 👥 Example Users (Simulated)

| Email              | Companies Accessed     |
|--------------------|------------------------|
| alice@email.com    | Meta                   |
| bob@email.com      | JPMorgan, AT&T         |
| charlie@email.com  | Citi, Walmart          |

Defined in `users/user_access.json`

## 🧠 Sample Usage

1. Login with a test email (e.g. alice@email.com)
2. Ask: “What was Meta’s Q4 revenue?”
3. System:
   - Retrieves matching content from Meta-only documents
   - Generates an answer using the local language model
   - Saves the Q&A in chat history

## 🏗️ Architectural Principles

- Modularized folders: easy to swap in OpenAI, Pinecone, LangChain, etc.
- Security-aware: enforces user-level data access
- Offline-first: works in private environments with no internet
- Scalable: easily extendable to multiple users, cloud deployment

## 🚀 Future Enhancements

- OAuth2 authentication (instead of plain email)
- Docker containerization
- Streamlit Cloud or private Kubernetes deployment
- Support for image/PDF OCR extraction
- Integration with ElasticSearch or Pinecone for enterprise scale

## 📬 Author

**Sai Lalitha**  
🎓 MSc in Control Systems & Microelectronics  
💼 For Quantiphi's Associate Architect interview


