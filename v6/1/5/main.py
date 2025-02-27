from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI()

# Пользовательские классы исключений
class CustomExceptionA(Exception):
    def __init__(self, message: str):
        self.message = message

class CustomExceptionB(Exception):
    def __init__(self, message: str):
        self.message = message

# Модель реагирования на ошибки
class ErrorResponse(BaseModel):
    error: str
    message: str
    status_code: int

# Обработчик для CustomExceptionA
@app.exception_handler(CustomExceptionA)
async def custom_exception_a_handler(request: Request, exc: CustomExceptionA):
    return JSONResponse(
        status_code=400,
        content={"error": "CustomExceptionA", "message": exc.message, "status_code": 400}
    )

# Обработчик для CustomExceptionB
@app.exception_handler(CustomExceptionB)
async def custom_exception_b_handler(request: Request, exc: CustomExceptionB):
    return JSONResponse(
        status_code=404,
        content={"error": "CustomExceptionB", "message": exc.message, "status_code": 404}
    )

# Конечная точка, которая вызывает CustomExceptionA
@app.get("/endpoint_a")
async def endpoint_a(condition: bool = True):
    if not condition:
        raise CustomExceptionA(message="Условие не выполнено")
    return {"message": "Условие выполнено"}

# Конечная точка, которая вызывает CustomExceptionB
@app.get("/endpoint_b/{item_id}")
async def endpoint_b(item_id: int):
    if item_id != 1:
        raise CustomExceptionB(message="Ресурс не найден")
    return {"item_id": item_id}
