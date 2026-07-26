from tools.calculator import calculate
from tools.rag_tool import search_knowledge_base

def run_agent(question):
    if any(op in question for op in ["+","-","*","/"]):
        expression = (
            question
            .replace("what is", "")
            .replace("?","")
            .strip()
        )
        return calculate(expression)
    return search_knowledge_base(question)