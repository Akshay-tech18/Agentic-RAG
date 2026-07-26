# import chromadb
# from ollama import chat, embeddings

# client = chromadb.PersistentClient(
#     path="vectordb"
# )

# collection = client.get_collection(
#     "college_rules"
# )

# def rerank(question, documents):
#     """
#     this is the very simple lexical reranker
#     later this will we replaced by the a AI reranker
#     """

#     question_words = set(question.lower().split())

#     scores = []

#     for doc in documents:
#         doc_words = set(doc.lower().split())
#         overlap = len(question_words & doc_words)
#         scores.append((overlap, doc))
#     scores.sort(reverse=True)
#     return [doc for _, doc in scores]

# question = input("Ask a question : ")

# question_embedding = embeddings(
#     model="nomic-embed-text",
#     prompt=question
# )["embedding"]

# results = collection.query(
#     query_embeddings = [question_embedding],
#     n_results = 10
# )

# documents = results["documents"][0]
# documents = rerank(question, documents)
# documents = documents[:3]

# context = "\n\n".join(documents)

# prompt = f"""
# You are an AI assistant

# Answer only using the context below
# If answer is not present in the context
# Say: "I dont have enough Information"

# context : {context}
# Question : {question}

# Answer : 
# """

# response = chat(
#     model = "qwen2.5-coder:7b",
#     messages=[
#         {
#             "role":"user",
#             "content":prompt
#         }
#     ]
# )

# print("\nAnswer:\n")
# print(response["message"]["content"])

from retriever import retrieve
from reranker import reranker
from prompt_builder import build_prompt
from llm import generate_answer
from config import FINAL_K
from memory import (add_message, get_history)
from query_rewriter import rewrite_query

def ask(question):
    history = get_history()
    rewritten_question = rewrite_query(question, history)
    print("\nRewritten Query: ")
    print(rewritten_question)
    documents, metadata, distances = retrieve(rewritten_question)
    ranked = reranker(rewritten_question, documents, metadata, distances)
    ranked = ranked[:FINAL_K]
    documents = [item[1] for item in ranked]
    context = "\n\n".join(documents)
    prompt = build_prompt(question, context,history)
    answer = generate_answer(prompt)
    # print("\nSources\n")
    # for item in ranked:
    #     meta = item[2]
    #     print(
    #         f"- {meta['source']}"
    #         f"(Chunk {meta['chunk']})"
    #     )
    sources = []
    for item in ranked:
        meta = item[2]
        source = (
            f"{meta['source']} "
            f"(Chunk {meta['chunk']})"
        )
        if source not in sources:
            sources.append(source)
    add_message("user",question)
    add_message("assistant", answer)
    return {
        "answer": answer,
        "sources": sources
    }