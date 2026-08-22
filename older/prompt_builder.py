def build_prompt(question, context, history):
    history_text = ""
    for message in history:
        history_text += (
            f"{message['role']}: "
            f"{message['content']}\n"
        )
    return f"""
You are an AI assistant.
Answer ONLY from the given context

Previous conversation:
{history_text}

Context : {context}
Instructions:
1. Answer only from the context
2.Do not invent facts.
3. If information is missing, 
say:
"I don't have enough information"
4.Be concise
Current Question : {question}
Answer : 
"""
