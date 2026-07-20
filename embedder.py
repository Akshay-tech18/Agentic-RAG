# from ollama import embeddings

# response = embeddings(
#     model="nomic-embed-text",
#     prompt="students can borrow three book."
# )

# vector = response["embedding"]

# print(type(vector))
# print(len(vector))

# print(vector[:10])

from ollama import embeddings

sentences = [
    "Students can borrow three books.",
    "Hostel closes at 9pm.",
    "electronic gadgets are prohibited."
]

for sentence in sentences:
    response = embeddings(
        model="nomic-embed-text",
        prompt=sentence
    )

    vector = response["embedding"]
    print(sentence)
    print()
    print("vector length: ", len(vector))
    print("first five values")
    print(vector[:5])
    print()