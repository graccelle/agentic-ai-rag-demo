from rag.embedder import Embedder
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from agent.agent_core import Agent

def main():
    embedder = Embedder()
    store = VectorStore("data/sample_docs")
    retriever = Retriever(embedder, store)
    agent = Agent(retriever=retriever)

    query = "Summarize the documents."
    print("Query:", query)
    print("\nAgent Response:\n")
    print(agent.run(query))

if __name__ == "__main__":
    main()
