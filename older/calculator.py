def calculate(expression):
    try:
        return str(eval(expression))
    except Exception:
        return "Invalid mathematical expression"