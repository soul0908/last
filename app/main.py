from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return { "message" : "얼른 집 가거라...!"}