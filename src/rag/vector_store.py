import os
import faiss
import numpy as np

class VectorStore:
    def __init__(self, folder: str):
        self.folder = folder
        self.docs = self._load_docs()
        self.index = None

    def _load_docs(self):
        docs = []
        for fname in os.listdir(self.folder):
            full_path = os.path.join(self.folder, fname)
            if os.path.isfile(full_path):
                with open(full_path, "r", encoding="utf-8") as f:
                    docs.append(f.read())
        return docs

    def build_index(self, embeddings):
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings.astype(np.float32))
        self.index = index

    def search(self, query_embedding, k: int = 3):
        distances, indices = self.index.search(query_embedding.astype(np.float32), k)
        return indices[0]
