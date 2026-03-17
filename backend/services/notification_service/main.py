from fastapi import FastAPI
from wrappers.notification_wrapper.main import send_email_transaction_notification_wrapper

app = FastAPI(title="Notification Service")

@app.post("/send-transaction-notification")
async def send_notification(to_email: str, username: str):
    return await send_email_transaction_notification_wrapper(to_email, username)