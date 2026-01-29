_last_doc = None

def save_last(text: str):
    global _last_doc
    _last_doc = text

def get_last():
    return _last_doc
