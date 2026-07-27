from llm import generate_answer

def summarise(text):
    prompt = f"""
Summarise the following text.
{text}
"""
    return generate_answer(prompt)