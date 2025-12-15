from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
import httpx
import os

app = FastAPI(title="Vanate ERP Backend")

SUPABASE_URL = "https://ukbwavuphtwuqrhrher.supabase.co"
SUPABASE_KEY = "sb_publishable_3p6l2qGhCQg9dvUk2BXo7Q_0T8To-md"
OPENAI_KEY = os.getenv("OPENAI_API_KEY")  # Key будет в Vercel Environment Variables

HEADERS = {
    "apikey": SUPABASE_KEY,
    "Authorization": f"Bearer {SUPABASE_KEY}",
    "Content-Type": "application/json",
    "Prefer": "return=representation"
}

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ... (остальной код тот же, что я давал раньше, с ботом на OpenAI)

# В /bot:
client = httpx.Client()
openai_headers = {"Authorization": f"Bearer {OPENAI_KEY}", "Content-Type": "application/json"}
# и т.д.

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)