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

from ollama import chat

question = input("Ask me anything: ")

response = chat(
    model="qwen2.5-coder:7b",
    messages=[
        {
            "role":"user",
            "content": question
        }
    ]
)

print("\nAI:\n")
print(response["message"]["content"])