# import uvicorn
from fastapi import FastAPI
from fastapi.responses import FileResponse
 
app = FastAPI()

@app.get("/")
def root():
    return FileResponse("index.html")

# @app.get("/")
# async def root():
#     return FileResponse('/home/user/git/github.com/ilyabobrusev/stepik_fast_start_fastapi/v2/1/2/index.html')

# альтернативный вариант
# @app.get("/", response_class = FileResponse)
# def root_html():
#     return "/home/user/git/github.com/ilyabobrusev/stepik_fast_start_fastapi/v2/1/2/index.html"

# if __name__ == "__main__":
#     uvicorn.run("main:app", reload=True)
