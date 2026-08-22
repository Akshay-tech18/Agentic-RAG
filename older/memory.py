chat_history = []
MAX_HISTORY = 6
def add_message(role, content):
    chat_history.append(
        {
            "role":role,
            "content":content
        }
    )
    if len(chat_history) > MAX_HISTORY:
        chat_history.pop(0)

def get_history():
    return chat_history