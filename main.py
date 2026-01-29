from fastapi import FastAPI, Request, Response
from messenger import verify_webhook, handle_message

app = FastAPI()

@app.get("/webhook")
def webhook_verify(request: Request):
    return verify_webhook(request)

@app.post("/webhook")
async def webhook_receive(request: Request):
    payload = await request.json()
    await handle_message(payload)
    return Response(status_code=200)
