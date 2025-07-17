import numpy as np
from typing import List, Tuple

class InMemoryVectorStore:
    def __init__(self):
        self.data = []  # List of (embedding, chunk, source_file)

    def add(self, embedding: list, chunk: str, source_file: str):
        self.data.append((np.array(embedding), chunk, source_file))

    def search(self, query_embedding: list, top_k=3) -> List[Tuple[str, str, float]]:
        query_vec = np.array(query_embedding)
        scored = []
        for emb, chunk, fname in self.data:
            score = np.dot(query_vec, emb) / (np.linalg.norm(query_vec) * np.linalg.norm(emb) + 1e-8)
            scored.append((chunk, fname, score))
        scored.sort(key=lambda x: x[2], reverse=True)
        return scored[:top_k] 