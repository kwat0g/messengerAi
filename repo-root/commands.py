from dropbox_client import download_by_path, download_by_shared_link
from parser import extract_text
from ai import summarize_text
from memory import save_last, get_last

def process_command(text: str) -> str:
    text = text.strip()

    # Dropbox support
    if text.startswith("study dropbox:"):
        ref = text.replace("study dropbox:", "").strip()

        if ref.startswith("http"):
            data = download_by_shared_link(ref)
            mime = "application/pdf"
        else:
            if not ref.startswith("/"):
                ref = "/" + ref
            data = download_by_path(ref)
            mime = "application/pdf"

        document_text = extract_text(data, mime)
        save_last(document_text)
        return summarize_text(document_text)

    # Public links (Phase 1)
    if text.startswith("study "):
        from fetcher import fetch_content
        url = text.split(" ", 1)[1]
        content, mime = fetch_content(url)
        document_text = extract_text(content, mime)
        save_last(document_text)
        return summarize_text(document_text)

    if text == "summarize last":
        last = get_last()
        return summarize_text(last) if last else "No document studied yet."

    return "Unknown command."
