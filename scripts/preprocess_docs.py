import os
import fitz  # PyMuPDF
from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pickle

DATA_DIR = "../data/raw_pdfs"
EMBED_DIR = "../embeddings/faiss_index"
CHUNK_SIZE = 500

def read_pdf_text(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def chunk_text(text, chunk_size=CHUNK_SIZE):
    words = text.split()
    return [" ".join(words[i:i+chunk_size]) for i in range(0, len(words), chunk_size)]

def process_all_pdfs():
    model = SentenceTransformer('all-MiniLM-L6-v2')
    corpus = []
    metadata = []
    for filename in os.listdir(DATA_DIR):
        if filename.endswith(".pdf"):
            company = filename.split("_")[0]
            text = read_pdf_text(os.path.join(DATA_DIR, filename))
            chunks = chunk_text(text)
            for chunk in chunks:
                corpus.append(chunk)
                metadata.append(company)
    embeddings = model.encode(corpus, convert_to_tensor=False)
    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))
    os.makedirs(EMBED_DIR, exist_ok=True)
    faiss.write_index(index, os.path.join(EMBED_DIR, "index.faiss"))
    with open(os.path.join(EMBED_DIR, "corpus.pkl"), "wb") as f:
        pickle.dump((corpus, metadata), f)

if __name__ == "__main__":
    process_all_pdfs()
