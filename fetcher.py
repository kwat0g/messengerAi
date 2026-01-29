import requests
from config import MAX_FILE_MB

def fetch_content(url: str):
    r = requests.get(url, timeout=15, stream=True)
    r.raise_for_status()

    size_mb = int(r.headers.get("Content-Length", 0)) / (1024 * 1024)
    if size_mb > MAX_FILE_MB:
        raise ValueError("File too large")

    return r.content, r.headers.get("Content-Type", "")
