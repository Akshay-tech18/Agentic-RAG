# from ollama import chat
# from config import LLM_MODEL

# def choose_tool(question):
#     prompt = f"""
# You are an AI Planner.
# Available tools:
# 1.Calculator
# Use for arithmetic
# 2.rag
# Use for answering questions
# from the knowledge base

# Question: {question}
# Return ONLY one word.
# calculator or rag
# """

#     response = chat(
#         model = LLM_MODEL,
#         messages=[
#             {
#                 "role":"user",
#                 "content":prompt
#             }
#         ]
#     )

#     return response["message"]["content"].strip().lower()

# from ollama import chat
# from config import LLM_MODEL


# def choose_tool(question):

#     prompt = f"""
# You are an AI planner.

# Available tools:

# calculator
# - Mathematical expressions
# - Arithmetic
# - Multiplication
# - Division
# - Addition
# - Subtraction

# rag
# - Questions about the knowledge base
# - Documents
# - Policies
# - Rules

# Examples:

# Question:
# 12 + 8

# Tool:
# calculator

# Question:
# What is the hostel curfew?

# Tool:
# rag

# Question:
# 25 * 7

# Tool:
# calculator

# Question:

# {question}

# Return ONLY:

# calculator

# or

# rag
# """

#     response = chat(

#         model=LLM_MODEL,

#         messages=[
#             {
#                 "role":"user",
#                 "content":prompt
#             }
#         ]
#     )

#     return response["message"]["content"].strip().lower()

import json

from ollama import chat

from config import LLM_MODEL


def create_plan(question):

    prompt = f"""
You are an AI planner.

Available tools:

calculator

Arguments:
expression

rag

Arguments:
query

Return ONLY valid JSON.

Examples

Question:

25 * 8

Output:

{{
"tool":"calculator",
"arguments":{{
"expression":"25*8"
}}
}}

------------------

Question:

What is the hostel curfew?

Output:

{{
"tool":"rag",
"arguments":{{
"query":"What is the hostel curfew?"
}}
}}

------------------

Question:

{question}
"""

    response = chat(

        model=LLM_MODEL,

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ]
    )

    text = response["message"]["content"]

    # return json.loads(text)
    try:

        # return json.loads(text)
        plan = json.loads(text)
        return plan

    except Exception:

        return {

            "tool":"rag",

            "arguments":{

                "query":question

            }
        }


# import json
# import re
# from ollama import chat
# from config import LLM_MODEL


# def choose_tool(question):
#     prompt = f"""
# You are an AI planner.

# Available tools:

# calculator
# Arguments: expression

# rag
# Arguments: query

# Return ONLY valid JSON.

# Examples:

# Question:
# 25 * 8

# Output:
# {{
#   "tool": "calculator",
#   "arguments": {{
#     "expression": "25*8"
#   }}
# }}

# ------------------

# Question:
# What is the hostel curfew?

# Output:
# {{
#   "tool": "rag",
#   "arguments": {{
#     "query": "What is the hostel curfew?"
#   }}
# }}

# ------------------

# Question:
# {question}
# """

#     response = chat(
#         model=LLM_MODEL,
#         messages=[
#             {
#                 "role": "user",
#                 "content": prompt,
#             }
#         ],
#         format="json",  # 1. Forces Ollama to output valid JSON
#     )

#     text = response.message.content if hasattr(response, "message") else response["message"]["content"]

#     match = re.search(r"\{.*\}", text, re.DOTALL)
#     clean_text = match.group(0) if match else text.strip()

#     try:
#         return json.loads(clean_text)
#     except json.JSONDecodeError as e:
#         print(f"\n[Planner Error] Could not parse LLM output. Raw string was:\n{text}\n")
#         raise e