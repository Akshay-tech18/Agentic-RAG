import numpy as np
from ollama import embeddings

model = "nomic-embed-text"

question = "How many books can students borrow?"

chunks = [
    "Students can borrow up to three books. ",
    "Hostel closes at 9 PM.",
    "Electronic gadgets are prohibited."
]

question_vector = embeddings(
    model = model,
    prompt = question
)["embedding"]

scores = []

for chunk in chunks:
    chunk_vector = embeddings(
        model = model,
        prompt = chunk
    )["embedding"]

    similarity = np.dot(question_vector, chunk_vector) / (
        np.linalg.norm(question_vector) * 
        np.linalg.norm(chunk_vector)
    )

    scores.append((chunk, similarity))

scores.sort(key=lambda x: x[1], reverse=True)

print("\nSimilarity Results:\n")

for chunk, score in scores:
    print(f"{score:.4f} --> {chunk}")