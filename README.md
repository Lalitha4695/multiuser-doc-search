# 🧠 Multi-User Document Search with Local Language Model (Offline RAG)

A secure, offline, and user-aware document retrieval and Q&A system developed as part of the **Associate Architect role interview at Quantiphi**. This project demonstrates how semantic search and local language models can be combined to power intelligent enterprise search solutions without relying on external APIs.

---

## 🚀 Features

- 🔐 Per-user document access control
- 🧠 Semantic search using FAISS + SentenceTransformers
- 💬 Local model-based answer generation (Flan-T5)
- 🖥️ Interactive UI with Streamlit
- 📦 Fully offline (no API keys or internet)

---

## 🛠️ Tech Stack

| Component       | Technology                    |
|-----------------|-------------------------------|
| Embeddings      | SentenceTransformers (MiniLM) |
| Vector Search   | FAISS                         |
| Language Model  | HuggingFace Flan-T5 (local)   |
| UI              | Streamlit                     |
| Storage         | Pickle-based chat memory      |

---

## 🗂️ Project Structure

```
multiuser-doc-search/
├── app.py                    # Streamlit frontend
├── requirements.txt          # Dependencies list
├── README.md                 # Project overview
│
├── scripts/
│   ├── preprocess_docs.py    # PDF to chunks + embeddings
│   ├── access_control.py     # Email → company access mapping
│   └── query_handler.py      # RAG logic with Flan-T5 model
│
├── users/
│   └── user_access.json      # Static user access control
│
├── data/
│   └── raw_pdfs/             # Input PDF documents
│
├── embeddings/
│   └── faiss_index/          # Stores FAISS index + corpus.pkl
│
└── chat_context/
    └── history_store.pkl     # Saved chat logs per user
```

---

## ⚙️ How to Run Locally

1. **Install Dependencies**
```bash
pip install -r requirements.txt
```

2. **Add Documents**
Place your PDFs inside:
```
data/raw_pdfs/
```

3. **Preprocess for Search**
```bash
cd scripts
python preprocess_docs.py
```

4. **Launch the App**
```bash
cd ..
streamlit run app.py
```

---

## 👤 Demo Users

| Email              | Accessible Companies     |
|--------------------|--------------------------|
| alice@email.com    | Meta                     |
| bob@email.com      | JPMorgan, AT&T           |
| charlie@email.com  | Citi, Walmart            |

---

## 🧠 Sample Interaction

1. User logs in with their email
2. Enters query like: _“What was Meta's Q4 revenue?”_
3. The system:
   - Retrieves relevant passages (if accessible)
   - Sends them to Flan-T5 for response generation
   - Displays the result and saves it in chat history

---

## 📦 Future Ideas

- Replace static JSON with dynamic user authentication
- Containerize with Docker
- Add OCR layer for image-based PDFs
- Switch to scalable vector DB (Pinecone, Weaviate)
- LLM orchestration via LangChain or LlamaIndex

---

## 🧑‍💼 Author

**Sai Lalitha Ponugupati**  
Developed for the Associate Architect interview at **Quantiphi**