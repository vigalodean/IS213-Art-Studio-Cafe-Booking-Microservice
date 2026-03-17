from fastapi import FastAPI, Request, Body, Response
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

# the composite service is also hit directly from the browser when you run
# services with Docker (the gateway sometimes fails or you may open the URL
# manually), so we need CORS here as well.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

CALENDAR_WRAPPER_URL = "http://calendar-wrapper:8000"

@app.get("/calendar-url")
async def get_bookings():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{CALENDAR_WRAPPER_URL}/calendar-url")
    return res.json()