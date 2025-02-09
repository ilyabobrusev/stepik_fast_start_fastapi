from fastapi import FastAPI
from models.User import User
import uvicorn

app = FastAPI()

@app.post('/user')
def check_user_age(user: User):
    if user.age >= 18:
        user.is_adult = True
    return user

if __name__=="__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
