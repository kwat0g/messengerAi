import dropbox
from config import MAX_FILE_MB
import os

dbx = dropbox.Dropbox(os.getenv("DROPBOX_ACCESS_TOKEN"))

def download_by_path(path: str) -> bytes:
    metadata, response = dbx.files_download(path)

    size_mb = metadata.size / (1024 * 1024)
    if size_mb > MAX_FILE_MB:
        raise ValueError("File too large")

    return response.content


def download_by_shared_link(url: str) -> bytes:
    metadata, response = dbx.sharing_get_shared_link_file(url)

    size_mb = metadata.size / (1024 * 1024)
    if size_mb > MAX_FILE_MB:
        raise ValueError("File too large")

    return response.content
