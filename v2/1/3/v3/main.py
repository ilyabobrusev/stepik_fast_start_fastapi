from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")  # Указываем папку с шаблонами

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/calculate", response_class=HTMLResponse)
async def sum_nums(request: Request, num1: int = Form(...), num2: int = Form(...)):
    result = num1 + num2
    context = {
        "request": request,
        "result": result,
    }
    return templates.TemplateResponse("index.html", context=context)
