from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Wajo AI Video Analysis API is running!"}

