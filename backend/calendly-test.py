import requests
import os
from dotenv import load_dotenv

load_dotenv()  
access_token = os.getenv("ACCESS_TOKEN")
user_uri = "https://api.calendly.com/users/1a6a3bd6-fd02-4e6a-a19b-85aafe75f251"
events_url = f"https://api.calendly.com/scheduled_events?user={user_uri}"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json"
}

# Get Calendly user info 
url = "https://api.calendly.com/users/me"
response = requests.get(url, headers=headers)
data = response.json()
print(data)
print()

# Optional: fetch all events, handling pagination
all_events = []
while events_url:
    response = requests.get(events_url, headers=headers)
    data = response.json()
    all_events.extend(data.get("collection", []))
    events_url = data.get("pagination", {}).get("next_page")

for event in all_events:
    event_id = event.get("uri").split("/")[-1]
    
    # Fetch invitees for each event
    invitees_url = f"https://api.calendly.com/scheduled_events/{event_id}/invitees"
    r = requests.get(invitees_url, headers=headers)
    invitees_data = r.json().get("collection", [])
    invitee_names = [i.get("name") for i in invitees_data] or ["N/A"]
    
    print(f"Event Name: {event.get('name')}")
    print(f"Start Time: {event.get('start_time')}")
    print(f"End Time: {event.get('end_time')}")
    print(f"Status: {event.get('status')}")
    print(f"Invitees: {', '.join(invitee_names)}")
    print("-" * 40)