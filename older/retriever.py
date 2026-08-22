import chromadb
from ollama import embeddings

from older.config import (
    DB_PATH,
    COLLECTION_NAME,
    EMBEDDING_MODEL,
    TOP_K
)

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_collection(COLLECTION_NAME)

def retrieve(question):
    question_embedding = embeddings(
        model = EMBEDDING_MODEL,
        prompt=question
    )["embedding"]

    results = collection.query(
        query_embeddings=[
            question_embedding
        ],
        n_results=TOP_K
    )

    documents = results["documents"][0]
    metadata = results["metadatas"][0]
    distances = results["distances"][0]
    return documents, metadata, distances