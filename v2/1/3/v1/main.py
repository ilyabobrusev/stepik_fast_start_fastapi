from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

# Определяем модель данных для входных параметров
class Numbers(BaseModel):
    num1: float
    num2: float

@app.post("/calculate")
async def calculate(numbers: Numbers):
    # Вычисляем сумму двух чисел
    result = numbers.num1 + numbers.num2
    return {"result": result}
