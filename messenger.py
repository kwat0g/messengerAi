from fastapi import Request, Response
from config import VERIFY_TOKEN

def verify_webhook(request: Request):
    params = request.query_params
    if (
        params.get("hub.mode") == "subscribe"
        and params.get("hub.verify_token") == VERIFY_TOKEN
    ):
        return Response(content=params.get("hub.challenge"), status_code=200)

    return Response(status_code=403)

async def handle_message(payload: dict):
    # minimal stub
    print("MESSAGE RECEIVED", payload)
