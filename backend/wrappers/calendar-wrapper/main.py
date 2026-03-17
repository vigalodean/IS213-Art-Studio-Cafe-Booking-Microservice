from fastapi import FastAPI

app = FastAPI(title="Calendar Service")

@app.get("/calendar-url")
async def get_calendar_url():
    """Return Calendly URL"""
    return {"success": True, "booking_url": "https://calendly.com/nicholasang-sg/art-cafe-booking"}
