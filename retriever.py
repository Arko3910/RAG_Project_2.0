import faiss
import numpy as np

index = faiss.IndexFlatL2(384)
documents = []

def add_document(text, embedding):
    index.add(np.array([embedding]))
    documents.append(text)

def retrieve(query_embedding, k=3):
    if index.ntotal == 0:
        return []
    _, I = index.search(np.array([query_embedding]), k)
    return [documents[i] for i in I[0]]
