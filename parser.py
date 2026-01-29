from io import BytesIO
from bs4 import BeautifulSoup
from PyPDF2 import PdfReader
import docx

def extract_text(data: bytes, mime: str) -> str:
    if "pdf" in mime:
        reader = PdfReader(BytesIO(data))
        return "\n".join(p.extract_text() for p in reader.pages if p.extract_text())

    if "word" in mime:
        doc = docx.Document(BytesIO(data))
        return "\n".join(p.text for p in doc.paragraphs)

    if "html" in mime or "text" in mime:
        soup = BeautifulSoup(data, "html.parser")
        return soup.get_text(separator="\n")

    raise ValueError("Unsupported file type")
