class Retriever:
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.store = vector_store
        self._init_index()

    def _init_index(self):
        emb = self.embedder.embed(self.store.docs)
        self.store.build_index(emb)

    def retrieve(self, query, k=3):
        q = self.embedder.embed([query])
        idxs = self.store.search(q, k)
        return [self.store.docs[i] for i in idxs]
