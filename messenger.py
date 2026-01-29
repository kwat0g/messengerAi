from fastapi import Request
from fastapi.responses import PlainTextResponse
import os

VERIFY_TOKEN = os.getenv("VERIFY_TOKEN")


def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge, status_code=200)

    return PlainTextResponse(content="Verification failed", status_code=403)
