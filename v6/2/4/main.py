from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, conint, EmailStr, constr, ValidationError
from typing import Optional

app = FastAPI()

# Модель Pydantic для пользовательских данных
class User(BaseModel):
    username: str
    age: conint(gt=18) # type: ignore
    email: EmailStr
    password: constr(min_length=8, max_length=16) # type: ignore
    phone: Optional[str] = 'Unknown'

# Конечная точка для создания пользователя
@app.post("/user/")
async def create_user(user: User):
    return {"message": "User created successfully", "user": user}

# Пользовательская обработка ошибок проверки
@app.exception_handler(ValidationError)
async def validation_exception_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"detail": exc.errors(), "body": exc.body}),
    )

# Пользовательская обработка ошибок HTTP
@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content=jsonable_encoder({"detail": exc.detail}),
    )
