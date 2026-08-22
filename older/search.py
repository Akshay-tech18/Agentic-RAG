import chromadb
from ollama import embeddings
client = chromadb.PersistentClient(
    path="vectordb"
)

collection = client.get_collection(
    name="college_rules"
)

question = "How many books can students borrow?"
question_embedding = embeddings(
    model="nomic-embed-text",
    prompt=question
)["embedding"]

results = collection.query(
    query_embeddings=[question_embedding],
    n_results=3
)

print(results.keys())
print("\n")
print(results["documents"])
print("\n")
print(results["metadatas"])
print("\n")
print(results["distances"])

