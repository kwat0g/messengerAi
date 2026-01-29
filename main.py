from fastapi import FastAPI, Request
from messenger import verify_webhook, handle_message

app = FastAPI()


@app.get("/webhook")
async def webhook_verify(request: Request):
    return verify_webhook(request)


@app.post("/webhook")
async def webhook_receive(request: Request):
    payload = await request.json()
    await handle_message(payload)
    return {"status": "ok"}
