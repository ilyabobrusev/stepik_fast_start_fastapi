from fastapi import FastAPI, HTTPException, Request, status
from fastapi.responses import JSONResponse
from fastapi.exceptions import RequestValidationError
from pydantic import BaseModel, EmailStr, constr, ValidationError
from typing import Optional
import time

app = FastAPI()

# Модель для данных пользователя
class User(BaseModel):
    username: str
    email: EmailStr
    password: constr(min_length=8, max_length=16) # type: ignore

# Модель для ответа на ошибку
class ErrorResponseModel(BaseModel):
    status_code: int
    message: str
    error_code: str

# Пользовательские исключения
class UserNotFoundException(HTTPException):
    def __init__(self, detail: str = "User not found"):
        super().__init__(status_code=status.HTTP_404_NOT_FOUND, detail=detail)

class InvalidUserDataException(HTTPException):
    def __init__(self, detail: str = "Invalid user data"):
        super().__init__(status_code=status.HTTP_400_BAD_REQUEST, detail=detail)

# База данных (для примера)
fake_db = {}

# Конечная точка для регистрации пользователя
@app.post("/register/")
async def register_user(user: User):
    if user.username in fake_db:
        raise InvalidUserDataException(detail="Username already exists")
    fake_db[user.username] = user.dict()
    return {"message": "User registered successfully", "user": user}

# Конечная точка для получения данных пользователя
@app.get("/user/{username}")
async def get_user(username: str):
    if username not in fake_db:
        raise UserNotFoundException()
    return fake_db[username]

# Пользовательский обработчик для UserNotFoundException
@app.exception_handler(UserNotFoundException)
async def user_not_found_exception_handler(request: Request, exc: UserNotFoundException):
    error_response = ErrorResponseModel(
        status_code=status.HTTP_404_NOT_FOUND,
        message=str(exc.detail),
        error_code="USER_NOT_FOUND"
    )
    return JSONResponse(
        status_code=error_response.status_code,
        content=error_response.dict(),
        headers={"X-ErrorHandleTime": str(time.time())}
    )

# Пользовательский обработчик для InvalidUserDataException
@app.exception_handler(InvalidUserDataException)
async def invalid_user_data_exception_handler(request: Request, exc: InvalidUserDataException):
    error_response = ErrorResponseModel(
        status_code=status.HTTP_400_BAD_REQUEST,
        message=str(exc.detail),
        error_code="INVALID_USER_DATA"
    )
    return JSONResponse(
        status_code=error_response.status_code,
        content=error_response.dict(),
        headers={"X-ErrorHandleTime": str(time.time())}
    )

# Пользовательский обработчик для RequestValidationError
@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    error_response = ErrorResponseModel(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        message="Validation error",
        error_code="VALIDATION_ERROR"
    )
    return JSONResponse(
        status_code=error_response.status_code,
        content=error_response.dict(),
        headers={"X-ErrorHandleTime": str(time.time())}
    )