import os
import faiss
import pickle
import torch
from sentence_transformers import SentenceTransformer
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
from scripts.access_control import get_user_access

# Set paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EMBED_DIR = os.path.join(BASE_DIR, "embeddings", "faiss_index")
CHAT_STORE = os.path.join(BASE_DIR, "chat_context", "history_store.pkl")

# Load a lightweight, encoder-decoder local model (Flan-T5)
MODEL_NAME = "google/flan-t5-base"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSeq2SeqLM.from_pretrained(MODEL_NAME)
model.eval()

# Load vector index and corpus
model_embed = SentenceTransformer('all-MiniLM-L6-v2')

with open(os.path.join(EMBED_DIR, "corpus.pkl"), "rb") as f:
    corpus, metadata = pickle.load(f)

index = faiss.read_index(os.path.join(EMBED_DIR, "index.faiss"))

try:
    with open(CHAT_STORE, 'rb') as f:
        chat_history = pickle.load(f)
except:
    chat_history = {}

# Generate answer from local encoder-decoder model
def generate_answer_with_local_model(context_chunks, query):
    context = "\n\n".join(context_chunks)
    prompt = f"""Use the following excerpts to answer the question:

{context}

Question: {query}

If the information in the excerpts is insufficient to fully answer the question, acknowledge this in your response.
"""

    inputs = tokenizer(prompt, return_tensors="pt", truncation=True, max_length=1024)
    with torch.no_grad():
        outputs = model.generate(**inputs, max_new_tokens=200)
    answer = tokenizer.decode(outputs[0], skip_special_tokens=True)

    return answer.strip()

# Main query handler
def get_response(user_email, query):
    vector = model_embed.encode([query])
    D, I = index.search(vector, 5)

    allowed_companies = get_user_access(user_email)
    context_chunks = [corpus[idx] for idx in I[0] if metadata[idx] in allowed_companies]

    if context_chunks:
        answer = generate_answer_with_local_model(context_chunks, query)
        
        # Add additional information lines
        source_info = [f"Source: {metadata[I[0][i]]}" for i in range(min(3, len(I[0]))) 
                      if I[0][i] < len(metadata) and metadata[I[0][i]] in allowed_companies]
        
        results = [
            ("Local AI Answer", answer),
            ("Additional Information", "\n".join(source_info))
        ]
    else:
        # when no relevant information is found
        results = [("Response", "Not sufficient information found in the document to answer your query.")]

    # Maintain chat history
    if user_email not in chat_history:
        chat_history[user_email] = []

    chat_history[user_email].append({"query": query, "response": results})

    os.makedirs(os.path.dirname(CHAT_STORE), exist_ok=True)
    with open(CHAT_STORE, 'wb') as f:
        pickle.dump(chat_history, f)

    return results

def get_history(user_email):
    return chat_history.get(user_email, [])
