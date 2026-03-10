from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import httpx

app = FastAPI()

AUTH_SERVICE = "http://auth-service:8000"
BOOKING_SERVICE = "http://booking-service:8000"

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -------------------------
# AUTH ROUTES
# -------------------------

@app.post("/login")
async def login(request: Request):
    data = await request.json()

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{AUTH_SERVICE}/login",
            json=data,
            cookies=request.cookies
        )

    return res.json()


@app.post("/register")
async def register(request: Request):
    data = await request.json()

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{AUTH_SERVICE}/register",
            json=data,
            cookies=request.cookies
        )

    return res.json()


@app.post("/logout")
async def logout(request: Request):

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{AUTH_SERVICE}/logout",
            cookies=request.cookies
        )

    return res.json()


@app.get("/profile")
async def profile(request: Request):

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{AUTH_SERVICE}/profile",
            cookies=request.cookies
        )

    return res.json()

@app.post("/bookings")
async def create_booking(request: Request):
    data = await request.json()

    async with httpx.AsyncClient() as client:
        res = await client.post(
            f"{BOOKING_SERVICE}/bookings",
            json=data,
            cookies=request.cookies
        )

    return res.json()


@app.get("/bookings")
async def get_bookings(request: Request):

    async with httpx.AsyncClient() as client:
        res = await client.get(
            f"{BOOKING_SERVICE}/bookings",
            cookies=request.cookies
        )

    return res.json()