from fastapi import FastAPI, Cookie
 
app = FastAPI()
 
@app.get("/")
def root(last_visit = Cookie()):
    return  {"last visit": last_visit}
