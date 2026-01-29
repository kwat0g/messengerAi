from fastapi import Request
from fastapi.responses import PlainTextResponse
import os



def verify_webhook(request: Request):
    params = request.query_params

    mode = params.get("hub.mode")
    token = params.get("hub.verify_token")
    challenge = params.get("hub.challenge")

    if mode == "subscribe" and token == VERIFY_TOKEN:
        return PlainTextResponse(content=challenge, status_code=200)

    return PlainTextResponse(content="Verification failed", status_code=403)


async def handle_message(payload: dict):
    for entry in payload.get("entry", []):
        for event in entry.get("messaging", []):
            sender_id = event["sender"]["id"]

            # Allow first run if ALLOWED_SENDER_ID is empty
            if ALLOWED_SENDER_ID and sender_id != ALLOWED_SENDER_ID:
                return

            if "message" in event and "text" in event["message"]:
                text = event["message"]["text"]
                reply = process_command(text)
                send_message(sender_id, reply)


def send_message(recipient_id: str, text: str):
    url = "https://graph.facebook.com/v18.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text[:2000]},
    }

    requests.post(url, params=params, json=payload, timeout=10)
