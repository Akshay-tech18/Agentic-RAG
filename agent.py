# from tools.calculator import calculate
# from tools.rag_tool import search_knowledge_base

# def run_agent(question):
#     if any(op in question for op in ["+","-","*","/"]):
#         expression = (
#             question
#             .replace("what is", "")
#             .replace("?","")
#             .strip()
#         )
#         return calculate(expression)
#     return search_knowledge_base(question)


# from planner import choose_tool
# from tools.calculator import calculate
# from tools.rag_tool import search_knowledge_base

# def run_agent(question):
#     tool = choose_tool(question)
#     print(f"\n Planner chose: {tool}")
#     if tool == "calculator":
#         expression = (
#             question
#             .replace("what is", "")
#             .replace("?","")
#             .strip()
#         )
#         return calculate(expression)
#     elif tool == "rag":
#         return search_knowledge_base(question)
#     return "Planner selected an unknown tool."

# from planner import choose_tool
# from tools.calculator import calculate
# from tools.rag_tool import search_knowledge_base

# def run_agent(question):
#     tool_call = choose_tool(question)
#     print("\n tool call")
#     print(tool_call)
#     tool = tool_call["tool"]
#     arguments = tool_call["arguments"]
#     if tool == "calculator":
#         expression = arguments["expression"]
#         return calculate(expression)
#     elif tool == "rag":
#         query = arguments["query"]
#         return search_knowledge_base(query)
#     return "unknown Tool."

from planner import create_plan
from tools.rag_tool import search_knowledge_base
from tools.summariser import summarise
from tools.calculator import calculate

def run_agent(question):
    plan = create_plan(question)
    print("\nExcution plan")
    print(plan)
    result = None
    for i,step in enumerate(plan,start=1):
        try:
            tool = step["tool"]
            arguments = step["arguments"]
            print(f"Running step {i} : {tool}")
            if tool == "rag":
                result = search_knowledge_base(arguments["query"])
            elif tool == "calculator":
                result = calculate(arguments["expression"])
            elif tool == "summariser":
                result = summarise(result)
        except Exception as e:
            return f"Plan failed at step {i} ({tool}) : {e}"
    return result