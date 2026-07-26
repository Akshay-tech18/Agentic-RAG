import chromadb
from ollama import embeddings

chunks = [

"College Library Rules",

"Students can borrow up to three books.",

"Books should be returned within fourteen days.",

"Late returns will result in a fine.",

"Hostel Rules",

"Students must return before 9 PM."
]

client = chromadb.PersistentClient(
    path="vectordb"
)

collection = client.get_or_create_collection(
    name="college_rules"
)

for index, chunk in enumerate(chunks):
    response = embeddings(
        model = "nomic-embed-text",
        prompt=chunk
    )

    vector = response["embedding"]

    collection.add(
        ids=[f"chunk_{index}"],
        documents=[chunk],
        embeddings=[vector],
        metadatas=[
            {
                "source":"college_rules.txt",
                "chunk":index
            }
        ]
    )

print("All chunks stored successfully !")

results = collection.get()
print(results.keys())
print(results["documents"])