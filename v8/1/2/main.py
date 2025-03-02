from fastapi import FastAPI, Request

app = FastAPI()

@app.middleware("http")
async def my_middleware(request: Request, call_next):
    print('Мидлвэр начал работу')
    response = await call_next(request)
    print('Мидлвэр получил обратно управление')
    return response

@app.get("/")
def index():
    print('привет из основного обработчика пути')
    return {"message": "Hello, world!"}


