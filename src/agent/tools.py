def local_summarizer(docs):
    """Very simple local summarizer that truncates text to the first N words."""
    combined = " ".join(docs)
    words = combined.split()
    max_words = 80
    snippet = " ".join(words[:max_words])
    return f"Local Summary (no external LLM used): {snippet}..."
