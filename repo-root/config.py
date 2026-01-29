import os
from dotenv import load_dotenv

load_dotenv()

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")
PAGE_ACCESS_TOKEN = os.getenv("PAGE_ACCESS_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

ALLOWED_SENDER_ID = os.getenv("ALLOWED_SENDER_ID")  # your Messenger ID
MAX_FILE_MB = 15
