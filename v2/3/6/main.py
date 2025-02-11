from fastapi import FastAPI
from models import Feedback

app = FastAPI()

fake_db = []

@app.get('/get_all_feedback')
async def get_all_feedback():
    return fake_db

@app.post("/feedback")
async def feedback(feed_back: Feedback):
    fake_db.append(feed_back)
    return {"message": f"Feedback received. Thank you, {feed_back.name}!"}
