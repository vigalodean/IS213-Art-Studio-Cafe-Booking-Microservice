from fastapi import FastAPI
import httpx

app = FastAPI()

AUTH_SERVICE = "http://auth-service:8001"
BOOKING_SERVICE = "http://booking-service:8002"

@app.get("/dashboard")
async def dashboard():

    async with httpx.AsyncClient() as client:
        profile = await client.get(f"{AUTH_SERVICE}/profile")
        bookings = await client.get(f"{BOOKING_SERVICE}/bookings")

    return {
        "profile": profile.json(),
        "bookings": bookings.json()
    }