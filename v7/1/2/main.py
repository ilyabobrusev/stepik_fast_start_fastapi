from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Модель для регистрации пользователя
class UserRegister(BaseModel):
    username: str
    email: str

# Модель для пользователя
class User(BaseModel):
    id: int
    username: str
    email: str

# Временное хранилище пользователей
users_db = {}

@app.post("/register")
async def register_user(user: UserRegister):
    user_id = len(users_db) + 1
    new_user = User(id=user_id, username=user.username, email=user.email)
    users_db[user_id] = new_user
    return new_user

@app.get("/user/{user_id}")
async def get_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    return users_db[user_id]

@app.delete("/user/{user_id}")
async def delete_user(user_id: int):
    if user_id not in users_db:
        raise HTTPException(status_code=404, detail="User not found")
    del users_db[user_id]
    return {"message": "User deleted"}