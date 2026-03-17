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

AUTH_URL = "http://auth-service:8000"              
CALENDAR_WRAPPER_URL = "http://calendar-wrapper:8000"

# In-memory session store
sessions = {}

@app.post("/register")
async def register(request: Request, response: Response, user: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{AUTH_URL}/register", json=user)
    # forward any Set-Cookie header from auth-service
    if "set-cookie" in res.headers:
        response.headers["set-cookie"] = res.headers.get("set-cookie")
    if res.json().get("success"):
        sessions[user["username"]] = user["username"]
    return res.json()

@app.post("/login")
async def login(request: Request, response: Response, user: dict = Body(...)):
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{AUTH_URL}/login", json=user)
    # pass through auth cookie
    if "set-cookie" in res.headers:
        response.headers["set-cookie"] = res.headers.get("set-cookie")
    if res.json().get("success"):
        sessions[user["username"]] = user["username"]
    return res.json()

@app.get("/profile")
async def profile(request: Request):
    username = request.cookies.get("session")
    if username and username in sessions:
        return {"success": True, "username": username}
    return {"success": False, "message": "Not authenticated"}


@app.post("/logout")
async def logout(request: Request, response: Response):
    # tell auth-service to remove cookie and clear composite session
    async with httpx.AsyncClient() as client:
        res = await client.post(f"{AUTH_URL}/logout", cookies=request.cookies)
    # forward Set-Cookie (deletion) if present
    if res.headers.get("set-cookie"):
        response.headers["set-cookie"] = res.headers.get("set-cookie")
    # clear our own session store
    username = request.cookies.get("session")
    if username:
        sessions.pop(username, None)
    # propagate cookie deletion to client as fallback
    response.delete_cookie("session", path="/", samesite="none")
    return {"success": True, "message": "Logged out"}

@app.get("/calendar-url")
async def get_bookings():
    async with httpx.AsyncClient() as client:
        res = await client.get(f"{CALENDAR_WRAPPER_URL}/calendar-url")
    return res.json()