from fastapi import FastAPI
import uvicorn

from models import User


app = FastAPI()

user = User(**{"name": "John Doe", "id": 1})

@app.get("/users")
async def users():
    return user

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
