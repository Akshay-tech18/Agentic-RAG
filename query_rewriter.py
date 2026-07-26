from ollama import chat
from config import LLM_MODEL

def rewrite_query(question, history):
    history_text = ""
    for message in history:
        history_text += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )

    prompt = f"""
You are an AI assistant.
Given the conversation history
and the lastest user question,
rewrite the lastest question into a standlone question.
Do not answer it.
Only return the rewritten question.
Conversation: {history_text}
Current Question: {question}
"""
    
    response = chat(
        model = LLM_MODEL,
        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    return response["message"]["content"].strip()