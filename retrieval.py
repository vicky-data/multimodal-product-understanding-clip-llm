import faiss
import numpy as np

dimension = 512
index = faiss.IndexFlatL2(dimension)

def add_embeddings(embeddings):
    index.add(np.array(embeddings))

def search(query_embedding, k=3):
    distances, indices = index.search(np.array([query_embedding]), k)
    return indices
