from fastapi import FastAPI, Response
 
app = FastAPI()
 
@app.get("/")
def root():
    data = "Hello from here"
    return Response(content=data, media_type="text/plain", headers={"Secret-Code" : "123459"})
