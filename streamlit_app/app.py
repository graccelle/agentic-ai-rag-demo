import streamlit as st
from rag.embedder import Embedder
from rag.vector_store import VectorStore
from rag.retriever import Retriever
from agent.agent_core import Agent

st.title("Agentic AI RAG Demo (Local • No API Key)")

st.markdown(
    "This demo runs a tiny agent that uses embeddings + vector search to summarize local documents."
)

query = st.text_input("Ask a question about the local documents:", "Summarize the documents.")

if st.button("Run Agent"):
    embedder = Embedder()
    store = VectorStore("data/sample_docs")
    retriever = Retriever(embedder, store)
    agent = Agent(retriever=retriever)

    with st.spinner("Thinking locally..."):
        result = agent.run(query)

    st.subheader("Agent Response")
    st.write(result)
