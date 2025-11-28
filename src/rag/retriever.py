class Retriever:
    def __init__(self, embedder, vector_store):
        self.embedder = embedder
        self.store = vector_store
        self._initialize_index()

    def _initialize_index(self):
        embeddings = self.embedder.embed(self.store.docs)
        self.store.build_index(embeddings)

    def retrieve(self, query: str, k: int = 3):
        query_emb = self.embedder.embed([query])
        ids = self.store.search(query_emb, k)
        return [self.store.docs[i] for i in ids]
