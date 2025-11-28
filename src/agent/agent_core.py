from agent.tools import local_summarizer

class Agent:
    def __init__(self, retriever):
        self.retriever = retriever

    def run(self, query: str):
        docs = self.retriever.retrieve(query)
        return local_summarizer(docs)
