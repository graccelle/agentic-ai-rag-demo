import os, faiss, numpy as np

class VectorStore:
    def __init__(self, folder):
        self.folder = folder
        self.docs = self._load_docs()
        self.index = None

    def _load_docs(self):
        docs = []
        for fname in os.listdir(self.folder):
            with open(os.path.join(self.folder, fname),'r',encoding='utf-8') as f:
                docs.append(f.read())
        return docs

    def build_index(self, embeddings):
        dim = embeddings.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeddings)
        self.index = index

    def search(self, query_emb, k=3):
        distances, idx = self.index.search(query_emb, k)
        return idx[0]
