from fastapi import FastAPI
from wrappers.calendar_wrapper.main import get_calendar_url_wrapper

app = FastAPI(title="Calendar Service")

@app.get("/calendar-url")
async def get_calendar():
    return await get_calendar_url_wrapper()