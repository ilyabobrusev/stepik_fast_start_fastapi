from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel
import jwt
from jwt import PyJWTError
from datetime import datetime, timedelta
from typing import Optional

# Настройки для JWT
SECRET_KEY = "your_secret_key"  # Замените на реальный секретный ключ
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

# Модель пользователя
class User(BaseModel):
    username: str
    password: str

# "База данных" пользователей
fake_users_db = {
    "john_doe": {
        "username": "john_doe",
        "password": "securepassword123",  # В реальном приложении храните хэшированные пароли
    }
}

# Функция для проверки пользователя
def authenticate_user(username: str, password: str) -> Optional[User]:
    user_data = fake_users_db.get(username)
    if user_data and user_data["password"] == password:
        return User(**user_data)
    return None

app = FastAPI()

# Модель для запроса на вход
class LoginRequest(BaseModel):
    username: str
    password: str

# Модель для токена
class Token(BaseModel):
    access_token: str
    token_type: str

# Функция для создания JWT токена
def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

# Конечная точка для входа
@app.post("/login", response_model=Token)
async def login(login_request: LoginRequest):
    user = authenticate_user(login_request.username, login_request.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid credentials",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": user.username}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}

# Защищенная конечная точка
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

@app.get("/protected_resource")
async def protected_resource(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
    except PyJWTError:
        raise credentials_exception
    return {"message": f"Hello, {username}! You have accessed the protected resource!"}
