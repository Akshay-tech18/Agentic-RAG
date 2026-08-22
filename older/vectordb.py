import chromadb

client = chromadb.PersistentClient(path="vectordb")

collection = client.get_or_create_collection(
    name="college_rules"
)

print("Database Created Successfully")
