import requests
from config import VERIFY_TOKEN, PAGE_ACCESS_TOKEN, ALLOWED_SENDER_ID
from commands import process_command

def verify_webhook(request):
    params = request.query_params
    if params.get("hub.verify_token") == VERIFY_TOKEN:
        return int(params.get("hub.challenge"))
    return "Verification failed"

async def handle_message(payload):
    for entry in payload.get("entry", []):
        for event in entry.get("messaging", []):
            sender = event["sender"]["id"]
            if sender != ALLOWED_SENDER_ID:
                return

            if "message" in event and "text" in event["message"]:
                text = event["message"]["text"]
                reply = process_command(text)
                send_message(sender, reply)

def send_message(recipient_id, text):
    url = "https://graph.facebook.com/v18.0/me/messages"
    params = {"access_token": PAGE_ACCESS_TOKEN}
    payload = {
        "recipient": {"id": recipient_id},
        "message": {"text": text[:2000]}
    }
    requests.post(url, params=params, json=payload, timeout=10)
