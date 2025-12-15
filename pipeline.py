from .embeddings import embed
from .retriever import retrieve
from .generator import generate_answer

def run_rag(query):
    q = embed(query)
    docs = retrieve(q)
    return generate_answer(query, docs)
