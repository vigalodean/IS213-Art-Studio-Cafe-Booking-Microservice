from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles

app = FastAPI()

app.mount("/images", StaticFiles(directory="images"), name="images")
# Allow frontend later to access this service
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mock database (Activity catalogue)
activities = [
    {
        "id": "art-jamming",
        "name": "Art Jamming",
        "category": "Painting",
        "description": "Express your creativity on canvas with guidance.",
        "price": 45,
        "duration": "2 hours",
        "image": "http://localhost:8000/images/art_jamming.jpg"
    },
    {
        "id": "oil-painting",
        "name": "Oil Painting",
        "category": "Painting",
        "description": "Learn oil painting techniques with professionals.",
        "price": 60,
        "duration": "3 hours",
        "image": "http://localhost:8000/images/oil_painting.jpg"
    },
    {
        "id": "acrylic-painting",
        "name": "Acrylic Painting",
        "category": "Painting",
        "description": "Fun and vibrant acrylic painting session.",
        "price": 40,
        "duration": "2 hours",
        "image": "http://localhost:8000/images/acrylic_painting.jpg"
    },
    {
        "id": "clay-sculpting",
        "name": "Clay Sculpting",
        "category": "Sculpting",
        "description": "Create your own clay masterpiece.",
        "price": 50,
        "duration": "2.5 hours",
        "image": "http://localhost:8000/images/clay_sculpting.jpg"
    },
    {
        "id": "watercolor-workshop",
        "name": "Watercolor Workshop",
        "category": "Painting",
        "description": "Relax with soft watercolor techniques.",
        "price": 35,
        "duration": "1.5 hours",
        "image": "http://localhost:8000/images/watercolor.jpg"
    }
]

# Health check
@app.get("/")
def home():
    return {"message": "Activity Service is running"}

# Browse all activities (catalogue)
@app.get("/getAllActivities")
def get_activities():
    return {"activities": activities}

# Get single activity (details page)
@app.get("/activities/{activity_id}")
def get_activity(activity_id: int):
    for activity in activities:
        if activity["id"] == activity_id:
            return activity
    raise HTTPException(status_code=404, detail="Activity not found")

# Filter by category
@app.get("/activities/category/{category}")
def get_by_category(category: str):
    filtered = [a for a in activities if a["category"].lower() == category.lower()]
    return {"activities": filtered}