from fastapi import FastAPI
from app.analyzer import analyze_repository

app = FastAPI()

@app.get("/review")
def review(url: str):
    return analyze_repository(url)

