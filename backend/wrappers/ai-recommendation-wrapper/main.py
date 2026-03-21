import os
from dotenv import load_dotenv
from fastapi import FastAPI
from groq import Groq
from prompts import SYSTEM_PROMPT

load_dotenv()
app = FastAPI()
client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

@app.post("/chat")
async def chat(request: dict):
    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT },
            {"role": "user", "content": request["message"]}
        ],
        model="llama-3.1-8b-instant"
    )
    return {"response": chat_completion.choices[0].message.content}
