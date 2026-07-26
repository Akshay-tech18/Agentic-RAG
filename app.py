# from ollama import chat

# response = chat(
#     model = "qwen2.5-coder:7b",
#     messages=[
#         {
#             "role":"user",
#             "content":"what is python?"
#         }
#     ]
# )

# print(response["message"]["content"])

# from ollama import chat

# question = input("Ask me anything: ")

# response = chat(
#     model="qwen2.5-coder:7b",
#     messages=[
#         {
#             "role":"user",
#             "content": question
#         }
#     ]
# )

# print("\nAI:\n")
# print(response["message"]["content"])

# from ollama import chat

# messages = []

# print("=" * 40)
# print("     Local AI assistant")
# print("=" * 40)

# while True:
#     question = input("\n You: ")

#     if question.lower() == "exit":
#         print("\nGoodBye!")
#         break

#     messages.append(
#         {
#             "role":"user",
#             "content": question
#         }
#     )

#     response = chat(
#         model="qwen2.5-coder:7b",
#         messages=messages
#     )

#     answer = response["message"]["content"]
#     print("\nAI: ")
#     print(answer)

#     messages.append(
#         {
#             "role":"assistant",
#             "content": answer
#         }
#     )

# from ollama import chat

# messages=[
#     {
#         "role":"system",
#         "content":"""
# you are an AI teacher.
# explain concepts simply.
# use real-life examples.
# keep answer under 150 words.
# if appropriate, end with one short quize question.
# """
#     }
# ]

# print("=" * 50)
# print("     AI teacher")
# print("=" * 50)

# while True:
#     question = input("\nYou: ")

#     if question.lower() == "exit":
#         break

#     messages.append(
#         {
#             "role":"user",
#             "content":question
#         }
#     )

#     response = chat(
#         model="qwen2.5-coder:7b",
#         messages=messages
#     )

#     answer = response["message"]["content"]

#     print("\n Teacher \n")
#     print(answer)

#     messages.append(
#         {
#             "role":"user",
#             "content":answer
#         }
#     )

from rag import ask

while True:
    question = input("\nAsk: ")
    if question.lower() == "exit":
        break
    result = ask(question)
    # print("\n Answer: \n")
    # print(answer)
    print("\n Answer \n")
    print(result["answer"])
    print("\nSources: ")
    for s in result["sources"]:
        print(f"- {s}")