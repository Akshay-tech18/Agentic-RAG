def reranker(question, documents, metadata, distances):
    question_words = set(
        question.lower().split()
    )

    ranked = []

    for doc, meta, distance in zip(documents, metadata, distances):
        # doc_words = set(doc.lower().split())

        overlap = len(question_words & set(doc.lower().split()))

        ranked.append((overlap, doc, meta, distance))
    ranked.sort(reverse=True)
    return ranked
