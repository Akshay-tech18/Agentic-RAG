from ollama import chat
from older.config import LLM_MODEL

def generate_answer(prompt):
    response = chat(
        model = LLM_MODEL,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response["message"]["content"]