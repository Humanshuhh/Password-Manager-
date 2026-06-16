from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message " : "Hello world"}
def get_students(branch: str):
    return {"branch": branch}