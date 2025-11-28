def local_summarizer(docs):
    text = " ".join(docs)
    words = text.split()
    summary = " ".join(words[:60])
    return f"Local Summary (no LLM required): {summary}..."
